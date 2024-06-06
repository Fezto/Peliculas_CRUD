class ButtonCellRenderer {
    init(params) {
        this.params = params;
        this.eGui = document.createElement('div');


        let editButton = document.createElement('button');
        editButton.className = "btn-edit btn btn-warning";
        editButton.innerHTML = '<i class="bi bi-pencil-square "></i>';
        editButton.addEventListener('click', () => {
            let modalElement = document.getElementById('modalId'); // Reemplaza 'modalId' con el ID de tu modal
            let modalInstance = new bootstrap.Modal(modalElement, {}); // Establece el contenido del modal
            modalInstance.show();
        });

        let deleteButton = document.createElement('button');
        deleteButton.className = "btn-delete btn btn-danger";
        deleteButton.innerHTML = '<i class="bi bi-trash "></i>';
        deleteButton.addEventListener('click', () => {
            const table_name = document.querySelector("#main_table").getAttribute("data-table-name")
            const rowData = this.params.node.data;
            const id = rowData.id
            axios.delete(`/index/${table_name}/${id}`)
            gridApi.applyTransaction({ remove: [rowData] });
        });

        this.eGui.appendChild(editButton);
        this.eGui.appendChild(deleteButton);
    }

    getGui() {
        return this.eGui;
    }

    refresh(params) {
        return true;
    }
}