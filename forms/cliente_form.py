from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ClienteForm(FlaskForm):
  nombre = StringField(
      'Nombre Completo', validators=[DataRequired(), Length(min=3, max=100)]
  )
  email = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
  telefono = StringField(
      'Teléfono', validators=[DataRequired(), Length(min=7, max=15)]
  )
  ciudad = StringField(
      'Ciudad', validators=[DataRequired(), Length(min=2, max=50)]
  )
  submit = SubmitField('Guardar Cliente')