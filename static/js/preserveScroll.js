// Preserve Scroll Position on Page Reload for table sorting
window.onload = function() {
    if (localStorage.getItem("scrollPosition")) {
        window.scrollTo(0, localStorage.getItem("scrollPosition"));
    }
};

window.onbeforeunload = function() {
    localStorage.setItem("scrollPosition", window.scrollY);
};