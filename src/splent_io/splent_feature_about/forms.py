from flask_wtf import FlaskForm
from wtforms import SubmitField


class SplentFeatureAboutForm(FlaskForm):
    submit = SubmitField("Save splent_feature_about")
