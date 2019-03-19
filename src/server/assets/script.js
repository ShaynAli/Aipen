function activitySelect() {
    var x = document.getElementById("activity").value;
    if (x == "Test") {
        document.getElementById("group1").disabled = false;
        document.getElementById("group2").disabled = true;
        document.getElementById("dataSelect").style.visibility = "visible";
    }

    if (x == "Test2") {
        document.getElementById("group1").disabled = true;
        document.getElementById("group2").disabled = false;
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

    currentState.push(activity)
    currentState.push(data)

    if (document.getElementById("model1").checked) {
        currentState.push("model1");
    }

    if (document.getElementById("model2").checked) {
        currentState.push("model2");
    }

    if (document.getElementById("model3").checked) {
        currentState.push("model3");
    }

    if (document.getElementById("model4").checked) {
        currentState.push("model4");
    }


}