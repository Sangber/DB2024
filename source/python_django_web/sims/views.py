import MySQLdb
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def student_index(request):
    sid         = request.GET.get('sid', '')
    sname       = request.GET.get('sname', '')
    gender      = request.GET.get('gender', '')
    birth_date  = request.GET.get('birth_date', '')
    mname       = request.GET.get('mname', '')

    sql =  "SELECT sid, sname, gender, birth_date, major.mname FROM student, major WHERE student.major_id = major.mid "
    if sid.strip() != '':
        sql = sql + " and sid = '" + sid + "'"
    if sname.strip() != '':
        sql = sql + " and sname = '" + sname + "'"

    print(sql)
    conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')
    with conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        students = cursor.fetchall()
    return render(request, 'student/index.html', {'students': students,
                                                  'sid': sid,
                                                  'sname': sname,
                                                  'gender': gender,
                                                  'birth_date': birth_date,
                                                  'mname': mname})

def major_index(request):
    mid         = request.GET.get('mid', '')
    mname       = request.GET.get('mname', '')

    sql =  "SELECT mid, mname FROM major WHERE 1=1 "
    if mid.strip() != '':
        sql = sql + " and mid = '" + mid + "'"
    if mname.strip() != '':
        sql = sql + " and mname = '" + mname + "'"

    print(sql)
    conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')
    with conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        majors = cursor.fetchall()
    return render(request, 'major/index.html', {'majors': majors,
                                                'mid': mid,
                                                'mname': mname})