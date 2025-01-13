

const show_passwd=document.getElementById("showpass");

show_passwd.addEventListener("change",()=>{

    let password=document.getElementById("id_password1");
    let conf_password=document.getElementById("id_password2");

    if(password.type == "password"){
        password.type="text";
        conf_password.type="text";
    }else{
        password.type="password";
        conf_password.type="password";
    }

});