drop table user_info;
create table user_info
(
    nickname varchar(100),
    username varchar(100),
    dept_id int,
    game_count int
) charset = utf8;

insert into user_info values ("zhangsan","张三",1,108);
insert into user_info values ("lisi","李四",1,120);
insert into user_info values ("wangwu","王五",2,170);
insert into user_info values ("zhaosi","赵四",2,10);
insert into user_info values ("tom","汤姆",3,190);

drop table dept_info;
create table dept_info
(
    dept_id int,
    dept_name varchar(100)
) charset = utf8;

insert into dept_info values (1,"财务");
insert into dept_info values (2,"IT");
insert into dept_info values (3,"开发");

create table temp_5
(
    dept_name varchar(100),
    user_name varchar(100),
    game_count int
) charset = utf8;

insert into temp_5
select b.dept_name,a.username,a.game_count
from
(
    (
        select *
        from user_info 
        order by game_count desc
    ) a
    left join
    dept_info b
    on a.dept_id = b.dept_id
);

create table temp_5_1
(
    dept_name varchar(100),
    user_name varchar(100),
    game_count int
) charset = utf8;

insert into temp_5_1
select * 
from temp_5
order by game_count desc;

create table temp_5_2
(
    dept_name varchar(100),
    user_name varchar(100),
    game_count int
) charset = utf8;

insert into temp_5_2
select * 
from temp_5_1
group by dept_name;