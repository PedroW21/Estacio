console.log($(".list-aboutJquery").html()); //seleciona toda a lista

console.log($(".list-item").eq(0).html()); // somente o primeiro item


$(".list-aboutJquery").append("<li>Item inserido pelo jQuery</li>");

$(".title").after("<p>Olá! Item inserido pelo jQuery</p>");

$(".list-item").eq(3).remove();