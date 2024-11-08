insert into Clientes(
idCliente, nomeCliente,cidadeCliente, estadoCliente, paisCliente
)
select DISTINCT idcliente,nomecliente,cidadecliente,estadocliente,paiscliente
from tb_locacao

insert or ignore into Carro(
idCarro, kmCarro,classiCarro,marcaCarro,modeloCarro,anoCarro,idCombustivel
)
SELECT DISTINCT idcarro,max(kmcarro),classicarro,marcacarro,modelocarro,anocarro,idcombustivel 
from tb_locacao
group by idcarro,classicarro,marcacarro,modelocarro,anocarro,idcombustivel

insert or ignore into Combustivel(
	idCombustivel,tipoCombustivel
)
SELECT DISTINCT idcombustivel,tipocombustivel from tb_locacao

insert or ignore into Vendedor(
idVendedor,nomeVendedor,sexoVendedor,estadoVendedor
)
SELECT DISTINCT idvendedor,nomevendedor,sexovendedor,estadovendedor from tb_locacao

insert or ignore into Locacao(
idLocacao,dataLocacao,horaLocacao,qtdDiaria,vlrDiaria,dataEntrega,horaEntrega,
 idCliente,idVendedor,idCarro,idCombustivel
)
SELECT DISTINCT idlocacao,datalocacao,horalocacao,qtddiaria,vlrdiaria,dataentrega,horaentrega,
idcliente,idvendedor,idcarro,idcombustivel
from tb_locacao