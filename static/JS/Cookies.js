function setCookie(name,value,exdays){
    var d = new Date();
    d.setTime(d.getTime()+(exdays*24*60*60*1000));
    var expires = "expires="+d.toGMTString();
    document.cookie = name+"="+value+"; "+expires+";path=/";

}
function getCookie(name){
    var name = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i].trim();
        if (c.indexOf(name)==0) { return c.substring(name.length,c.length); }
    }
    return "";
}
//删除所有cookie
function clearCookie(){ 
var keys=document.cookie.match(/[^ =;]+(?=\=)/g); 
if (keys) { 
for (var i = keys.length; i--;) 
document.cookie=keys[i]+'=0;expires=' + new Date( 0).toUTCString() 
} 
}
