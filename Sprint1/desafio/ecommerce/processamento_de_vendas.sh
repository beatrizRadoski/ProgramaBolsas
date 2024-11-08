cd /home/beatriz/ecommerce
mkdir vendas
cp dados_de_vendas.csv /home/beatriz/ecommerce/vendas/arquivo_dados_de_vendas.csv

cd vendas && mkdir backup
cd ..
cp dados_de_vendas.csv /home/beatriz/ecommerce/vendas/backup/dados-$(date +'%F').csv

cd vendas/backup/
mv dados-$(date +'%F').csv backup-dados-$(date +'%F').csv

touch relatório-$(date +'%F').txt arquivo0.txt 

date +'%F %l:%M' > arquivo0.txt 
head -n 2 backup-dados-$(date +'%F').csv |tail -n 1 |cut -d',' -f5 >> arquivo0.txt
tail -n 1 backup-dados-$(date +'%F').csv |cut -d',' -f5 >> arquivo0.txt
tail -n +2 backup-dados-$(date +'%F').csv | wc -l >> arquivo0.txt 
head -n 10 backup-dados-$(date +'%F').csv >> arquivo0.txt

cat arquivo0.txt  > relatório-$(date +'%F').txt
rm arquivo0.txt

zip backup-dados-$(date +'%F').zip backup-dados-$(date +'%F').csv
rm backup-dados-$(date +'%F').csv
cd ..
rm arquivo_dados_de_vendas.csv

