DROP FUNCTION IF EXISTS gpa;
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
    RETURN gpa;
END //
DELIMITER ;