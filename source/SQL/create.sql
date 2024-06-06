USE lab02;

DROP TABLE IF EXISTS major;
CREATE TABLE major (
	mid CHAR(8) CHECK (REGEXP_LIKE(mid, '^M[0-9]{3}$')),
    mname VARCHAR(100) check (mname is not null),
    PRIMARY KEY (mid)
);

DROP TABLE IF EXISTS student;
CREATE TABLE student (
	sid CHAR(8) CHECK (REGEXP_LIKE(sid, '^S[0-9]{3}$')),
    sname VARCHAR(100) check (sname is not null),
    gender VARCHAR(8) check (gender = '男' or gender = '女'),
    birth_date DATE,
    major_id CHAR(8),
    s_status VARCHAR(100) check (s_status = '合格' or s_status = '不合格') DEFAULT '合格',
    Foreign Key (major_id) REFERENCES major(mid) ON DELETE CASCADE,
    PRIMARY KEY (sid)
);

DROP TABLE IF EXISTS course;
CREATE TABLE course (
	cid CHAR(8) CHECK (REGEXP_LIKE(cid, '^C[0-9]{3}$')),
    cname VARCHAR(100) check (cname is not null),
    major_id CHAR(8),
    Foreign Key (major_id) REFERENCES major(mid) ON DELETE CASCADE,
    PRIMARY KEY (cid)
);

DROP TABLE IF EXISTS award;
CREATE TABLE award (
	aid CHAR(8) CHECK (REGEXP_LIKE(aid, '^A[0-9]{3}$')),
    aname VARCHAR(100) check (aname is not null),
    PRIMARY KEY (aid)
);

DROP TABLE IF EXISTS sc;
CREATE TABLE sc (
	student_id CHAR(8),
    course_id  CHAR(8),
    score INT check (score >= 10 and score <= 100) DEFAULT 0,
    Foreign Key (student_id) REFERENCES student(sid) ON DELETE CASCADE,
    Foreign Key (course_id)  REFERENCES course(cid)  ON DELETE CASCADE,
    PRIMARY KEY (student_id, course_id)
);

DROP TABLE IF EXISTS sa;
CREATE TABLE sa (
	student_id CHAR(8),
    award_id   CHAR(8),
    award_time DATE,
    Foreign Key (student_id) REFERENCES student(sid) ON DELETE CASCADE,
    Foreign Key (award_id)   REFERENCES award(aid)   ON DELETE CASCADE,
    PRIMARY KEY (student_id, award_id, award_time)
);
