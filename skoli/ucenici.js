function showTab(tabId) {
    // Сакриј све таб панеле
    const panels = document.querySelectorAll('.tab-panel');
    panels.forEach(panel => panel.classList.remove('active'));

    // Скини "active" са свих табова
    const tabs = document.querySelectorAll('.tab');
    tabs.forEach(tab => tab.classList.remove('active'));

    // Прикажи изабрани таб и панел
    document.getElementById(tabId).classList.add('active');
    event.currentTarget.classList.add('active');
}
