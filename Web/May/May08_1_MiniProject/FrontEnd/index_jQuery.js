
let selectedId = null;

function machineDataSelect() {
    $.getJSON("http://127.0.0.1:5678/machine.sel", function (data) {
        let html = "";
        data.forEach(function(car) {

            html += `
                <li>
                    <a href='#editPage' data-id='${car.no}' data-color='${car.color}' data-status='${car.status}' data-date='${car.check_date}'>
                    <h3>${car.no}. ${car.color} - ${car.status}</h3>
                    <p>${car.check_date}</p>
                    </a>
                </li>`;
        });
        
        $("#carList").listview("destroy").empty();
        $("#carList").html(html).listview();
    });
}

function machineDataRegister() {
    $("#registerBtn").off("click").on("click", function () {
        var color = $("#colorInput").val();
        var status = $("#statusInput").val();

        var url = "http://127.0.0.1:5678/machine.reg?color=" + color + "&status=" + status;

        $.getJSON(url, function(result) {
            alert(JSON.stringify(result));
        });

        $("#colorInput").val("");
        $("#statusInput").val("");

        machineDataSelect();
    });
    
}

function machineDataDelete() {

    $("#deleteBtn").off("click").on("click", function () {
        
        var car_num = $("#editNoDisplay").text();
        
        var url = "http://127.0.0.1:5678/machine.del?number=" + car_num;

        $.getJSON(url, function(result) {
            alert(JSON.stringify(result));
        });

        machineDataSelect();

        $.mobile.changePage("#mainPage", { reverse: true });
    });

}

function machineDataEdit() {

    $("#editSubmit").off("click").on("click", function () {
        
        var car_num = $("#editNoDisplay").text();
        var color = $("#editColor").val();
        var status = $("#editStatus").val();
        
        var url = "http://127.0.0.1:5678/machine.upd?number=" + car_num + "&color=" + color + "&status=" + status;

        $.getJSON(url, function(result) {
            alert(JSON.stringify(result));
        });

        machineDataSelect();

        $.mobile.changePage("#mainPage", { reverse: true });
    });

}

$(document).on("pagebeforeshow", "#mainPage", function () {


    machineDataRegister();

    machineDataSelect();

    machineDataDelete();

    machineDataEdit();

    
    $(document).on("click", "#carList a", function () {
        selectedCarId = $(this).data("id");
        const color = $(this).data("color");
        const status = $(this).data("status");
    
        $("#editNoDisplay").text(selectedCarId);
        $("#editColor").val(color);
        $("#editStatus").val(status);
    });


/*
    $(document).on("pagebeforeshow", "#listPage", function () {
        $.getJSON("http://127.0.0.1:8888/machine.list", function (data) {
            let html = "<ul data-role='listview'>";
            data.forEach(function(car) {
                html += `<li><a href="#editPage" data-id="${car.id}" data-color="${car.color}" data-status="${car.status}">${car.id}: ${car.color} - ${car.status} (${car.time})</a></li>`;
            });
            html += "</ul>";
            $("#carList").html(html).trigger("create");
        });
    });

    $(document).on("click", "#carList a", function () {
        selectedId = $(this).data("id");
        $("#editColor").val($(this).data("color"));
        $("#editStatus").val($(this).data("status"));
    });

    $("#editSubmit").click(function () {
        var color = $("#editColor").val();
        var status = $("#editStatus").val();
        var url = `http://127.0.0.1:8888/machine.update?id=${selectedId}&color=${color}&status=${status}`;
        $.getJSON(url, function (result) {
            alert(result[“결과”]);
        });
    });
    */
});