var contas = '{"agencia": "0123-4","tipo": "física","nome": "José Maria","numero": "000.000-00"}';

// Converte o objeto JavaScript para JSON

var contasJson = JSON.parse(contas);

// Exibindo em uma tag HTML teorica

//document.getElementsByClassName("example").innerHTML = `Agência: ${contasJson[0].agencia}`;

console.log(`Agência: ${contasJson.agencia} | Natureza: ${contasJson.tipo} | Nome: ${contasJson.nome} | Numero: ${contasJson.numero}`);
