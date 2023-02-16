function validateform(){  
    var name = document.getElementById('user-id').value;  
    var password = document.getElementById('password-id').value;  
    if (name==null || name=="")
        {
        alert("Please enter your name");  
        return false;  
        }
        else if(password==""||(password<4))
        {  
        alert("Enter password");  
        return false;  
        }  
        return true;
    }

function validate(){
    var name = document.getElementById('user-id').value;
    var email = document.getElementById('email-id').value;
    var password = document.getElementById('password-id').value;
    var cpass = document.getElementById('cpass-id').value;
    if (name==""||name=="NULL")
        {
            alert("please fill out the name field");
            return false;
        }
        atpos = email.indexOf("@");
        dotpos = email.lastIndexOf(".");
        if ((atpos<1)||(dotpos-atpos<2)){
            alert("Please enter a valid e-mail address");
            return false;
        }
        if((password!=cpass)||(password<6))
        {
            alert("Password must be same!");
            return false;
        }
        return true;
    }

function inputvalidation(){
    var input = document.getElementById('input-id').value;
    if(input=="" || input=="NULL")
        {
            alert("Please enter a task !");
            return false;
        }
        return true;
    }