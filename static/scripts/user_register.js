function editarContraseña() {
    // Habilitar la edición de contraseñas
    document.getElementById('contrasena').disabled = false;
    document.getElementById('confirmar-contrasena').disabled = false;
}

function guardarCambios() {
    // Obtener los nuevos valores
    var nuevaContrasena = document.getElementById('contrasena').value;
    var confirmarNuevaContrasena = document.getElementById('confirmar-contrasena').value;

    // Validar que las contraseñas coincidan
    if (nuevaContrasena !== confirmarNuevaContrasena) {
        alert('Las contraseñas no coinciden');
        return;
    }

    // Aquí puedes enviar los datos actualizados al servidor o hacer otras operaciones según tus necesidades

    // Deshabilitar la edición después de guardar cambios
    document.getElementById('contrasena').disabled = true;
    document.getElementById('confirmar-contrasena').disabled = true;

    // Mensaje de éxito (puedes adaptarlo a tus necesidades)
    alert('Cambios guardados correctamente');
}