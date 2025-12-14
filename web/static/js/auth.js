function togglePassword(el) {
    const input = el
        ? el.previousElementSibling
        : document.getElementById("password");

    input.type = input.type === "password" ? "text" : "password";
}
