$(document).ready(function()
{
    $('#likebtn').on('click',function(event)
    {
        $.ajax({
    
            type:'GET',
            url:'/liked?sr='+$('#postsr').text()+'&slug='+$('#postslug').text()
            
        })
        .done(function(data)
        {
           if(data.redirect)
           {
            window.location.href=data.redirect;
           }
           if(data.liked)
           {
               $('#likebtn').attr({'class':'btn btn-danger'})
               $('#likes').text(data.likecnt)
           }
           else
           {
               $('#likebtn').attr({'class':'btn btn-outline-danger'})
               $('#likes').text(data.likecnt)
           }
        })
        event.preventDefault()
    })
})