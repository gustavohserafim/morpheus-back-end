function login() {

    var payload = {};
    payload.email = $('#email').val();
    payload.password = $('#password').val();
    var data = JSON.stringify(payload);

    $.ajax({
        type: "POST",
        url: "/api/auth",
        dataType: "json",
        contentType: 'application/json',
        data: data,
        statusCode: {
            200: function (data) {
                localStorage.auth_token = data['data']['token'];

                $.ajaxSetup({
                    headers: {
                        'Authorization': localStorage.auth_token
                    }
                });

                window.location = '/index.html';
            },
            401: $('#login_error').show(),
        } // return console log
    });

}

$(document).ready(function () {
    $('#login_error').hide();

    var token = localStorage.auth_token;

    if (token !== undefined) {
        window.location = '/index.html';
    }

});
