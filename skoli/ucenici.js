function showTab(tabId, ev) {
    const panels = document.querySelectorAll('.tab-panel');
    const tabs = document.querySelectorAll('.tab');

    // Hide all panels
    panels.forEach(panel => {
        panel.classList.remove('active');
        panel.style.opacity = '0';
    });

    // Remove active from all buttons
    tabs.forEach(tab => tab.classList.remove('active'));

    // Show the requested panel
    const activePanel = document.getElementById(tabId);
    if (!activePanel) return;
    activePanel.classList.add('active');

    // Fade in
    setTimeout(() => {
        activePanel.style.opacity = '1';
    }, 100);

    // Mark the clicked button active if event provided
    if (ev && ev.currentTarget) ev.currentTarget.classList.add('active');
}
