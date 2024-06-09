DROP FUNCTION IF EXISTS gpa;
DROP FUNCTION IF EXISTS major_gpa;
DELIMITER //
CREATE FUNCTION gpa(sid CHAR(8))
RETURNS FLOAT
READS SQL DATA
BEGIN
    DECLARE course_count INT DEFAULT 0;
    DECLARE score_total  INT DEFAULT 0;
    DECLARE gpa FLOAT DEFAULT 0;
    SELECT SUM(score) INTO score_total FROM sc WHERE sc.student_id=sid;
    SELECT COUNT(score) INTO course_count FROM sc WHERE sc.student_id=sid;
    SET gpa = score_total / course_count;
    RETURN ROUND(gpa, 2); -- 保留两位小数
END //

CREATE FUNCTION major_gpa(sid CHAR(8))
RETURNS FLOAT
READS SQL DATA
BEGIN
    DECLARE major_course_count INT DEFAULT 0;
    DECLARE major_score_total  INT DEFAULT 0;
    DECLARE major_gpa FLOAT DEFAULT 0;
    SELECT SUM(score) INTO major_score_total
    FROM sc, course c, student s
    WHERE sc.student_id=sid and sc.course_id=c.cid and c.major_id=s.major_id and s.sid = sid;
    SELECT COUNT(score) INTO major_course_count
    FROM sc, course c, student s
    WHERE sc.student_id=sid and sc.course_id=c.cid and c.major_id=s.major_id and s.sid = sid;
    SET major_gpa = major_score_total / major_course_count;
    RETURN ROUND(major_gpa, 2); -- 保留两位小数
END //
DELIMITER ;