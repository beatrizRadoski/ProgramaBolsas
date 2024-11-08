select cdpro,nmcanalvendas, nmpro,
        sum(qtd) as quantidade_vendas
from tbvendas 
where status = 'Concluído'
group by cdpro, nmpro, nmcanalvendas
order by quantidade_vendas asc
limit 10

