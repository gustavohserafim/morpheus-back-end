function send_material() {
    var payload = {};
    payload.name = $ ("#name").val();
    payload.ncm = $ ("#ncm").val();
    payload.description= $ ("#description").val();
    var data = JSON.stringify(payload);

    $.ajax({
        type: "POST",
        url: "/material",
        dataType: "json",
        contentType: 'application/json',
        data: data,
        statusCode: 200
    });
}