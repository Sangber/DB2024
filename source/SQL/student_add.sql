DROP PROCEDURE IF EXISTS student_add;
DELIMITER //
CREATE PROCEDURE student_add(
    IN sid CHAR(8),
    IN sname VARCHAR(100),
    IN gender VARCHAR(8),
    IN birth_date DATE,
    IN major_id CHAR(8),
    OUT flag INT
)
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET @status = 1; -- 异常检测句柄
    INSERT INTO student (sid, sname, gender, birth_date, major_id)
    VALUES (sid, sname, gender, birth_date, major_id);
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