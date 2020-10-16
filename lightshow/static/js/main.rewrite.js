$(document).ready(function () {
    const sliderHtml =
        "<div class=\"d-flex w-100\">\n" +
        "<input type=\"range\" class=\"custom-range\" id=\"customRange11\" min=\"0\" max=\"200\">\n" +
        "<span class=\"font-weight-bold text-primary ml-2 valueSpan\"></span>\n" +
        "</div>";

    const buttonHtml =
        "<div class=\"flex-fill mr-2\">\n" +
        "<button class=\"btn btn-primary\" style=\"min-width: 150px; width: 100%; height: 65px;\">Rainbow</button>\n" +
        "</div>";

    // Selectors
    let $power = $("#power");

    // Variables
    let ledState = false;

    $power.on("click", function () {
        ledState = !ledState;
        $power.attr("fill", ledState ? "green" : "red")
    });

    let socket = io();

});
