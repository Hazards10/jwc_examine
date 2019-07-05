	$(function(){

		//快捷菜单
		bindQuickMenu();

		//菜单切换(测试)
		bindAdminMenu();
		ChangeNav("first");

		//菜单开关
		LeftMenuToggle();

		//全部功能开关
		AllMenuToggle();

		//取消菜单链接虚线
		$(".head").find("a").click(function(){$(this).blur()});
		$(".menu").find("a").click(function(){$(this).blur()});


	}).keydown(function(event){//快捷键
		if(event.keyCode ==116 ){
			url = $("#main").attr("src");
			main.location.href = url;
			return false;
		}
		if(event.keyCode ==27 ){
			$("#qucikmenu").slideToggle("fast")
		}
	});

	function bindQuickMenu(){//快捷菜单
		$("#ac_qucikmenu").bind("mouseenter",function(){
			$("#qucikmenu").slideDown("fast");
		}).dblclick(function(){
			$("#qucikmenu").slideToggle("fast");
		}).bind("mouseleave",function(){
			hidequcikmenu=setTimeout('$("#qucikmenu").slideUp("fast");',700);
			$(this).bind("mouseenter",function(){clearTimeout(hidequcikmenu);});
		});
		$("#qucikmenu").bind("mouseleave",function(){
			hidequcikmenu=setTimeout('$("#qucikmenu").slideUp("fast");',700);
			$(this).bind("mouseenter",function(){clearTimeout(hidequcikmenu);});
		}).find("a").click(function(){
			$(this).blur();
			$("#qucikmenu").slideUp("fast");
			$("#ac_qucikmenu").text($(this).text());
		});
	}


	function bindAdminMenu(){
		$("#nav").find("a").click(function(){
			ChangeNav($(this).attr("_for"));
		});

		$("#menu").find("dt").click(function(){
			dt = $(this);
			dd = $(this).next("dd");
			if(dd.css("display")=="none"){
				dd.slideDown("fast");
				dt.css("background-position","left bottom");
			}else{
				dd.slideUp("fast");
				dt.css("background-position","left top");
			}
		});

		$("#menu dd ul li a").click(function(){
			$(this).addClass("thisclass").blur().parents("#menu").find("ul li a").not($(this)).removeClass("thisclass");
			//url = $(this).attr("_href");
			//main.location.href = url;
			//return false;
		});
	}

	function ChangeNav(nav){//菜单跳转
		$("#nav").find("a").removeClass("thisclass");
		$("#nav").find("a[_for='"+nav+"']").addClass("thisclass").blur();
		$("body").attr("class","showmenu");
		$("#menu").find("div[id^=items]").hide();
		$("#menu").find("#items_"+nav).show().find("dl dd").hide().find("ul li a").removeClass("thisclass");
		$("#menu").find("#items_"+nav).show().find("#dl_items_1"+"_1").show().find("dd").show().find("ul li a").removeClass("thisclass");
		$("#menu").find("#items_"+nav).show().find("#dl_items_1"+"_2").show().find("dd").show().find("ul li a").removeClass("thisclass");
		$("#menu").find("#items_"+nav).show().find("#dl_items_1"+"_3").show().find("dd").show().find("ul li a").removeClass("thisclass");
		$("#menu").find("#items_"+nav).show().find("#dl_items_1"+"_4").show().find("dd").show().find("ul li a").removeClass("thisclass");
		$("#menu").find("#items_"+nav).show().find("#dl_items_1"+"_5").show().find("dd").show().find("ul li a").removeClass("thisclass");
		$("#menu").find("#items_"+nav).show().find("#dl_items_1"+"_6").show().find("dd").show().find("ul li a").removeClass("thisclass");
		$("#menu").find("#items_"+nav).show().find("#dl_items_1"+"_7").show().find("dd").show().find("ul li a").removeClass("thisclass");
		$("#menu").find("#items_"+nav).show().find("#dl_items_1"+"_8").show().find("dd").show().find("ul li a").removeClass("thisclass");
		$("#menu").find("#items_"+nav).show().find("#dl_items_1"+"_9").show().find("dd").show().find("ul li a").removeClass("thisclass");
		$("#menu").find("#items_"+nav).show().find("#dl_items_1"+"_10").show().find("dd").show().find("ul li a").removeClass("thisclass");
		$("#menu").find("#items_"+nav).show().find("dd ul li a").eq(0).addClass("thisclass").blur();
	}

	function LeftMenuToggle(){   //显示隐藏侧边的菜单
		$("#togglemenu").click(function(){
			if($("body").attr("class")=="showmenu"){
				$("body").attr("class","hidemenu");
				$(this).html("显示菜单");
			}else{
				$("body").attr("class","showmenu");
				$(this).html("隐藏菜单");
			}
		});
	}


	function AllMenuToggle(){
		mask = $(".pagemask,.iframemask,.allmenu");
		$("#allmenu").click(function(){
				mask.show();
		});
		//mask.mousedown(function(){alert("123");});
		mask.click(function(){mask.hide();});
	}
	
	//function reinitIframe(Frame) {  //iframe框架自适应高度,支持火狐，支持嵌套
//    var iframeportal = document.getElementById(Frame);  
//    var iframeHeight = iframeportal.height;  
//    try {  
//        if (iframeportal == null) iframeportal = document.getElementById(Frame);  
//        var height = 0;  
//        if (isFirefox = navigator.userAgent.indexOf("Firefox") > 0) {  
//            height = iframeportal.contentWindow.document.documentElement.offsetHeight;  
//        }  
//        else {  
//            height = iframeportal.contentWindow.document.body.scrollHeight;  
//        }  
//        if (iframeHeight != height) iframeportal.height = height;  
//    }  
//    catch (ex) { }  
//	}  
