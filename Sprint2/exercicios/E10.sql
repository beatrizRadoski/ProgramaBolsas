with valor_total_vendas as (
select
    vendedor.nmvdd, 
    vendedor.perccomissao,
    vendas.qtd,
    vendas.vrunt,
    SUM(qtd*vrunt) as "valor_total_vendas"
from tbvendedor as vendedor 
left join tbvendas as vendas 
    on vendedor.cdvdd = vendas.cdvdd
where vendas.status = 'Concluído'
group by vendedor.nmvdd
)

select 
    nmvdd as "vendedor",
    "valor_total_vendas",
    round((valor_total_vendas*(perccomissao)/100),2) as "comissao"
from valor_total_vendas
ORDER BY "comissao" desc
    
