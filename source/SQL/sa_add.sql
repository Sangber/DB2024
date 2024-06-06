DROP PROCEDURE IF EXISTS sa_add;
DELIMITER //
CREATE PROCEDURE sa_add(
    IN student_id CHAR(8),
    IN award_id   CHAR(8),
    IN award_time DATE,
    OUT flag INT
)
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET @status = 1;
    INSERT INTO sa (student_id, award_id, award_time)
    VALUES (student_id, award_id, award_time);
    IF @status = 1 THEN
        SET flag = 1;
        ROLLBACK;
    ELSE
        SET flag = 0;
        COMMIT;
    END IF;
END //
DELIMITER ;