const show_passwd=document.getElementById("showpass");

show_passwd.addEventListener("change",()=>{

    let password=document.getElementById("password");

    if(password.type == "password"){
        password.type="text";
    }else{
        password.type="password";
    }

});