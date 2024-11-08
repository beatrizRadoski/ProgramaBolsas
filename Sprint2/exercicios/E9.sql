select pd.cdpro, ve.nmpro
from tbestoqueproduto as pd
left join tbvendas as ve
on pd.cdpro = ve.cdpro
where ve.status = 'Concluído' and (ve.dtven between '2014-02-03' and '2018-02-02')
group by pd.cdpro,ve.nmpro
order by count(ve.cdpro) desc
limit 1