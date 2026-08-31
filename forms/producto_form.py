from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class ProductoForm(FlaskForm):
  nombre = StringField(
      'Nombre del Producto',
      validators=[DataRequired(), Length(min=2, max=100)],
  )
  categoria = StringField(
      'Categoría', validators=[DataRequired(), Length(min=2, max=50)]
  )
  precio = DecimalField(
      'Precio ($)', validators=[DataRequired(), NumberRange(min=0.01)]
  )
  stock = IntegerField('Stock', validators=[DataRequired(), NumberRange(min=0)])
  submit = SubmitField('Guardar Producto')