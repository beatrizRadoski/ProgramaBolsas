select distinct au.nome
from autor as au
left join livro as li
on au.codautor = li.autor
left join editora as ed
on li.editora = ed.codeditora
left join endereco
on ed.endereco = endereco.codendereco
where endereco.estado not in ('PARANÁ','SANTA CATARINA','RIO GRANDE DO SUL')
order by au.nome
