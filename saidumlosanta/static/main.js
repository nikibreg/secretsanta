function getInputField() {
    var div = document.createElement("div")
    div.classList.add("input-field")
    return div
}

function getHolder() {
    var container = document.createElement('div')
    container.id = document.querySelectorAll('#holder').length

    var name = document.createElement('input')
    name.id = "first_name"
    name.name = "name" + container.id
    name.type = "text"
    name.classList.add("validate")
    var nameLabel = document.createElement("label")
    nameLabel.setAttribute("for", "first_name")
    nameLabel.innerText = "First Name"
    var nameIcon = document.createElement("i")
    nameIcon.classList.add("material-icons", "prefix")
    nameIcon.innerText = "account_circle"

    var nameInput = getInputField()
    nameInput.appendChild(nameIcon)
    nameInput.appendChild(name)
    nameInput.appendChild(nameLabel)

    var email = document.createElement("input")
    email.id = "email"
    email.name = "email" + container.id
    email.type = "email"
    email.classList.add("validate")
    var emailLabel = document.createElement("label")
    emailLabel.setAttribute("for", "email")
    emailLabel.innerText = "E-mail"
    var emailIcon = document.createElement("i")
    emailIcon.classList.add("material-icons", "prefix")
    emailIcon.innerText = "alternate_email"

    var emailInput = getInputField()
    emailInput.appendChild(emailIcon)
    emailInput.appendChild(email)
    emailInput.appendChild(emailLabel)

    var want = document.createElement("input")
    want.id = "want"
    want.name = "want" + container.id
    want.type = "text"
    want.classList.add("validate")
    var wantLabel = document.createElement("label")
    wantLabel.setAttribute("for", "want")
    wantLabel.innerText = "I want (detailed description)... "


    var wantInput = getInputField()
    wantInput.appendChild(want)
    wantInput.appendChild(wantLabel)

    var holder = document.createElement('div')
    holder.id = "holder"

    container.append(nameInput)
    container.append(emailInput)
    container.append(wantInput)
    holder.append(container)

    var showButton = document.createElement("i")
    showButton.classList.add("material-icons", "showButton")
    showButton.innerText = "remove_red_eye"
    showButton.onclick = () => onShowButtonClick(container.id)
    holder.append(showButton)

    return holder
}

function addPerson() {
    document.getElementById('mainForm').append(getHolder())
    if (document.querySelectorAll('#holder').length >= 3) {
        document.getElementById("submitButton").classList.remove("disabled")
    }
}

function onShowButtonClick(n) {
    var container = document.getElementById(n)
    if (container.style.filter == "blur(6px)") {
        container.style.filter = "blur(0px)"
    } else {
        container.style.filter = "blur(6px)"
    }

}

(() => {
    addPerson();
    initTooltips()
})()


function initTooltips() {
    var elems = document.querySelectorAll('.tooltipped');
    var instances = M.Tooltip.init(elems);
}
