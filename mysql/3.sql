drop table user_info;
create table user_info
(
    nickname varchar(100),
    username varchar(100),
    sex varchar(100)
);

alter table user_info add PRIMARY key(nickname);

drop table address;
create table address
(
    address_id int,
    nickname varchar(100),
    city varchar(100),
    state varchar(100)
);

alter table address add primary key(address_id);

insert into user_info values ("tom","a","F");
insert into user_info values ("lana","b","F");
insert into user_info values ("zoo","c","M");

insert into address values (1,"lana","杭州","浙江");
insert into address values (2,"tom","桂林","广西");

select a.nickname,a.username,a.sex,b.city,b.state
from
(
    user_info a
    left JOIN
    address b
    on a.nickname = b.nickname
);