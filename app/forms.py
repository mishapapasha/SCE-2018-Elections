from flask_babel import gettext
from flask_wtf import Form, validators
from wtforms import StringField, BooleanField, TextField
from wtforms.validators import DataRequired

from app.models import User


class LoginForm(Form):
    name = StringField('name', validators=[DataRequired()])
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])

    #first_name = StringField('First_name', validators=[DataRequired()])
    # def validate(self):
    #     return True
    #
    # def validate(self):
    #     valid = Form.validate(self)
    #     if not valid:
    #         return False
    #
    #     user = User.query.filter_by(first_name=self.first_name.data).first()
    #     if user is not None:
    #         self.first_name.errors.append(gettext('This nickname is already in use. Please choose another one.'))
    #         return False
    #     return True