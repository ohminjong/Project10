function signUpCheck(){

    let username = document.getElementById("username")
    let password = document.getElementById("password")
    let name = document.getElementById("name")
    let phone = document.getElementById("phone")
    let mbti = document.getElementById("mbti")
    let email = document.getElementById("email")
    let student_id = document.getElementById("student_id")
    let profile_img = document.getElementById("profile_img")

    if(username.value = ""){
      alert("ID 를 입력하세요.");
      username.focus();
      return false;
    }
    if(password.value = ""){
      alert("비밀번호를 입력하세요.");
      password.focus();
      return false;
    }
    if(name.value = "") {
      alert("이름을 입력하세요.");
      name.focus();
      return false;
    }
    if(phone.value = "") {
      alert("전화번호를 입력하세요,");
      phone.focus();
      return false;
    }
    if(mbti.value = "") {
      alert("mbti 를 입력하세요.");
      mbti.focus();
      return false;
    }
    if(email.value = "") {
      alert("이메일을 입력하세요.");
      email.focus();
      return false;
    }
    else if(!email.include('@')) {
        alert("이메일 형식이 잘못되었습니다.");
    }
    else if(student_id.value = "") {
      alert("학번을 입력하세요");
      student_id.focus();
      return false;
    }
}
