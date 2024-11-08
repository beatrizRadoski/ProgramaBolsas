CREATE TABLE Clientes(
  	idCliente int PRIMARY KEY,
	nomeCliente varchar,
  	cidadeCliente varchar,
  	estadoCliente varchar,
  	paisCliente varchar
)

CREATE TABLE Vendedor(
	idVendedor int PRIMARY KEY,
  	nomeVendedor varchar,
  	sexoVendedor varchar,
  	estadoVendedor varchar
)

CREATE TABLE Combustivel(
	idCombustivel int PRIMARY KEY,
  	tipoCombustivel varchar 
)

Create table Carro(
	idCarro int PRIMARY KEY,
  	kmCarro int,
  	classiCarro varchar,
  	marcaCarro varchar,
  	modeloCarro varchar,
  	anoCarro int,
  	idCombustivel int,
  	FOREIGN key (idCombustivel) REFERENCES Combustivel(idCombustivel)
)

create table Locacao(
	idLocacao int PRIMARY KEY,
  	dataLocacao varchar,
  	horaLocacao varchar ,
  	qtdDiaria int,
  	vlrDiaria float,
  	dataEntrega varchar,
  	horaEntrega varchar,
  	idCliente int,
    idVendedor int,
    idCarro int,
  	idCombustivel int,
  	FOREIGN key (idCliente) REFERENCES Clientes(idCliente),
  	FOREIGN key (idVendedor) REFERENCES Vendedor(idVendedor),
  	FOREIGN key (idCarro) REFERENCES Carro(idCarro)
)

UPDATE Locacao
set idCombustivel = (
	SELECT Carro.idCombustivel
  	FROM Carro
  	wHERE Carro.idCarro = Locacao.idCarro
)



