DROP TRIGGER IF EXISTS student_status_1;
DROP TRIGGER IF EXISTS student_status_2;
DELIMITER //
CREATE TRIGGER student_status_1
AFTER INSERT ON sc
FOR EACH ROW
BEGIN
    DECLARE c_count INT DEFAULT 0;
    SELECT COUNT(*) INTO c_count FROM sc
    WHERE student_id = NEW.student_id and score < 60;
    IF c_count >= 3 THEN
        UPDATE student
        SET s_status = '不合格'
        WHERE sid = NEW.student_id;
    END IF;
END //
CREATE TRIGGER student_status_2
AFTER UPDATE ON sc
FOR EACH ROW
BEGIN
    DECLARE c_count INT DEFAULT 0;
    SELECT COUNT(*) INTO c_count FROM sc
    WHERE student_id = NEW.student_id and score < 60;
    IF c_count >= 3 THEN
        UPDATE student SET s_status = '不合格'
        WHERE sid = NEW.student_id;
    ELSE
        UPDATE student SET s_status = '合格'
        WHERE sid = NEW.student_id;
    END IF;
END //
DELIMITER ;