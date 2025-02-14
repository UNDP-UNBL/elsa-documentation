document.addEventListener("DOMContentLoaded", function () {
    let langOption = document.querySelector("option[value='es']");
    if (langOption) {
        langOption.textContent = "Español";
    }
});
