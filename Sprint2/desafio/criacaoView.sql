create view dimCarro as 
select idCarro as idCarro,
		kmCarro as kmCarro,
		classiCarro as classiCarro,
		marcaCarro as marcaCarro,
		modeloCarro as modeloCarro,
		anoCarro as anoCarro,
		idCombustivel as idCombustivel
from Carro;

create view FatoLocacao as 
select 	idLocacao as idLocacao,
		dataLocacao as dataLocacao,
		horaLocacao as horaLocacao,
		qtdDiaria as qtdDiaria,
		vlrDiaria as vlrDiaria,
		dataEntrega as dataEntrega,
		horaEntrega as horaEntrega,
		idCliente as idCliente,
		idVendedor as idVendedor,
		idCarro as idCarro,
		idCombustivel as idCombustivel
from Locacao;

create view dimCombustivel as 
select 	idCombustivel as idCombustivel,
		tipoCombustivel as tipoCombustivel
from Combustivel;

create view dimVendedor as 
select 	idVendedor as idVendedor,
		nomeVendedor as nomeVendedor,
		sexoVendedor as sexoVendedor,
		estadoVendedor as estadoVendedor
from Vendedor;

create view dimClientes as 
select 	idCliente as idCliente,
		nomeCliente as nomeCliente,
		cidadeCliente as cidadeCliente,
		estadoCliente as estadoCliente,
		paisCliente as paisCliente
from Clientes;