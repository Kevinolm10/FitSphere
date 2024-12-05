// Password rule validator
document.addEventListener("DOMContentLoaded", function () {
    const passwordField = document.querySelector("input[type='password']");

    // Ensure the password field is present
    if (!passwordField) {
        console.error("Password field not found!");
        return;
    }

    const rulesList = passwordField.closest(".form-group").querySelector("ul");

    if (!rulesList) {
        console.error("Rules list (ul) not found!");
        return;
    }

    const liElements = rulesList.querySelectorAll("li");

    // Check if there are enough <li> elements for all the password criteria
    if (liElements.length < 4) {
        console.error("Insufficient password rule <li> elements found!");
        return;
    }

    const checkPasswordLength = (password) => password.length >= 8;
    const checkPasswordNumeric = (password) => /\d/.test(password) && !/^\d+$/.test(password);
    const checkPasswordCommon = (password) => !["123456", "password", "qwerty", "abc123"].includes(password);
    const checkPasswordSimilar = (password, username) => !password.toLowerCase().includes(username.toLowerCase());

    // Event listener for when the password field changes
    passwordField.addEventListener("input", function () {
        const password = passwordField.value;
        const username = document.querySelector("input[name='username']").value; // You may want to adjust this based on your form

        // Password length validation
        if (checkPasswordLength(password)) {
            liElements[0].classList.add("valid");
            liElements[0].classList.remove("invalid");
        } else {
            liElements[0].classList.add("invalid");
            liElements[0].classList.remove("valid");
        }

        // Numeric check
        if (checkPasswordNumeric(password)) {
            liElements[1].classList.add("valid");
            liElements[1].classList.remove("invalid");
        } else {
            liElements[1].classList.add("invalid");
            liElements[1].classList.remove("valid");
        }

        // Common password check
        if (checkPasswordCommon(password)) {
            liElements[2].classList.add("valid");
            liElements[2].classList.remove("invalid");
        } else {
            liElements[2].classList.add("invalid");
            liElements[2].classList.remove("valid");
        }

        // Similarity check with username
        if (checkPasswordSimilar(password, username)) {
            liElements[3].classList.add("valid");
            liElements[3].classList.remove("invalid");
        } else {
            liElements[3].classList.add("invalid");
            liElements[3].classList.remove("valid");
        }
    });
});