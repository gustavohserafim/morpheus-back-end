function send_adress() {
    var payload = {};
    payload.client_id = $('#client_id').val();
    payload.adress = $('#adress').val();
    payload.type = 1;
    var data = JSON.stringify(payload);
    console.log(payload);
    $.ajax({
        type: "POST",
        url: "/address",
        dataType: "json",
        contentType: 'application/json',
        data: data,
        statusCode: 200
    });
}