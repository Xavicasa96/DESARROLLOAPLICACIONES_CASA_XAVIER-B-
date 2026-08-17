from flask import Flask, render_template

app = Flask(__name__)

# Ruta Principal (Informativa / Index)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta Módulo Productos
@app.route('/productos')
def productos():
    lista_productos = [
        {"id": 101, "nombre": "Laptop Pro 15", "categoria": "Equipos", "precio": 1200.00, "stock": 15},
        {"id": 102, "nombre": "Monitor 4K 27\"", "categoria": "Periféricos", "precio": 350.00, "stock": 8},
        {"id": 103, "nombre": "Teclado Mecánico RGB", "categoria": "Accesorios", "precio": 85.50, "stock": 25}
    ]
    return render_template('productos.html', productos=lista_productos)

# Ruta Módulo Clientes
@app.route('/clientes')
def clientes():
    lista_clientes = [
        {"id": 1, "nombre": "Carlos Mendoza", "email": "carlos.mendoza@email.com", "telefono": "0991234567", "ciudad": "Loja"},
        {"id": 2, "nombre": "María Sarango", "email": "maria.sarango@email.com", "telefono": "0987654321", "ciudad": "Quito"}
    ]
    return render_template('clientes.html', clientes=lista_clientes)

# Ruta Módulo Proveedores
@app.route('/proveedores')
def proveedores():
    lista_proveedores = [
        {"id": 1, "empresa": "TechSupply S.A.", "contacto": "Juan Pérez", "telefono": "022555111", "ruc": "1190123456001"},
        {"id": 2, "empresa": "Sistemas Globales", "contacto": "Ana Guerrero", "telefono": "042888999", "ruc": "1790987654001"}
    ]
    return render_template('proveedores.html', proveedores=lista_proveedores)

# Ruta Módulo Facturación
@app.route('/facturacion')
def facturacion():
    lista_facturas = [
        {"nro": "FAC-001", "cliente": "Carlos Mendoza", "fecha": "2026-08-15", "total": 1550.00, "estado": "Pagada"},
        {"nro": "FAC-002", "cliente": "María Sarango", "fecha": "2026-08-16", "total": 85.50, "estado": "Pendiente"}
    ]
    return render_template('facturacion.html', facturas=lista_facturas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)