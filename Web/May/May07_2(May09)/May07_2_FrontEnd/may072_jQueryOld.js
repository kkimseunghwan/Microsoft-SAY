function connectMachineRegEvent() {
    $("button").click(function () {
        var c = $("#colorInput").val();
        var s = $("#statusInput").val();

        var url = "http://195.168.9.201:5698/machine.reg?color=" + c + "&status=" + s;
        $.getJSON(url, function (json) {
            alert(json.result);
            getMachineData(1);
        });

        $("#colorInput").val("");
        $("#statusInput").val("");
    });
}

function connectMachineSearchEvent() {
    $("#searchInput").keyup(function (e) {
        getMachineData(1);
    });
}

function connectMainpageGoEvent() {
    $("#goMainPageA").click(function () {
        getMachineData(1);
    });
}

function getMachineData(page) {
    var searchTxt = $("#searchInput").val();
    var url = "http://195.168.9.201:5698/machine.get?page=" + page + "&search=" + searchTxt;
    $.getJSON(url, function (json) {
        $("ul").empty();
        $.each(json.machines, function (i, m) {
            var br1 = $("<br>");
            var br2 = $("<br>");
            var li = $("<li></li>").append(m.color, br1, m.status, br2, m.checkDate);
            $("ul").append(li);
        });
        $("ul").listview("refresh");

        $("#pageControlArea td").empty();
        for (var i = 1; i <= json.pageCount; i++) {
            var a = $("<a></a>").attr("onclick", "getMachineData(" + i + ");").text(i);
            $("#pageControlArea td").append(a);
        }
    });
}

$(function () {
    connectMachineRegEvent();
    connectMachineSearchEvent();
    connectMainpageGoEvent();
});