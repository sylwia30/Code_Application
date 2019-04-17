$(function () {
    var links = $('.titles');

    links.on('click', function (event) {
        event.preventDefault();
        let div = $(this).parent().next();
        div.toggle('.exercise')
    })

// var links = document.querySelectorAll("a");
// console.log(links[0])
//
//  links[0].addEventListener("click", function (event) {
//     event.preventDefault();
//     var div = this.parentElement.nextElementSibling;
//     div.style.display = 'none'
//     // classList.remove("hidden-exercise");
// });
});
