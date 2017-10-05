/* do some require.js stuff here? */
/* TODO: make the url configurable */
function getnames(gender, number, callback) {
    var jqxhr = $.get('http://localhost:5000/names?gender=' + gender + '&number=' + number, gotnames)
        .done(function(data) {
            callback(data);
        })
        .fail(function(jqXHR, textStatus, errorThrown) {
            alert("getnames failed " + textStatus);
        });
}

function gotnames(stuff) {
    console.log("/names returned: " + stuff);
}
