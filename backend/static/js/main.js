// Sidebar (Page left) open / close action:
var closeActiveElement = document.getElementById("page-left");
var closeToggleButton = document.getElementById("sidebar-close");

closeToggleButton.onclick = function () {
    if(closeActiveElement.classList.contains("collapse") === false) {
        closeActiveElement.classList.toggle("collapse");
    } else {
        closeActiveElement.classList.remove("collapse");
    }
};

// Sidebar (Page left) menu close / open action with cookies:
var toggleButtons = document.getElementsByClassName("collapse-menu-link");
let cookies = document.cookie.split(";");

for(let i=0; i<cookies.length; i++) {
    let cookie = cookies[i].split("=");
    if(cookie[0] === "open_menu_action") {
        if(cookie[1] != "false") {
            let menu_number = parseInt(cookie[1]);
            for(let i=0; i<toggleButtons.length; i++) {
                if(i === menu_number) {
                    let toggleButton = toggleButtons[i];
                    let activeElement = toggleButtons[i].nextElementSibling;
                    
                    activeElement.classList.remove("collapse");
                }
            }
        }
    }
}

for(let i=0; i<toggleButtons.length; i++) {
    let toggleButton = toggleButtons[i];
    let activeElement = toggleButtons[i].nextElementSibling;

    toggleButton.addEventListener("click", function(event) {
        
        if(activeElement.classList.contains("collapse") === false) {
            activeElement.classList.add("collapse");
            document.cookie = "open_menu_action=false;path=/";
        } else {
            for(let i=0; i<toggleButtons.length; i++) {
                let activeElementInside = toggleButtons[i].nextElementSibling
                activeElementInside.classList.add("collapse");
            }
            activeElement.classList.remove("collapse");
            document.cookie = "open_menu_action=" + i + ";path=/";
        }  

    });
}

// Filter close action:
var activeElement = document.getElementById("content-filter");
var toggleButton = document.getElementById("content-filter-button");

toggleButton.onclick = function () {

    if(activeElement.classList.contains("collapse") === false) {
        activeElement.classList.add("collapse");
    } else {
        activeElement.classList.remove("collapse");
    }
};
