with vendas_por_vendedor as (
select vendedor.cdvdd, vendedor.nmvdd, count(vendas.cdvdd) as "quantidade" 
from tbvendedor as vendedor 
left join tbvendas as vendas
on vendedor.cdvdd = vendas.cdvdd
where vendas.status = 'Concluído'
group by vendedor.cdvdd
order by "quantidade" desc
)


select vendas_por_vendedor.cdvdd, vendas_por_vendedor.nmvdd
from vendas_por_vendedor
limit 1