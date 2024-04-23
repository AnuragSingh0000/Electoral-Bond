use dccp;
select * from bond_data;
SET SQL_SAFE_UPDATES = 0;


UPDATE bond_data
SET year = YEAR(STR_TO_DATE(Date_of_Encashment, '%d/%b/%Y'))
