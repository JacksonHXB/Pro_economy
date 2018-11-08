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
	
	
	
	
})