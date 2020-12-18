create table app_info
(
    id int,
    app_name varchar(100)
) charset = utf8;

ALTER table app_info add PRIMARY key(id);

insert into app_info values (1,"第五人格");
insert into app_info values (2,"第五人格");
insert into app_info values (3,"荒野行动");
insert into app_info values (4,"倩女幽魂");
insert into app_info values (5,"绝地求生");
insert into app_info values (6,"海岛纪元");
insert into app_info values (7,"海岛纪元");

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
