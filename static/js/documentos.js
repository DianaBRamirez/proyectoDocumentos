function confirmarEliminacion() {
    if (confirm("¿Desea borrar la actividad?")) {
      // Aquí va el código que ejecutará la acción de eliminación
      alert("Elemento eliminado exitosamente.");
      return true; // Permite que se complete la acción
    } else {
      return false; // Cancela la acción
    }
  }

  function confirmarAgregar() {
    if (confirm("¿Desea guardar el registro?")) {
      // Aquí va el código que ejecutará la acción de eliminación
      alert("Registro guardado");
      return true; // Permite que se complete la acción
    } else {
      return false; // Cancela la acción
    }
  }

  function confirmarEditar() {
    if (confirm("¿Desea guardar los cambios?")) {
      // Aquí va el código que ejecutará la acción de eliminación
      alert("Registro guardado");
      return true; // Permite que se complete la acción
    } else {
      return false; // Cancela la acción
    }
  }