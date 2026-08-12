from flask import (
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required

from splent_io.splent_feature_about import about_bp
from splent_io.splent_feature_about.models import AboutSection
from splent_framework.db import db
from splent_framework.services.service_locator import service_proxy
from splent_framework.utils.text import slugify

about_service = service_proxy("AboutService")


# =====================================================================
# PUBLIC
# =====================================================================
@about_bp.route("/about", methods=["GET"])
def index():
    sections = about_service.published_sections()
    return render_template("about/index.html", sections=sections)


# =====================================================================
# ADMIN — domain-specific management (the "plugin" screen)
# =====================================================================
def _slugify(value):
    return slugify(value) or "section"


def _unique_slug(title, exclude_id=None):
    base = _slugify(title)
    slug, i = base, 2
    while True:
        q = AboutSection.query.filter_by(slug=slug)
        if exclude_id:
            q = q.filter(AboutSection.id != exclude_id)
        if not q.first():
            return slug
        slug, i = f"{base}-{i}", i + 1


def _ordered_sections():
    """All sections (incl. drafts) in page order."""
    return AboutSection.query.order_by(
        AboutSection.order.asc(), AboutSection.id.asc()
    ).all()


def _form_to_data(form):
    return {
        "title": (form.get("title") or "").strip(),
        "content": (form.get("content") or "").strip(),
        "order": int(form.get("order") or 0),
        "published": bool(form.get("published")),
    }


@about_bp.route("/admin/about", methods=["GET"])
@login_required
def admin_index():
    return render_template("about/admin/list.html", sections=_ordered_sections())


@about_bp.route("/admin/about/new", methods=["GET", "POST"])
@login_required
def admin_new():
    if request.method == "POST":
        data = _form_to_data(request.form)
        if not data["title"]:
            flash("Title is required.", "danger")
            return redirect(url_for("about.admin_new"))
        data["slug"] = _unique_slug(data["title"])
        db.session.add(AboutSection(**data))
        db.session.commit()
        flash(f"Added {data['title']}.", "success")
        return redirect(url_for("about.admin_index"))
    return render_template("about/admin/form.html", section=None)


@about_bp.route("/admin/about/<int:section_id>/edit", methods=["GET", "POST"])
@login_required
def admin_edit(section_id):
    section = AboutSection.query.get_or_404(section_id)
    if request.method == "POST":
        data = _form_to_data(request.form)
        if not data["title"]:
            flash("Title is required.", "danger")
            return redirect(url_for("about.admin_edit", section_id=section_id))
        if data["title"] != section.title:
            data["slug"] = _unique_slug(data["title"], exclude_id=section.id)
        for key, value in data.items():
            setattr(section, key, value)
        db.session.commit()
        flash(f"Updated {section.title}.", "success")
        return redirect(url_for("about.admin_index"))
    return render_template("about/admin/form.html", section=section)


@about_bp.route("/admin/about/<int:section_id>/move", methods=["POST"])
@login_required
def admin_move(section_id):
    section = AboutSection.query.get_or_404(section_id)
    direction = (request.form.get("direction") or "").strip()
    ordered = _ordered_sections()
    # Renumber sequentially so a swap is always well-defined, then swap with
    # the neighbour in the requested direction.
    for i, s in enumerate(ordered, start=1):
        s.order = i
    idx = ordered.index(section)
    target = idx - 1 if direction == "up" else idx + 1
    if 0 <= target < len(ordered):
        other = ordered[target]
        section.order, other.order = other.order, section.order
    db.session.commit()
    return redirect(url_for("about.admin_index"))


@about_bp.route("/admin/about/<int:section_id>/delete", methods=["POST"])
@login_required
def admin_delete(section_id):
    section = AboutSection.query.get_or_404(section_id)
    title = section.title
    db.session.delete(section)
    db.session.commit()
    flash(f"Removed {title}.", "success")
    return redirect(url_for("about.admin_index"))
