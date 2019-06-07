function clientsSelect(){

    $.ajax({
        type: "GET",
        url: "/api/client",
        dataType: "json",
        contentType: 'application/json',
        headers: { 'Authorization': localStorage.auth_token },
        success: function (response) {

            response = response['data'];

            var clients = [];

            for (var k = 0; k < response.length; k++){
                clients.push({'value': response[k]['id'], 'text': response[k]['name']})
            }

            var selectBox = document.getElementById('client');

            for(var i = 0, l = clients.length; i < l; i++){
                var option = clients[i];
                selectBox.options.add( new Option(option.text, option.value, option.selected) );
            }

        }

    });

}

function transportSelect(){

    $.ajax({
        type: "GET",
        url: "/api/transport",
        dataType: "json",
        contentType: 'application/json',
        headers: { 'Authorization': localStorage.auth_token },
        success: function (response) {

            response = response['data'];

            var transport = [];

            for (var k = 0; k < response.length; k++){
                transport.push({'value': response[k]['id'], 'text': response[k]['name']})
            }

            var selectBox = document.getElementById('transport');

            for(var i = 0, l = transport.length; i < l; i++){
                var option = transport[i];
                selectBox.options.add( new Option(option.text, option.value, option.selected) );
            }

        }

    });

}

function create_ci(){
    event.preventDefault();


    if (confirm("Tem certeza que deseja cadastrar a CI?")){

        $.ajax({
            type: "POST",
            url: "/api/ci",
            dataType: "json",
            contentType: 'application/json',
            headers: { 'Authorization': localStorage.auth_token },
            data: JSON.stringify({
                'client_id': parseInt($("#client").val()),
                'transport_id': parseInt($("#transport").val())
            }),
            success: function (response) {
                var ci_id = response['created_id']
            }
        });

        var items = [];

        // $('input[name^="amount"]').each(function(index, item){
        // var value = $('input[id^="txtAnswer"]').val();
        // var id = $('input[id^="txtAnswer"]').attr('id');
        // alert('id: ' + id + ' value:' + value);
// });

    }

}

$('#addItem').on('click', function(){
    event.preventDefault();
    var form = $(this).closest("form");

    var fields = form.find("input[name^=amount]");

    var x = fields.get().reduce((x, element) => {
        var thisx = element.name.match(/amount\[(\d+)\]/);
        console.log(thisx);
    if (thisx) {
        thisx = +thisx[1];
        if (x < thisx) {
            x = thisx;
        }
    }
    return x;
    }, 0);

    ++x;

    form.append('<label for="amount['+x+']"><input type="number" class="form-control" name="amount['+x+']" placeholder="1" min="1" required="required"></label>');
    form.append('<label for="unit['+x+']"><input type="text" class="form-control" name="unit['+x+']" placeholder="Big Bags" required="required"></label>');
    form.append('<label for="name['+x+']"><input type="text" class="form-control" name="name['+x+']" placeholder="Brass Scrap Honey" required="required"></label>');
    form.append('<label for="weight_unit['+x+']"><input type="number" class="form-control" name="weight_unit['+x+']" step="any" min="1" placeholder="1.0" required="required"></label>');
    form.append('<label for="net_weight['+x+']"><input type="number" class="form-control" name="net_weight['+x+']" step="any" min="1" placeholder="25.0" required="required"></label>');
    form.append('<label for="ncm['+x+']"><input type="number" class="form-control" name="ncm['+x+']" placeholder="7281" minlength="4" maxlength="8" required="required"></label>');
    form.append('<label for="value['+x+']"><input type="number" class="form-control" name="value['+x+']" placeholder="4.53" min="1" required="required"></label><br>');

});


$(document).ready(function () {
    clientsSelect();
    transportSelect();

});