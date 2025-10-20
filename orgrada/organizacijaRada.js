// Отварање / затварање падајућих менија кликом
const headers = document.querySelectorAll('.test-header');

function closeAllDropdowns() {
    document.querySelectorAll('.options-list.show').forEach(d => d.classList.remove('show'));
    headers.forEach(b => b.setAttribute('aria-expanded', 'false'));
    headers.forEach(b => b.innerHTML = b.innerHTML.replace('▲', '▼'));
}

headers.forEach(button => {
    button.addEventListener('click', (e) => {
        const dropdown = button.nextElementSibling;

        if (dropdown.classList.contains('show')) {
            dropdown.classList.remove('show');
            button.setAttribute('aria-expanded', 'false');
            button.innerHTML = button.innerHTML.replace('▲', '▼');
        } else {
            closeAllDropdowns();
            dropdown.classList.add('show');
            button.setAttribute('aria-expanded', 'true');
            button.innerHTML = button.innerHTML.replace('▼', '▲');
        }
        e.stopPropagation();
    });
});

// Close when clicking outside
document.addEventListener('click', (e) => {
    if (!e.target.closest('.test-card')) {
        closeAllDropdowns();
    }
});

// Close on Escape
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeAllDropdowns();
});
