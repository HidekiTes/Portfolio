document.addEventListener("DOMContentLoaded", ()=>{
    
    let wireframeContainer = document.getElementById("wireframeEstrutura");
    let wireframeHTML = `
        <div class = "wireframe-comp-footer_back">
        </div>
    `

    // wireframeContainer.innerHTML=wireframeHTML
    wireframeContainer.insertAdjacentHTML("beforeend",wireframeHTML)
})