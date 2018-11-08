$(function(){
	setAutoWebSize()/*自动调整body的尺寸*/
	
	/*自动调整当前body的尺寸*/
	function setAutoWebSize(){
		let browserHight = $(document).height()
		let browserWidth = $(document).width()
		$("body").css({"width":browserWidth,"height":browserHight})
		console.log(browserHight)
	}
	
})




















































