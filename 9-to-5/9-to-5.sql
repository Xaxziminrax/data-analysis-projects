/*

select * from laborstatisticsdb.dbo.datatype
where data_type_text LIKE '%women%';

select * from LaborStatisticsDB.dbo.supersector
where supersector_name LIKE '%financial%';

*/

/*
select * from LaborStatisticsDB.dbo.industry
where industry_name LIKE '%commercial banking%'

select DISTINCT * from LaborStatisticsDB.dbo.series
where supersector_code = 55 AND data_type_code = 10 AND industry_code = 55522110;
*/

--select * from LaborStatisticsDB.dbo.datatype;

--select top 25 * from LaborStatisticsDB.dbo.industry

--select top 25 * from LaborStatisticsDB.dbo.footnote

--select top 25 * from LaborStatisticsDB.dbo.annual_2016
--ORDER BY "value" DESC;


--select top 15 * from LaborStatisticsDB.dbo.annual_2016;
/*
select * from LaborStatisticsDB.dbo.series
WHERE data_type_code IN (1, 25, 26);

select * from LaborStatisticsDB.dbo.annual_2016
where series_id LIKE '%01' or series_id LIKE '%25' or series_id like '%26'
order by [period] DESC
*/
/*
select sum([value]) AS "sumAllWomen"
from LaborStatisticsDB.dbo.annual_2016 
where series_id LIKE '%10';

select *
from LaborStatisticsDB.dbo.annual_2016 
where series_id LIKE '%10';
*/
/*
select sum([value]) AS "sumProdAndNonSup"
from LaborStatisticsDB.dbo.annual_2016 
where series_id LIKE '%06';
*/
/*
select avg([value]) as "avgWeeklyHrsWorkedProd"
from LaborStatisticsDB.dbo.january_2017
where series_id LIKE '%07'
*/

/*
select SUM([value]) as "totalWeeklyPayrollProd"
from LaborStatisticsDB.dbo.january_2017
where series_id LIKE '%81'
*/
/*
select * 
from LaborStatisticsDB.dbo.january_2017
where series_id LIKE '%81'
ORDER BY "value" ASC;

select * 
from LaborStatisticsDB.dbo.series
where series_id = 'CES2023720081';

select *   
from LaborStatisticsDB.dbo.industry
where industry_code = 20237200;
*/
/*
SELECT TOP 50 * 
FROM LaborStatisticsDB.dbo.annual_2016 as a
LEFT JOIN LaborStatisticsDB.dbo.series as s ON a.series_id = s.series_id
RIGHT JOIN LaborStatisticsDB.dbo.datatype as d ON s.data_type_code = s.data_type_code
FULL OUTER JOIN LaborStatisticsDB.dbo.industry as i ON i.industry_code = s.industry_code
ORDER BY a.id;
*/
/*
SELECT series_id, [value], industry_code, industry_name
from LaborStatisticsDB.dbo.january_2017 as j
INNER JOIN  LaborStatisticsDB.dbo.industry as i ON j.id = i.id
WHERE [value] > (
    select AVG(a.value) from LaborStatisticsDB.dbo.annual_2016 as a
    where a.series_id LIKE '%82');
*/
/*
SELECT avg([value]) as "avgEarnings", period, [year]
FROM LaborStatisticsDB.dbo.annual_2016
WHERE series_id LIKE '%30'
GROUP BY [year], [period]
UNION
SELECT avg([value]) as "avgEarnings", period, [year]
from LaborStatisticsDB.dbo.january_2017
WHERE series_id LIKE '%30'
GROUP BY [year], [period]
*/
/*
select i.industry_name, j.value
from LaborStatisticsDB.dbo.industry as i
INNER JOIN LaborStatisticsDB.dbo.january_2017 as j ON i.id = j.id
where j.[value] > (
    select avg(j.value) 
    from LaborStatisticsDB.dbo.january_2017 as j
    where (j.series_id LIKE '%30' OR j.series_id LIKE '%31')
) 
AND (j.[series_id] LIKE '%30' OR j.series_id LIKE '%31')
ORDER BY j.value DESC
*/
/*
select avg([value]) from LaborStatisticsDB.dbo.
WHERE prod
*/