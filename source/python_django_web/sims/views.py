import MySQLdb
from django.shortcuts import render

# Create your views here.
def index(request):
    sid         = request.GET.get('sid', '')
    sname       = request.GET.get('sname', '')
    gender      = request.GET.get('gender', '')
    birth_date  = request.GET.get('birth_date', '')
    mname       = request.GET.get('mname', '')

    sql =  "SELECT sid, sname, gender, birth_date, mname \
            FROM student, major \
            WHERE student.major_id = major.mid "
    if sid.strip() != '':
        sql = sql + " and sid = '" + sid + "'"
    if sname.strip() != '':
        sql = sql + " and sname = '" + sname + "'"

    print(sql)
    conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="db2024", charset='utf8')
    with conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        students = cursor.fetchall()
    return render(request, 'student/index.html', {'学生': students,
                                                  '学号': sid,
                                                  '姓名': sname,
                                                  '性别': gender,
                                                  '出生日期': birth_date,
                                                  '专业': mname})
