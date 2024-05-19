function expandir_sidebar() {
    let nav = document.getElementById("sidebar");
    let imagem = document.getElementsByClassName("integrante-img");
    let legend = document.getElementsByClassName("nome_integrante");
    nav.style.width = "10%";
    nav.style.height = "75%";

    for (var i = 0; i < imagem.length; i++) {
        imagem[i].style.height = "80px";
        imagem[i].style.width = "80px";
    }

    for (var i = 0; i < legend.length; i++) {
        legend[i].style.overflow = "visible";
        legend[i].style.display = "block";
    }
}

function retrair_sidebar() {
    let nav = document.getElementById("sidebar");
    let imagem = document.getElementsByClassName("integrante-img");
    let legend = document.getElementsByClassName("nome_integrante");
    nav.style.width = "5%";
    nav.style.height = "50%";

    for (var i = 0; i < imagem.length; i++) {
        imagem[i].style.height = "55px";
        imagem[i].style.width = "55px";
    }

    for (var i = 0; i < legend.length; i++) {
        legend[i].style.overflow = "hidden";
        legend[i].style.display = "none";
    }
}
