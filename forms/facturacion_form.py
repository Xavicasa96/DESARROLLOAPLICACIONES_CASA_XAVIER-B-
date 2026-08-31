from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class FacturacionForm(FlaskForm):
  nro = StringField(
      'Nº de Factura', validators=[DataRequired(), Length(min=3, max=20)]
  )
  cliente = StringField(
      'Cliente', validators=[DataRequired(), Length(min=3, max=100)]
  )
  total = DecimalField(
      'Total ($)', validators=[DataRequired(), NumberRange(min=0.01)]
  )
  estado = StringField(
      'Estado (Pagada / Pendiente)',
      validators=[DataRequired(), Length(min=3, max=20)],
  )
  submit = SubmitField('Guardar Factura')