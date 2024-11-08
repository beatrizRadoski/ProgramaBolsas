select 
    count(*) as "quantidade",
    ed.nome, endereco.estado,endereco.cidade
from livro as li
left join editora as ed 
on ed.codeditora = li.editora
left join endereco as endereco
on ed.endereco = endereco. codendereco
group by ed.nome
order by "quantidade" desc