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

    $settings.on("input", "input.custom-range", function () {
        $(this).parent().find(".valueSpan").html($(this).val());
    });

    $settings.on("change", "input", function () {
        socket.emit("setting", Number($(this).attr("setting-index")), $(this).val());
    });

    $animations.on("click", ".animation-button", function () {
        console.log(`${$(this).attr("animation-index")}`)
        socket.emit("animation", Number($(this).attr("animation-index")));
    });

    // Handle server event,s
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
                        `<label class="w-100"> ${settings[index]["name"]}:  ` +
                        `<span class="font-weight-bold text-primary valueSpan">${settings[index]["value"]}` +
                        `</span>\n` +
                        `<input type="range" class="custom-range" setting-index="${index}" ` +
                        `value=${settings[index]["value"]} min="${settings[index]["range"][0]}" ` +
                        `max="${settings[index]["range"][1]}" step="${settings[index]["step"]}">\n` +
                        `</label>\n` +

                        `</div>\n`;
                    break;
                case "color":
                    html +=
                        `<div class="d-flex color-setting">\n` +
                        `<label class="w-100"> ${settings[index]["name"]}\n` +
                        `<input class="color-setting primary-color" type="color" setting-index="${index}" ` +
                        `value="${settings[index]["value"]}">\n` +
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
        animation = $animations.find(`[animation-index=${_animation}]`);
        animation.toggleClass("btn-outline-primary");
    });

    socket.on("animations", function (animations) {
        // Draw animation buttons
        let html = "";
        for (let index = 0; index < animations.length; index++) {
            html +=
                `<div class="flex-fill mr-2">\n` +
                `<button animation-index="${index}" class="btn btn-primary animation-button">\n` +
                `${animations[index]}\n` +
                `</button>\n` +
                `</div>\n`;
        }
        $animations.html(html);
    });
});
