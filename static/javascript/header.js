let open = false;

const hamburger = $('#hamburger');
const nav = $('header > nav');

if (hamburger) {
    hamburger.click(() => {
        if (!open) {
            hamburger.addClass('active');
            nav.addClass('open');
            open = true;
        } else {
            hamburger.removeClass('active');
            nav.removeClass('open');
            open = false;
        }
    });

    window.addEventListener('resize', () => {
        if (window.innerWidth > 768 && open) {
            hamburger.removeClass('active');
            nav.removeClass('open');
            open = false;
        }
    });
}




