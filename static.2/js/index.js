$(function(){
    $(".button-collapse").sideNav();
});

function checkLoggedUser() {
    var token = $.cookie('access_token_cookie');

    if (token === undefined) {
        window.location = '/static/login.html';
    }
}

function getCIs() {

    $.ajax({
        type: "GET",
        url: "/api/home",
        dataType: "json",
        contentType: 'application/json',
        success: function (data) {

            var col = [];
            for (var i = 0; i < data.length; i++) {
                for (var key in data[i]) {
                    if (col.indexOf(key) === -1) {
                        col.push(key);
                    }
                }
            }
            var table = document.createElement("table");
            var tr = table.insertRow(-1);

            for (var i = 0; i < col.length; i++) {
                var th = document.createElement("th");
                th.innerHTML = col[i];
                tr.appendChild(th);
            }

            for (var i = 0; i < data.length; i++) {

                tr = table.insertRow(-1);

                for (var j = 0; j < col.length; j++) {
                    var tabCell = tr.insertCell(-1);
                    tabCell.innerHTML = data[i][col[j]];
                }
            }


            var divContainer = document.getElementById("ci");
            divContainer.innerHTML = "";
            divContainer.appendChild(table)
        }
    });
}

$(document).ready(function () {
    checkLoggedUser();
    getCIs();
});