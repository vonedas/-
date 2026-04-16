
/*搜索分页处理开始*/

var tablesave = $("#allitems").html();
tablesave = "<div id='allitems'>" + tablesave + "</div>"
var search = "";

var currentPage = 1;

function goTablePage(pno, psize) {

    search = $("#search").val();
    $("#allitems").replaceWith(tablesave);

    // console.log(tablesave);

    var num = $("#allitems .oneitem").length;

    var scindex = [];
    for (var i = 1; i < (num + 1); i++) {

        var trhtml = $("#allitems .oneitem").eq(i - 1)

        var tdarr = trhtml.find('td')

        for (var k = 0; k < tdarr.length; k++) {

            var searchitem = $("#search" + k).val()

            if (tdarr[k].innerText.indexOf(searchitem) == -1 && searchitem) {
                scindex.push(i - 1);
                break;
            }

        }

        if ($("#allitems .oneitem")[i - 1].innerText.indexOf(search) == -1 && search) {
            scindex.push(i - 1);
        }


    }

    for (var i = scindex.length - 1; i >= 0; i--) {
        $("#allitems .oneitem")[scindex[i]].remove();
    }

    num = $("#allitems .oneitem").length;

    var totalPage = 0;//总页数
    var pageSize = psize;//每页显示行数
    //总共分几页
    if (num / pageSize > parseInt(num / pageSize)) {
        totalPage = parseInt(num / pageSize) + 1;
    } else {
        totalPage = parseInt(num / pageSize);
    }
    var currentPage = pno;//当前页数
    var startRow = (currentPage - 1) * pageSize + 1;//开始显示的行 31
    var endRow = currentPage * pageSize;//结束显示的行  40
    endRow = (endRow > num) ? num : endRow;  //40
    //遍历显示数据实现分页
    for (var i = 1; i < (num + 1); i++) {
        if (i >= startRow && i <= endRow) {
            $("#allitems .oneitem")[i - 1].style.display = "inline-block";
        } else {
            $("#allitems .oneitem")[i - 1].style.display = "none";
        }
    }
    var tempStr1 = "共" + num + "条记录 分" + totalPage + "页 当前第" + currentPage + "页";
    if (currentPage > 1) {

        $("#shangyiye").off("click");
        $("#shangyiye").click(function () {
            goTablePage(currentPage - 1, psize)
        });
    } else {

        $("#shangyiye").off("click");
    }
    if (currentPage < totalPage) {
        $("#xiayiye").off("click");
        $("#xiayiye").click(function () {
            goTablePage(currentPage + 1, psize)
        });
    } else {
        $("#xiayiye").off("click");
    }

    try {
        document.getElementById("tempStr1").innerHTML = tempStr1;
    } catch (error) {

    }


    $("#dangqianye").html(currentPage);

    $("#searchbtn").off("click");
    $("#searchbtn").prop("type", "button");
    $("#searchbtn").click(function () {
        goTablePage(1, psize)
    });

}

goTablePage(1, 10)

/*搜索分页处理结束*/
