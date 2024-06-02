$(document).ready(function () {
    let table = $('#data').DataTable({
        language: {
            processing: "Procesando...",
            search: "Buscar:",
            lengthMenu: "Mostrar primeros _MENU_",
            info: "Mostrando de _START_ a _END_ de _TOTAL_ elementos",
            infoEmpty: "Mostrando 0 elementos",
            infoFiltered: "(filtrado de _MAX_ elementos en total)",
            infoPostFix: "",
            loadingRecords: "Cargando registros...",
            zeroRecords: "No se encontraron registros",
            emptyTable: "No hay datos disponibles en la tabla",
            paginate: {
                first: "Primero",
                previous: "<",
                next: ">",
                last: "Último"
            },
            aria: {
                sortAscending: ": activar para ordenar la columna de manera ascendente",
                sortDescending: ": activar para ordenar la columna de manera descendente"
            }
        },
        columnDefs: [
            {
                targets: -1,
                data: null,
                defaultContent: '<button type="button" class="btn-edit btn btn-warning"><i class="bi bi-pencil-square "></i></button><button type="button" class="btn-delete btn btn-danger mr-3 pr-3"><i class="bi bi-trash mr-3 pr-3"></i></button>',
            }
        ]


    });

    $('#data tbody').on('click', '.btn-edit', function () {
        let registry = table.row($(this).parents("tr"));
        let registry_data = registry.data()
        let id = registry_data[0]

        let table_name = $("#data").attr("name")

        let formData = {}

        // Seleccionar todos los inputs del formulario y obtener su nombre y valor
        $('form :input').each(function(){
            let input = $(this); // This is the jquery object of the input, complete with jQuery goodness
            formData[input.attr('name')] = input.val();
        });

        console.log(formData)



    });

    $('#data tbody').on('click', '.btn-delete', function () {
        let registry = table.row($(this).parents('tr'));
        let registry_data = registry.data()
        let id = registry_data[0]

        let table_name = $("#data").attr("name")

        let formData = {}

        $.ajax({
            url: `/index/${table_name}/${id}`,
            type: "DELETE",
            data: {"id": id},
            success: () => registry.remove().draw(),
            error: () => console.log("Error al realizar la eliminación!")
        })
    });
});

