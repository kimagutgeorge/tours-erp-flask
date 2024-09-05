$(document).ready(function(){
    // login form
    $('#login-form').on('submit', function(e){
        e.preventDefault()
        $.ajax({
            url:'/process?link=user-login',
            method:'POST',
            data:$('#login-form').serialize(),
            success:function(data){
                $('#login-result').html(data)
                setTimeout(() => {
                    $('#login-result').html('')
                }, 3000);
            }
        })
    })
})