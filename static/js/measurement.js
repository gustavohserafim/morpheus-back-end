function send_measurement() {
    var payload = [];
    payload.measuremnt = $ ("#name").val();
    payload.description = $ ("#description").val();
    var data = JSON.stringify(payload);

    $.ajax({
        type: "POST",
        url: "/measurement",
        dataType: "json",
        contentType: 'application/json',
        data: data,
        statusCode: 200
    });
}