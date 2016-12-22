$(function() {
    //when the Add Field button is clicked
    $("#add-alts").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#name-fields").append('<i>, </i><input name="alt" type="text" maxlength="500"><i class="fa fa-minus-circle delete" aria-hidden="true"></i>'); });

    $("#add-pics").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#pic-fields").append('<div><input type="text" name="pictures" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>'); });

    $("#add-sources").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#source-fields").append('<div><input type="text" name="sources" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>'); });

    $("#add-occasions").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#occasion-fields").append('<div><input type="text" name="occasions" maxlength="500"><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>'); });

    $("#add-ingredients").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#ingredient-fields").append('<div><input type="text" name="ingredients" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>'); });

    $("#add-instructions").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#instruction-fields").append('<div><label>Text: <input type="text" name="instructions-text" maxlength="9999"></label><label>Photo: <input type="text" name="instructions-photo" maxlength="9999"></label><label>Video: <input type="text" name="instructions-video" maxlength="9999"></label><label>Gif: <input type="text" name="instructions-gif" maxlength="9999"></label><label>Note: <input type="text" name="instructions-note" maxlength="9999"></label><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>'); });

    $("body").on("click", ".delete", function (e) {
        $(this).parent("div").remove();
    });

    $(window).scroll(headerScroll);

    // $('.chart-group-tab').dblclick(function () {
    //     var number_active = $('.active').length;
    //     if (number_active === 0) {
    //         $('tbody').toggleClass('show-group');
    //     }
    //     $(this).toggleClass('chart-cell-' + $(this).text().toLowerCase());
    //     $(this).toggleClass('active');
    //     var tablestring = '.' + $(this).text().toLowerCase() + '-table';
    //     $(tablestring).toggleClass('show-group');
    //     if ((number_active === 1) && (!($(this).hasClass('active')))) {
    //         $('tbody').addClass('show-group');
    //     }
    // });

    $('.chart-group-tab').click(function () {
        if ($(this).hasClass('active') === true) {
            $(this).toggleClass('chart-cell-' + $(this).text().toLowerCase());
            $(this).toggleClass('active');
            $('tbody').addClass('show-group');
        } else {
            $('tbody').removeClass('show-group');
            $('.chart-group-tab').removeClass('chart-cell-fruit chart-cell-vegetables chart-cell-herbs chart-cell-nuts chart-cell-sea chart-cell-air chart-cell-land active');
            $(this).toggleClass('chart-cell-' + $(this).text().toLowerCase());
            $(this).toggleClass('active');
            var tablestring = '.' + $(this).text().toLowerCase() + '-table';
            $(tablestring).toggleClass('show-group');
        }
    });


    $('.fa-sort-alpha-asc').click(function () {
        var this_table = '.' + $(this).parents('tbody').attr('class').split(" ")[0];
        $(this_table).find('.fa-calendar').each(function() {
            $(this).removeAttr('id');
        });
        $(this_table).find('.fa-sort-alpha-asc').each(function() {
            $(this).attr('id', 'active-sort');
        });
        $(this_table).slice(1).addClass('hide-sort');
        $(this_table).slice(0, 1).removeClass('hide-sort');
    });

    $('.fa-calendar').click(function () {
        var this_table = '.' + $(this).parents('tbody').attr('class').split(" ")[0];
        $(this_table).find('.fa-sort-alpha-asc').each(function() {
            $(this).removeAttr('id');
        });
        $(this_table).find('.fa-calendar').each(function() {
            $(this).attr('id', 'active-sort');
        });
        $(this_table).slice(0, 1).addClass('hide-sort');
        $(this_table).slice(1).removeClass('hide-sort');
    });

});

var showDeleteIngredient = function (index, table) {
    var row = $(table).children(".chart-row")[index];
    $(row).children('.month-cell').css('display', 'none');
    $(row).find('.delete-ingredient-cell').css('display', "table-cell");
}

var showChartRow = function (index, table) {
    var row = $(table).children(".chart-row")[index];
    $(row).find('.delete-ingredient-cell').css('display', "none");
    $(row).children('.month-cell').css('display', 'table-cell');
}

var headerScroll = function () {
    var header = $('.relative-header');
    var offset = header.offset();
    var scrolltop = $(window).scrollTop();
    var fixed_header = $('.fixed-header');
    if (scrolltop > offset.top) {
        fixed_header.css("display", "table");
    } else {
        fixed_header.css("display", "none");
    };
}
