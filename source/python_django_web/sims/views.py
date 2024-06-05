import MySQLdb
from django.db import IntegrityError
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

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
    return render(request, 'major/index.html', {'majors': majors})

def major_edit(request):
    if request.method == 'GET':
        mid = request.GET.get('mid', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT mid, mname FROM major where mid =%s", [mid])
            major = cursor.fetchone()
        return render(request, 'major/edit.html', {'major': major})
    else:
        mid     = request.POST.get('mid', '')
        mname   = request.POST.get('mname', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE major set mname=%s where mid =%s", [mname, mid])
            conn.commit()
        return redirect('../major')

def student_index(request):
    sid         = request.GET.get('sid', '')
    sname       = request.GET.get('sname', '')

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
    return render(request, 'student/index.html', {'students': students})

def student_add(request):
    if request.method == 'GET':
        conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM major")
            options = cursor.fetchall()
        return render(request, 'student/add.html', {'options': options})
    else:
        sid         = request.POST.get('sid', '')
        sname       = request.POST.get('sname', '')
        gender      = request.POST.get('gender', '')
        birth_date  = request.POST.get('birth_date', '')
        major_id    = request.POST.get('major_id', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("call student_add(%s, %s, %s, %s, %s)", [sid, sname, gender, birth_date, major_id])
            conn.commit()
        return redirect('../student')

def student_delete(request):
    sid = request.GET.get('sid', '')
    conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM student WHERE sid =%s", [sid])
        conn.commit()
    return redirect('../student')

def course_index(request):
    cid         = request.GET.get('cid', '')
    cname       = request.GET.get('cname', '')

    sql =  "SELECT cid, cname, major.mname FROM course, major WHERE course.major_id = major.mid "
    if cid.strip() != '':
        sql = sql + " and cid = '" + cid + "'"
    if cname.strip() != '':
        sql = sql + " and cname = '" + cname + "'"

    print(sql)
    conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')
    with conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        courses = cursor.fetchall()
    return render(request, 'course/index.html', {'courses': courses})