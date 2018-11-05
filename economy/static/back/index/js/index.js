$(function () {
    $(".containerLeft").mouseover(function () { //当鼠标进入一级菜单图标面板时
        $(".firstMenu").css({"display":"block"})
    })
    $(".firstMenu").mouseleave(function () { //当鼠标离开一级菜单面板时
        $(".firstMenu").css({"display":"none"})
    })
    $(".li_1").mouseover(function () {//显示一级面板s
        $(".li_2").css({ "background": "grey" })
        $(".li_3").css({ "background": "grey" })
        $(".li_1").css({ "background": "red" })
    })
    $(".li_2").mouseover(function () {//显示一级面板s
        $(".li_1").css({ "background": "grey" })
        $(".li_3").css({ "background": "grey" })
        $(".li_2").css({"background":"red"})
    })
    $(".li_3").mouseover(function () {//显示一级面板s
        $(".li_1").css({ "background": "grey" })
        $(".li_2").css({ "background": "grey" })
        $(".li_3").css({"background":"red"})
    })
    $(".addMenu").click(function () {//添加一级菜单类
        console.log("增加菜单")
        //向后台传递数据，再iframe里面返回页面
        $(".frame").attr({"src":"../addMenu/addMenu.html"})
    })
});

























