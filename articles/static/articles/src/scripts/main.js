document.addEventListener("DOMContentLoaded", DOMContentLoaded);

function DOMContentLoaded() {
    console.log('DOM content loaded');
}

new Pjax({
    elements: "a",
    selectors: ["title", ".site-header", ".content"]
})

document.addEventListener("pjax:success", DOMContentLoaded)
