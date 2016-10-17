$(function() {
    //when the Add Field button is clicked
    $("#add").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#items").append('<div><input name="alt" type="text" maxlength="500"><button class="delete" type="button">Delete</button></div>'); });

    $("#add-pics").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#pic-fields").append('<div><input type="text" name="pictures" maxlength="9999"><button class="delete" type="button">Delete</button></div>'); });

    $("#add-sources").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#source-fields").append('<div><input type="text" name="sources" maxlength="9999"><button class="delete" type="button">Delete</button></div>'); });

    $("#add-occasions").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#occasion-fields").append('<div><input type="text" name="occasions" maxlength="500"><button class="delete" type="button">Delete</button></div>'); });

    $("#add-ingredients").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#ingredient-fields").append('<div><input type="text" name="ingredients" maxlength="9999"><button class="delete" type="button">Delete</button></div>'); });

    $("#add-instructions").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#instruction-fields").append('<div><label>Text: <input type="text" name="instructions-text" maxlength="9999"></label><label>Photo: <input type="text" name="instructions-photo" maxlength="9999"></label><label>Video: <input type="text" name="instructions-video" maxlength="9999"></label><label>Gif: <input type="text" name="instructions-gif" maxlength="9999"></label><label>Note: <input type="text" name="instructions-note" maxlength="9999"></label><button class="delete" type="button">Delete</button></div>'); });

    $("body").on("click", ".delete", function (e) {
        $(this).parent("div").remove();
    });
});
