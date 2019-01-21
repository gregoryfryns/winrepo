$("#search-btn").click(function () {
    console.log("click!");
    if (typeof (Storage) !== "undefined") {
        window.sessionStorage.setItem("searchTerms", ($('#search-input').val()));
    }
    window.location.href = "/list/";
});

$( document ).ready(function() {
    console.log("loaded");
    if (typeof (Storage) !== "undefined" && window.sessionStorage.getItem("searchTerms")) {
        $('#search-input').val(window.sessionStorage.getItem("searchTerms"));
    }
});