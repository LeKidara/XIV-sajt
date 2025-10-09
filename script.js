const hamburger = document.getElementById('hamburger');
const offcanvas = document.getElementById('offcanvas');
const exitBtn = document.getElementById('exit-btn');
const dropdownToggles = document.querySelectorAll('.dropdown-toggle');

// Funkcija za otvaranje offcanvas menija
hamburger.addEventListener('click', () => {
    offcanvas.style.right = '0';
});

// Funkcija za zatvaranje offcanvas menija
exitBtn.addEventListener('click', () => {
    offcanvas.style.right = '-250px';
});

// Dodaj događaj za otvaranje/zatvaranje podmenija
dropdownToggles.forEach(toggle => {
    toggle.addEventListener('click', (e) => {
        e.preventDefault(); // Sprečava default ponašanje linka

        const dropdownMenu = toggle.nextElementSibling; // Pronalazi odgovarajući podmeni

        // Zatvara sve otvorene podmenije i uklanja klasu 'active' sa svih strelica
        document.querySelectorAll('.dropdown-menu').forEach(menu => {
            if (menu !== dropdownMenu) {
                menu.style.display = 'none';
            }
        });
        document.querySelectorAll('.dropdown-toggle').forEach(item => {
            if (item !== toggle) {
                item.classList.remove('active');
            }
        });

        // Prikazuje ili sakriva podmeni i rotira strelicu
        if (dropdownMenu.style.display === 'block') {
            dropdownMenu.style.display = 'none';
            toggle.classList.remove('active');
        } else {
            dropdownMenu.style.display = 'block';
            toggle.classList.add('active');
        }
    });
});
