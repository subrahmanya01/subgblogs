

function popup_visible(linkaddr)
{
    let popup  = document.getElementById(String(linkaddr));
    console.log(linkaddr)
    popup.style="visibility:visible; top:100% ; transform:translate(-50%,-50%) scale(1);";
       
}
function no_btn_func(linkaddr)
{
    let popup  = document.getElementById(String(linkaddr));
    
    popup.style="visibility:hidden; top:0 ; transform:translate(-50%,-50%) scale(0.1);";
}
