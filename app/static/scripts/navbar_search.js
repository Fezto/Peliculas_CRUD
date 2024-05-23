$(document).ready(function(){
    $("#search").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $(".table_name").each(function() {
            var text = $(this).text().toLowerCase();
            if (text.indexOf(value) > -1) {
                $(this).animate({opacity: '1'}, 200); // Restaura la opacidad a 1 con una animación
                $(this).css('pointer-events', 'auto'); // Hace el elemento clickeable
                $(this).find('a').removeClass('disabled'); // Habilita el enlace
            } else {
                $(this).animate({opacity: '0.2'}, 200); // Reduce la opacidad a 0.2 con una animación
                $(this).css('pointer-events', 'none'); // Hace el elemento no clickeable
                $(this).find('a').addClass('disabled'); // Deshabilita el enlace
            }
        });
    });
});