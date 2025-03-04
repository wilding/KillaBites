$(function() {


    // filter recipes on pageback
    var selected_cuisine = $('.dropdown-cuisine option:selected').text();
    var selected_course = $('.dropdown-course option:selected').text();
    var selected_group = $('.dropdown-group option:selected').text();
    // var selected_month = $('.dropdown-month option:selected').text();
    $('tbody tr').each(function () {
        if ($(this).hasClass('cuisine-' + selected_cuisine) === true && $(this).hasClass('course-' + selected_course) === true && $(this).hasClass('group-' + selected_group) === true) {
            $(this).removeClass('hide-recipe');
        }
        else {
            $(this).addClass('hide-recipe');
        }
    });
    // show/hide the clear button
    if (selected_cuisine != 'Cuisine') {
        $('.dropdown-cuisine').siblings().css('visibility', 'visible');
    }
    if (selected_course != 'Course') {
        $('.dropdown-course').siblings().css('visibility', 'visible');
    }
    if (selected_group != 'Group') {
        $('.dropdown-group').siblings().css('visibility', 'visible');
    }
    // if (selected_month != 'Month') {
    //     $('.dropdown-month').siblings().css('visibility', 'visible');
    // }


    // filter by dropdown menu
    $('select').change(function () {
        var selected_cuisine = $('.dropdown-cuisine option:selected').text();
        var selected_course = $('.dropdown-course option:selected').text();
        var selected_group = $('.dropdown-group option:selected').text();
        // var selected_month = $('.dropdown-month option:selected').text();
        var monthlist = $('.menu-month-container').find('.checkbox');
        let checkedmonths = [];
        monthlist.each(function() {
            if ($(this).prop('checked')) {
                checkedmonths.push($(this).prop('name'));
            }
        });
        // show/hide the clear button
        if (['Cuisine', 'Course', 'Group', 'Month'].indexOf($(this).val()) == -1) {
            $(this).siblings().css('visibility', 'visible');
        }
        else {
            $(this).siblings().css('visibility', 'hidden');
        }
        // filter the recipes
        $('tbody tr').each(function () {
            if (checkedmonths.length === 0 && $(this).hasClass('cuisine-' + selected_cuisine) === true && $(this).hasClass('course-' + selected_course) === true && $(this).hasClass('group-' + selected_group) === true) {
                    $(this).removeClass('hide-recipe');
            } else {
                let othermonth = false;
                for (m in checkedmonths) {
                    if ($(this).hasClass('month-' + checkedmonths[m]) === true) {
                        othermonth = true;
                    }
                }
                if (othermonth === true && $(this).hasClass('cuisine-' + selected_cuisine) === true && $(this).hasClass('course-' + selected_course) === true && $(this).hasClass('group-' + selected_group) === true) {
                    $(this).removeClass('hide-recipe');
                }
                else {
                    $(this).addClass('hide-recipe');
                }
            }
        });
    });

    // deselect dropdown menu
    $('.fa-times-circle').click( function() {
        var select = $(this).siblings().attr('class').slice(9);
        select = select.charAt(0).toUpperCase() + select.slice(1);
        $(this).siblings().val(select).change();
    });

    // filter months by clicking month cells
    $('.checkbox').click(function() {
        var selected_month = $(this).prop('name');
        var monthlist = $(this).parents('.menu-month-container').siblings().find('.checkbox');
        let checkedmonths = [];
        monthlist.each(function() {
            if ($(this).prop('checked')) {
                checkedmonths.push($(this).prop('name'));
            }
        })
        var selected_cuisine = $('.dropdown-cuisine option:selected').text();
        var selected_course = $('.dropdown-course option:selected').text();
        var selected_group = $('.dropdown-group option:selected').text();
        // click month ON
        if ($(this).prop('checked')) {
            $(this).parents('.menu-month-container').css('background', '#ab1c20');
            if (event.metaKey) {
                // Actions to perform when command + click occurs
                $('tbody tr').each(function () {
                    if ($(this).hasClass('month-' + selected_month) === true && $(this).hasClass('cuisine-' + selected_cuisine) === true && $(this).hasClass('course-' + selected_course) === true && $(this).hasClass('group-' + selected_group) === true) {
                        $(this).removeClass('hide-recipe');
                    } else if (checkedmonths.length === 0) {
                        $(this).addClass('hide-recipe');
                    }
                });
              } else {
                // Actions to perform when a regular click occurs without the command key
                $(this).parents('.menu-month-container').siblings().find('.checkbox').prop('checked', false);
                $(this).parents('.menu-month-container').siblings().css('background', 'none');
                $('tbody tr').each(function () {
                    if ($(this).hasClass('month-' + selected_month) === true && $(this).hasClass('cuisine-' + selected_cuisine) === true && $(this).hasClass('course-' + selected_course) === true && $(this).hasClass('group-' + selected_group) === true) {
                        $(this).removeClass('hide-recipe');
                    } else {
                        $(this).addClass('hide-recipe');
                    }
                });
              }            
        // click month OFF
        } else {
            $(this).parents('.menu-month-container').css('background', 'none');
            $('tbody tr').each(function () {
                // clearing last checked month
                if (checkedmonths.length === 0 && $(this).hasClass('cuisine-' + selected_cuisine) === true && $(this).hasClass('course-' + selected_course) === true && $(this).hasClass('group-' + selected_group) === true) {
                    $(this).removeClass('hide-recipe');
                // a different month is still checked
                } else {
                    let othermonth = false;
                    for (m in checkedmonths) {
                        if ($(this).hasClass('month-' + checkedmonths[m]) === true) {
                            othermonth = true;
                        }
                    }
                    if ($(this).hasClass('month-' + selected_month) === true && othermonth === false) {
                        $(this).addClass('hide-recipe');
                    }
                }
            });
        }
    });
});
