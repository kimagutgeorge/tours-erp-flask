$(document).ready(function(){
    // login form
    $('#login-form').on('submit', function(e){
        e.preventDefault()
        $.ajax({
            url:'/process?link=login',
            method:'POST',
            data:$('#login-form').serialize(),
            success: function(response) {
                // Handle success response
                $('#responseMessage').text(response.message);
                if (response.status === "success") {
                    // Redirect or perform actions after successful login
                    console.log('Logged in!');
                }
            },
            error: function(error) {
                // Handle error response
                $('#responseMessage').text('Login failed: ' + error.responseJSON.message);
            }
        })
    })
})