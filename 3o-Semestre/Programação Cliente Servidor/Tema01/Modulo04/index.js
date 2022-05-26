$("button").click(() => {
  $.ajax({
    url: "https://pokeapi.co/api/v2/pokemon?limit=10&offset=0",
    type: "GET",

    beforeSend: () => {
      $(".result").html("LOADING....");
    },
  })

    .done((msg) => {
      //pokes = msg.results;
      // console.log(pokes[0].name);

      //msgString = JSON.stringify(msg);
      //pokeNames = [];
      // $.each(pokes, (item, content)=> {
      //    pokeNames.push(content.name)
      // });
      // $(".result").html(pokeNames.toString());

      console.log(msg)
    })

    .fail((jqXHR, textStatus, errorMsg) => {
      console.log(
        `A requisição falhou e retornou com a seguinte mensagem ${errorMsg}`
      );
    });
});
