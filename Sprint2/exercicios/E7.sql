with publicacao_por_autor as (
    select autor.nome as nome, count(livro.publicacao) as publicados
    from autor 
    left join livro 
    on autor.codautor = livro.autor
    group by autor.nome
    
)
select nome
from publicacao_por_autor
where publicados = 0
order by nome
