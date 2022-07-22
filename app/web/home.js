window.resizeTo(1920, 1280)
const user_id = sessionStorage.getItem("user_id");
var table = document.getElementById("table");


async function get_passwords(user_id){
    console.log(user_id)
    passwords =  await eel.get_passwords(user_id)();
    return passwords
}

var passwords = get_passwords(user_id)
async function fill_table(){
    console.log(table)
    let passwords = await get_passwords(user_id);
    passwords = JSON.parse(passwords);
    let add = ``
    passwords.forEach(password => {
        add += `
        <tr>
            <td>${password[0]}</td>
            <td>${password[1]}</td>
            <td>${password[2]}</td>
            <td>${password[3]}</td>
            <td>${password[4]}</td>
        </tr>
    `
    table.innerHTML += add;
    })
}

fill_table();