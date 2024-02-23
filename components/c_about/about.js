document.addEventListener("DOMContentLoaded", function() {
    console.log("A about foi carregada");

    let aboutContainer = document.getElementById("about")
    console.log(document.getElementById("about"));

    let aboutHTML = 
        `
        <div class="wireframe-comp-2">
            <div class="title-container">
                <div class="title-layout">  
                    <h1 class="h1-style">AAAAAA</h1>
                    <h1 class="h2-style">BBBBBB</h1>
                    <p class="placeholder">CCCCCCCCCC</p>
                </div>
            </div> 
        </div>    
        `
    aboutContainer.innerHTML = aboutHTML; 

    let aboutCSS = document.createElement("link");
    aboutCSS.rel="stylesheet"
    aboutCSS.href="/components/c_about/about.css"

    let wireCSS = document.createElement("link");
    wireCSS.rel="stylesheet"
    wireCSS.href="/components/wireframe/wireframe.css"

    document.head.appendChild(aboutCSS)
    document.head.appendChild(wireCSS)
});