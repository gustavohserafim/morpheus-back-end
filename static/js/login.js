function login() {

    var payload = {};
    payload.email = $('#email').val();
    payload.password = $('#password').val();
    var data = JSON.stringify(payload);

    $.ajax({
        type: "POST",
        url: "/token/auth",
        dataType: "json",
        contentType: 'application/json',
        data: data,
        statusCode: {
            200: function (data) {
                var token = data['data']['token'];

                $.cookie('access_token_cookie', token);

                $.ajaxSetup({
                    headers: {
                        'Authorization': $.cookie('access_token_cookie')
                    }
                });

                window.location = '../static/index.html';
            },
            401: $('#login_error').show(),
        }
    });

}

$(document).ready(function () {
    $('#login_error').hide();

    var token = $.cookie('access_token_cookie');

    if (token !== undefined) {
        window.location = '../static/index.html';
    }

});
