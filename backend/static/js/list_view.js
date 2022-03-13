// Filter close action:
var activeFilterElement = document.getElementById("content-filter");
var toggleFilterButton = document.getElementById("content-filter-button");

toggleFilterButton.onclick = function () {

    if(activeFilterElement.classList.contains("collapse") === false) {
        activeFilterElement.classList.add("collapse");
    } else {
        activeFilterElement.classList.remove("collapse");
    }

};


// Table, grid display hided action buttons:
var activeBoxElementRow = document.getElementsByClassName("box-buttons");
var activeTableElementRow = document.getElementsByClassName("table-buttons-box");
var activeTableElementName = document.getElementById("table-buttons-action");
var toggleTableButton = document.getElementById("edit-button");

for(let i=0; i<cookies.length; i++) {
    let cookie = cookies[i].split("=");
    if(cookie[0] === "edit_model_action") {
        if(cookie[1] === "true") {
            if(activeBoxElementRow != null) {
                for(let i=0; i<activeBoxElementRow.length; i++) {
                    activeBoxElementRow[i].classList.remove("collapse");
                }
            }

            if(activeTableElementName != null) {
                activeTableElementRow[i].classList.remove("collapse");
            }

            if(activeTableElementRow != null) {
                for(let i=0; i<activeTableElementRow.length; i++) {
                    activeTableElementRow[i].classList.remove("collapse");
                }
            }
        }
    }
}

toggleTableButton.onclick = function () {

    if(activeTableElementName != null) {
        if(activeTableElementName.classList.contains("collapse") === false) {
            activeTableElementName.classList.add("collapse");
            document.cookie = "edit_model_action=false;path=/";
        } else {
            activeTableElementName.classList.remove("collapse");
            document.cookie = "edit_model_action=true;path=/";
        }
    }
    
    if(activeTableElementRow != null) {
        for(let i=0; i<activeTableElementRow.length; i++) {
            if(activeTableElementRow[i].classList.contains("collapse") === false) {
                activeTableElementRow[i].classList.add("collapse");
                document.cookie = "edit_model_action=false;path=/";
            } else {
                activeTableElementRow[i].classList.remove("collapse");
                document.cookie = "edit_model_action=true;path=/";
            }
        }
    }

    if(activeBoxElementRow != null) {
        for(let i=0; i<activeBoxElementRow.length; i++) {
            if(activeBoxElementRow[i].classList.contains("collapse") === false) {
                activeBoxElementRow[i].classList.add("collapse");
                document.cookie = "edit_model_action=false;path=/";
            } else {
                activeBoxElementRow[i].classList.remove("collapse");
                document.cookie = "edit_model_action=true;path=/";
            }
        }
    }

    console.log(cookies)

};
