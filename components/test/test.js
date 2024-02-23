document.addEventListener("DOMContentLoaded", () => {
    // Lógica para carregar a introdução
    let introContainer = document.getElementById("intro");
    let introHTML = `
        <div class="wireframe-comp-1">
            <div class="title-container">
                <div class="title-layout">  
                    <h1 class="h1-style">AAAAAA</h1>
                    <h1 class="h2-style">BBBBBB</h1>
                </div>
            </div>
        </div>
    `;

    let introCSS = document.createElement("link");
    introCSS.rel = "stylesheet";
    introCSS.href = "/components/b_intro/intro.css";

    document.head.appendChild(introCSS);
    introContainer.innerHTML = introHTML;

    // Lógica para carregar o conteúdo do wireframe
    let wireframeContainer = document.getElementById("wireframeEstrutura");
    let wireframeHTML = `
        <div class="wireframe-container">
            <div class="wireframe-content"></div>
        </div>
    `;

    let wireframeCSS = document.createElement("link");
    wireframeCSS.rel = "stylesheet";
    wireframeCSS.href = "/components/wireframe/wireframe.css";

    document.head.appendChild(wireframeCSS);
    wireframeContainer.insertAdjacentHTML("beforeend", wireframeHTML);
});