function check_correctness()
{
    
    const passwrd=document.getElementById('form3Example4').value;
    const conf_pass = document.getElementById('form3Example5').value;
    let button=document.getElementById('reset');
    console.log(conf_pass,passwrd);

    if(conf_pass=="" ||passwrd=="")
    {
    document.getElementById('confirmpasswordspan').innerHTML="";
    button.disabled = true;
    }
    else if(passwrd == conf_pass)
    {
       
        button.disabled = false;
        document.getElementById('confirmpasswordspan').innerHTML="Matching";
        document.getElementById('confirmpasswordspan').style.color="green";
    }
    else
    {
        button.disabled = true;
        document.getElementById('confirmpasswordspan').innerHTML="Not Matching";
        document.getElementById('confirmpasswordspan').style.color="red";
    }
}