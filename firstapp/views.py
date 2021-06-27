from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register

# Create your views here.

def home(request):
	return HttpResponse("Hi Good Evening to all....")

def htmltag(req):
	return HttpResponse("<h2>Hi Welcome to APSSDC</h2>")

def usernameprint(req,uname):
	return HttpResponse("<h2>welcome <span style='color:orange'>mr {}</span></h2>".format(uname))

def uage(req,name,age):
	return HttpResponse("<h3 style='text-align:center;background-color:green;padding:23px'>Hi my name is <span style='color:purple'>{}</span> and my age is<span style='color:red'>{}</span></h3>".format(name,age))

def employee(req,eid,ename,eage):
	return HttpResponse("<script>alert('Hi welcome {}')</script><h3>Hi welcome {} and your age is {} and your id is {}</h3>".format(ename,ename,eage,eid))

def html(request):
	return render(request,'html/sample.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})

def nameid(request,id,ename):
	k = {'i':id,'n':ename}
	return render(request,'html/etml.html',k)

def studentdetails(request):
	return render(request,'html/std.html')

def internaljs(request):
	return render(request,'html/internaljs.html')

def myform(req):
	if req.method=="POST":
		#print(req.POST)
		uname = req.POST['uname']
		rollno = req.POST['rollno']
		email = req.POST.get('email')
		data= {'username':uname,'rno':rollno,'emailID':email}
		return render(req,'html/display.html',data)

	return render(req,'html/myform.html')

def teja(request):
	if request.method=="POST":
		#print(request.POST)
		firstname=request.POST['firstname']
		lastname=request.POST['lastname']
		email=request.POST['email']
		number=request.POST['number']
		gender=request.POST['gender']
		Address=request.POST['Address']
		languages=request.POST.getlist('languages')
		result={'firstname':firstname,'lastname':lastname,'emailID':email,'phonenumber':number,'gender':gender,'Address':Address,'languages':languages}
		return render(request,'html/tjdisplay.html',result)
	return render(request,'html/tk.html')

def task(request):
	if request.method=="POST":
		#print(request.POST)
		email=request.POST['email']
		password=request.POST['password']
		logininfo={'email':email,'password':password}
		return render(request,'html/task1.html',logininfo)
	return render(request,'html/login.html')

def bootstrapfun(request):
	return render(request,'html/sampleboot.html')

def tej(request):
	return render(request,'html/tejak.html')

def registration(request):
	#name = "siva"
	#email = "siva@gmail.com"
	reg = Register(name="rasool",email="rasool@gmail.com")
	reg.save()
	return HttpResponse("row inserted successfully")

def registration1(request):
	#print(request.POST)
	if request.method=='POST':
		name = request.POST['name']
		email = request.POST['emailid']
		reg = Register(name=name,email=email)
		reg.save()
		return HttpResponse("inserted successfully")

	return render(request,'html/accregister.html')

def display(request):
	data = Register.objects.all()
	return render(request,'html/display1.html',{'data':data})

def sview(request,y):
	w = Register.objects.get(id=y)
	return render(request,'html/sview.html',{'y':w})
	#return HttpResponse("Your ID is: {} and Your emailid is:{}".format(w.():

def supd(request,q):
	t = Register.objects.get(id=q)
	if request.method=="POST":
		na=request.POST['n']
		em=request.POST['e']
		t.name = na
		t.email = em
		#print(t.name,t.email)
		t.save()
		return redirect('/display')
	return render(request,'html/supdate.html',{'p':t})

def sudl(request,p):
	b = Register.objects.get(id=p)
	if request.method=="POST":
		b.delete()
		return redirect('/display')
	return render(request,'html/sndel.html',{'z':b})