$(function(){
    var data_dq = document.getElementById("data_dq");
    var j = new Date();
    // time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time(j)))
    console.log(j)
    data_dq.innerHTML = j

    function gettotle(){
				var tnum = 0;
				var tprice = 0;
				$(".sp li").each(function(){

					if($(this).find(".xz").prop("checked")){
						tnum += parseInt($(this).find(".gwspsl").find("b").html());
						tprice += parseInt($(this).find(".gwspxj").find("b").html());
					}
				});
				$("#totalsp").html(tnum);
				$("#addjg").html(tprice);
			}

    


    $("#jian").click(function(){
				var n = parseInt($(this).next().html());
				if (n>1) {
					n--;
				}
				$(this).next().html(n);
				var price = parseFloat($(this).parent().prev().html());

				$(this).parent().next().find("b").html(n*price);
				gettotle();

			});

    $("#jia").click(function(){
				var n = parseInt($(this).prev().html());
				n++;
				$(this).prev().html(n);
				var price = parseFloat($(this).parent().prev().html());

				$(this).parent().next().find("b").html(n*price);
				gettotle();
			});




   



//     document.getElementById("data_dq").onclick = function () {
//
//     timeId = window.setTimeout(function () {
//
//     console.log("一次性定时器开启");
//
// }, 1000);
//
// };



})