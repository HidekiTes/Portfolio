document.addEventListener("DOMContentLoaded", function() {
    let navbarContainer = document.getElementById("navbar");

    let navbarHTML = 
        `
            <div class="navbar-container">
                <div class="navbar-content">
                    <div class="navbar-item">(Logo)</div>
                    <div class="navbar-content-center">
                        <a class="" href="#">Introdução</a>
                        <a class="" href="#">Sobre Mim</a>
                        <a class="" href="#">Certificações</a>
                        <a class="" href="#">Projetos</a>
                    </div>
                    <div class="navbar-item">Contato</div>
                </div>
            </div>    
        ` 
    navbarContainer.innerHTML = navbarHTML;

    let navbarCSS = document.createElement("link");
    navbarCSS.rel="stylesheet"
    navbarCSS.href="/components/navbar/navbar.css"
    
    document.head.appendChild(navbarCSS)



    
});

