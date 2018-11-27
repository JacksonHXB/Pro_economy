$(function(){		
	$(".queryCountry").click(function(){
		let country = $(".country").val()
		new Promise(function(mySuccess,myFail){
        	$.ajax({
                type: 'GET',
                url:'/macroData/gdps/countries/'+country,
                success: function (res) {
                	mySuccess(JSON.parse(res))
                }
            })
        }).then(function(res){
        	console.log("执行了")
        	// 基于准备好的dom，初始化echarts实例
            var myChart = echarts.init(document.getElementById('main'));
     
            // 指定图表的配置项和数据
            var option = {
                title: {
                    text: '香港历年的GDP数据'
                },
                tooltip: {},
                legend: {
                    data:['销量']
                },
                xAxis: {
                    data: Object.keys(res["data"])
                },
                yAxis: {},
                series: [{
                    name: '销量',
                    type: 'bar',
                    data: Object.values(res["data"])
                }]
            };
     
            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
        })
	})
	

	
	
})

