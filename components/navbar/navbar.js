document.addEventListener("DOMContentLoaded", function() {
    console.log("DOM fully loaded and parsed");

    let navbarContainer = document.getElementById("navbar");

    let navbarHTML = 
        `
            <div class="navbar-container">
                <div class="navbar-content">
                    <div class="navbar-item">(Logo)</div>
                    <div class="navbar-content-center">
                        <div class="navbar-item">Introdução</div>
                        <div class="navbar-item">Sobre Mim</div>
                        <div class="navbar-item">Certificações</div>
                        <div class="navbar-item">Projetos</div>
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

