create table app_info
(
    id int,
    app_name varchar(100)
) charset = utf8;

ALTER table app_info add PRIMARY key(id);

insert into app_info values (1,"�����˸�");
insert into app_info values (2,"�����˸�");
insert into app_info values (3,"��Ұ�ж�");
insert into app_info values (4,"ٻŮ�Ļ�");
insert into app_info values (5,"��������");
insert into app_info values (6,"������Ԫ");
insert into app_info values (7,"������Ԫ");

create table temp_app_info
(
    id int(11) not null
);
insert into temp_app_info 
select a.id 
from 
(
    select max(id) as id 
    from app_info group by app_name
) a;

delete 
from app_info
where id not in 
(
    select id 
    from temp_app_info
);


-- delete from app_info
-- where id in 
-- (
--     SELECT a.ID
--     FROM 
--     (
--         select id
--         from app_info  
--         group by app_name  
--         having  count(id) > 1
--     ) a
-- )
-- and id not in (select min(id) from app_info group by id  
-- having count(id)>1);
