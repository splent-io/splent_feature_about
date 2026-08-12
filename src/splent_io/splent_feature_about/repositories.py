from __future__ import annotations

from splent_io.splent_feature_about.models import AboutSection
from splent_framework.repositories.BaseRepository import BaseRepository


class AboutRepository(BaseRepository):
    def __init__(self):
        super().__init__(AboutSection)

    def list_published(self) -> list[AboutSection]:
        return (
            AboutSection.query.filter_by(published=True)
            .order_by(AboutSection.order.asc(), AboutSection.id.asc())
            .all()
        )

    def get_by_slug(self, slug: str) -> AboutSection | None:
        return AboutSection.query.filter_by(slug=slug).first()
