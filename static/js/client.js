function send_client() {
    var payload = {};
    payload.name = $('#name').val();
    payload.phone = $('#phone').val();
    payload.fax = $('#fax').val();
    payload.contact = $('#contact').val();
    var data = JSON.stringify(payload);

    $.ajax({
        type: "POST",
        url: "/client",
        dataType: "json",
        contentType: 'application/json',
        data: data,
        statusCode: 200
    });
}

function getClients() {

    $('#clients').DataTable( {
        "ajax": "/client",
        "columns": [
            { "data": "id" },
            { "data": "name" },
            { "data": "phone" },
            { "data": "fax" },
            { "data": "contact" }
        ]
    } );

    // $.ajax({
    //     type: "GET",
    //     url: "/client",
    //     dataType: "json",
    //     contentType: 'application/json',
    //     statusCode: {
    //         200: function (data) {
    //             return data
    //         }
    //     }
    // });



}

$(document).ready(function () {

    getClients();



    // var token = $.cookie('access_token_cookie');

    // if (token !== undefined) {
    //     window.location = '/static/index.html';
    //
    // }

});

