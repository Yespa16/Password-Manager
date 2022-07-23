async function add_password(event){
    let app = form.elements["app"].value;
    let email = form.elements["email"].value;
    let username = form.elements["username"].value;
    let password = form.elements["password"].value;
    let confirm = form.elements["confirm"].value;
    let description= form.elements["description"].value;

    let info = document.getElementById("info");
    let error = document.getElementById("error");

    let user_id = sessionStorage.getItem("user_id");

    // Data validation
    if (email=="" && username==""){
        error.innerText = "You must enter either email or username";
        event.preventDefault();
        return 0;

    }
    if (password != confirm){
        error.innerText = "Passwords does not match!";
        event.preventDefault();
        return 0;
    }

    let response = await eel.create_password(user_id, app, password,  username, email,  description)();
    response = JSON.parse(response);
    if (response.type == "Success"){
        info.innerText = response.message;
    }else if (response.type == "Error"){
        error.innerText = response.message;
    }

}
let form = document.getElementById("form");
form.addEventListener("submit", add_password);