with vendedor_menor_valor as (
select 
    vendedor.cdvdd,
    sum(vendas.qtd*vendas.vrunt) as valor_total_vendas
from tbvendedor as vendedor 
left join tbvendas as vendas 
on vendedor.cdvdd = vendas.cdvdd
where vendas.status = 'Concluído'
group by vendedor.cdvdd
having valor_total_vendas > 0 
order by valor_total_vendas 
)

select dependente.cddep,
    dependente.nmdep,
    dependente.dtnasc,
    vendedor_menor_valor.valor_total_vendas
from tbdependente as dependente 
left join vendedor_menor_valor
on dependente.cdvdd = vendedor_menor_valor.cdvdd
order by vendedor_menor_valor.valor_total_vendas asc 
limit 1

