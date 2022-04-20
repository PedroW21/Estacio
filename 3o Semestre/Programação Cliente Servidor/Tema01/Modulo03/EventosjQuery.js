$(() => {
  console.log("Evento document.ready disparado");
});

$("button").click(() => { // caso eu utilizasse o on("click") ele poderia também "escutar" em valores dinamicamente colocados pelo jQuery
  $("h1").after("<img src='https://picsum.photos/200'><img>");
});


