window.resizeTo(1920, 1280)
const user_id = sessionStorage.getItem("user_id");
var table = document.getElementById("table");



function show_passwords(passwords){
    // Reseting table
    table.innerHTML = `
    <tr>
        <th>App</th>
        <th>Email</th>
        <th>Username</th>
        <th>Password</th>
        <th>Description</th>
        <th>------</th>
    </tr>
    `
    passwords.forEach(password => {

        let add = ``
        add += `
        <tr>
            <td>${password[1]}</td>
            <td>${password[2]}</td>
            <td>${password[3]}</td>
            <td>${password[4]}</td>
            <td>${password[5]}</td>
            <td><button class="delete_btn" onClick="deletePassword(${password[0]})">Delete</button></td>
        </tr>
    `
    table.innerHTML += add;
    })
}


async function get_passwords(user_id){
    passwords =  await eel.get_passwords(user_id)();
    return passwords
}



async function fill_table(){
    let passwords = await get_passwords(user_id);
    passwords = JSON.parse(passwords);
    show_passwords(passwords);
    
}

fill_table();


async function deletePassword(id){
    let response = await eel.delete_password(id)();
    response = JSON.parse(response);
    if (response.type == "Error"){
        alert(response.message);
    }else{
        location.reload();
    }
}



// Filter passwords
const search_btn = document.getElementById("search_btn");
search_btn.addEventListener("click", async () => {
    const app = document.getElementById("search").value.toLowerCase();
    let passwords = await get_passwords(user_id);
    passwords = JSON.parse(passwords);

    let result = [];
    passwords.forEach(password => {
        if (password[0] === app) {
            result.push(password);
        }
        
    })
    
    show_passwords(result);



})