$(function() {

    // remove name fields when the - button is clicked
    $('body').on('click', '.delete', function () {
        $(this).parent('div').remove();
    });

    // add picture fields when the + button is clicked
    $('body').on('click', '.add-pictures', function () {
        $('<div><input type="text" name="pictures" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i><i class="fa fa-plus-circle add add-pictures" aria-hidden="true"></i></div>').insertAfter($(this).parent());
    });

    // add source fields when the + button is clicked
    $('body').on('click', '.add-sources', function () {
        $('<div><input type="text" name="sources" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i><i class="fa fa-plus-circle add add-sources" aria-hidden="true"></i></div>').insertAfter($(this).parent());
    });

    // add occasion fields when the + button is clicked
    $('body').on('click', '.add-occasions', function () {
        $('<div><input type="text" name="occasions" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i><i class="fa fa-plus-circle add add-occasions" aria-hidden="true"></i></div>').insertAfter($(this).parent());
    });

    // add instruction fields when the + button is clicked
    $('body').on('click', '.add-instructions', function () {
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
        // return - add new input below and move the cursor to it
        if (e.which == 13) {
            e.preventDefault();
            var old_value = $(this).val().slice(0, this.selectionStart);
            var new_value = $(this).val().slice(this.selectionStart);
            $(this).val(old_value);
            $('<div><input type="text" name="ingredients" maxlength="9999" value="' + new_value + '"></div>').insertAfter($(this).parent());
            $(this).parent().next().find('input').focus();
        }
        // delete
        else if (e.which == 8 && this.selectionStart == 0) {
            var previous = $(this).parent().prev().find('input');
            e.preventDefault();
            var current_val = this.value;
            var prev_val = $(this).parent().prev().find('input').val();
            var prev_len = prev_val.length;
            previous.val(prev_val + current_val);
            previous.focus();
            previous[0].setSelectionRange(prev_len, prev_len);
            previous.siblings('i').removeClass('invisible');
            $(this).parent('div').remove();
        }
        // show rearrange button if input has a value
        else if (!$(this).val()) {
            $(this).siblings('i').removeClass('invisible');
        }
        // hide rearrange button when deleting only character from length 1 input
        else if (e.which == 8 && $(this).val().length == 1) {
            $(this).siblings('i').addClass('invisible');
        }

    });

    // navigate instruction inputs with enter and delete keys
    $('body').on('keydown', 'input[name=instructions-text]', function(e) {
        if (e.which == 13) {
            e.preventDefault();
            $('<div class="instruction-cell"><i class="invisible">-&nbsp;</i><input type="text" name="instructions-text" maxlength="9999"><input type="text" name="instructions-note" maxlength="9999" style="display: none;"><input type="text" name="instructions-photo" maxlength="9999"><input type="text" name="instructions-video" maxlength="9999"><input type="text" name="instructions-gif" maxlength="9999"></div>').insertAfter($(this).parent());
            $(this).parent().next().find('input').first().focus();
        }
        else if (e.which == 8 && $(this).val().length == 0) {
            e.preventDefault();
            $(this).parent().prev().find('input').focus();
            $(this).parent('div').remove();
        }
        else if (!$(this).val()) {
            $(this).siblings('i').removeClass('invisible');
            $(this).siblings('.instruction-buttons').removeClass('invisible');
        }
        else if (e.which == 8 && $(this).val().length == 1) {
            $(this).siblings('i').addClass('invisible');
            $(this).siblings('.instruction-buttons').addClass('invisible');
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
        containment: '.ingredients',
        handle: '.fa-bars'
    });

    $('.instructions').sortable({
        axis: 'y',
        containment: '.instructions',
        handle: '.fa-bars'
    });

    // show/hide instruction-note input
    $('.fa-sticky-note-o').click( function() {
        $(this).parent().siblings('input[name=instructions-note]').toggleClass('hidden');
        $(this).parent().siblings('input[name=instructions-note]').focus();
    });

    // show/hide instruction-note input
    $('.show-media-inputs').click( function() {
        $(this).parent().siblings('.instruction-media-inputs').toggleClass('hidden');
        $(this).parent().siblings('.instruction-media-inputs').children().first().focus();
    });




    // select last ingredient/instruction when clicking below ingredients/instructions
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
    $('.delete-recipe-button').click(function () {
        $('.delete-recipe-buttons').removeClass('hidden');
    });

});
