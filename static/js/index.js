function printCi() {
    $('#new_ci_btn').hide();
    $('#ci_print_btn').hide()

    window.print();
}

function getCI(ci_id) {

    $.ajax({
        type: "GET",
        url: "/api/ci/"+ci_id,
        dataType: "json",
        contentType: 'application/json',
        headers: { 'Authorization': localStorage.auth_token },
        success: function (response) {

            var tbl = '<p><strong>CI code:</strong> '+ response['data']['id']+'</p>';
            tbl+= '<p><strong>Client:</strong> '+ response['data']['client_name']+'</p>';
            tbl+= '<p><strong>Created at:</strong> '+ response['data']['created_at']+'</p>';
            tbl+= '<p><strong>Transport:</strong> '+ response['data']['transport']['name']+'</p>';
            tbl+= '<p><strong>Transport type:</strong> '+ response['data']['transport']['type']+'</p><br>';

            response = response['data']['materials'];

            //--->create data table > start
            tbl +='<table class="table table-hover">';
            //--->create table header > start
            tbl +='<thead>';
            tbl +='<tr>';
            tbl +='<th>Amount</th>';
            tbl +='<th>Unit</th>';
            tbl +='<th>Description</th>';
            tbl +='<th>Weight Unit</th>';
            tbl +='<th>Net Weight</th>';
            tbl +='<th>NCM</th>';
            tbl +='<th>Value (USD)</th>';
            tbl +='</tr>';
            tbl +='</thead>';
            //--->create table header > end

            //--->create table body > start
            tbl +='<tbody>';

            //--->create table body rows > start
            $.each(response, function(index, val)
            {
                var row_id = val['id'];
                //loop through ajax row data
                tbl +='<tr row_id="'+row_id+'">';
                tbl +='<td ><div class="row_data" edit_type="click" col_name="amount">'+val['amount']+'</div></td>';
                tbl +='<td ><div class="row_data" edit_type="click" col_name="amount">'+val['unit']+'</div></td>';
                tbl +='<td ><div class="row_data" edit_type="click" col_name="client">'+val['name']+'</div></td>';
                tbl +='<td ><div class="row_data" edit_type="click" col_name="created_at">'+val['weight_unit']+'</div></td>';
                tbl +='<td ><div class="row_data" edit_type="click" col_name="created_at">'+val['net_weight']+'</div></td>';
                tbl +='<td ><div class="row_data" edit_type="click" col_name="created_at">'+val['ncm']+'</div></td>';
                tbl +='<td ><div class="row_data" edit_type="click" col_name="created_at">'+val['value']+'</div></td>';

                tbl +='</tr>';
            });

            //--->create table body rows > end

            tbl +='</tbody>';
            //--->create table body > end

            tbl +='</table>';
            tbl +='<br><button onclick="printCi();" class="btn btn-info" id="ci_print_btn" >Imprimir</button>';
            //--->create data table > end

            //out put table data
            $(document).find('.tbl_user_data').html(tbl);

        }

    });
}

function table(response) {

    //--->create data table > start
    var tbl = '';
    tbl +='<table class="table table-hover">';

    //--->create table header > start
    tbl +='<thead>';
    tbl +='<tr>';
    tbl +='<th>Cod. da CI</th>';
    tbl +='<th>Cliente</th>';
    tbl +='<th>Data de criação</th>';
    tbl +='<th>Visualizar</th>';
    tbl +='</tr>';
    tbl +='</thead>';
    //--->create table header > end


    //--->create table body > start
    tbl +='<tbody>';

    //--->create table body rows > start
    $.each(response, function(index, val)
    {
        var row_id = val['id'];
        //loop through ajax row data
        tbl +='<tr row_id="'+row_id+'">';
        tbl +='<td ><div class="row_data" edit_type="click" col_name="ci_id">'+row_id+'</div></td>';
        tbl +='<td ><div class="row_data" edit_type="click" col_name="client">'+val['client_name']+'</div></td>';
        tbl +='<td ><div class="row_data" edit_type="click" col_name="created_at">'+val['created_at']+'</div></td>';


        //--->edit options > start
        tbl +='<td>';

        tbl +='<span class="btn_edit" > <a href="#" class="btn btn-link " row_id="'+row_id+'" > Abrir</a> </span>';


        tbl +='</td>';
        //--->edit options > end

        tbl +='</tr>';
    });

    //--->create table body rows > end

    tbl +='</tbody>';
    //--->create table body > end

    tbl +='</table>';
    //--->create data table > end

    //out put table data
    $(document).find('.tbl_user_data').html(tbl);


    //--->button > print > start
    $(document).on('click', '.btn_edit', function(event)
    {
        event.preventDefault();
        var tbl_row = $(this).closest('tr');

        var row_id = tbl_row.attr('row_id');

        getCI(row_id);

    });
    //--->button > print > end


}



function getHome() {

    $.ajax({
        type: "GET",
        url: "/api/home",
        dataType: "json",
        contentType: 'application/json',
        headers: { 'Authorization': localStorage.auth_token },
        success: function (response) {
            table(response['data']);
        }

    });


}

function formHide() {
    var form = $('#form');

    if (form.is(":visible")){
        form.hide();
    }else{
        form.show();
    }
}

$(document).ready(function () {
    $('#created_message').hide();
    $('#form').hide();

    getHome();
});



