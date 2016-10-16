/* do some require.js stuff here? */
/* TODO: make the url configurable */
function getnames(gender, number) {
    var jqxhr = $.get('http://localhost:5000/names?gender=' + gender + '&number=' + number, gotnames)
        .done(function() {
            alert("done function called");
        })
        .fail(function() {
            alert("fail function called");
        })
        .always(function() {
            alert("always function called");
        });

    // Perform other work here ...

    // Set another completion function for the request above
    jqxhr.always(function() {
        alert("second always function called");
    });
}

function gotnames(stuff) {
    console.log("/names returned: " + stuff);
}
