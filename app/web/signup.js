

function signup(event) {
    var error = document.getElementById("error")

    let email = form.elements["email"].value;
    let password = form.elements["password"].value;
    let confirm_password = form.elements["confirm"].value;
    let pin = form.elements["pin"].value;

    
    // Data validation 
    if (password != confirm_password) {
        error.innerText = "Passwords does not match!";
        e.preventDefault();
        return 0;
    }
    if (!constainsOnlyNumbers(pin)){
        error.innerText = "Pin must contain only digits"
        event.preventDefault();
        return 0;
        
    }
    if (pin.length != 4){
        error.innerText = "Pin must be 4 digits long!";
        event.preventDefault();
        return 0;
    }


    send_data(email, password, pin);
    


    // Send data to backend
    async function send_data(){
        let response = await eel.sign_up(email, password, pin)();
        response = JSON.parse(response)
        if (response.type == "Error") {
            error.innerText = response.message

        }else if (response.type == "Success") {
            // Redirect to home page, pass user id 
            sessionStorage.setItem("user_id", response.vars.user_id);
            window.location.href = "home.html"

        }
    }
}


function constainsOnlyNumbers(str) {
    return /^[0-9]+$/.test(str);
}



const form = document.getElementById("form");
form.addEventListener("submit", signup);