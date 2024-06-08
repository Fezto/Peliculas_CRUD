let modal = document.getElementById("main_modal")
let modal_form = document.getElementById("modal_form")

modal_form.addEventListener("submit", async function (event) {
    event.preventDefault()

    const table_name = get_current_table_name()
    let formData = new FormData(this);
    axios({
        method: "POST",
        url: `/index/${table_name}`,
        data: formData,
        headers: {
            "X-Requested-With": "XMLHttpRequest",
        }
    }).then(function(response) {
        console.log(response.data.message);
        create_table(table_name)
    }).catch(function(error) {
        console.log(error);
    });

    let bootstrapModal = bootstrap.Modal.getInstance(modal)
    bootstrapModal.hide()
});

let addButton = document.querySelector(".btn-add")
addButton.addEventListener('click', () => {
show_modal({id: "main_modal"})
});

