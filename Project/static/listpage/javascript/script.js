document.getElementById('open_btn').addEventListener('click', function () {
    document.getElementById('sidebar').classList.toggle('open-sidebar');
});

function redirecionar_url() {
    // Obtém a URL gerada pelo Flask usando url_for
    var url = url_for('landing.landing_page');
    // Redireciona o usuário para a URL
    window.location.href = url;
}
