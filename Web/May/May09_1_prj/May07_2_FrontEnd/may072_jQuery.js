function connectMachineRegEvent() {
    $("button").click(function () {
        var c = $("#colorInput").val();
        var s = $("#statusInput").val();

        var url = "http://127.0.0.1:5678/machine.reg?color=" + c + "&status=" + s;
        $.getJSON(url, function (json) {
            alert(json.result);
            getMachineData();
        });

        $("#colorInput").val("");
        $("#statusInput").val("");
    });
}

function getMachineData(page) {
    $.getJSON("http://127.0.0.1:5678/machine.get?page=" + page, function (json) {
        // 게시판
        $("ul").empty();
        $.each(json.machines, function (i, m) {
            var br1 = $("<br>");
            var br2 = $("<br>");
            var li = $("<li><li>").append(m.color, br1, m.status, br2, m.checkDate);
            $("ul").append(li);
        });
        $("ul").listview("refresh");

        // 페이지
        $("#pageControlArea td").empty();
        for (var i = 1; i <= json.pageCount; i++) {
            var a = $("<a></a>").attr("onclick", "getMachineData(" + i + ");").text(i);
            $("#pageControlArea td").append(a);
        }
    });
}

$(function () {
    connectMachineRegEvent();
    getMachineData(1);
});