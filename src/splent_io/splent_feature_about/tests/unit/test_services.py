"""
Unit tests for splent_feature_about.

Unit tests verify individual classes and functions in isolation.
External dependencies (DB, HTTP, other services) MUST be mocked.
These tests should be fast and have zero side effects.
"""

from unittest.mock import MagicMock

from splent_io.splent_feature_about.services import AboutService


def _service_with_mock_repository():
    service = AboutService()
    service.repository = MagicMock()
    return service


def test_published_sections_delegates_to_repository():
    service = _service_with_mock_repository()
    service.repository.list_published.return_value = ["first", "second"]

    assert service.published_sections() == ["first", "second"]
    service.repository.list_published.assert_called_once_with()


def test_get_by_slug_delegates_to_repository():
    service = _service_with_mock_repository()
    service.repository.get_by_slug.return_value = "section"

    assert service.get_by_slug("who-we-are") == "section"
    service.repository.get_by_slug.assert_called_once_with("who-we-are")
