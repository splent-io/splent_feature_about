"""No shared seed content.

What a website says about itself is the least shareable content there is, so
this feature ships structure only. A product seeds its own sections from
``src/<product>/seeders.py`` (see the framework's product seeders support),
typically with a seeder class declaring::

    replaces = ("splent_io.splent_feature_about",)
"""

from splent_framework.seeders.BaseSeeder import BaseSeeder


class AboutSeeder(BaseSeeder):
    def run(self):
        self.seed([])
