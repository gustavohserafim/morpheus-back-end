function checkLoggedUser() {
    var token = $.cookie('access_token_cookie');

    if (token === undefined) {
        window.location = '/static/login.html';
    }
}

$(document).ready(function () {
    checkLoggedUser();
});