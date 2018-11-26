$(function(){	
	/*显示左侧菜单栏*/
	$(".view_main").mousemove(function(e){
		if(e.clientX<10){//当鼠标在距屏幕左50px内
			$(".view_leftNav").css({"display":"block"})
			$(".view_content").css({"width":"92%"})
		}
	})
	
	/*隐藏左侧菜单栏*/
	$(".view_leftNav").mouseout(function(){
		$(".view_leftNav").css({"display":"none"})
	})
	
	//点击宏观经济数据按钮
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
})















