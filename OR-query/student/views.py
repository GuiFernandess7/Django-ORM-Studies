from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q

# Part 2 - OR
#################################################################
def student_list_(request):

    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)
    print(request)

    return render(request, 'output.html',{'posts':posts})

def student_list_(request):
    posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(surname__startswith='baldwin')

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list_(request):
    posts = Student.objects.filter(Q(surname__startswith='austin') | ~Q (surname__startswith='baldwin') | Q (surname__startswith='avery-parker'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

# Part 3 - AND
#####################

def student_list_(request):
    posts = (Student.objects.filter(classroom=1) &
            Student.objects.filter(age=20))
    
    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list_(request):
    posts = Student.objects.filter(Q(surname__startswith='baldwin') &
                                   Q(firstname__startswith='lakisha'))
    
    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts':posts})

# Part 4 - UNION
#####################

def student_list(request):

    posts = Student.objects.all().values("firstname").union(
        Teacher.objects.all().values("firstname")
    )

    print(posts)
    print(connection.queries)
    return render(request, 'output.html', {'posts':posts})

# Part 5 - NOT
#####################

def student_list_(request):

    posts = (Student.objects.exclude(age__gt=20) # greater than 20
    & Student.objects.exclude(firstname__startswith="raquel"))
    
    print(posts)
    print(connection.queries)
    return render(request, 'output.html', {'posts':posts})

# or

def student_list_(request):
    
    posts = Student.objects.filter(~Q(age__gt=20)&~Q(surname__startswith='baldwin'))
    print(posts)
    print(connection.queries)
    return render(request, 'output.html', {'posts':posts})

# Part 6 - Select and Output individual fields
######################

def student_list_(request):

    posts = Student.objects.filter(classroom=1).only
    ('firstname', 'age')

    print(posts)
    print(connection.queries)
    return render(request, 'output.html', {'data':posts})

# Part 7 - Bypassing ORM using raw method
######################

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def student_list(request):

    posts = Student.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM student_student")
    r = dictfetchall(cursor)
    print(r)

    return render(request, "output.html", {'data': r})
