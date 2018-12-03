$(function(){	
	/*显示左侧菜单栏*/
	$(".view_main").mousemove(function(e){
		if(e.clientX<10){//当鼠标在距屏幕左50px内
			console.log(e)
			$(".view_leftNav").css({"display":"block"})
			$(".view_content").css({"width":"92%"})
		}
	})
	
	/*隐藏左侧菜单栏
	$(".view_leftNav").mouseout(function(){
		$(".view_leftNav").css({"display":"none"})
	})
	 * */
	
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
	$(".btn").click(function(){
		let href = $(this).attr("attr-href")//取出自定义的属性
		window.open(href, '_blank',"top=100,left=100,height=600,width=1000,menubar=no,toolbar=no,status=no,scrollbars=yes")
	})
	
	/*点击关闭按钮*/
	$(".closeIcon").click(function(){
		$(".newsTip").css({"display":"none"})
	})
})













