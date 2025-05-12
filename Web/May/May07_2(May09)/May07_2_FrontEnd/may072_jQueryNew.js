var mainPage = false;
var page = 1;

function connectCoverpageGoEvent() {
    $("#goCoverPageA").click(function () {
        mainPage = false;
    });
}

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
        page = 1;
        getMachineData();
    });
}

function connectMainpageGoEvent() {
    $("#goMainPageA").click(function () {
        mainPage = true;
        page = 1;
        getMachineData();
    });
}

function connectScrollEvent() {
    $(window).scroll(function () {
        var htmlHeight = $(document).height();
        var browserHeight = $(window).height();
        var browserOffsetTop = $(window).scrollTop();
        var browserOffsetBottom = browserOffsetTop + browserHeight;
        if (mainPage && (browserOffsetBottom >= htmlHeight - 20)) {
            page++;
            getMachineData();
        }
    });
}

function getMachineData() {
    var searchTxt = $("#searchInput").val();
    var url = "http://195.168.9.201:5698/machine.get?page=" + page + "&search=" + searchTxt;
    $.getJSON(url, function (json) {
        if (page == 1) {
            $("ul").empty();
        }
        $.each(json.machines, function (i, m) {
            var br1 = $("<br>");
            var br2 = $("<br>");
            var a = $("<a></a>").attr("href", "#detailPage")
                .attr("onclick", "goDetailPage(" + m.no + ");")
                .append(m.color, br1, m.status, br2, m.checkDate);
            var li = $("<li></li>").append(a);
            $("ul").append(li);
        });
        $("ul").listview("refresh");
    });
}

function goDetailPage(no) {
    alert(no);
}

$(function () {
    connectCoverpageGoEvent();
    connectMachineRegEvent();
    connectMachineSearchEvent();
    connectMainpageGoEvent();
    connectScrollEvent();
});