String.prototype.format = function () {
    let a = this;
    for (let k in arguments) {
        a = a.replace(new RegExp("\\{" + k + "\\}", 'g'), arguments[k]);
    }
    return a
}

let socket = io();
let state; // Are the LEDS on or off
let settings = [];
let animations = [];
let animation = 0;

// JQuerry selectors
let $power = $("#power");

function load_power() {
    console.log(state)
    $power.text("Turn ".concat(state ? "off" : "on"));
    $power[0].className = state ? "button-selected" : "button";
}

function load_settings() {
    document.getElementById("settings").innerHTML = "";
    for (let index = 0; index < settings.length; index++) {
        switch (settings[index]["type"]) {
            case "slider":
                document.getElementById("settings").innerHTML += "<div class=\"slidecontainer\">\n";
                document.getElementById("settings").innerHTML +=
                    "<label htmlFor={0}>{0}</label>\n<input onChange='socket.emit(\"setting\", {4}, this.value)' class=slider type='range' step={5} min={1} max={2} value={3} id={0}>".format(
                        settings[index]["name"],
                        settings[index]["range"][0], settings[index]["range"][1], settings[index]["value"],
                        index, settings[index]["step"]
                    );
                document.getElementById("settings").innerHTML += "</div>";
                break;
            case "color":
                document.getElementById("settings").innerHTML += "<div class=\"color\">\n";
                document.getElementById("settings").innerHTML +=
                    "<label htmlFor={0}>{0}</label>\n<input onChange='socket.emit(\"setting\", {2}, this.value)' class=color type='color' value={1} id={0}>".format(
                        settings[index]["name"], settings[index]["value"], index
                    );
                document.getElementById("settings").innerHTML += "</div>";
                console.log(settings[index]["value"])
                break;
            case "text":
                break;
            default:
                break;
        }
    }
}

function load_animations() {
    document.getElementById("animations").innerHTML = "<div>";
    for (let index = 0; index < animations.length; index++) {
        if (index === animation) {
            document.getElementById("animations").innerHTML +=
                "<button class='button-selected' onClick='socket.emit(\"animation\", {1})' id={0}>{0}</button>".format(animations[index], index);
        } else {
            document.getElementById("animations").innerHTML +=
                "<button class='button' onClick='socket.emit(\"animation\", {1})' id={0}>{0}</button>".format(animations[index], index);
        }
    }
    document.getElementById("animations").innerHTML += "</div>";
}

socket.on("connect", function () {
    console.log("Connected to server");
});

$power.click(function () {
    socket.emit("power");
    return false;
});

socket.on("power", function (_state) {
    state = _state;
    load_power();
});

socket.on("settings", function (_settings) {
    settings = _settings;
    load_settings();
});

socket.on('animations', function (_animations) {
    animations = _animations;
    load_animations();
})

socket.on('animation', function (_animation) {
    animation = _animation;
    load_animations();
})