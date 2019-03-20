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

function init() {
    setInterval(update, 10000)
}

function update() {
    if (document.getElementById("play-button").disabled) {
        var x = 1; // Fetch
    }
}

function play() {
    var activity = document.getElementById("activity").value;
    var data = document.getElementById("dataSelect").value;
    var models = []
    var leaderboardSelector = document.getElementById("leaderboardSelector");

    if (document.getElementById("model1").checked) {
        models.push("model1");
        newOption = createNewOption("model1")

        if (!checkOptions(leaderboardSelector, newOption))
            leaderboardSelector.add(newOption);
    }

    if (document.getElementById("model2").checked) {
        models.push("model2");
        newOption = createNewOption("model2")

        if (!checkOptions(leaderboardSelector, newOption))
            leaderboardSelector.add(newOption);
    }

    if (document.getElementById("model3").checked) {
        models.push("model3");
        newOption = createNewOption("model3")

        if (!checkOptions(leaderboardSelector, newOption))
            leaderboardSelector.add(newOption);
    }

    if (document.getElementById("model4").checked) {
        models.push("model4");
        newOption = createNewOption("model4")

        if (!checkOptions(leaderboardSelector, newOption))
            leaderboardSelector.add(newOption);
    }

    document.getElementById("play-button").disabled = true;
    document.getElementById("pause-button").disabled = false;
    document.getElementById("next-gen").disabled = false;
    document.getElementById("prev-gen").disabled = false;

    var serverRequest = {
        requests: {
            "new_arena": {
                "model_ids": models
            }
        },
        webState:
        {
            "activity": activity,
            "data": data,
            "models": models
        }
    };

    console.log(JSON.stringify(serverRequest));
    (post("/request", serverRequest).then(function(data) {
        console.log(data)
    }))

}

function stop() {
    document.getElementById("pause-button").disabled = true;
    document.getElementById("next-gen").disabled = true;
    document.getElementById("prev-gen").disabled = true;
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

    if (options.length == 0)
        return false;

    for (i = 0; i < options.length; i++) {
        if (checkOption.value == options[i].value) {
            return true;
        }
    }

    return false;
}

function post(path, params) {

    var url = path

    return fetch(url, {
        method: "POST",
        body: JSON.stringify(params),
        headers: new Headers({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
    })
    .then(response => response.json());
}

// POST request when play button is clicked.
$(document).ready(function(){
    $('#play-button').on('click', function(e){
      e.preventDefault()
      $.ajax({
        url:'./update_plot',
        type:'post',
        success : function(data){
          $('#statistics').html(data)
        }
      })
    });
});
