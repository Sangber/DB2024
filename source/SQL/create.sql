-- source/SQL/create.sql
USE lab02;

-- 专业
DROP TABLE IF EXISTS major;
CREATE TABLE major (
    -- 专业代码（主键，已加入格式约束）
    -- 专业名称（不能为空）
    -- 专业概念图（可以为空）
	mid CHAR(8) CHECK (REGEXP_LIKE(mid, '^M[0-9]{3}$')),
    mname VARCHAR(100) NOT NULL,
    logo MediumBlob,
    PRIMARY KEY (mid)
);

-- 学生
DROP TABLE IF EXISTS student;
CREATE TABLE student (
    -- 学号（主键，已加入格式约束）
    -- 姓名（不能为空）
    -- 性别（加入约束，只能为“男”或“女”）
    -- 出生日期
    -- 专业代码（外键，已定义级联删除）
    -- 及格状态（加入约束，只能为“合格”或“不合格”）
	sid CHAR(8) CHECK (REGEXP_LIKE(sid, '^S[0-9]{3}$')),
    sname VARCHAR(100) NOT NULL,
    gender VARCHAR(8) check (gender = '男' or gender = '女'),
    birth_date DATE,
    major_id CHAR(8),
    s_status VARCHAR(100) check (s_status = '合格' or s_status = '不合格') DEFAULT '合格',
    Foreign Key (major_id) REFERENCES major(mid) ON DELETE CASCADE,
    PRIMARY KEY (sid)
);

-- 课程
DROP TABLE IF EXISTS course;
CREATE TABLE course (
    -- 课程代码（主键，已加入格式约束）
    -- 课程名称（不能为空）
    -- 专业代码（外键，已定义级联删除）
	cid CHAR(8) CHECK (REGEXP_LIKE(cid, '^C[0-9]{3}$')),
    cname VARCHAR(100) NOT NULL,
    major_id CHAR(8),
    Foreign Key (major_id) REFERENCES major(mid) ON DELETE CASCADE,
    PRIMARY KEY (cid)
);

-- 奖惩
DROP TABLE IF EXISTS award;
CREATE TABLE award (
    -- 奖惩代码（主键，已加入格式约束）
    -- 奖惩内容（不能为空）
	aid CHAR(8) CHECK (REGEXP_LIKE(aid, '^A[0-9]{3}$')),
    aname VARCHAR(100) NOT NULL,
    PRIMARY KEY (aid)
);

-- 选课情况
DROP TABLE IF EXISTS sc;
CREATE TABLE sc (
    -- 学号（外键，已定义级联删除）
    -- 课程代码（外键，已定义级联删除）
    -- 分数
    -- （学号，课程代码）组成主键
	student_id CHAR(8),
    course_id  CHAR(8),
    score INT check (score >= 10 and score <= 100) DEFAULT 0,
    Foreign Key (student_id) REFERENCES student(sid) ON DELETE CASCADE,
    Foreign Key (course_id)  REFERENCES course(cid)  ON DELETE CASCADE,
    PRIMARY KEY (student_id, course_id)
);

-- 获奖/惩情况
DROP TABLE IF EXISTS sa;
CREATE TABLE sa (
    -- 学号（外键，已定义级联删除）
    -- 奖惩代码（外键，已定义级联删除）
    -- 获奖/惩时间
    -- （学号，奖惩代码，获奖/惩时间）组成主键
	student_id CHAR(8),
    award_id   CHAR(8),
    award_time DATE,
    Foreign Key (student_id) REFERENCES student(sid) ON DELETE CASCADE,
    Foreign Key (award_id)   REFERENCES award(aid)   ON DELETE CASCADE,
    PRIMARY KEY (student_id, award_id, award_time)
);
