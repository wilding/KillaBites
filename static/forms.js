$(function() {

    // add picture fields when the + button is clicked
    $("#add-pics").click(function (e) {
        $("#pic-fields").append('<div><input type="text" name="pictures" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>'); });

    // add source fields when the + button is clicked
    $("#add-sources").click(function (e) {
        $("#source-fields").append('<div><input type="text" name="sources" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>'); });

    // add occasion fields when the + button is clicked
    $("#add-occasions").click(function (e) {
        $("#occasion-fields").append('<div><input type="text" name="occasions" maxlength="500"><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>'); });

    // add ingredient fields when the + button is clicked
    $("#add-ingredients").click(function (e) {
        $("#ingredient-fields").append('<div><input type="text" name="ingredients" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>'); });

    // add instruction fields when the + button is clicked
    $("#add-instructions").click(function (e) {
        $("#instruction-fields").append('<div><label>Text: <input type="text" name="instructions-text" maxlength="9999"></label><label>Photo: <input type="text" name="instructions-photo" maxlength="9999"></label><label>Video: <input type="text" name="instructions-video" maxlength="9999"></label><label>Gif: <input type="text" name="instructions-gif" maxlength="9999"></label><label>Note: <input type="text" name="instructions-note" maxlength="9999"></label><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>'); });

    // remove name fields when the - button is clicked
    $("body").on("click", ".delete", function (e) {
        $(this).parent("div").remove();
    });

});
