$(function() {

    // Click through pictures using arrows on the recipe card
    $('.recipe-pic-arrows').click(function (e) {
        var background_list = $(this).parent().css('background-image').split(', ');
        if ($(this).find('.fa').hasClass('fa-chevron-left')) {
            var new_background = background_list.pop();
            for (i in background_list) {
                new_background += ',' + background_list[i];
            }
            $('.recipe-pictures').css('background-image', new_background);
        }
        else {
            var old_background = background_list[0];
            var new_background = background_list[1];
            for (i in background_list) {
                if (i != 0 && i != 1) {
                    new_background += ',' + background_list[i];
                }
            }
            new_background += ',' + old_background;
            $('.recipe-pictures').css('background-image', new_background);
        }
    });


    // Click through pictures using arrows on the large picture popup
    $('.picture-popup-arrows').click(function(e) {
        var current = $(this).siblings('img:not(.hidden)');
        if ($(this).find('.fa').hasClass('fa-chevron-left')) {
            if ($('.picture-popup').find('img').first().hasClass('hidden')) {
                current.addClass('hidden');
                current.prev('img').removeClass('hidden');
            }
            else {
                current.addClass('hidden');
                $('.picture-popup').find('img').last().removeClass('hidden');
            }
        }
        else {
            if ($('.picture-popup').find('img').last().hasClass('hidden')) {
                current.addClass('hidden');
                current.next('img').removeClass('hidden');
            }
            else {
                current.addClass('hidden');
                $('.picture-popup').find('img').first().removeClass('hidden');
            }
        }
    });


    // Show large picture popup when double clicking the picture
    $('.recipe-pic-button').dblclick(function (e) {
        var background = $(this).parent().css('background-image').split(', ')[0].slice(4, -1);
        background = background.replace('http://localhost:8080', '');
        $('.picture-popup-background').removeClass('hidden');
        $('.picture-popup').find('[src=' + background + ']').removeClass('hidden');
    });


    // Close the large picture popup by clicking the popup background
    $('.picture-popup-background').click(function (e) {
        if ($(e.target).is('.picture-popup-background')) {
            $('.picture-popup-background').addClass('hidden');
            $('.picture-popup').find('img:not(.hidden)').addClass('hidden');
        }
    });


});


$(document).keyup(function(e) {
    if (e.which == 27) {
        $('.picture-popup-background').click();
        console.log('esc!');
    }
    else if (e.which == 37) {
        $('.picture-popup-arrows').find('.fa-chevron-left').click();
    }
    else if (e.which == 39) {
        $('.picture-popup-arrows').find('.fa-chevron-right').click();
    }
});
