DROP PROCEDURE IF EXISTS sc_add;
DELIMITER //
CREATE PROCEDURE sc_add(
    IN student_id CHAR(8),
    IN course_id  CHAR(8),
    IN score INT,
    OUT flag INT
)
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET @status = 1; -- 异常检测句柄
    INSERT INTO sc (student_id, course_id, score)
    VALUES (student_id, course_id, score);
    -- 根据是否产生异常，决定是回滚还是提交
    IF @status = 1 THEN
        SET flag = 1;
        ROLLBACK;
    ELSE
        SET flag = 0;
        COMMIT;
    END IF;
END //
DELIMITER ;