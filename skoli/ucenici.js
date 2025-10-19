function showTab(tabId) {
    const panels = document.querySelectorAll('.tab-panel');
    const tabs = document.querySelectorAll('.tab');

    // Скривање свих табова
    panels.forEach(panel => {
        panel.classList.remove('active');
        panel.style.opacity = '0';
    });

    // Скидање "active" класе са свих дугмића
    tabs.forEach(tab => tab.classList.remove('active'));

    // Приказ изабраног таба
    const activePanel = document.getElementById(tabId);
    activePanel.classList.add('active');

    // Лагано појављивање
    setTimeout(() => {
        activePanel.style.opacity = '1';
    }, 100);

    // Активирање таб дугмета
    event.currentTarget.classList.add('active');
}
