let current_arena = -1;
let arena_list = [];
let arena_running = false;

let activity
let models = []

function string_to_html(html_string) {
    let template = document.createElement("template");
    template.innerHTML = html_string.trim();
    return template.content.cloneNode(true);
}

function init() {
    get_activities().then(function(data) {
        // Set activities list
        document.getElementById("activity-1").value = data.activity_ids[0];
        document.getElementById("activity-1").text = data.activity_names[0];
    });

    setInterval(update, 1000);
}

// POST request when play button is clicked.
//$(document).ready(function(){
//    $('#play-button').on('click', function(e){
//      e.preventDefault();
//      $.ajax({
//        url:'./update_plot',
//        type:'post',
//        success : function(data){
//          $('#statistics').html(data)
//        }
//      })
//    });
//});

function activitySelect() {
    let x = document.getElementById("activity-selection").value;
    $("#model-table tr").remove();
    document.getElementById("model-header").innerHTML = `
        <th>Enable</th> <th>Model Name</th>`;
    get_models(x).then(function(data) {
        console.log(data);
        document.getElementById("model-table").appendChild(string_to_html(
            build_model_pool(data)));
    });
}

function build_model_pool(data) {
    model_str = '';
    
    for (let i = 0; i < data.model_ids.length; i++) {
        var m_id = data.model_ids[i];
        model_str += `
        <tr>
            <td><input type="checkbox" onchange="model_select(this)" id="` + 
            m_id + `"></td><td>`+ data.model_names[i] + `</td>
        </tr>
        `
    }
    
    return model_str;
}

function model_select(checkbox) {
    var model_id = checkbox.id;
    if (checkbox.checked) {
            
        if (!models.includes(model_id)) {
            console.log("selecting model " + model_id);
            models.push(model_id);
        }
    } 
    
    else {
        if (models.includes(model_id)) {
            console.log("deselecting model " + model_id);
            models.splice(models.indexOf(model_id), 1);
        }
    }
    console.log(models);
}


function update() {
    if (document.getElementById("play-button").disabled) {
        let x = 1; // Fetch
    }
    model_select
}

function play() {
    // if (current_arena != null && !arena_running) {
    //     start_arena(current_arena);
    // }
    new_arena();
    console.log(arena_list);
}

function stop() {
    document.getElementById("pause-button").disabled = true;
    document.getElementById("get-generation").disabled = true;
    document.getElementById("pause-button").disabled = false;
    stop_arena(current_arena);

}

function post(path, params,) {
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

// Arena Routes

// Create new arena and return the new id
function new_arena() {
    console.log("Creating new arena");
    //console.log(get_activities());

    post("/arena/new_arena",
    {
        'models': models,
        'activity': document.getElementById('activity-selection').value
    }
    ).then(function (response) {
        let arena_id = response["arena_id"];
        console.log("Generated new arena with id: " + arena_id);
        arena_list.push(arena_id);
        set_arena(arena_id);
        start_arena(arena_list);
    });
}

// Set the current arena instance
function set_arena(id) {
    console.log("Updating current arena to id: " + id);
    current_arena = id;
}

// Start the current arena
function start_arena(id) {
    console.log("Starting arena:" + id);
    post("/arena/" + id + "/start");
    arena_running = true;
}

// Stop the current arena
function stop_arena(id) {
    console.log("Stopping arena:" + id);
    post("/arena/" + id + "/stop_arena");
    arena_running = false;
}

// Generation Routes

// Retrieve a specified generation, or the last if num is -1
function get_generation(arena_id, num) {
    if (arena_id == -1 || arena_id == '' || arena_id == null) {
        arena_id = current_arena;
    }
    get("/arena/" + arena_id + "/generation/" + num, function(response) {
        
    });
}

// Model Routes

function get_activities() {
    console.log("Retrieving activities");
    return post("/activity")
}

function get_models(activity_id) {
    console.log("Retrieving models for activity " + activity_id);
    return post("/activity/" + activity_id + "/models");
}
