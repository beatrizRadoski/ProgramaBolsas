select autor.codautor,
        autor.nome,
        count(livro.cod) as "quantidade_publicacoes"
from autor 
left join livro
on autor.codautor = livro.autor
group by autor.nome
order by "quantidade_publicacoes" desc
limit 1
