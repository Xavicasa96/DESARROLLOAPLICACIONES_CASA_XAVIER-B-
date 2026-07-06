// 1. Capturar los elementos del HTML
const form = document.getElementById('miFormulario');
const titulo = document.getElementById('titulo');
const desc = document.getElementById('descripcion');
const estado = document.getElementById('estado');
const lista = document.getElementById('lista');
const contador = document.getElementById('contador');
const mensaje = document.getElementById('mensaje');

let totalRegistros = 0; // Un simple número para contar

// 2. Funciones de Validación (Devuelven true o false)
function validarTitulo() {
    if (titulo.value.length < 4) {
        titulo.className = "form-control is-invalid";
        return false;
    } else {
        titulo.className = "form-control is-valid";
        return true;
    }
}

function validarDesc() {
    if (desc.value.length < 15) {
        desc.className = "form-control is-invalid";
        return false;
    } else {
        desc.className = "form-control is-valid";
        return true;
    }
}

function validarEstado() {
    if (estado.value === "") {
        estado.className = "form-control is-invalid";
        return false;
    } else {
        estado.className = "form-control is-valid";
        return true;
    }
}

// 3. Validaciones en tiempo real (Eventos input y blur)
titulo.addEventListener('input', validarTitulo);
titulo.addEventListener('blur', validarTitulo);

desc.addEventListener('input', validarDesc);
desc.addEventListener('blur', validarDesc);

estado.addEventListener('change', validarEstado);
estado.addEventListener('blur', validarEstado);

// 4. El evento principal: Enviar el Formulario
form.addEventListener('submit', function(evento) {
    evento.preventDefault(); // Evita que la página parpadee o se recargue

    // Ejecutamos las validaciones
    let tValido = validarTitulo();
    let dValida = validarDesc();
    let eValido = validarEstado();

    // Si todo está correcto
    if (tValido && dValida && eValido) {
        
        // --- CREAR Y MOSTRAR ---
        const nuevoElemento = document.createElement('li');
        nuevoElemento.className = "list-group-item d-flex justify-content-between align-items-center";
        
        // Escribimos el HTML dentro de la etiqueta <li>
        nuevoElemento.innerHTML = `
            <div>
                <strong>${titulo.value}</strong> - <span class="badge bg-secondary">${estado.value}</span>
                <br> <small class="text-muted">${desc.value}</small>
            </div>
            <button class="btn btn-danger btn-sm">Eliminar</button>
        `;

        // --- ELIMINAR ---
        // Le agregamos la función de eliminar al botoncito que acabamos de crear
        nuevoElemento.querySelector('button').addEventListener('click', function() {
            nuevoElemento.remove(); // Borra el elemento de la pantalla
            totalRegistros--;       // Resta uno al total
            contador.textContent = totalRegistros; // Actualiza el texto
        });

        // Pegamos el nuevo elemento en la lista de la pantalla
        lista.appendChild(nuevoElemento);

        // --- CONTAR ---
        totalRegistros++;
        contador.textContent = totalRegistros;

        // Mostrar mensaje de éxito
        mensaje.textContent = "Registro exitoso";
        mensaje.className = "alert alert-success d-block";

        // Limpiar el formulario y quitar los bordes verdes
        form.reset();
        titulo.className = "form-control";
        desc.className = "form-control";
        estado.className = "form-control";

    } else {
        // Mostrar mensaje de error si algo falló
        mensaje.textContent = "Por favor, corrija los campos en rojo";
        mensaje.className = "alert alert-danger d-block";
    }

    // Ocultar el mensaje (sea de éxito o error) después de 3 segundos
    setTimeout(function() {
        mensaje.className = "alert d-none";
    }, 3000);
});