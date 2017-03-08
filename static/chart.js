$(function() {


    // add name fields when the + button is clicked
    $("#add-alts").click(function (e) {
        $("#name-fields").append('<i>, </i><input name="alt" type="text" maxlength="500"><i class="fa fa-minus-circle delete" aria-hidden="true"></i>'); });


    // remove name fields when the - button is clicked
    $("body").on("click", ".delete", function (e) {
        $(this).parent("div").remove();
    });


    // fix header row to top when scrolling down
    $(window).scroll(headerScroll);


    // filter chart by group by clicking tabs
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


    // sort group alphabetically by clicking a->z symbol
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


    // sort group by month by clicking calendar symbol
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


// show delete ingredient cell when trash button is clicked
var showDeleteIngredient = function (index, table) {
    var row = $(table).children(".chart-row")[index];
    $(row).children('.month-cell').css('display', 'none');
    $(row).find('.delete-ingredient-cell').css('display', "table-cell");
}


// show regular chart row when cancel is clicked from the delete ingredient cell
var showChartRow = function (index, table) {
    var row = $(table).children(".chart-row")[index];
    $(row).find('.delete-ingredient-cell').css('display', "none");
    $(row).children('.month-cell').css('display', 'table-cell');
}


// helper function for fixing header row to the top when scrolling
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
