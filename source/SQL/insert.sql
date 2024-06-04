USE lab02;

INSERT INTO major (mid, mname)
VALUES
('M001', '计算机科学与技术'),
('M002', '数学'),
('M003', '物理学'),
('M004', '管理学'),
('M005', '化学与材料科学'),
('M006', '地球与空间科学');

INSERT INTO student (sid, sname, gender, birth_date, major_id)
VALUES
('S001', '张明', '男', '2005-03-15', 'M001'),
('S002', '孙芳芳', '女', '2005-08-14', 'M001'),
('S003', '邓洁', '女', '2005-11-17', 'M001'),
('S004', '田思思', '女', '2005-05-14', 'M001'),
('S005', '董芳', '女', '2005-08-27', 'M001'),
('S006', '李华东', '女', '2005-07-22', 'M002'),
('S007', '钟强', '男', '2005-12-31', 'M002'),
('S008', '施梅梅', '女', '2005-06-29', 'M002'),
('S009', '刘强', '男', '2005-10-30', 'M002'),
('S010', '马艳', '女', '2005-12-14', 'M002'),
('S011', '陈涛涛', '男', '2005-11-08', 'M003'),
('S012', '谢娜', '女', '2005-05-07', 'M003'),
('S013', '胡伟', '男', '2005-09-05', 'M003'),
('S014', '杨娟', '女', '2005-03-03', 'M003'),
('S015', '廖强强', '男', '2005-04-09', 'M003'),
('S016', '王丽', '女', '2005-06-02', 'M004'),
('S017', '周宇飞', '男', '2005-10-23', 'M004'),
('S018', '曹芳', '女', '2005-04-26', 'M004'),
('S019', '冯波涛', '男', '2005-07-18', 'M004'),
('S020', '顾平', '男', '2005-09-12', 'M004'),
('S021', '黄建军', '男', '2005-09-28', 'M005'),
('S022', '何欣', '女', '2005-02-28', 'M005'),
('S023', '阮杰', '男', '2005-08-21', 'M005'),
('S024', '蒋梅梅', '女', '2005-11-24', 'M005'),
('S025', '韩丽', '女', '2005-02-05', 'M005'),
('S026', '赵飞', '男', '2005-04-19', 'M006'),
('S027', '吴刚刚', '男', '2005-07-11', 'M006'),
('S028', '贾敏', '女', '2005-12-08', 'M006'),
('S029', '沈杰', '男', '2005-05-31', 'M006'),
('S030', '秦刚', '男', '2005-07-04', 'M006');

INSERT INTO course (cid, cname, major_id)
VALUES
('C001', '计算机程序设计', 'M001'),
('C002', '高等数学', 'M002'),
('C003', '经典力学', 'M003'),
('C004', '企业管理', 'M004'),
('C005', '分析化学', 'M005'),
('C006', '地球系统概论', 'M006'),
('C007', '数字电路与逻辑设计', 'M001'),
('C008', '离散数学', 'M002'),
('C009', '量子力学', 'M003'),
('C010', '财务管理', 'M004'),
('C011', '计算机操作系统', 'M001'),
('C012', '概率论与数理统计', 'M002'),
('C013', '电磁学', 'M003'),
('C014', '市场营销', 'M004'),
('C015', '物理化学', 'M005');

INSERT INTO award(aid, aname)
VALUES
('A001', '优秀学生一等奖学金'),
('A002', '三好学生'),
('A003', '优秀毕业生'),
('A004', '违纪通报'),
('A005', '警告'),
('A006', '优秀学生二等奖学金'),
('A007', '勤工俭学奖'),
('A008', '校级奖学金'),
('A009', '记过'),
('A010', '优秀学生三等奖学金'),
('A011', '社会实践奖'),
('A012', '国家励志奖学金'),
('A013', '留校察看'),
('A014', '校园文明奖'),
('A015', '自律奖');