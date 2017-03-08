$(function() {

    // highlight ingredients when clicked
    $('.homepage-pic').click(function () {
        $(this).parent().toggleClass('active-ingredient');
    });

});
