
function my_pass(){
  var x = document.getElementbyID("id_show_pass")
  if (x.type==="password"){
    x.type="text";
  }else{
    x.type = "password";
  }
}
