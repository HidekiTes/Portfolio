document.addEventListener("DOMContentLoaded", function() {
    console.log("O footer foi carregado");

    let footerContainer = document.getElementById("footer")
    console.log(document.getElementById("footer"));

    let footerHTML = 
        `
        <div class="wireframe-comp-footer_back">
            <div class="img-icons">
                <img src="/img/icons/facebook.svg" alt="" srcset="">
                <img src="/img/icons/instagram.svg" alt="" srcset="">
                <img src="/img/icons/twitch.svg" alt="" srcset="">
            </div>
        </div>    
        `
    footerContainer.innerHTML = footerHTML; 

    let footerCSS = document.createElement("link");
    footerCSS.rel="stylesheet"
    footerCSS.href="/components/f_footer/footer.css"

    let wireCSS = document.createElement("link");
    wireCSS.rel="stylesheet"
    wireCSS.href="/components/wireframe/wireframe.css"

    document.head.appendChild(footerCSS)
    document.head.appendChild(wireCSS)
});