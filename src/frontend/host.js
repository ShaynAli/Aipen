// host.js

function init() {

}

function get_asset_with_name(asset_name) {
    console.log("Begin search for " + asset_name);
    post("/assets/" + asset_name);
}



function post(path, params, method) {

    var url = "localhost:" + path;

    return fetch(url, {
        method: "POST",
        headers: new Headers({
            "Accept": "application/json",
            "Content-Type": "application/json"
        }) 
    })
    .then(response => response.json());
}