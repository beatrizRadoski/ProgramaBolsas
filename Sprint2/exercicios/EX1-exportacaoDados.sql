select 
	li.cod as CodLivro,
    li.titulo as Titulo,
    au.codautor as CodAutor,
    au.nome as NomeAutor,
    li.valor as Valor,
    ed.codeditora as CodEditora,
    ed.nome as NomeEditora
from autor as au 
left join livro as li 
on au.codautor = li.autor
left join editora as ed 
on li.editora = ed.codeditora
order by Valor DESC
LIMIT 10