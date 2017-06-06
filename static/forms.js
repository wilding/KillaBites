$(function() {

    // remove name fields when the - button is clicked
    $("body").on("click", ".delete", function (e) {
        $(this).parent("div").remove();
    });

    // add picture fields when the + button is clicked
    $("body").on("click", ".add-pictures", function (e) {
        $('<div><input type="text" name="pictures" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i><i class="fa fa-plus-circle add add-pictures" aria-hidden="true"></i></div>').insertAfter($(this).parent());
    });

    // add source fields when the + button is clicked
    $("body").on("click", ".add-sources", function (e) {
        $('<div><input type="text" name="sources" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i><i class="fa fa-plus-circle add add-sources" aria-hidden="true"></i></div>').insertAfter($(this).parent());
    });

    // add occasion fields when the + button is clicked
    $("body").on("click", ".add-occasions", function (e) {
        $('<div><input type="text" name="occasions" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i><i class="fa fa-plus-circle add add-occasions" aria-hidden="true"></i></div>').insertAfter($(this).parent());
    });

    // add instruction fields when the + button is clicked
    $("body").on("click", ".add-instructions", function (e) {
        $('<div class="instruction-cell"><label>- <input type="text" name="instructions-text" maxlength="9999"></label><i class="fa fa-minus-circle delete" aria-hidden="true"></i><i class="fa fa-plus-circle add add-instructions" aria-hidden="true"></i><label>Photo: <input type="text" name="instructions-photo" maxlength="9999"></label><label>Video: <input type="text" name="instructions-video" maxlength="9999"></label><label>Gif: <input type="text" name="instructions-gif" maxlength="9999"></label><label>Note: <input type="text" name="instructions-note" maxlength="9999"></label></div>').insertAfter($(this).parent());
    });



    // $('input[name=ingredients]').keyup(function(e) {
    //     if (e.which == 38) {
    //         console.log('up');
    //         e.preventDefault();
    //         $(this).parent().prev().find('input').select();
    //     }
    //     else if (e.which == 40) {
    //         e.preventDefault();
    //         console.log('down');
    //         $(this).parent().next().find('input').select();
    //     }
    // });

    // navigate ingredient inputs with enter and delete keys
    $('body').on('keydown', 'input[name=ingredients]', function(e) {
        if (e.which == 13) {
            e.preventDefault();
            $('<div><input type="text" name="ingredients" maxlength="9999"></div>').insertAfter($(this).parent());
            $(this).parent().next().find('input').select();
        }
        else if (e.which == 8) {
            if ($(this).val().length == 0) {
                e.preventDefault();
                $(this).parent().prev().find('input').focus();
                $(this).parent("div").remove();
            }
        }

    });

    // navigate instruction inputs with enter and delete keys
    $('body').on('keydown', 'input[name=instructions-text]', function(e) {
        if (e.which == 13) {
            e.preventDefault();
            $('<div class="instruction-cell"><i class="invisible">-&nbsp;</i><input type="text" name="instructions-text" maxlength="9999"><input type="text" name="instructions-note" maxlength="9999" style="display: none;"><input type="text" name="instructions-photo" maxlength="9999"><input type="text" name="instructions-video" maxlength="9999"><input type="text" name="instructions-gif" maxlength="9999"></div>').insertAfter($(this).parent());
            $(this).parent().next().find('input').select();
        }
        else if (e.which == 8 && $(this).val().length == 0) {
            e.preventDefault();
            $(this).parent().prev().find('input').focus();
            $(this).parent("div").remove();
        }
        else if (!$(this).val()) {
            $(this).siblings('i').removeClass('invisible');
        }
        else if (e.which == 8 && $(this).val().length == 1) {
            $(this).siblings('i').addClass('invisible');
        }
    });

    $('.edit-recipe-pictures').sortable({
        cancel: '.add-picture-mini',
        containment: 'parent',
        tolerance: 'pointer',
        items: '.sortable-mini'
    });

    $('.ingredients').sortable({
        axis: 'y',
        containment: '.ingredients'
    });




    // select last ingredient when clicking below ingredients
    $('.ingredients').click( function (e) {
        if (e.target == this) {
            $(this).find('input').last().focus();
        }
    });
    $('.instructions').click( function (e) {
        if (e.target == this) {
            $(this).find('input[name=instructions-text]').last().focus();
        }
    });


    // edit recipe months by clicking month cells
    $('.checkbox').click(function() {
        if ($(this).prop('checked')) {
           $(this).parents('.recipe-month-container').css('background', '#ab1c20');
        } else {
            $(this).parents('.recipe-month-container').css('background', 'none');
        }
    });

    // show delete recipe form when the 'Delete' button is clicked
    $(".delete-recipe-button").click(function (e) {
        $('.delete-recipe-buttons').removeClass('hidden');
    });

});
