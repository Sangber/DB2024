DROP PROCEDURE IF EXISTS student_edit;
DELIMITER //
CREATE PROCEDURE student_edit(
    in sid CHAR(8),
    in sname VARCHAR(100),
    in gender VARCHAR(8),
    in birth_date DATE,
    in major_id CHAR(8)
)
begin
    UPDATE student as s
    SET s.sname = sname, s.gender = gender, s.birth_date = birth_date, s.major_id = major_id
    WHERE s.sid = sid;
end //
DELIMITER ;