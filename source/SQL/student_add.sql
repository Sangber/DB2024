DROP PROCEDURE IF EXISTS student_add;
DELIMITER //
CREATE PROCEDURE student_add(
    in sid CHAR(8),
    in sname VARCHAR(100),
    in gender VARCHAR(8),
    in birth_date DATE,
    in major_id CHAR(8)
)
BEGIN
    INSERT INTO student (sid, sname, gender, birth_date, major_id)
    VALUES
    (sid, sname, gender, birth_date, major_id);
END //
DELIMITER ;