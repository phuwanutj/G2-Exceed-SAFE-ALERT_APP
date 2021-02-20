function display_c(){
    var refresh=10;
    mytime=setTimeout('display_ct()',refresh)
    }

function display_ct() {
    var today = new Date();
    var seconds = today.getSeconds();
    var minutes = today.getMinutes();
    var hours = today.getHours();
    minutes = ("0" + minutes).slice(-2);
    hours = ("0" + hours).slice(-2);
    seconds = ("0" + seconds).slice(-2);
    var time = hours + ":" + minutes + ":" + seconds;
    document.getElementById("current-time").innerHTML = time;
    display_c();
}
