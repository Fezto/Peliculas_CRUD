
function show_modal({id, action, registry_id = null}){
    let modal_element = document.getElementById(id ?? "main_modal");
    let modal_title = document.querySelector(".modal-title")

    modal_title.textContent = action === "POST" ? "Añadir registro" : "Editar Registro"
    modal_element.setAttribute("action", action)
    modal_element.setAttribute("registry-id", registry_id)
    let modal_instance = new bootstrap.Modal(modal_element, {});
    modal_instance.show();
}

function get_current_table_name(){
    return window.location.pathname.split('/')[2];
}