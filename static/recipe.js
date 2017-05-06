$(function() {

    $('.recipe-pic-arrows').click(function (e) {
        var background_list = $(this).parent().css('background-image').split(' ');
        if ($(this).find('.fa').hasClass('fa-chevron-left')) {
            var new_background = background_list.pop();
            for (i in background_list) {
                new_background += ',' + background_list[i].slice(0, -1);
            }
            $('.recipe-pictures').css('background-image', new_background);
        }
        else {
            var old_background = background_list[0].slice(0, -1);
            var new_background = background_list[1].slice(0, -1);
            for (i in background_list) {
                if (i != 0 && i != 1) {
                    new_background += ',' + background_list[i];
                }
            }
            new_background += ',' + old_background;
            $('.recipe-pictures').css('background-image', new_background);
        }
    });

});
