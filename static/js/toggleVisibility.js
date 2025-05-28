function toggleVisibility(tableId) {
    let table = document.getElementById(tableId);
    if (table.style.display === "none") {
        table.style.display = "table";
    } else {
        table.style.display = "none";
    }
}

// Hide tables initially when the page loads
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("my-ah-scores-tbl").style.display = "table";
    document.getElementById("my-mf-scores-tbl").style.display = "table";
});