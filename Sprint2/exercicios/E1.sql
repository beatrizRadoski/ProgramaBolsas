CREATE TABLE 'past1' ('c1' TEXT);
INSERT INTO 'past1' (c1) VALUES 
 ('select *'), 
 ('from livro'), 
 ('where cast(strftime(''%Y'', publicacao) as integer) > 2014'), 
 ('order by cod');