document.addEventListener("DOMContentLoaded", ()=>{
    
    let wireframeContainer = document.getElementById("wireframeEstrutura");
    let wireframeHTML = `
        <div class = "wireframe-container">
            <div class = "wireframe-content"></div>
        </div>
    `

    // wireframeContainer.innerHTML=wireframeHTML
    wireframeContainer.insertAdjacentHTML("beforeend",wireframeHTML)
})