async function select_all(table){
    try {
        const response = await axios.get(`/data/${table}/body`);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

async function select_columns(table){
    try {
        const response = await axios.get(`/data/${table}/columns`);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

function create_table(table_name){
    select_all(table_name).then(result => {
        let table_body = result;
        select_columns(table_name).then(result => {
            let table_columns = result.map(column => ({ field: column, filter: true}));

            table_columns.push({
                headerName: "Acciones",
                cellRenderer: function() {
                    return '<button type="button" class="btn-edit btn btn-warning"><i class="bi bi-pencil-square "></i></button><button type="button" class="btn-delete btn btn-danger mr-3 pr-3"><i class="bi bi-trash mr-3 pr-3"></i></button>';
                },
                sortable: false,
                filter: false,
                minWidth: 150,
                maxWidth: 150
            });

            const gridOptions = {
                rowData: table_body,
                columnDefs: table_columns,
                defaultColDef: {
                    flex: 1,
                    filter: "agTextColumnFilter",
                    floatingFilter: true,
                },
                pagination: true,
                paginationPageSize: 10,
                paginationPageSizeSelector: [10,20,50,100],
                onFirstDataRendered: function(params) {
                    params.api.autoSizeColumns();
                }
            }

            const table = document.querySelector("#main_table");
            while (table.firstChild) {
                table.removeChild(table.firstChild);
            }

            gridApi = agGrid.createGrid(document.querySelector("#main_table"), gridOptions);

            localStorage.setItem('currentTable', table_name);
        });
    });
}

const navbar_tables = document.querySelectorAll(".nav-link");
var bsOffcanvas = new bootstrap.Offcanvas(document.querySelector("#offcanvasDarkNavbar"));

navbar_tables.forEach(navbar => {
    navbar.addEventListener("click", function (event) {
        event.preventDefault()
        const table_name = this.getAttribute("href");
        console.log(table_name)
        create_table(table_name)

        history.pushState(null, '', table_name);

        bsOffcanvas.hide();
    })
})

window.onload = function() {
    const currentTable = localStorage.getItem('currentTable');
    if (currentTable) {
        create_table(currentTable);
    }
};