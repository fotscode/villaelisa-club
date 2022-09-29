from wtforms.form import Form
from wtforms import StringField, SubmitField, SelectField, IntegerField,validators
from wtforms.validators import ValidationError



class AssociateForm(Form):
    
    DNI_number = IntegerField('DNI', validators=[validators.input_required()])
    DNI_type  = SelectField('Tipo de documento', choices=[('DNI', 'DNI'), ('LC', 'LC'), ('LE', 'LE')],validators=[validators.input_required()])
    gender = SelectField('Genero', choices=[('male', 'Hombre'), ('female', 'Mujer'), ('other', 'Otro')],validators=[validators.input_required()])
    address = StringField('Direccion', validators=[validators.input_required()])
    phone_number = IntegerField('Telefono')
    add_associate= SubmitField('Agregar Asociado')
    
    
    def validate_age(form, field):
        if field.data < 13:
            raise ValidationError("We're sorry, you must be 13 or older to register")
