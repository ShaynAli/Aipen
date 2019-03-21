let current_arena = -1;
let arena_list = [];

function init() {
    get_activities().then( function(data) {
        console.log(data)
    });

    setInterval(update, 1000);
    
}


function activitySelect() {
    let x = document.getElementById("activity").value;
    if (x === "Test") {
        document.getElementById("group1").hidden = false;
        document.getElementById("group2").hidden = true;
        document.getElementById("dataSelect").style.visibility = "visible";
    }

    if (x === "Test2") {
        document.getElementById("group1").hidden = true;
        document.getElementById("group2").hidden = false;
        document.getElementById("dataSelect").style.visibility = "visible";
    }
}

function update() {
    if (document.getElementById("play-button").disabled) {
        let x = 1; // Fetch
    }
}

function play() {
    new_arena();
}

function stop() {
    document.getElementById("pause-button").disabled = true;
    document.getElementById("next-gen").disabled = true;
    document.getElementById("prev-gen").disabled = true;
}

function post(path, params) {

    return fetch(path, {
        method: "POST",
        body: JSON.stringify(params),
        headers: new Headers({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
    })
    .then(response => response.json());
}

function get(path, callback) {
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState === 4 && xmlHttp.status === 200) {
            callback(xmlHttp.responseText);
        }
        xmlHttp.open("GET", path, true);
        xmlHttp.send(null);
    }
}

// POST request when play button is clicked.
$(document).ready(function(){
    $('#play-button').on('click', function(e){
      e.preventDefault();
      $.ajax({
        url:'./update_plot',
        type:'post',
        success : function(data){
          $('#statistics').html(data)
        }
      })
    });
});

// Arena Routes

// Create new arena and return the new id
function new_arena() {
    console.log("Creating new arena");

    post("/arena/new_arena",
    {
        'models': [],
        'activity': 312
    }
    ).then(function (response) {
        let arena_id = response["arena_id"];
        console.log("Generated new arena with id: " + arena_id);
        arena_list.push(arena_id);
        set_arena(id);
    });
}

// Set the current arena instance
function set_arena(id) {
    console.log("Updating current arena to id:" + id);
    current_arena(id);
}

// Start the current arena
function start_arena(id) {
    console.log("Starting arena:" + id);
    post("/arena/" + id + "/start_arena");
    // NOTE: (1) does the id need to be specified? or use current_arena
}

// Stop the current arena
function stop_arena(id) {
    console.log("Stopping arena:" + id);
    post("/arena/" + id + "/stop_arena");
    // NOTE: v.s. (1)
}

// Generation Routes

// Retrieve a specified generation, or the last if num is -1
function get_generation(num) {
    get("/arena/" + id + "/generation/" + num, function(response) {
        // TODO
    });
}

// Model Routes

function get_activities() {
    console.log("Retrieving activities");
    return post("/activity")
}