/* do some require.js stuff here? */
/* TODO: make the url configurable */
function getnames(gender, number) {
    var jqxhr = $.get('http://localhost:5000/names?gender=' + gender + '&number=' + number, gotnames)
        .done(function() {
            alert("second success");
        })
        .fail(function() {
            alert("error");
        })
        .always(function() {
            alert("finished");
        });

    // Perform other work here ...

    // Set another completion function for the request above
    jqxhr.always(function() {
        alert("second finished");
    });
}

function gotnames(stuff) {
    console.log("/names returned: " + stuff);
}
