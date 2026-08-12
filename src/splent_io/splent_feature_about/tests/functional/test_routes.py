"""
Functional tests for splent_feature_about.

Functional tests use Flask's test client to exercise full HTTP
request/response cycles (GET, POST, redirects, rendered HTML).
"""

from splent_framework.db import db

from splent_io.splent_feature_about.models import AboutSection


def _seed_sections(app):
    with app.app_context():
        db.session.add_all(
            [
                AboutSection(
                    slug="who-we-are",
                    title="Who we are",
                    content="<p>Intro</p>",
                    order=1,
                    published=True,
                ),
                AboutSection(
                    slug="our-values",
                    title="Our values",
                    content="<p>Values</p>",
                    order=2,
                    published=True,
                ),
                AboutSection(
                    slug="hidden-section",
                    title="Hidden section",
                    content="<p>Draft</p>",
                    order=3,
                    published=False,
                ),
            ]
        )
        db.session.commit()


def test_index_is_reachable(test_client):
    """The About page is public."""
    response = test_client.get("/about")
    assert response.status_code == 200


def test_index_shows_published_sections_in_order(test_app, test_client):
    """Published sections render with their titles and slug anchors, in order."""
    _seed_sections(test_app)
    response = test_client.get("/about")
    assert response.status_code == 200
    html = response.data.decode()
    assert "Who we are" in html
    assert "Our values" in html
    assert 'id="who-we-are"' in html
    assert 'id="our-values"' in html
    assert html.index('id="who-we-are"') < html.index('id="our-values"')


def test_index_hides_unpublished_sections(test_app, test_client):
    """Draft sections never reach the public page."""
    _seed_sections(test_app)
    html = test_client.get("/about").data.decode()
    assert "Hidden section" not in html
    assert 'id="hidden-section"' not in html
