function checkLoggedUser() {
    var token = $.cookie('access_token_cookie');

    if (token === undefined) {
        window.location = '/login';
    }
}

$(document).ready(function () {
    checkLoggedUser();
});