function checkLoggedUser() {
    var token = $.cookie('access_token_cookie');

    if (token === undefined && window.location.href !== 'https://morpheus.gq/login.html') {
        window.location = '/login.html';
    }
}

$(document).ready(function () {
    checkLoggedUser();
});