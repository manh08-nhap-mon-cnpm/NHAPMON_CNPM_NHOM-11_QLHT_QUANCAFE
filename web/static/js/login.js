document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("togglePassword")
    const password = document.getElementById("password")

    if (toggle) {
        toggle.addEventListener("click", () => {
            password.type = password.type === "password" ? "text" : "password"
            toggle.textContent = password.type === "password" ? "👁️" : "🙈"
        })
    }
})
