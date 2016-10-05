$(function() {
    //when the Add Field button is clicked
    $("#add").click(function (e) {
        //Append a new row of code to the "#items" div
        $("#items").append('<div><input name="alt" type="text" maxlength="500"><button class="delete" type="button">Delete</button></div>'); });

    $("body").on("click", ".delete", function (e) {
        $(this).parent("div").remove();
    });
});
