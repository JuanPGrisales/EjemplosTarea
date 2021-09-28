let loginNoxiun = new loginCompañia();
$(document).ready(function () {
  // jQuery methods go here...

  $("#buttonLogin").click(function () {
    let userName = $("#usernameLogin").val();
    let password = $("#passwordLogin").val();
    alert(loginNoxiun.loginUser(userName, password));
  });

  $("#buttonNewUser").click(function () {
    $("#cajaLogin").css("display","none");
    $("#cajaNewUser").css("display","flex");
  });

  $("#buttonCreateUser").click(function () {
    let userName = $("#usernameNew").val();
    let password = $("#passwordNew").val();
    let password2 = $("#password2New").val();
    if (password == password2) {
      loginNoxiun.createUser(userName, password);
      $("#cajaNewUser").css("display","none");
      $("#cajaLogin").css("display","flex");
    } else alert("Passwords are not the same");
  });
});
