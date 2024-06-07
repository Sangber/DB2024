import MySQLdb
import random
import base64
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql030520", db="lab02", charset='utf8')

def index(request):
    return render(request, 'index.html')

def passed(request):
    if request.method == 'GET':
        path = request.GET.get('path', '')
        return render(request, 'passed.html', {'path':path})
    else:
        path = request.POST.get('path', '')
        path = path.replace("_", "/")
        return redirect('/sims/%s' % (path))

def failed(request):
    if request.method == 'GET':
        path = request.GET.get('path', '')
        return render(request, 'failed.html', {'path':path})
    else:
        path = request.POST.get('path', '')
        path = path.replace("_", "/")
        return redirect('/sims/%s' % (path))

def major_index(request):
    mid         = request.GET.get('mid', '')
    mname       = request.GET.get('mname', '')

    sql =  "SELECT mid, mname, logo FROM major WHERE 1=1 "
    if mid.strip() != '':
        sql = sql + " and mid = '" + mid + "'"
    if mname.strip() != '':
        sql = sql + " and mname = '" + mname + "'"

    print(sql)
    with conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        majors = cursor.fetchall()
    for major in majors:
        if major['logo'] != None:
            major['logo'] = base64.b64encode(major['logo']).decode('utf-8')
    return render(request, 'major/index.html', {'majors': majors})

def major_edit(request):
    if request.method == 'GET':
        mid = request.GET.get('mid', '')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT mid, mname FROM major WHERE mid=%s", [mid])
            major = cursor.fetchone()
        return render(request, 'major/edit.html', {'major': major})
    else:
        mid     = request.POST.get('mid', '')
        mname   = request.POST.get('mname', '')
        if len(mname) > 100:
            return redirect('/sims/failed/?path=%s' % ('major_'))
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE major SET mname=%s WHERE mid=%s", [mname, mid])
            conn.commit()
        return redirect('/sims/passed/?path=%s' % ('major_'))

def major_upload(request):
    if request.method == 'GET':
        mid = request.GET.get('mid', '')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT mid, mname FROM major WHERE mid=%s", [mid])
            major = cursor.fetchone()
        return render(request, 'major/upload.html', {'major': major})
    else:
        mid     = request.POST.get('mid', '')
        logo    = request.FILES.get('logo', None)
        if logo: logo = logo.read()
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            if logo != None:
                cursor.execute("UPDATE major SET logo=%s WHERE mid=%s", [logo, mid])
            else:
                cursor.execute("UPDATE major SET logo=NULL WHERE mid=%s", [mid])
            conn.commit()
        return redirect('/sims/passed/?path=%s' % ('major_'))

def student_index(request):
    sid         = request.GET.get('sid', '')
    sname       = request.GET.get('sname', '')

    sql =  "SELECT sid, sname, gender, birth_date, major.mname, s_status, \
        gpa(sid) as s_gpa, major_gpa(sid) as s_major_gpa \
            FROM student, major WHERE student.major_id = major.mid "
    if sid.strip() != '':
        sql = sql + " and sid = '" + sid + "'"
    if sname.strip() != '':
        sql = sql + " and sname = '" + sname + "'"

    print(sql)
    with conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        students = cursor.fetchall()
    for student in students:
        student['birth_date'] = student['birth_date'].strftime('%Y-%m-%d')
    return render(request, 'student/index.html', {'students': students})

def student_add(request):
    if request.method == 'GET':
        
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
        if len(sid) > 8 or len(sname) > 100:
            return redirect('/sims/failed/?path=%s' % ('student_'))
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("CALL student_add(%s, %s, %s, %s, %s, @flag)", [sid, sname, gender, birth_date, major_id])
            conn.commit()
            cursor.execute("SELECT @flag")
            flag = cursor.fetchone()
        # print(flag)
        if flag['@flag'] == 0:
            return redirect('/sims/passed/?path=%s' % ('student_'))
        else:
            return redirect('/sims/failed/?path=%s' % ('student_'))

def student_edit(request):
    if request.method == 'GET':
        sid = request.GET.get('sid', '')
        
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT sid, sname, gender, birth_date, major_id FROM student WHERE sid =%s", [sid])
            student = cursor.fetchone()
        student['birth_date'] = student['birth_date'].strftime('%Y-%m-%d')
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
        if len(sname) > 100:
            return redirect('/sims/failed/?path=%s' % ('student_'))
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE student as s\
                           SET s.sname = %s, s.gender = %s, s.birth_date = %s, s.major_id = %s\
                           WHERE s.sid = %s", [sname, gender, birth_date, major_id, sid])
            conn.commit()
        return redirect('/sims/passed/?path=%s' % ('student_'))

def student_delete(request):
    sid = request.GET.get('sid', '')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM student WHERE student.sid = %s", [sid])
        conn.commit()
    return redirect('/sims/passed/?path=%s' % ('student_'))

