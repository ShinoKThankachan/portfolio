document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.querySelector(".hamburger");
    const navbar = document.querySelector(".navbar ul");

    hamburger.addEventListener("click", function () {
        navbar.classList.toggle("active");
    });
});
