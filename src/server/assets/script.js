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

//function dataHide() {
//    document.getElementById("dataSelect").style.visibility = "hidden";
//    document.getElementById("group1").disabled = true;
//    document.getElementById("group2").disabled = true;
//}

function play() {
    var activity = document.getElementById("activity").value;
    var data = document.getElementById("dataSelect").value;
    var currentState = []
    var leaderboardSelector = document.getElementById("leaderboardSelector");

    currentState.push(activity)
    currentState.push(data)

    if (document.getElementById("model1").checked) {
        currentState.push("model1");
        leaderboardSelector.add(createNewOption("model1"));
    }

    if (document.getElementById("model2").checked) {
        currentState.push("model2");
        leaderboardSelector.add(createNewOption("model2"));
    }

    if (document.getElementById("model3").checked) {
        currentState.push("model3");
        leaderboardSelector.add(createNewOption("model3"));
    }

    if (document.getElementById("model4").checked) {
        currentState.push("model4");
        leaderboardSelector.add(createNewOption("model4"));
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