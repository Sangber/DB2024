-- 删除学生之前，先将其在sc和sa中的记录删除
-- 使用触发器实现

DROP PROCEDURE IF EXISTS student_delete;
DELIMITER //
CREATE PROCEDURE student_delete(
    in sid CHAR(8)
)
begin
    DELETE FROM student
    WHERE s.sid = sid;
end //
DELIMITER ;