select au.nome, au.codautor, au.nascimento, count(li.cod) as "quantidade"
from autor as au 
left join livro as li 
on au.codautor = li.autor
group by au.nome
order by au.nome