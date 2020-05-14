from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, DateField, RadioField, SelectField
from wtforms.validators import ValidationError, InputRequired, Length, Email
from wtforms.fields.html5 import EmailField

class Applicant(FlaskForm):
    last_name = StringField('Last Name', validators=[
        InputRequired(), Length(max=100)
    ])
    first_name = StringField('First Name', validators=[
        InputRequired(), Length(max=100)
    ])
    ss = IntegerField('SS#', validators=[
        InputRequired(),
    ])
    expedition = DateField('Expedition', validators=[
        InputRequired(), Length(max=100)
    ])
    expiration = DateField('Expiration', validators=[
        InputRequired(), Length(max=100)
    ])
    cell_phone = IntegerField('Cell PH')
    home_phone = IntegerField('Cell PH')
    address = StringField('Address', validators=[
        InputRequired(),
        Length(150)
    ])
    city = StringField('City', validators=[
        InputRequired(),
        Length(150)
    ])
    state = StringField('State', validators=[
        InputRequired(),
        Length(150)
    ])
    zip_code = IntegerField('ZIP', validators=[
        InputRequired(),
        Length(max=5)
    ])
    email = EmailField('Email', validators=[
        InputRequired(),
        Email()
    ])
    employer = StringField('Employer', validators=[
        InputRequired(),
    ])
    years = IntegerField('Years', validators=[
        InputRequired(),
        Length(max=2)
    ])
    salary = IntegerField('Salary', validators=[
        InputRequired(),

    ])
    position = StringField('Position', validators=[
        InputRequired(),
        Length(max=100)
    ])
    business_phone = IntegerField('Business PH', validators=[
        InputRequired()
    ])
    previous_employer = StringField('Previous Employer (if above less than 3 years)')
    other_income = StringField('Source of other income')

    status = SelectField('Status', choices=[
        ('Paid', 'Paid'), 
        ('Mortgaged', 'Mortgaged'), 
        ('Rent', 'Rent')
    ])

    mortgaged_company = StringField('Mortgaged Company')
    monthy_payment = IntegerField('Monthly Payment')
    long_here = StringField('How long here')

    personal_reference_name = StringField('Name', validators=[
        InputRequired()
    ])
    personal_reference_relationship = StringField('Relationship', validators=[
        InputRequired()
    ])
    personal_reference_phone = StringField('Phone', validators=[
        InputRequired()
    ])

    
class CoApplicant(FlaskForm):
    last_name = StringField('Last Name', validators=[
        InputRequired(), Length(max=100)
    ])
    first_name = StringField('First Name', validators=[
        InputRequired(), Length(max=100)
    ])
    ss = IntegerField('SS#', validators=[
        InputRequired(),
    ])
    expedition = DateField('Expedition', validators=[
        InputRequired(), Length(max=100)
    ])
    expiration = DateField('Expiration', validators=[
        InputRequired(), Length(max=100)
    ])
    cell_phone = IntegerField('Cell PH')
    home_phone = IntegerField('Cell PH')
    address = StringField('Address', validators=[
        InputRequired(),
        Length(150)
    ])
    city = StringField('City', validators=[
        InputRequired(),
        Length(150)
    ])
    state = StringField('State', validators=[
        InputRequired(),
        Length(150)
    ])
    zip_code = IntegerField('ZIP', validators=[
        InputRequired(),
        Length(max=5)
    ])
    email = EmailField('Email', validators=[
        InputRequired(),
        Email()
    ])
    employer = StringField('Employer', validators=[
        InputRequired(),
    ])
    years = IntegerField('Years', validators=[
        InputRequired(),
        Length(max=2)
    ])
    salary = IntegerField('Salary', validators=[
        InputRequired(),

    ])
    position = StringField('Position', validators=[
        InputRequired(),
        Length(max=100)
    ])
    business_phone = IntegerField('Business PH', validators=[
        InputRequired()
    ])
    previous_employer = StringField('Previous Employer (if above less than 3 years)')
    other_income = StringField('Source of other income')

class MortgageInfo(FlaskForm):
    status = SelectField('Status', choices=[
        ('Paid', 'Paid'), 
        ('Mortgaged', 'Mortgaged'), 
        ('Rent', 'Rent')
    ])

    mortgaged_company = StringField('Mortgaged Company')
    monthy_payment = IntegerField('Monthly Payment')
    long_here = StringField('How long here')

class PersonalReferences(FlaskForm):
    personal_reference_name = StringField('Name', validators=[
        InputRequired()
    ])
    personal_reference_relationship = StringField('Relationship', validators=[
        InputRequired()
    ])
    personal_reference_phone = StringField('Phone', validators=[
        InputRequired()
    ])
