$(function() {


    /////////////// table header /////////////////////////////////////////////


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


    /////////////// sort table rows /////////////////////////////////////////////


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


    /////////////// edit ingredient forms /////////////////////////////////////////////


    // add name fields when the + button is clicked
    $(".add-alts").click(function () {
        var id = $(this).parent().siblings('.name-fields').attr('data-id');
        $(this).parent().siblings('.name-fields').append('<div class="added-name"><input name="alt" type="text" maxlength="500" form="ingredient_form_' + id + '"><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>');
    });


    // remove name fields when the - button is clicked and save original deleted names
    $('body').on('click', '.delete', function () {
        if ($(this).parent().hasClass('og-name')) {
            var name = $(this).siblings('input[name=alt]').val();
            var id = $(this).parents('.name-fields').attr('data-id')
            if (deleted_names[id]) {
                deleted_names[id].push(name);
            } else {
                deleted_names[id] = [name];
            }
        }
        $(this).parent("div").remove();
    });


    // edit ingredient months by clicking month cells
    $('.checkbox').click(function() {
        var group = $(this).parents('.ingredient-month-menu').siblings('.group-menu').find('input[name=group]:checked').val();
        if ($(this).prop('checked')) {
           $(this).parents('.ingredient-month-container').css('background', ingredient_group_colors[group][0]);
        } else {
            $(this).parents('.ingredient-month-container').css('background', 'none');
        }
    });


    // change month input colors by clicking on different groups
    $('input[name=group]').click(function() {
        var group = $(this).val();
        var month_menu = $(this).parents('.group-menu').siblings('.ingredient-month-menu')
        var months = month_menu.find('input[type=checkbox]:checked');
        month_menu.css('background', ingredient_group_colors[group][1]);
        months.each(function() {
            $(this).parents('.ingredient-month-container').css('background', ingredient_group_colors[group][0]);
        });
    });


    // select full picture url by clicking textarea
    $('.triple-container-1').click(function() {
        $(this).find('textarea').select();
    });


    // show and hide 'are you sure you want to delete' warning by clicking delete and cancel buttons
    $('.soft-delete').click(function() {
        $(this).parents('.triple-container-3').addClass('hide-buttons');
        $(this).parents('.triple-container-3').siblings('.triple-container-3').removeClass('hide-buttons');
    });


    // show edit ingredient row when edit button is clicked
    $('.fa-pencil-square-o').click(function() {
        $(this).parents('.chart-row').css('display', 'none');
        $(this).parents('.chart-row').next('.edit-chart-row').css('display', 'table-row');
    });


    // hide edit ingredient row when cancel button is clicked
    $('.cancel-ingredient-button').click(function() {
        $(this).parents('.edit-chart-row').css('display', 'none');
        $(this).parents('.edit-chart-row').prev('.chart-row').css('display', 'table-row');
    });


    // correctly reset month input background and name input when the reset button is clicked
    $('.reset-ingredient-button').click(function() {
        var group = $(this).parents('.edit-chart-row').siblings().prev('.title-row').find('.group-title').text().toLowerCase();
        var month_menu = $(this).parents('.edit-ingredient-triple').siblings('.ingredient-month-menu');
        var months = month_menu.find('.og-checkbox');
        month_menu.css('background', ingredient_group_colors[group][1]);
        month_menu.find('.ingredient-month-container').css('background', 'none');
        months.each(function() {
            $(this).parents('.ingredient-month-container').css('background', ingredient_group_colors[group][0]);
        });
        $(this).parents('.edit-ingredient-cell').siblings('.edit-ingredient-name-cell').find('.added-name').remove();
        var id = $(this).attr('data-id');
        var name_fields = $(this).parents('.edit-chart-row').find('.name-fields');
        var names_to_add = deleted_names[id];
        for (i in names_to_add) {
            name_fields.append('<div class="og-name"><input name="alt" type="text" maxlength="500" form="ingredient_form" value="' + names_to_add[i] + '"><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>');
        };
        deleted_names[id] = [];
    });


    // correctly reset month input background and name input when the reset button is clicked
    $('.reset-new-ingredient-button').click(function() {
        var month_menu = $(this).parents('.edit-ingredient-triple').siblings('.ingredient-month-menu');
        month_menu.css('background', 'rgba(123, 31, 162, 0.3)');
        month_menu.find('.ingredient-month-container').css('background', 'none');
        $(this).parents('.edit-ingredient-cell').siblings('.edit-ingredient-name-cell').find('.added-name').remove();
    });


    // show new ingredient row when the + button is clicked
    $('.add-ingredient-link').click( function () {
        $('.new-ingredient').addClass('show-group');
        $('.new-ingredient').find('input[name=name]').focus();
    });
    // hide new ingredient row when cancel button is clicked
    $('.cancel-new-ingredient-button').click(function() {
        $('.new-ingredient').removeClass('show-group');
    });


});


// json with ingredient groups as keys and lists of colors as values
var ingredient_group_colors = {
    'fruit': ['#7B1FA2', 'rgba(123, 31, 162, 0.3)'],
    'vegetables': ['#43A047', 'rgba(67, 160, 71, 0.3)'],
    'herbs': ['#7CB342', 'rgba(124, 179, 66, 0.3)'],
    'nuts': ['#6D4C41', 'rgba(109, 76, 65, 0.3)'],
    'sea': ['#1E88E5', 'rgba(30, 136, 229, 0.3)'],
    'air': ['#FDD835', 'rgba(253, 216, 53, 0.3)'],
    'land': ['#E53935', 'rgba(229, 57, 53, 0.3)']
};


var deleted_names = {};


// helper function for fixing header row to the top when scrolling
var headerScroll = function () {
    var header = $('.relative-header');
    var offset = header.offset();
    var scrolltop = $(window).scrollTop();
    var fixed_header = $('.fixed-header');
    if (scrolltop > offset.top) {
        fixed_header.css('display', 'table');
    } else {
        fixed_header.css('display', 'none');
    }
};
