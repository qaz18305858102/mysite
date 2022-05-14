function input_username(userlist) {
    var username = document.getElementById("Username");
    /*
    * 6到12位（字母，数字，）
    **/
    var patt = /^.*(?=.{6,12})(?=.*\d)(?=.*[a-zA-Z]).*$/;
    var hint = document.getElementById("username_hint");

    if (patt.test(username.value)) {
        for (i in userlist) {
            if (userlist[i] == username.value) {
                hint.innerHTML = "用户名已存在";
                hint.style.color = "red"
                return "用户名已存在"
            }
        }
        hint.innerHTML = "用户名合法";
        hint.style.color = "green"
        return 1
    } else {
        hint.innerHTML = "请输入正确的用户名";
        hint.style.color = "red"
        return "请输入正确的用户名"
    }
}

// function username_check(name){
//     var username = document.getElementById("Username");
//     var hint = document.getElementById("username_hint");
//     for (i in name){
//         if (i.username == username){
//             hint.innerHTML = "用户名已存在";
//             hint.style.color = "red"
//             return "用户名已存在"
//         }
//         return 1
//     }
// }

function input_Email() {
    var Email = document.getElementById("UserEmail");
    /*
    * 邮箱正则
    **/
    var patt = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    var hint = document.getElementById("Email_hint");
    if (patt.test(Email.value)) {
        hint.innerHTML = "邮箱合法";
        hint.style.color = "green"
        return 1
    } else {
        hint.innerHTML = "请输入正确的邮箱";
        hint.style.color = "red"
        return "请输入正确的邮箱"
    }
}

function input_password() {
    var password = document.getElementById("Password");
    /*
    * 最少6位，包括至少1个大写字母，1个小写字母，1个数字，1个特殊字符
    **/
    var patt = /^.*(?=.{6,12})(?=.*\d)(?=.*[a-zA-Z]).*$/;
    var hint = document.getElementById("password_hint");
    if (patt.test(password.value)) {

        hint.innerHTML = "密码合法";
        hint.style.color = "green"
        return 1
    } else {
        hint.innerHTML = "请输入正确的密码";
        hint.style.color = "red"
        return "请输入正确的密码"
    }
}

function check_sub(userlist) {
    var username = document.getElementById("Username");
    var Email = document.getElementById("UserEmail");
    var password = document.getElementById("Password");
    var Repeatpassword = document.getElementById("Repeatpassword");

    //获取下拉框的值
    var sid = document.getElementById("sid");
    var index = sid.selectedIndex;
    var val = sid.options[index].value;
    var Answer = document.getElementById("Answer");


    if (username.value == "") {
        alert("用户名不能为空");
        return false;
    }
    for (i in userlist) {
        if (userlist[i] == username.value) {
            alert("用户名已存在");
            return false;
        }
    }

    if (Email.value == "") {
        alert("邮箱不能为空");
        return false;
    }
    if (password.value == "") {
        alert("密码不能为空");
        return false;
    }
    if (val == "") {
        alert("请选择问题");
        return false;
    }
    if (Answer.value == "") {
        alert("请输入问题答案");
        return false;
    }
    if (input_username() != 1 || input_password() != 1 || input_Email() != 1) {
        alert("用户名，密码，邮箱不合法");
        return false;
    }
    if (password.value != Repeatpassword.value) {
        alert("密码不一致");
        return false;
    }
        // if (date!="注册成功"){
        //     alert(date);
        //     return false;
    // }
    else {
        return true;
    }
}



