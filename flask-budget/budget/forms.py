from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from budget.models import Category


class ExampleForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    remember = BooleanField('Remember Me')


class CategoryForm(FlaskForm):
    category = StringField('Category', 
                           validators=[DataRequired()])
    submit = SubmitField('Add Category')

    def validate_category(self, category_input):
        category = Category.query.filter_by(category=category_input).first()

        if category:
            raise  ValidationError('Category already exists')
    