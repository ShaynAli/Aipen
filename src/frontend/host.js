// host.js

function init() {

}

// Use for retrieval of named assets
function get_asset_with_name(asset_name) {
    console.log("Begin search for " + asset_name);
    post("/assets/" + asset_name);
}

// TODO: definition of custom problems through routes?
function define_problem() {
    
}

// TODO: Use when selecting activities from sidebar nav
function activity_select(activity) {

}

// TODO: Define the configuration of an arena run
function arena_setup() {

}

function evaluate(problem_id) {

}



function post(path, params, method) {

    var url = "localhost:5000" + path;

    return fetch(url, {
        method: "POST",
        headers: new Headers({
            "Accept": "application/json",
            "Content-Type": "application/json"
        }) 
    })
    .then(response => response.json());
}