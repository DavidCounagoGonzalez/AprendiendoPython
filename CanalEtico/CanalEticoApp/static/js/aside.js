document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('toggleAside');
    const sidebar = document.getElementById('sidebarJS');

    toggleButton.addEventListener('click', function() {
        sidebar.classList.toggle('activo');
    });
});