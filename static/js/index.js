function checkLoggedUser() {
    var token = $.cookie('access_token_cookie');

    if (token === undefined) {
        window.location = '/static/login.html';
    }
}

function getHome() {

    $.ajax({
        type: "GET",
        url: "/api/company",
        //dataType: "json",
        //contentType: 'application/json',
        success: function () {
            $('#login_form').hide();
            $('#logged').show();
        }
    });
}

$(document).ready(function () {
    checkLoggedUser();


});