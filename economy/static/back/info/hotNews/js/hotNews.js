$(function(){	
	/* 点击搜索按钮 */
	$(".search").click(function(){
		console.log("search")
		let targetWeb = $(".targetWeb").val()
		switch(targetWeb){
		case "sina":
			console.log("点击了新浪")
			sinaHotNews()// 执行了点击凤凰函数
			break;
		case "fengHuang":
			console.log("点击了凤凰")
			break;
		default:
			console.log("默认为新浪")
		}
	})
})

/* 点击了凤凰 */
function sinaHotNews(){
	new Promise(function(mySuccess,myFail){
    	$.ajax({
            type: 'POST',
            url:'http://localhost:8001/back/info/hotNews/sina',
            data: {},
            success: function (res) {
            	var data = eval("("+res+")")
            	mySuccess(data)
            }
        })
    }).then(function(res){
        console.log(res)
        buildTable(res)
    })
}

/* 根据结果集合创建表格 */
function buildTable(res){
	console.log("创建表格")
	var table = document.getElementById("table")
	for(let i = 0; i<res.length; i++){
		var tr = document.createElement("tr")
		for(var key in res[i]){
			var td = document.createElement("td")
			var txt = document.createTextNode(res[i][key]);
			td.appendChild(txt);
			tr.appendChild(td);
		}
		
		
//		for(let j = 0; j<res[i].keys().length; j++){
//			var td = document.createElement("td")
//			var txt = document.createTextNode(res[i][]);
//			td.appendChild(txt);
//			tr.appendChild(td);
//		}
		table.appendChild(tr);
	}
}





































