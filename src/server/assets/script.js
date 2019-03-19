function activitySelect() {
    var x = document.getElementById("activity").value;
    if (x == "Test") {
        document.getElementById("group1").disabled = false;
        document.getElementById("group2").disabled = true;
    }

    if (x == "Test2") {
        document.getElementById("group1").disabled = true;
        document.getElementById("group2").disabled = false;
    }
}

