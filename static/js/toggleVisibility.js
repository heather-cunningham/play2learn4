function toggleVisibility(tableId) {
    let table = document.getElementById(tableId);
    if (table.style.display === "none") {
        table.style.display = "block";
    } else {
        table.style.display = "none";
    }
}

// Hide tables initially when the page loads
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("my-ah-tbl-container").style.display = "table";
    document.getElementById("my-mf-tbl-container").style.display = "block";
});