def course_index(request):
    cid         = request.GET.get('cid', '')
    cname       = request.GET.get('cname', '')

    sql =  "SELECT cid, cname, major.mname FROM course, major \
        WHERE course.major_id = major.mid \
            ORDER by cid"
    if cid.strip() != '':
        sql = sql + " and cid = '" + cid + "'"
    if cname.strip() != '':
        sql = sql + " and cname = '" + cname + "'"

    print(sql)
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
    with conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        awards = cursor.fetchall()
    return render(request, 'award/index.html', {'awards': awards})

def sa_index(request):
    sname = request.GET.get('sname', '')
    aname = request.GET.get('aname', '')

    sql =  "SELECT sid, sname, aid, aname, award_time FROM student, award, sa WHERE student.sid = sa.student_id and award.aid = sa.award_id"
    if sname.strip() != '':
        sql = sql + " and sname = '" + sname + "'"
    if aname.strip() != '':
        sql = sql + " and aname = '" + aname + "'"

    print(sql)
    with conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        sas = cursor.fetchall()
    for sa in sas:
        sa['award_time'] = sa['award_time'].strftime('%Y-%m-%d')
    return render(request, 'sa/index.html', {'sas': sas})

def sa_add(request):
    if request.method == 'GET':
        
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT aid, aname FROM award")
            awards = cursor.fetchall()
            cursor.execute("SELECT sid, sname FROM student")
            students = cursor.fetchall()
        return render(request, 'sa/add.html', {'awards': awards, 'students': students})
    else:
        student_id  = request.POST.get('student_id', '')
        award_id    = request.POST.get('award_id', '')
        award_time  = request.POST.get('award_time', '')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("CALL sa_add(%s, %s, %s, @flag)", [student_id, award_id, award_time])
            conn.commit()
            cursor.execute("SELECT @flag")
            flag = cursor.fetchone()
        # print(flag)
        if flag['@flag'] == 0:
            return redirect('/sims/passed/?path=%s' % ('sa_'))
        else:
            return redirect('/sims/failed/?path=%s' % ('sa_'))

def sa_delete(request):
    sid = request.GET.get('sid', '')
    aid = request.GET.get('aid', '')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM sa WHERE student_id=%s and award_id=%s", [sid, aid])
        conn.commit()
    return redirect('/sims/passed/?path=%s' % ('sa_'))

def sc_index(request):
    sname = request.GET.get('sname', '')
    cname = request.GET.get('aname', '')

    sql =  "SELECT sid, sname, cid, cname, score FROM student, course, sc WHERE student.sid = sc.student_id and course.cid = sc.course_id"
    if sname.strip() != '':
        sql = sql + " and sname = '" + sname + "'"
    if cname.strip() != '':
        sql = sql + " and cname = '" + cname + "'"

    print(sql)
    with conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        scs = cursor.fetchall()
    return render(request, 'sc/index.html', {'scs': scs})

def sc_add(request):
    if request.method == 'GET':
        
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT cid, cname FROM course")
            courses = cursor.fetchall()
            cursor.execute("SELECT sid, sname FROM student")
            students = cursor.fetchall()
        return render(request, 'sc/add.html', {'courses': courses, 'students': students})
    else:
        student_id  = request.POST.get('student_id', '')
        course_id   = request.POST.get('course_id', '')
        score = random.randint(50, 90)
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("CALL sc_add(%s, %s, %s, @flag)", [student_id, course_id, score])
            conn.commit()
            cursor.execute("SELECT @flag")
            flag = cursor.fetchone()
        # print(flag)
        if flag['@flag'] == 0:
            return redirect('/sims/passed/?path=%s' % ('sc_'))
        else:
            return redirect('/sims/failed/?path=%s' % ('sc_'))

def sc_edit(request):
    if request.method == 'GET':
        sid  = request.GET.get('sid', '')
        cid  = request.GET.get('cid', '')
        
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT sid, sname, cid, cname, score FROM student, course, sc WHERE sid=student_id and cid=course_id and sid=%s and cid=%s", [sid, cid])
            sc = cursor.fetchone()
        return render(request, 'sc/edit.html', {'sc': sc})
    else:
        student_id  = request.POST.get('student_id', '')
        course_id   = request.POST.get('course_id', '')
        score       = request.POST.get('score', '')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE sc SET score=%s WHERE student_id=%s and course_id=%s", [score, student_id, course_id])
            conn.commit()
        return redirect('/sims/passed/?path=%s' % ('sc_'))

def sc_delete(request):
    sid = request.GET.get('sid', '')
    cid = request.GET.get('cid', '')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM sc WHERE student_id=%s and course_id=%s", [sid, cid])
        conn.commit()
    return redirect('/sims/passed/?path=%s' % ('sc_'))
