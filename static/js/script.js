// --- COMPLEMENTO SEMANA 8: CONTROL DE SPINNER SIMULADO ---
// Capturamos el spinner que agregamos en el HTML
const spinnerCarga = document.getElementById('spinnerCarga');

form.addEventListener('submit', function(evento) {
    // Si los campos son válidos (reutilizando tus variables lógicas)
    let tValido = validarTitulo();
    let dValida = validarDesc();
    let eValido = validarEstado();

    if (tValido && dValida && eValido) {
        // Mostramos el spinner quitando la clase 'd-none' de Bootstrap
        spinnerCarga.classList.remove('d-none');
        
        // Simulamos la carga por 1.5 segundos y luego lo volvemos a ocultar
        setTimeout(function() {
            spinnerCarga.classList.add('d-none');
        }, 1500);
    }
});