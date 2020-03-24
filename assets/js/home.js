const nav = document.querySelector('.mobile-menu');

const tog = document.querySelector('.nav-link');

const li = document.querySelectorAll('nav-link li');

const backTo = document.querySelector('.back-top');



nav.addEventListener('click', () => {
    tog.classList.toggle('nav-active');
    nav.classList.toggle('toggle');

    // li.forEach((link, index) => {

    //     if (link.style.animation) {
    //         link.style.animation = '';

    //     } else {
    //         link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
    //     }
    //});
});


window.addEventListener("scroll", () => {

    if (window.pageYOffset > 400) {
        //Show button

        backTo.style.display = 'block';
    } else {

        //hide button
        backTo.style.display = 'none';
    }

});


//back to top animation
backTo.addEventListener('click', () => {
    window.scrollTo(0, 0);

});