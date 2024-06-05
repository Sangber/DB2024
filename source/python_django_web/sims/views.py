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

def student_edit(request):
    if request.method == 'GET':
        sid = request.GET.get('sid', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT sid, sname, gender, birth_date, major_id FROM student where sid =%s", [sid])
            student = cursor.fetchone()
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM major")
            options = cursor.fetchall()
        return render(request, 'student/edit.html', {'student': student, 'options': options})
    else:
        sid         = request.POST.get('sid', '')
        sname       = request.POST.get('sname', '')
        gender      = request.POST.get('gender', '')
        birth_date  = request.POST.get('birth_date', '')
        major_id    = request.POST.get('major_id', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("call student_edit(%s, %s, %s, %s, %s)", [sid, sname, gender, birth_date, major_id])
            conn.commit()
        return redirect('../student')

def student_delete(request):
    sid = request.GET.get('sid', '')
    conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("call student_delete(%s)", [sid])
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

def award_index(request):
    aid         = request.GET.get('aid', '')
    aname       = request.GET.get('aname', '')

    sql =  "SELECT aid, aname FROM award WHERE 1=1 "
    if aid.strip() != '':
        sql = sql + " and aid = '" + aid + "'"
    if aname.strip() != '':
        sql = sql + " and aname = '" + aname + "'"

    print(sql)
    conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')
    with conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        awards = cursor.fetchall()
    return render(request, 'award/index.html', {'awards': awards})

def sa_index(request):
    sname = request.GET.get('sname', '')
    aname = request.GET.get('aname', '')

    sql =  "SELECT sid, sname, aid, aname, award_time FROM student, award, sa"
    "WHERE sid = student_id and aid = award_id"
    if sname.strip() != '':
        sql = sql + " and sname = '" + sname + "'"
    if aname.strip() != '':
        sql = sql + " and aname = '" + aname + "'"

    print(sql)
    conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')
    with conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        sas = cursor.fetchall()
    return render(request, 'sa/index.html', {'sas': sas})

def sa_add(request):
    if request.method == 'GET':
        sid = request.GET.get('sid', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT aid, aname FROM award", [sid])
            options = cursor.fetchall()
        return render(request, 'sa/add.html', {'sid': sid, 'options': options})
    else:
        student_id  = request.POST.get('sid', '')
        award_id    = request.POST.get('award_id', '')
        award_time  = request.POST.get('award_time', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO sa (student_id, award_id, award_time)"
                           "VALUES(%s, %s, %s)", [student_id, award_id, award_time])
            conn.commit()
        return redirect('../sa')

def sa_delete(request):
    sid = request.GET.get('sid', '')
    aid = request.GET.get('aid', '')
    conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM sa WHERE sid=%s and aid=%s", [sid, aid])
        conn.commit()
    return redirect('../sa')