from flask import Flask, flash, redirect, render_template, url_for
from forms.cliente_form import ClienteForm
from forms.facturacion_form import FacturacionForm
from forms.producto_form import ProductoForm
from forms.proveedor_form import ProveedorForm

app = Flask(__name__)
app.config['SECRET_KEY'] = (
    'clave_secreta_super_segura_para_csrf'  # Requerido para Flask-WTF
)

# Listas temporales en memoria para la aplicación
lista_productos = [
    {
        'id': 101,
        'nombre': 'Laptop Pro 15',
        'categoria': 'Equipos',
        'precio': 1200.00,
        'stock': 15,
    },
    {
        'id': 102,
        'nombre': 'Monitor 4K 27"',
        'categoria': 'Periféricos',
        'precio': 350.00,
        'stock': 8,
    },
    {
        'id': 103,
        'nombre': 'Teclado Mecánico RGB',
        'categoria': 'Accesorios',
        'precio': 85.50,
        'stock': 25,
    },
]

lista_clientes = [
    {
        'id': 1,
        'nombre': 'Carlos Mendoza',
        'email': 'carlos.mendoza@email.com',
        'telefono': '0991234567',
        'ciudad': 'Loja',
    },
    {
        'id': 2,
        'nombre': 'María Sarango',
        'email': 'maria.sarango@email.com',
        'telefono': '0987654321',
        'ciudad': 'Quito',
    },
]

lista_proveedores = [
    {
        'id': 1,
        'empresa': 'TechSupply S.A.',
        'contacto': 'Juan Pérez',
        'telefono': '022555111',
        'ruc': '1190123456001',
    },
    {
        'id': 2,
        'empresa': 'Sistemas Globales',
        'contacto': 'Ana Guerrero',
        'telefono': '042888999',
        'ruc': '1790987654001',
    },
]

lista_facturas = [
    {
        'nro': 'FAC-001',
        'cliente': 'Carlos Mendoza',
        'fecha': '2026-08-15',
        'total': 1550.00,
        'estado': 'Pagada',
    },
    {
        'nro': 'FAC-002',
        'cliente': 'María Sarango',
        'fecha': '2026-08-16',
        'total': 85.50,
        'estado': 'Pendiente',
    },
]


# Ruta Principal (Informativa / Index con variables y diccionarios)
@app.route('/')
def index():
  sistema_info = {
      'nombre': 'Sistema de Gestión Integral',
      'version': 'v3.0 - Formularios con Flask-WTF',
      'desarrollador': 'Xavier Casa',
  }
  return render_template('index.html', info=sistema_info)


# Ruta Módulo Productos (Soporta GET y POST para validación de formularios)
@app.route('/productos', methods=['GET', 'POST'])
def productos():
  form = ProductoForm()
  if form.validate_on_submit():
    nuevo_prod = {
        'id': len(lista_productos) + 101,
        'nombre': form.nombre.data,
        'categoria': form.categoria.data,
        'precio': float(form.precio.data),
        'stock': form.stock.data,
    }
    lista_productos.append(nuevo_prod)
    flash('¡Producto registrado exitosamente!', 'success')
    return redirect(url_for('productos'))
  return render_template(
      'productos.html', productos=lista_productos, form=form
  )


# Ruta Módulo Clientes
@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
  form = ClienteForm()
  if form.validate_on_submit():
    nuevo_cli = {
        'id': len(lista_clientes) + 1,
        'nombre': form.nombre.data,
        'email': form.email.data,
        'telefono': form.telefono.data,
        'ciudad': form.ciudad.data,
    }
    lista_clientes.append(nuevo_cli)
    flash('¡Cliente registrado exitosamente!', 'success')
    return redirect(url_for('clientes'))
  return render_template('clientes.html', clientes=lista_clientes, form=form)


# Ruta Módulo Proveedores
@app.route('/proveedores', methods=['GET', 'POST'])
def proveedores():
  form = ProveedorForm()
  if form.validate_on_submit():
    nuevo_prov = {
        'id': len(lista_proveedores) + 1,
        'empresa': form.empresa.data,
        'contacto': form.contacto.data,
        'telefono': form.telefono.data,
        'ruc': form.ruc.data,
    }
    lista_proveedores.append(nuevo_prov)
    flash('¡Proveedor registrado exitosamente!', 'success')
    return redirect(url_for('proveedores'))
  return render_template(
      'proveedores.html', proveedores=lista_proveedores, form=form
  )


# Ruta Módulo Facturación
@app.route('/facturacion', methods=['GET', 'POST'])
def facturacion():
  form = FacturacionForm()
  if form.validate_on_submit():
    nueva_fac = {
        'nro': form.nro.data,
        'cliente': form.cliente.data,
        'fecha': '2026-08-30',
        'total': float(form.total.data),
        'estado': form.estado.data,
    }
    lista_facturas.append(nueva_fac)
    flash('¡Factura registrada exitosamente!', 'success')
    return redirect(url_for('facturacion'))
  return render_template(
      'facturacion.html', facturas=lista_facturas, form=form
  )


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001, debug=True)