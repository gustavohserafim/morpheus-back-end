function checkLoggedUser() {
    if (localStorage.auth_token === undefined && window.location.href !== 'https://morpheus.gq/login.html') {
        window.location = '/login.html';
    }
}

$(document).ready(function () {
    checkLoggedUser();
});