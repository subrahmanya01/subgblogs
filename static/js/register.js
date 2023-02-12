function strength_check()
{
    let inp = document.getElementById('form3Example4').value;
    const low_alpa=/[a-z]/i;
    const high_alpa=/[A-Z]/g;
    const num=/[0-9]/i;
    const symb=/[@|$|!|&|*|%|#]/i;
    let cnt=0;
    if(low_alpa.test(inp))
     cnt++;
     if(high_alpa.test(inp))
     cnt++;
     if(num.test(inp))
     cnt++;
     if(symb.test(inp))
     cnt++;
    if(inp.length==0)
    document.getElementById('pass_strength').innerHTML="";
    else if(cnt<3)
    {
    document.getElementById('pass_strength').innerHTML="Weak";
    document.getElementById('pass_strength').style.color="red";
    }
    else if(cnt==3)
    {
    document.getElementById('pass_strength').innerHTML="Medium";
    document.getElementById('pass_strength').style.color="violet";
    }
    else
    {
    document.getElementById('pass_strength').innerHTML="Strong";
    document.getElementById('pass_strength').style.color="green";

    }

}
function email_or_not()
{
    let val=document.getElementById('form3Example3').value;
    if(val=="")
    {
        document.getElementById('email_or_not').innerHTML="";  
    }
    else if(val.includes("@gmail.com") ||val.includes("@yahoo.com" ||val.includes("@kletech.ac.in")))
    {
        document.getElementById('email_or_not').innerHTML="";
        document.getElementById('form_submit').disabled=false;   
    }
    else
    {
        document.getElementById('form_submit').disabled=true;
        document.getElementById('email_or_not').innerHTML="Wrong email";  
    }

}

var cnt=0;
function checkbox_val()
{
    if(cnt%2==0)
    {
        document.getElementById("form3Example4").type = 'text';
        cnt++;
    }
    else
    {
        document.getElementById("form3Example4").type = 'password';
        cnt++;
    }

}


