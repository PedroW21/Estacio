var contas = {
  agencia: "0123-4",
  tipo: "física",
  nome: "José Maria",
  numero: "000.000-00",
};

var contasToJSON = JSON.stringify(contas);

// Armazena os dados no navegador 

localStorage.setItem("ContasJSON", contasToJSON);

// Capturar (recuperar) essas informações

var disparaAlertComInfos = localStorage.getItem("ContasJSON");

// Devo fazer o parse em seguida e depois é so montar uma template string com as infos
