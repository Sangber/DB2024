DROP FUNCTION IF EXISTS major_gpa;
DELIMITER //
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
    RETURN major_gpa;
END //
DELIMITER ;