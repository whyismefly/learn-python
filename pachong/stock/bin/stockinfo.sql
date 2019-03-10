SELECT * FROM stock_test.stockinfo;
select * from stock_test.stockinfo group by code having count(code) > 1;
SELECT * FROM stock_test.stockinfo where pe <15;
select count(*)  from stock_test.stockinfo;
select count(*)  from stock_test.stockinfo where code is null;
select count(*)  from stock_test.stockinfo where pe is null;
select count(*)  from stock_test.stockinfo where pe = 0;
select *  from stock_test.stockinfo where pe != 0 and pe <15;
select count(*)  from stock_test.stockinfo where pe != 0 and pe <15;
select *  from stock_test.stockinfo where pe != 0 and pe <15 order by pe DESC;
select *  from stock_test.stockinfo where pe != 0 and pe <15 order by pe ASC;
select *  from stock_test.stockinfo where pe != 0 and pe <15 and rev>0 and profit>0 and gpr>0  order by pe ASC;
select *,COUNT(*)AS industry_num from stock_test.stockinfo where pe != 0 and pe <15 and rev>0 and profit>0 and gpr>0 GROUP BY industry order by pe ASC;

/*SELECT origin,count(*) num FROM user_operation_log GROUP BY origin;*/

SET SQL_SAFE_UPDATES = 0;
delete from stock_test.stockinfo;
truncate table stock_test.stockinfo;#truncate没有log记录操作，数据不可恢复
-- 建议使用delete -- 
/*
		 truncate和delete的区别
         1、事务：truncate是不可以rollback的，但是delete是可以rollback的；
              原因：truncate删除整表数据(ddl语句,隐式提交)，delete是一行一行的删除，可以rollback
         2、效果：truncate删除后将重新水平线和索引(id从零开始) ,delete不会删除索引    
         3、 truncate 不能触发任何Delete触发器。
         4、delete 删除可以返回行数
         推荐这种注释
         */