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

    // SocketIO
    let socket = io();
    let animation = 0;

    // Selectors
    const $power = $("#power");
    const $animations = $("#animations"); // Animations div
    const $settings = $("#settings"); // Settings div

    // Helper functions

    // Handle client events
    $power.on("click", function () {
        socket.emit("power");
    });

    $settings.find($(".setting")).on("change", function () {
        console.log("setting", $(this).attr("id"), $(this).attr("value"));
        socket.emit("setting", $(this).attr("id"), $(this).attr("value"));
    });

    $animations.find($(".animation-button")).on("click", function () {
        console.log("animation", $(this).attr("id"))
        socket.emit("animation", $(this).attr("id"));
    });

    // Handle server events
    socket.on("power", function (animationState) {
        $power.attr("fill", animationState ? "green" : "red");
    });

    socket.on("settings", function (settings) {
        $(this).find(".valueSpan").html($(this).val());
    });

    socket.on("animation", function (_animation) {
        console.log("RECEIVED animation")

        console.log($animations.find($(`#${animation}`)))

        // animation = _animation;

    });

    socket.on("animations", function (animations) {
        // Draw animation buttons
        console.log("RECEIVED ANIMATIONS");
        for (let i = 0; i < animations.length; i++) {
        }
    });
});
