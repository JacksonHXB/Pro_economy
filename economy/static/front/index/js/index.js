$(function(){	
	
console.log("执行了index.js")

/*给右下角设置时间*/
$.setTime = function(){
	setInterval(function(){
		var time = dateFtt("yyyy-MM-dd hh:mm:ss", new Date())
		$(".currentTime").text(time)
	},1000)
}


/*显示左侧菜单栏*/
//$(".view_main").mousemove(function(e){
//	console.log(e)
//	if(e.clientX<10){//当鼠标在距屏幕左50px内
//		$(".view_leftNav").css({"display":"block"})
//		$(".view_content").css({"width":"92%"})
//	}
//})
/*隐藏左侧菜单栏*/
//$(".view_leftNav").mouseout(function(){
//	$(".view_leftNav").css({"display":"none"})
//})







/*点击宏观经济数据按钮*/
$("#macroData").click(function(){
	$("#iframe").attr({"src":"http://localhost:8001/macroData"})
    new Promise(function(mySuccess,myFail){
    	$.ajax({
            type: 'POST',
            url:'/toXiaoBing',
            data: JSON.stringify({
                flag:'macroData'
            }),
            success: function (res) {
            	var data = eval("("+res+")")
            	mySuccess(data.data)
            }
        })
    }).then(function(res){
        $(".xiaoBing").attr({"src":res})
        document.getElementById("xiaoBing").play()
    })
})	


/*点击新闻*/
$('body').on('click', '.btn', function(){  //使用最新的on函数绑定，body是第一次加载就存在的元素
	let href = $(this).attr("attr-href")
	window.open(href, '_blank',"top=100,left=100,height=600,width=1000,menubar=no,toolbar=no,status=no,scrollbars=yes")
})


/*点击关闭按钮*/
$(".closeIcon").click(function(){
	$(".newsTip").fadeOut("normal")
})


$.getTopNews = function(){
	var newsTimer = setTimeout(function(){
		new Promise(function(mySuccess,myFail){
			$.ajax({
				type: 'GET',
				url:'/index/news/topNews',
				success: function (res) {
					var data = eval("("+res+")")
					mySuccess(data)
				}
			})
		}).then(function(res){
			$(".newsTip").fadeIn("normal")
//			$(".newsTip").css({"display":"block"})
			for(let i in res){
				let oneNew = "<li><div class='btn' attr-href="+ res[i]["href"] +">"+ res[i]["title"] +"</div></li>"
				$(".newLists").append(oneNew)
			}
		})
	},3000)
	setTimeout(function(){ //9s之后关闭新闻弹窗 
		$(".newsTip").fadeOut("normal")
	},9000)
	
}


/*定时向后台发送请求，获取最新的新闻信息*/
$.getLatestNew = function(){
	//向服务器请求数据
	
	
	setInterval(function(){//每1分钟向客户端发送请求
		console.log("获取最新新闻")
//		new Promise(function(mySuccess,myFail){
//			$.ajax({
//				type: 'POST',
//				url:'/toXiaoBing',
//				data: JSON.stringify({
//					flag:'macroData'
//				}),
//				success: function (res) {
//					var data = eval("("+res+")")
//					mySuccess(data.data)
//				}
//			})
//		}).then(function(res){
//			$(".xiaoBing").attr({"src":res})
//			document.getElementById("xiaoBing").play()
//		})
	},1000*60)
}


$.setTime()					//设置时间
$.getTopNews()				//获取新闻列表
$.getLatestNew()			//执行获取最新新闻

})

/*时间格式处理*/
function dateFtt(fmt,date)   { //author: meizz   
	var o = {   
		"M+" : date.getMonth()+1,                 //月份   
		"d+" : date.getDate(),                    //日   
		"h+" : date.getHours(),                   //小时   
		"m+" : date.getMinutes(),                 //分   
		"s+" : date.getSeconds(),                 //秒   
		"q+" : Math.floor((date.getMonth()+3)/3), //季度   
		"S"  : date.getMilliseconds()             //毫秒   
	};   
	if(/(y+)/.test(fmt))   
		fmt=fmt.replace(RegExp.$1, (date.getFullYear()+"").substr(4 - RegExp.$1.length));   
	for(var k in o)   
		if(new RegExp("("+ k +")").test(fmt))   
	fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));   
	return fmt;   
}















