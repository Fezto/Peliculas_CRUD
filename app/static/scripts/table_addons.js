async function select_all(table) {

    const response = await axios.get(`/data/${table}/body`);
    return response.data;

}

async function select_columns(table) {
    const response = await axios.get(`/data/${table}/columns`);
    return response.data;
}

function create_table(table_name) {
    select_all(table_name).then(result => {
        let table_body = result;
        select_columns(table_name).then(result => {
            let table_columns = result.map(column => ({field: column, filter: true}));

            table_columns.push({
                headerName: "",
                cellRenderer: ButtonCellRenderer,
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
                paginationPageSizeSelector: [10, 20, 50, 100]
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
const bsOffcanvas = new bootstrap.Offcanvas(document.querySelector("#offcanvasDarkNavbar"));

navbar_tables.forEach(navbar => {
    navbar.addEventListener("click", function (event) {
        const table_name = this.getAttribute("href");
        bsOffcanvas.hide();
    })
})

window.onload = function () {
    const currentTable = window.location.pathname.split('/')[2];
    if (currentTable) {
        create_table(currentTable);
    }
};
