var lastSubmittedIconId = "";

$(document).on("ready", () => {
    lastSubmittedIconId = $("#current-icon img").attr("alt");
});

$("#buttons #randomize-button").on("click", () => {
    const ownedIcons = $("#icons img");
    const randomIcon = ownedIcons[Math.floor(Math.random() * ownedIcons.length)];
    const currentIcon = $("#current-icon img");
    const currentIconName = $("#current-icon p");

    currentIcon.attr("src", randomIcon.src);
    currentIcon.attr("alt", randomIcon.alt);
    currentIconName.text(randomIcon.title);
});

$("#icons img").on("click", (event) => {
    const currentIcon = $("#current-icon img");
    const currentIconName = $("#current-icon p");
    if (currentIcon.attr("src") === event.target.src) {
        return;
    }

    currentIcon.attr("src", event.target.src);
    currentIcon.attr("alt", event.target.alt);
    currentIconName.text(event.target.title);
});

$("#buttons #save-button").on("click", function () {
    const saveButton = $("#buttons #save-button");
    const currentlySelectedIcon = $("#current-icon img");

    if (lastSubmittedIconId === currentlySelectedIcon.attr("alt")) {
        return;
    }

    var response = $.post(`/api/icon/${currentlySelectedIcon.attr("alt")}`).done(function () {
        if (response.status === 204) {
            saveButton.text("Successfully changed your icon!");
            saveButton.css("padding", "2% 3%");
            lastSubmittedIconId = currentlySelectedIcon.attr("alt");
        } else {
            saveButton.text("Something went wrong, make sure your League Of Legends client is open!");
        }
    });
    setTimeout(() => {
        saveButton.text("Set Summoner Icon");
        saveButton.css("padding", "2% 6%");
    }, 3000);
});

$("#searchbar input").on("keyup", function (event) {
    filterIcons($("#searchbar input").val().toLowerCase());
});


const filterIcons = (textToSearch) => {
    if (textToSearch === "") {
        $("#icons img").each(function () {
            $(this).show();
        });
    }

    $("#icons img").each(function () {
        if (!$(this).attr("title").toLowerCase().includes(textToSearch)) {
            $(this).fadeOut();

            return;
        }

        if ($(this).css("display") === "none") {
            $(this).fadeIn();

            return;
        }

        $(this).show();
    });
};
