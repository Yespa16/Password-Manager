

function login(event) {
    var error = document.getElementById("error")

    email = form.elements["email"].value;
    password = form.elements["password"].value;
    pin = form.elements["pin"].value


    // Data validation 
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
    event.preventDefault();


    // Send data to backend
    async function send_data(){
        let response = await eel.login(email, password, pin)();
        response = JSON.parse(response)
        if (response.type == "Error") {
            error.innerText = response.message

        }else if (response.type == "Success") {
            // Redirect to home page
            window.location.href = "home.html"

        }
    }
}


function constainsOnlyNumbers(str) {
    return /^[0-9]+$/.test(str);
}



const form = document.getElementById("form");
form.addEventListener("submit", login);