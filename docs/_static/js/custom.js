document.addEventListener("DOMContentLoaded", function () {
    let langDropdown = document.querySelectorAll("option[value='es']");
    langDropdown.forEach(option => option.textContent = "Español");
});