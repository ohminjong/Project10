function signUpCheck(){

    let id = document.getElementById("username").value
    let password = document.getElementById("password").value
    let name = document.getElementById("name").value
    let phone = document.getElementById("phone").value
    let mbti = document.getElementById("mbti").value
    let email = document.getElementById("email").value
    let student_id = document.getElementById("student_id").value
    let profile_img = document.getElementById("profile_img").value
    let check = true;

    // 이메일 유효 확인
    if(email.includes('@')){
        let emailId = email.split('@')[0]
        let emailServer = email.split('@')[1]
        if(emailId === "" || emailServer === ""){
          document.getElementById("emailError").innerHTML="이메일이 올바르지 않습니다."
          check = false
        }
        else{
          document.getElementById("emailError").innerHTML=""
        }
    }
    else{
        document.getElementById("emailError").innerHTML="이메일이 올바르지 않습니다."
        check = false
    }

    // 이름 유효 확인
    if(name===""){
        document.getElementById("nameError").innerHTML="이름을 입력해주세요."
        check = false
    }
    else{
        document.getElementById("nameError").innerHTML=""
    }

    //나머지는 요소 유효확인은 추후 구현


}