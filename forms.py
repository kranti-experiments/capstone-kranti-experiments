#Imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length
from wtforms.validators import ValidationError
import re


def validate_name(form, field):
    inp_text = field.data.strip()
    if len(inp_text) == 0:
        raise ValidationError('Enter Name to proceed!')
    if len(inp_text) > 50:
        raise ValidationError('Name must be less than 50 characters!')

    if(not re.match("^[A-Za-z0-9_.]*$", inp_text)):
        raise ValidationError("User Name contains not supported characters.\
                                Alhpabets/Numerals/Period/Underscore are only allowed.")
    if(not inp_text[0].isalpha()):
        raise ValidationError(f"Name should start with alphabet but not as {inp_text[0]}")

class CreateUserForm(FlaskForm):
    '''
    UserForm holds the place holders for the name and submit buttons
    Validators helps ensuring the data is filled without which next stepsn won't work
    '''
    name = StringField("What's Your Name ?!", validators=[InputRequired(), validate_name])
    submit = SubmitField("Test")

