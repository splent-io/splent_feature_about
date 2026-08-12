from flask import request, url_for

from splent_framework.hooks.template_hooks import register_template_hook


def about_admin_link():
    """Sidebar entry for the About management screen (the WP-plugin pattern)."""
    active = (
        "active"
        if request.endpoint and request.endpoint.startswith("about.admin")
        else ""
    )
    return (
        f'<li class="sidebar-item {active}">'
        f'<a class="sidebar-link" href="{url_for("about.admin_index")}">'
        '<i class="align-middle" data-feather="info"></i> '
        '<span class="align-middle">About</span>'
        "</a>"
        "</li>"
    )


register_template_hook("layout.authenticated_sidebar", about_admin_link)
