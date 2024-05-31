use lab02;

create table major (
	mid char(8),
    mname varchar(100) check (mname is not null),
    primary key(mid)
);

create table student (
	sid char(8),
    sname varchar(100) check (sname is not null),
    gender int check (gender = 0 or gender = 1), -- 0表示男，1表示女
    birth_date date,
    major_id char(8),
    foreign key (major_id) references major(mid),
    primary key (sid)
);

create table course (
	cid char(8),
    cname varchar(100) check (cname is not null),
    major_id char(8),
    foreign key (major_id) references major(mid),
    primary key (cid)
);
