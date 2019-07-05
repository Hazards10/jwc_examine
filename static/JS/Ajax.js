function req(url,data,callback){
	var xmlhttp;
	if(window.XMLHttpRequest){
		xmlhttp=new XMLHttpRequest();
	}
	else{
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function(){
		if(xmlhttp.readyState==4&&xmlhttp.status==200){
			//接收数据
		//	alert(JSON.parse(xmlhttp.responseText));
		if(callback){
				if(JSON.parse(xmlhttp.responseText)!='');{
					callback(JSON.parse(xmlhttp.responseText));
		}}
		}
		else{
			if(xmlhttp.readyState==1&&xmlhttp.status==0){}
		else if(xmlhttp.readyState==2&&xmlhttp.status==200){}
		else if(xmlhttp.readyState==3&&xmlhttp.status==200){}
		else {
			alert("未知错误！");
			}
		}
	}
	xmlhttp.open("POST",url,true);
	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	xmlhttp.send(data);
}

 function jqpost(url,jsondata){
    $.post(url,jsondata);
}
function getGuid()
{
    var guid = "";
    for (var i = 1; i <= 32; i++){
      var n = Math.floor(Math.random()*16.0).toString(16);
      guid +=   n;
      if((i==8)||(i==12)||(i==16)||(i==20))
        guid += "-";
    }
    return guid;    
}





