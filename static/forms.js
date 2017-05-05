$(function() {


    // add instruction fields when the + button is clicked
    $("#add-instructions").click(function (e) {
        $("#instruction-fields").append('<div><label>Text: <input type="text" name="instructions-text" maxlength="9999"></label><label>Photo: <input type="text" name="instructions-photo" maxlength="9999"></label><label>Video: <input type="text" name="instructions-video" maxlength="9999"></label><label>Gif: <input type="text" name="instructions-gif" maxlength="9999"></label><label>Note: <input type="text" name="instructions-note" maxlength="9999"></label><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>'); });






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


    // add ingredient fields when the + button is clicked
    $("body").on("click", ".add-ingredients", function (e) {
        $('<div><input type="text" name="ingredients" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i><i class="fa fa-plus-circle add add-ingredients" aria-hidden="true"></i></div>').insertAfter($(this).parent());
    });


    // add occasion fields when the + button is clicked
    $("body").on("click", ".add-occasions", function (e) {
        $('<div><input type="text" name="occasions" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i><i class="fa fa-plus-circle add add-occasions" aria-hidden="true"></i></div>').insertAfter($(this).parent());
    });







    // show delete recipe form when the 'Delete' button is clicked
    $(".delete-recipe-button").click(function (e) {
        $('.delete-recipe').css('display', 'flex');
    });

});
