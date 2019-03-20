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


    console.log(serverRequest);
    post("/request", serverRequest).then(function (newPlot) {
         console.log(newPlot);
        document.getElementById("statistics").innerHTML = newPlot;
    });
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
    .then(function(response) {
        return response;
    });
}

$(document).ready(function(){
        $('#play-button').on('click', function(e){
          // prevent page being reset, we are going to update only
          // one part of the page.
          e.preventDefault()
          $.ajax({
            url:'./request',
            type:'post',
            success : function(data){
              // server returns rendered "update_content.html"
              // which is just pure html, use this to replace the existing
              // html within the "plot content" div
              $('#statistics').html(data)
            }
          })
        });
      });