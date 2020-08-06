$(document).ready(function() {
   $("#btn_phone_verification_code").click(function(event) {
     event.preventDefault();
     console.log("i'm btn_phone_verification_code");
     $.ajax({
       url: '/phone_verification',
       type: 'POST',
       data: $('form').serialize(),
       success: function(response) {
         console.log(response);
         $('#div_phone_verification').html(response);
       },
       error: function(error) {
         console.log(error);
         $('#div_phone_verification').html(error);
     }
    });
  });

  $("#btn_phone_verification_confirm").click(function(event) {
    event.preventDefault();
    console.log("i'm btn_phone_verification_confirm");
    $.ajax({
      url: '/verify',
      type: 'POST',
      data: $('form').serialize(),
      success: function(response) {
        console.log(response);
        $('#div_phone_verification').html(response);
      },
      error: function(error) {
        console.log(error);
        $('#div_phone_verification').html(error);
    }
   });
 });
});
