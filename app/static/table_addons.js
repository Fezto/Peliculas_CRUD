$(document).ready(function () {
    $('#data').DataTable({
        language: {
            processing:     "Procesando...",
            search:         "Buscar:",
            lengthMenu:    "Mostrar primeros _MENU_",
            info:           "Mostrando de _START_ a _END_ de _TOTAL_ elementos",
            infoEmpty:      "Mostrando 0 elementos",
            infoFiltered:   "(filtrado de _MAX_ elementos en total)",
            infoPostFix:    "",
            loadingRecords: "Cargando registros...",
            zeroRecords:    "No se encontraron registros",
            emptyTable:     "No hay datos disponibles en la tabla",
            paginate: {
                first:      "Primero",
                previous:   "<",
                next:       ">",
                last:       "Último"
            },
            aria: {
                sortAscending:  ": activar para ordenar la columna de manera ascendente",
                sortDescending: ": activar para ordenar la columna de manera descendente"
            }
        }
    });
});

