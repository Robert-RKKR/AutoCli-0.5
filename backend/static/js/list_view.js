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
var activeTableElementRow = document.getElementsByClassName("table-buttons-box");
var activeTableElementName = document.getElementById("table-buttons-action");
var toggleTableButton = document.getElementById("edit-button");

toggleTableButton.onclick = function () {

    if(activeTableElementName.classList.contains("collapse") === false) {
        activeTableElementName.classList.add("collapse");
    } else {
        activeTableElementName.classList.remove("collapse");
    }

    for(let i=0; i<activeTableElementRow.length; i++) {
        if(activeTableElementRow[i].classList.contains("collapse") === false) {
            activeTableElementRow[i].classList.add("collapse");
        } else {
            activeTableElementRow[i].classList.remove("collapse");
        }
    }

};
