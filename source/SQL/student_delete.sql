-- 删除学生之前，先将其在sc和sa中的记录删除
-- 使用触发器实现

DROP PROCEDURE IF EXISTS student_delete;
DROP TRIGGER IF EXISTS cascade_delete;
DELIMITER //
CREATE TRIGGER cascade_delete BEFORE DELETE ON student FOR EACH ROW
BEGIN
    DELETE FROM sc WHERE sc.student_id = OLD.sid;
    DELETE FROM sa WHERE sa.student_id = OLD.sid;
END //

CREATE PROCEDURE student_delete(in sid CHAR(8))
BEGIN
    DELETE FROM student
    WHERE s.sid = sid;
END //
DELIMITER ;