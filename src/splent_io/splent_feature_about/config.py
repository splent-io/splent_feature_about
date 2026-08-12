"""
about feature configuration.

Reads this feature's environment variables into Flask app.config, which is
what templates and services see.

Every variable read here belongs under [tool.splent.config] in
pyproject.toml as well, with the same default. That block is how a product
learns the knob exists and what happens if it leaves it alone, and the two
disagreeing means behaviour depends on whether product:env --merge has run.

To regenerate from source code: splent feature:inject-config splent_feature_about
"""

import os  # noqa: F401 — used when adding env vars below


def inject_config(app):
    app.config.update(
        {
            # Add your feature's env vars here, e.g.:
            # "ABOUT_PATH": os.getenv("ABOUT_PATH", "about"),
        }
    )
