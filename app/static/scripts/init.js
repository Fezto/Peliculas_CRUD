function show_modal({id}){
    let modal_element = document.getElementById(id ?? "main_modal");
    let modal_instance = new bootstrap.Modal(modal_element, {});
    modal_instance.show();
}

function get_current_table_name(){
    return window.location.pathname.split('/')[2];
}