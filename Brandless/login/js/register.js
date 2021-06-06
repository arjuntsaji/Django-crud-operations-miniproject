     <script>
         $(document).ready(function () {
           $("#username").keyup(function() {
                $.ajax({
                   data: $(this).serialize(),
                   url:"{% url 'validate_username' %}",
                   success: function (response) {
                         if (response.is_taken ==true){
                            $('#username').removeClass('is-valid').addClass('is-invalid');
                            $('#username').after('<span style="color:red; class="error_form" id="usernameError">This username is not available</span>')
                          }
                          else{
                               $('#username').removeClass('is-invalid').addClass('is-valid');
                               $('#usernameError').remove();
                              }
                           },
                         error: function (response) {
                                console.log(response.responseJSON.errors)
                               }
                             });
                             return false;
                           });
                         })

     </script>