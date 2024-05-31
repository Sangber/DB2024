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

create table award (
	aid char(8),
    aname varchar(100) check (aname is not null),
    primary key (aid)
);

create table sc (
	student_id char(8),
    course_id  char(8),
    score int check (score >= 0 and score <= 100) default 0,
    foreign key (student_id) references student(sid),
    foreign key (course_id)  references course(cid),
    primary key (student_id, course_id)
);

create table sa (
	student_id char(8),
    award_id char(8),
    award_time date,
    foreign key (student_id) references student(sid),
    foreign key (award_id)   references award(aid),
    primary key (student_id, award_id)
);