from django.http.response import HttpResponse
from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect

# Create your views here.
def home(request):
    'show home page'
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        date = request.POST.get('dob')
        country = request.POST.get('Dropdownmenu')
        question = request.POST.get('question')
        try:
            cursor = connection.cursor()
            sql = 'insert into students values(null, %s,%s,%s,%s,%s,%s)'
            val = (firstname, lastname, email, date,  country, question)
            cursor.execute(sql, val)
            success = ''
            fail = ""
            id = cursor.lastrowid
            if id:
                success = "registraction success"
            else:
                fail = "registraction fail"
            return render(request , 'register.html' ,{'success': success,'fail':fail})
        except Exception as e:
            return render(request , 'register.html' , {'fail': str(e)})
    else:
        return render (request, 'register.html')

def login(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        email = request.POST.get('email')
        cursor=connection.cursor()
        sql="select * from students where firstname = %s and email = %s "
        val = (firstname , email)
        cursor.execute(sql,val)
        record = cursor.fetchall()
        if record:
            request.session['password'] = record[0][3]
            request.session['user_id'] = record[0][0]
            return render (request , 'login.html' , {'successmessage': 'login success '})
        else:
            return render (request,'login.html',{'message':'invalid username or password'})
    else:
        return render(request,'login.html')

