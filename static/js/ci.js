function send_ci() {
    var payload = {};
    payload.commercial_invoice_id = $('#ci_id').val();
    payload.measument_unit_id = $('#measurement_id').val();
    payload.material_id = $('#material_id').val();
    var data = JSON.stringify(payload);

    $.ajax({
        type: "POST",
        url: "/ci",
        dataType: "json",
        contentType: 'application/json',
        data: data,
        statusCode: 200
    });
}