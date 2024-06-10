/**
 * Esta función muestra un modal con un determinado id, acción y id de registro.
 *
 * @param {Object} params - Un objeto que contiene los parámetros para la función.
 * @param {string} params.id - El id del modal a mostrar.
 * @param {string} params.action - La acción a realizar (POST o PUT).
 * @param {string} [params.registry_id=null] - El id del registro a modificar (solo para PUT).
 */

function show_modal({id, action, registry_id = null}){
    let modal_element = document.getElementById(id ?? "main_modal");
    modal_element.setAttribute("action", action)
    modal_element.setAttribute("registry-id", registry_id)
    let modal_instance = new bootstrap.Modal(modal_element, {});
    modal_instance.show();
}

/**
 * Esta función obtiene el nombre de la tabla actual a partir de la URL de la página.
 *
 * @returns {string} El nombre de la tabla actual.
 */
function get_current_table_name(){
    return window.location.pathname.split('/')[2];
}