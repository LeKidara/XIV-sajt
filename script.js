/* Improved navbar/offcanvas JS
   - Compatible with `navbar.css` which toggles `.offcanvas.open` and `.dropdown-toggle.active`
   - Defensive: checks elements exist before wiring handlers
   - Closes menu on background click and when links are clicked
*/
(function () {
    const hamburger = document.getElementById('hamburger');
    const offcanvas = document.getElementById('offcanvas');
    const exitBtn = document.getElementById('exit-btn');
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
    // only close the menu when non-toggle links are clicked
    const offcanvasLinks = document.querySelectorAll('.offcanvas-links a:not(.dropdown-toggle)');

    function closeMenu() {
        if (offcanvas) offcanvas.classList.remove('open');
        if (hamburger) hamburger.classList.remove('active');
        document.body.classList.remove('menu-open');
    }

    function openMenu() {
        if (offcanvas) offcanvas.classList.add('open');
        if (hamburger) hamburger.classList.add('active');
        document.body.classList.add('menu-open');
    }

    if (hamburger && offcanvas) {
        hamburger.addEventListener('click', () => {
            if (offcanvas.classList.contains('open')) closeMenu();
            else openMenu();
        });
    }

    if (exitBtn) {
        exitBtn.addEventListener('click', closeMenu);
    }

    // Close when clicking on the overlay (offcanvas background)
    if (offcanvas) {
        offcanvas.addEventListener('click', (e) => {
            if (e.target === offcanvas) closeMenu();
        });
    }

    // Close when a navigation link inside offcanvas is clicked (so menu hides on navigation)
    if (offcanvasLinks && offcanvasLinks.length) {
        offcanvasLinks.forEach(a => {
            a.addEventListener('click', () => closeMenu());
        });
    }

    // Collapsible dropdowns inside offcanvas: toggle 'active' on the toggle element
    if (dropdownToggles && dropdownToggles.length) {
        dropdownToggles.forEach(toggle => {
            // support keyboard activation
            toggle.addEventListener('keydown', (ev) => {
                if (ev.key === 'Enter' || ev.key === ' ') {
                    ev.preventDefault();
                    toggle.click();
                }
            });

            toggle.addEventListener('click', (e) => {
                e.preventDefault();
                // If toggle lives inside offcanvas prefer local scope, otherwise global
                const scope = toggle.closest('.offcanvas') || document;

                // Close other toggles in same scope
                scope.querySelectorAll('.dropdown-toggle').forEach(t => {
                    if (t !== toggle) t.classList.remove('active');
                });

                // Toggle this one
                toggle.classList.toggle('active');
            });
        });
    }

})();
