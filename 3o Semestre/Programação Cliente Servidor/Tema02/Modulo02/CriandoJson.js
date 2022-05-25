// Cria um Obj Js

var contas = {
  agencia: "0123-4",
  tipo: "física",
  nome: "José Maria",
  numero: "000.000-00",
};

// Converte o objeto JavaScript para JSON

var contasJson = JSON.stringify(contas);

// Redirecionando para o endereço especificado (vida GET) o texto JSON

//window.location = "processa/json/?conta=" + contasJson;
