const form = document.querySelector(".js-form"),
input = form.querySelector("input"),
greeting = document.querySelector(".js-greetings");


const User_LS = "currentUser",
SHOWING_CN = "showing"

function paintGreeting(text)
{
    form.classList.remove(SHOWING_CN);
    greeting.classList.add(SHOWING_CN);
    greeting.innerText = `hello ${text}`;
}

function loadName()
{
    const currentUser = localStorage.getItem(User_LS);
    if (currentUser === null)
    {
        
    }

    else
    {
        paintGreeting(currentUser);
    }
}

function init()
{

}

init();