function activitySelect() {
    var x = document.getElementById("activity").value;
    if (x == "Test") {
        document.getElementById("group1").hidden = false;
        document.getElementById("group2").hidden = true;
        document.getElementById("dataSelect").style.visibility = "visible";
    }

    if (x == "Test2") {
        document.getElementById("group1").hidden = true;
        document.getElementById("group2").hidden = false;
        document.getElementById("dataSelect").style.visibility = "visible";
    }
}

function play() {
    var activity = document.getElementById("activity").value;
    var data = document.getElementById("dataSelect").value;
    var currentState = []
    var leaderboardSelector = document.getElementById("leaderboardSelector");

    currentState.push(activity)
    currentState.push(data)

    if (document.getElementById("model1").checked) {
        currentState.push("model1");
        newOption = createNewOption("model1")

        if (!checkOptions(leaderboardSelector, newOption))
            leaderboardSelector.add(newOption);
    }

    if (document.getElementById("model2").checked) {
        currentState.push("model2");
        newOption = createNewOption("model2")

        if (!checkOptions(leaderboardSelector, newOption))
            leaderboardSelector.add(newOption);
    }

    if (document.getElementById("model3").checked) {
        currentState.push("model3");
        newOption = createNewOption("model3")

        if (!checkOptions(leaderboardSelector, newOption))
            leaderboardSelector.add(newOption);
    }

    if (document.getElementById("model4").checked) {
        currentState.push("model4");
        newOption = createNewOption("model4")

        if (!checkOptions(leaderboardSelector, newOption))
            leaderboardSelector.add(newOption);
    }

    console.log(currentState);
    document.getElementById("play-button").disabled = true;
    document.getElementById("pause-button").disabled = false;
}

function pause() {
    document.getElementById("play-button").disabled = false;
    document.getElementById("pause-button").disabled = true;
}

// Takes selected model and displays the required leaderboard
function leaderboardSelect() {
}

// Creates a new select option based on given string value
function createNewOption(newOption) {
    var option = document.createElement("option");
    option.text = newOption;
    option.value = newOption;
    return option;
}

// Returns true if a given option is already part of a given list
function checkOptions(checkedList, checkOption) {
    var options = checkedList.options;
    console.log(options);

    if (options.length == 0)
        return false;

    for (i = 0; i < options.length; i++) {
        if (checkOption.value == options[i].value) {
            return true;
        }
    }

    return false;
}