DROP PROCEDURE IF EXISTS sc_add;
DELIMITER //
CREATE PROCEDURE sc_add(
    IN student_id CHAR(8),
    IN course_id  CHAR(8),
    IN score INT,
    OUT flag INT
)
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET @status = 1;
    INSERT INTO sc (student_id, course_id, score)
    VALUES (student_id, course_id, score);
    IF @status = 1 THEN
        SET flag = 1;
        ROLLBACK;
    ELSE
        SET flag = 0;
        COMMIT;
    END IF;
END //
DELIMITER ;