$(function(){
    $(".button-collapse").sideNav();
});

function send_adress() {
    var payload = {};
    payload.adress = $('#adress').val();
    var data = JSON.stringify(payload);

    $.ajax({
        type: "POST",
        url: "/adress",
        dataType: "json",
        contentType: 'application/json',
        data: data,
        statusCode: 200
    });
}