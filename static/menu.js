$(function() {


    // filter recipes on pageback
    var selected_cuisine = $('.dropdown-cuisine option:selected').text();
    var selected_course = $('.dropdown-course option:selected').text();
    var selected_group = $('.dropdown-group option:selected').text();
    var selected_month = $('.dropdown-month option:selected').text();
    $('tbody tr').each(function () {
        if ($(this).hasClass('cuisine-' + selected_cuisine) === true && $(this).hasClass('course-' + selected_course) === true && $(this).hasClass('group-' + selected_group) === true && $(this).hasClass('month-' + selected_month) === true) {
            $(this).removeClass('hide-recipe');
        }
        else {
            $(this).addClass('hide-recipe');
        }
    });


    // cuisine dropdown menu
    $('select').change(function () {
        var selected_cuisine = $('.dropdown-cuisine option:selected').text();
        var selected_course = $('.dropdown-course option:selected').text();
        var selected_group = $('.dropdown-group option:selected').text();
        var selected_month = $('.dropdown-month option:selected').text();
        // show/hide the clear button
        if (['Cuisine', 'Course', 'Group', 'Month'].indexOf($(this).val()) == -1) {
            $(this).siblings().css('visibility', 'visible');
        }
        else {
            $(this).siblings().css('visibility', 'hidden');
        }
        // filter the recipes
        $('tbody tr').each(function () {
            if ($(this).hasClass('cuisine-' + selected_cuisine) === true && $(this).hasClass('course-' + selected_course) === true && $(this).hasClass('group-' + selected_group) === true && $(this).hasClass('month-' + selected_month) === true) {
                $(this).removeClass('hide-recipe');
            }
            else {
                $(this).addClass('hide-recipe');
            }
        });
    });

    $('.fa-times-circle').click( function() {
        var select = $(this).siblings().attr('class').slice(9);
        select = select.charAt(0).toUpperCase() + select.slice(1);
        $(this).siblings().val(select).change();
    });
});
