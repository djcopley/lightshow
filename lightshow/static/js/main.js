$(document).ready(function () {
    // SocketIO
    const socket = io();

    // Variables
    let animation = $("");

    // Selectors
    const $power = $("#power");
    const $animations = $("#animations"); // Animations div
    const $settings = $("#settings"); // Settings div

    // Helper functions

    // Handle client events
    $power.on("click", function () {
        socket.emit("power");
    });

    $settings.find($("input")).on("change", function () {
        // $(this).find(".valueSpan").html($(this).find("input").val());
        socket.emit("setting", $(this).attr("settings-index"), $(this).attr("value"));
    });

    $animations.find($(".animation-button")).on("click", function () {
        socket.emit("animation", $(this).attr("animations-index"));
    });

    // Handle server events
    socket.on("power", function (animationState) {
        $power.attr("fill", animationState ? "green" : "red");
    });

    // Render settings HTML
    socket.on("settings", function (settings) {
        let html = "";

        for (let index = 0; index < settings.length; index++) {
            switch (settings[index]["type"]) {
                case "slider":
                    html +=
                        `<div class="d-flex slider-setting">\n` +
                        `<label> ${settings[index]["name"]}\n` +
                        `<input type="range" class="custom-range" settings-index="${index}" ` +
                        `value=${settings[index]["value"]} min="${settings[index]["range"][0]}" ` +
                        `max="${settings[index]["range"][1]}" step="${settings[index]["step"]}">\n` +
                        `</label>\n` +
                        `<span class="font-weight-bold text-primary ml-2 valueSpan">${settings[index]["value"]}` +
                        `</span>\n` +
                        `</div>\n`;
                    break;
                case "color":
                    html +=
                        `<div class="d-flex color-setting">\n` +
                        `<label> ${settings[index]["name"]}\n` +
                        `<input type="color" settings-index="${index}" value="${settings[index]["value"]}">\n` +
                        `</label>\n` +
                        `</div>\n`;
                    break;
                default:
                    console.log(`Unknown settings type: ${settings[index]["type"]}`);
                    break;
            }

            $settings.html(html);
        }
    });

    socket.on("animation", function (_animation) {
        animation.toggleClass("btn-outline-primary");
        animation = $animations.find(`[animation_index=${_animation}]`);
        animation.toggleClass("btn-outline-primary");
    });

    socket.on("animations", function (animations) {
        // Draw animation buttons
        for (let index = 0; index < animations.length; index++) {
            $animations.html(
                `<div class="flex-fill mr-2">\n` +
                `<button animation-index="${index}" class="btn btn-primary animation-button">\n` +
                `${animations[index]}\n` +
                `</button>\n` +
                `</div>\n`
            );
        }
    });
});
