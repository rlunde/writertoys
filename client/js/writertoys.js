/* do some require.js stuff here? */
/* TODO: make the url configurable */
function getnames(gender, number, callback) {
    var jqxhr = $.get('http://localhost:5000/names?gender=' + gender + '&number=' + number, gotnames)
        .done(function(data) {
            // alert("done function called");
            callback(data);
        })
        .fail(function() {
            alert("fail function called");
        })
        .always(function() {
            // alert("always function called");
        });
}

function gotnames(stuff) {
    console.log("/names returned: " + stuff);
}
