document.addEventListener("DOMContentLoaded", function() {
    console.log("A Intro foi carregada");

    let titleContainer = document.getElementById("intro")
    console.log(document.getElementById("intro"));

    let titleHTML = 
        `
            <div class="wireframe-comp-1">
                <div class="title-container">
                    <div class="title-layout">  
                        <h1 class="h1-style">AAAAAA</h1>
                        <h1 class="h2-style">BBBBBB</h1>
                    </div>
                </div> 
            </div>
        `
    titleContainer.innerHTML = titleHTML; 

    let titleCSS = document.createElement("link");
    titleCSS.rel="stylesheet"
    titleCSS.href="/components/b_intro/intro.css"

    let wireCSS = document.createElement("link");
    wireCSS.rel="stylesheet"
    wireCSS.href="/components/wireframe/wireframe.css"

    document.head.appendChild(titleCSS)
    document.head.appendChild(wireCSS)
});

