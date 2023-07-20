create table if not exists exceldata (
	id integer primare key,
	company varchar(4096),
	fact_forecast varchar(8),
	oliq_ooil varchar(4),
	date_ date,
	data integer
);