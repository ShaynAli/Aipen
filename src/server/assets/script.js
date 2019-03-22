let current_activity_id = null;
let current_arena_id = null;
let arena_list = [];
let arena_running = false;
let models = [];

function string_to_html(html_string) {
    let template = document.createElement("template");
    template.innerHTML = html_string.trim();
    return template.content.cloneNode(true);
}

function init() {
    document.getElementById("start-button").disabled = true;
    get_activities().then(function(data) {
        // Set activities list
        document.getElementById("activity-1").value = data.activity_ids[0];
        document.getElementById("activity-1").text = data.activity_names[0];
    });

    setInterval(update, 5000);
}

function activity_select() {
    let x = document.getElementById("activity-selection").value;
    $("#model-table tr").remove();
    document.getElementById("model-header").innerHTML = `
        <th>Enable</th> <th>Model Name</th>`;
    get_models(x).then(function(data) {
        document.getElementById("model-table").appendChild(string_to_html(
            build_model_pool(data)));
    });
}

function build_model_pool(data) {
    let model_str = '';
    
    for (let i = 0; i < data.model_ids.length; i++) {
        var m_id = data.model_ids[i];
        model_str += `
        <tr id="model-` + m_id + `" onclick="get_model_preview(this)">
            <td><input type="checkbox" onchange="model_select(this)" id="` +
            m_id + `"></td><td>`+ data.model_names[i] + `</td>
        </tr>
        `
    }
    
    return model_str;
}

function model_select(checkbox) {
    let model_id = checkbox.id;
    if (checkbox.checked) {
            
        if (!models.includes(model_id)) {
            console.log("selecting model " + model_id);
            models.push(model_id);
            document.getElementById("start-button").disabled = false;
        }
    } else {
        if (models.includes(model_id)) {
            console.log("Deselecting model " + model_id);
            models.splice(models.indexOf(model_id), 1);

            if (models.length === 0) {
                document.getElementById("start-button").disabled = true;
            }
        }
    }
    console.log("Current models: " + models);
}


function update() {
    console.log("In update");
    if (current_arena_id !== null) {
        console.log("Arena ID not null");
        if (arena_running) {
            console.log("Start button disabled");
            $(document).ready(function(){
                $.ajax({
                        url:'./arena/' + current_arena_id + "/generation_plot/START/END",
                        type:'post',
                        success : function(data){
                          $('#statistics').html(data)
                        }
                })
            })
        }
    }
    let model_select;
}

function start() {
    document.getElementById("stop-button").disabled = false;
    document.getElementById("start-button").disabled = true;
    document.getElementById("get-generation").disabled = false;
    if (current_arena_id !== null && !arena_running) {
        start_arena(current_arena_id);
        return;
    }
    new_arena();
}

function stop() {
    stop_arena(current_arena_id);
    document.getElementById("stop-button").disabled = true;
    document.getElementById("start-button").disabled = false;
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


// Create new arena and return the new id
function new_arena() {
    console.log("Creating new arena");

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
        start_arena(arena_id);
    });
}

// Set the current arena instance
function set_arena(id) {
    console.log("Updating current arena to id: " + id);
    current_arena_id = id;
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
    post("/arena/" + id + "/stop");
    arena_running = false;
}

// Generation Routes

// Retrieve a specified generation, or the last if num is -1
function get_generation() {
    let num = document.getElementById('generation-entry').value;

    post("/arena/" + current_arena_id + "/generation/" + num).then(function(data) {
        let leaderboard = data['leaderboard'];

        for (var i=0; i < 10; i++) {
            document.getElementById('type-' + (i+1)).innerHTML = leaderboard[i][0];
            document.getElementById('tid-' + (i+1)).innerHTML = leaderboard[i][1];
            document.getElementById('score-' + (i+1)).innerHTML = leaderboard[i][2];
        }
    });
}

function get_generations() {
    let start = "START";
    let end = "END";
    console.log("Get all generations");
    return post("/arena/" + current_arena_id + "/generations/" + start + "/" + end);
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

function get_model_preview(trow) {
    let _id = trow.id;
    _id = _id.substring(6);

    console.log("Retrieving model preview for " + _id)
    post("/model/" + _id).then(function(data) {
        console.log(data);
    })
}

