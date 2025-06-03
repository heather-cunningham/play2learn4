function toggleVisibility(tableId) {
    let table = document.getElementById(tableId);
    if (table) {
        if (table.style.display === "none") {
            table.style.display = "table";
        } else {
            table.style.display = "none";
        }
    } else {
        console.error("Element with ID '" + tableId + "' not found.");
    }
}

window.onload = function () {
    let ahTable = document.getElementById("my-ah-tbl-container");
    let mfTable = document.getElementById("my-mf-tbl-container");

    if (ahTable) {
        ahTable.style.display = "table";
    } else {
        console.warn("Warning: Table 'my-ah-tbl-container' not found.");
    }

    if (mfTable) {
        mfTable.style.display = "table";
    } else {
        console.warn("Warning: Table 'my-mf-tbl-container' not found.");
    }
};

// Catch unexpected errors
window.onerror = function (message, source, lineno, colno, error) {
    console.error("Caught error:", message,  error, "Line #:", lineno);
};