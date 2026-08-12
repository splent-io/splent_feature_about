from splent_framework.db import db


class AboutSection(db.Model):
    """One block of the public About page (e.g. Who we are, Our values)."""

    __tablename__ = "about_section"

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(255), nullable=False, unique=True, index=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, default="")  # rich text / HTML
    order = db.Column(db.Integer, default=0)
    published = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"AboutSection<{self.slug}>"
