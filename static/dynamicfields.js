$(function() {
    //when the Add Field button is clicked
    $("#add-alts").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#name-fields").append('<i>, </i><input name="alt" type="text" maxlength="500"><i class="fa fa-minus-circle delete" aria-hidden="true"></i>'); });

    $("#add-pics").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#pic-fields").append('<div><input type="text" name="pictures" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>'); });

    $("#add-sources").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#source-fields").append('<div><input type="text" name="sources" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>'); });

    $("#add-occasions").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#occasion-fields").append('<div><input type="text" name="occasions" maxlength="500"><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>'); });

    $("#add-ingredients").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#ingredient-fields").append('<div><input type="text" name="ingredients" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>'); });

    $("#add-instructions").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#instruction-fields").append('<div><label>Text: <input type="text" name="instructions-text" maxlength="9999"></label><label>Photo: <input type="text" name="instructions-photo" maxlength="9999"></label><label>Video: <input type="text" name="instructions-video" maxlength="9999"></label><label>Gif: <input type="text" name="instructions-gif" maxlength="9999"></label><label>Note: <input type="text" name="instructions-note" maxlength="9999"></label><i class="fa fa-minus-circle delete" aria-hidden="true"></i></div>'); });

    $("body").on("click", ".delete", function (e) {
        $(this).parent("div").remove();
    });

    $(window).scroll(headerScroll);

});

var showDeleteIngredient = function (index) {
    var row = $("tbody").children(".chart-row")[index];
    $(row).find('.delete-ingredient-cell').css('display', "table-cell");
    $(row).children('.month-cell').css('display', 'none');
}

var showChartRow = function (index) {
    var row = $("tbody").children(".chart-row")[index];
    $(row).find('.delete-ingredient-cell').css('display', "none");
    $(row).children('.month-cell').css('display', 'table-cell');
}

var headerScroll = function () {
    var header = $('.relative-header');
    var offset = header.offset();
    var scrolltop = $(window).scrollTop();
    var fixed_header = $('.fixed-header');
    if (scrolltop > offset.top) {
        fixed_header.css("display", "table");
    } else {
        fixed_header.css("display", "none");
    };
}
