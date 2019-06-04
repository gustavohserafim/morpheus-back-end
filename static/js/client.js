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
        "ajax": "/api/client",
        "columns": [
            { "data": "id" },
            { "data": "name" },
            { "data": "phone" },
            { "data": "fax" },
            { "data": "contact" }
        ]
    } );

}

function formHide() {
    var form = $('#client_form');

    if (form.is(":visible")){
        form.hide();
    }else{
        form.show();
    }
}

$(document).ready(function () {
    getClients();
});

