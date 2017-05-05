$(function() {

    // highlight ingredients when clicked
    $('.homepage-pic').click(function () {
        $(this).parent().toggleClass('active-ingredient');
    });


    $('.course-switcher-option').click(function() {
        $(this).siblings().removeClass('course-switcher-selected');
        $(this).addClass('course-switcher-selected');
        var course = $(this).text();
        $('.homepage-courses-' + course.split(' ')[0]).siblings().css('display', 'none');
        $('.homepage-courses-' + course.split(' ')[0]).css('display', 'block');
    });

});
