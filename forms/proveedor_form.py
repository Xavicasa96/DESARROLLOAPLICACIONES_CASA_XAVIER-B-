from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class ProveedorForm(FlaskForm):
  ruc = StringField('RUC', validators=[DataRequired(), Length(min=10, max=13)])
  empresa = StringField(
      'Empresa', validators=[DataRequired(), Length(min=2, max=100)]
  )
  contacto = StringField(
      'Nombre de Contacto', validators=[DataRequired(), Length(min=2, max=100)]
  )
  telefono = StringField(
      'Teléfono', validators=[DataRequired(), Length(min=7, max=15)]
  )
  submit = SubmitField('Guardar Proveedor')