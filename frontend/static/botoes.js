//botão hamburguer para mobile
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

menuToggle.addEventListener('click', () => {
    navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
    menuToggle.innerHTML = navLinks.style.display === 'flex' ? '✖' : '☰';
});

//trocas de tema
const themeToggle = document.getElementById('theme-toggle');
themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('light-theme');
    // Troca ícone do botão
    themeToggle.innerHTML = document.body.classList.contains('light-theme') ? '☀️' : '🌙';
});