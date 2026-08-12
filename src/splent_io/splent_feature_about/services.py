from splent_io.splent_feature_about.repositories import AboutRepository
from splent_framework.services.BaseService import BaseService


class AboutService(BaseService):
    def __init__(self):
        super().__init__(AboutRepository())

    def published_sections(self):
        return self.repository.list_published()

    def get_by_slug(self, slug: str):
        return self.repository.get_by_slug(slug)
