select 
	ed.codeditora as CodEditora,
    ed.nome as NomeEditora,
    Count(li.cod) as QuantidadeLivros
from editora as ed 
RIGHT join livro as li 
on ed.codeditora = li.editora
group by CodEditora, NomeEditora
order by QuantidadeLivros desc
limit 5