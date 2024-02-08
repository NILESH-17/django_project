from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from .models import Review
from django.contrib import messages
from django.db.models import Avg
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django import db
from django.db import connection
import itertools
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    all_reviews_list = Review.objects.all().order_by('-id')[:5]
    search_list1 =Review.objects.all().order_by('-id')[:1]
    search_list2 =Review.objects.all().order_by('-id')[1:2]
    search_list3 =Review.objects.all().order_by('-id')[2:3]
    search_list4 =Review.objects.all().order_by('-id')[3:4]
    search_list5 =Review.objects.all().order_by('-id')[4:5]
    search_list6 =Review.objects.all().order_by('-id')[5:6]
    return render(request, "base.html", {'all_reviews_list':all_reviews_list,'search_list1':search_list1,'search_list2':search_list2,'search_list3':search_list3,'search_list4':search_list4,'search_list5':search_list5,'search_list6':search_list6})
    #return render(request, "base.html")


#def technology(request): 
    # return response 
 #   all_reviews_list = Review.objects.filter(category='technology')
    #all_reviews_list = Review.objects.all()
  #  return render(request, "technology.html", {'all_reviews_list':all_reviews_list})

def entertainment(request): 
    # return response 
    all_reviews_list = Review.objects.filter(category='entertainment').order_by('rating')[:5]
    posts = Review.objects.all().filter(category='entertainment') # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    rating_reviews_list = Review.objects.filter(category='entertainment').distinct('company')
    cursor = connection.cursor()
    set1 = []
    my_set = cursor.execute("SELECT DISTINCT company FROM myapp_review WHERE category='entertainment' LIMIT 5")
    my_set = cursor.fetchall()
    for i in my_set:
        i = i[0]
        i = i
        set1.append(i)
    myd = {}
    li=[]
    company_name = []
    rating_avg = []
    for i in set1:
        u = cursor.execute(f"SELECT AVG(rating) FROM myapp_review WHERE company='{i}'")
        u = cursor.fetchall()
        listToStr = ' '.join([str(elem) for elem in u])
        listToStr = listToStr[10:11]
        listToStr = int(listToStr)
        myd.update({f"{i}": f"{u}"})
        li.append(listToStr)
        rating_avg.append(listToStr)
        company_name.append(i)
    final_ = []
    for c_name,r_avg in zip(company_name,rating_avg):
        final_.append(f"{c_name} - {r_avg}")

    return render(request, "entertainment.html",{'all_reviews_list':all_reviews_list,'rating_reviews_list':rating_reviews_list,'final_':final_,'page_obj': page_obj})

def medical(request): 
    # return response 
    all_reviews_list = Review.objects.filter(category='medical').order_by('rating')[:5]
    posts = Review.objects.all().filter(category='medical') # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    rating_reviews_list = Review.objects.filter(category='medical').distinct('company')
    cursor = connection.cursor()
    set1 = []
    my_set = cursor.execute("SELECT DISTINCT company FROM myapp_review WHERE category='medical' LIMIT 5")
    my_set = cursor.fetchall()
    for i in my_set:
        i = i[0]
        i = i
        set1.append(i)
    myd = {}
    li=[]
    company_name = []
    rating_avg = []
    for i in set1:
        u = cursor.execute(f"SELECT AVG(rating) FROM myapp_review WHERE company='{i}'")
        u = cursor.fetchall()
        listToStr = ' '.join([str(elem) for elem in u])
        listToStr = listToStr[10:11]
        listToStr = int(listToStr)
        myd.update({f"{i}": f"{u}"})
        li.append(listToStr)
        rating_avg.append(listToStr)
        company_name.append(i)
    final_ = []
    for c_name,r_avg in zip(company_name,rating_avg):
        final_.append(f"{c_name} - {r_avg}")

    return render(request, "medical.html",{'all_reviews_list':all_reviews_list,'rating_reviews_list':rating_reviews_list,'final_':final_,'page_obj': page_obj})


def fashion(request): 
    # return response 
    all_reviews_list = Review.objects.filter(category='fashion').order_by('rating')[:5]
    posts = Review.objects.all().filter(category='fashion') # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    rating_reviews_list = Review.objects.filter(category='fashion').distinct('company')
    cursor = connection.cursor()
    set1 = []
    my_set = cursor.execute("SELECT DISTINCT company FROM myapp_review WHERE category='fashion' LIMIT 5")
    my_set = cursor.fetchall()
    for i in my_set:
        i = i[0]
        i = i
        set1.append(i)
    myd = {}
    li=[]
    company_name = []
    rating_avg = []
    for i in set1:
        u = cursor.execute(f"SELECT AVG(rating) FROM myapp_review WHERE company='{i}'")
        u = cursor.fetchall()
        listToStr = ' '.join([str(elem) for elem in u])
        listToStr = listToStr[10:11]
        listToStr = int(listToStr)
        myd.update({f"{i}": f"{u}"})
        li.append(listToStr)
        rating_avg.append(listToStr)
        company_name.append(i)
    final_ = []
    for c_name,r_avg in zip(company_name,rating_avg):
        final_.append(f"{c_name} - {r_avg}")

    return render(request, "fashion.html",{'all_reviews_list':all_reviews_list,'rating_reviews_list':rating_reviews_list,'final_':final_,'page_obj': page_obj})

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
         
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register')
         
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )
         
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
         
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/register')
     
    # Render the registration page template (GET request)
    return render(request, 'register.html')

def signin(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login')
         
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
         
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/loggedin')
     
    # Render the login page template (GET request)
    return render(request, 'login.html')

#def review(request): 
#    # return response 
#    return render(request, "review.html")
def loggedin(request): 
    # return response 
    all_reviews_list = Review.objects.all()
    search_list1 =Review.objects.all().order_by('-id')[:1]
    search_list2 =Review.objects.all().order_by('-id')[1:2]
    search_list3 =Review.objects.all().order_by('-id')[2:3]
    search_list4 =Review.objects.all().order_by('-id')[3:4]
    search_list5 =Review.objects.all().order_by('-id')[4:5]
    search_list6 =Review.objects.all().order_by('-id')[5:6]
    return render(request, "loggedin.html", {'all_reviews_list':all_reviews_list,'search_list1':search_list1,'search_list2':search_list2,'search_list3':search_list3,'search_list4':search_list4,'search_list5':search_list5,'search_list6':search_list6})

def review(request):
   
    if request.method == "POST":
        username = request.POST['username']
        category = request.POST['category']
        company = request.POST['companyname']
        rating= request.POST['rating']
        rating = int(rating)
        review = request.POST['review']
        newreview = Review(username=username,category=category,company=company,rating=rating,review=review)
        newreview.save()
        messages.success(request, 'Form submission successful')
       
    return render(request, "review.html", {})

def logout(request):
    auth.logout(request)
    return render(request, "base.html")

def all_reviews(request):
    all_reviews_list = Review.objects.all()
    return render(request, "all_reviews.html", {'all_reviews_list':all_reviews_list})

def company_details(request):
    search_list1 =Review.objects.all().order_by('-id')[:1]
    search_list2 =Review.objects.all().order_by('-id')[1:2]
    search_list3 =Review.objects.all().order_by('-id')[2:3]
    search_list4 =Review.objects.all().order_by('-id')[3:4]
    search_list5 =Review.objects.all().order_by('-id')[4:5]
    search_list6 =Review.objects.all().order_by('-id')[5:6]
    return render(request, "company_details.html", {'search_list1':search_list1,'search_list2':search_list2,'search_list3':search_list3,'search_list4':search_list4,'search_list5':search_list5,'search_list6':search_list6})

def index(request):
   reviews_ = Review.objects.all() 
   avg = Review.objects.all().aggregate(Avg('rating'))
   avg = avg['rating__avg'] 
   print(type(avg))
   return render(request, "index.html", {'reviews_':reviews_,'avg':avg})

def index_ent(request):
    if request.method == "GET":
        searched = request.GET['searched']
        search_list_ent =Review.objects.all().filter(company=searched) & Review.objects.filter(category='entertainment')
        my_set = Review.objects.all().filter(company=searched)
        stat = Review.objects.filter(company=searched).aggregate(Avg('rating'))['rating__avg']
        stat = int(stat)
        stat = str(stat)
        stat_ = []
        stat_.append(stat)
        c_name = []
        c_name.append(searched)
        my_set = []
        for c_name,r_avg in zip(c_name,stat_):
            my_set.append(f"{c_name} - {r_avg}")
    return render(request, "index_ent.html", {'search_list_ent':search_list_ent,'my_set':my_set})

def index_(request):
    if request.method == "GET":
        searched = request.GET['searched']
        search_list =Review.objects.all().filter(company=searched)
        my_set = Review.objects.all().filter(company=searched)
        stat = Review.objects.filter(company=searched).aggregate(Avg('rating'))['rating__avg']
        print(stat)
        stat = int(stat)
        stat = str(stat)
        stat_ = []
        stat_.append(stat)
        c_name = []
        c_name.append(searched)
        my_set = []
        for c_name,r_avg in zip(c_name,stat_):
            my_set.append(f"{c_name} - {r_avg}")
    return render(request, "index_.html", {'search_list':search_list,'my_set':my_set})


def technology(request): 
    # return response 
    all_reviews_list = Review.objects.filter(category='technology').order_by('rating')
    posts = Review.objects.all().filter(category='technology') # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    rating_reviews_list = Review.objects.filter(category='technology' ).distinct('company')
    cursor = connection.cursor()
    set1 = []
    my_set = cursor.execute("SELECT DISTINCT company FROM myapp_review WHERE category='technology'  LIMIT 5")
    my_set = cursor.fetchall()
    for i in my_set:
        i = i[0]
        i = i
        set1.append(i)
    myd = {}
    li=[]
    company_name = []
    rating_avg = []
    for i in set1:
        u = cursor.execute(f"SELECT AVG(rating) FROM myapp_review WHERE company='{i}'")
        u = cursor.fetchall()
        listToStr = ' '.join([str(elem) for elem in u])
        listToStr = listToStr[10:11]
        listToStr = int(listToStr)
        myd.update({f"{i}": f"{u}"})
        li.append(listToStr)
        rating_avg.append(listToStr)
        company_name.append(i)
    final_ = []
    for c_name,r_avg in zip(company_name,rating_avg):
        final_.append(f"{c_name} - {r_avg}")

    return render(request, "technology.html",{'all_reviews_list':all_reviews_list,'rating_reviews_list':rating_reviews_list,'final_':final_,'page_obj': page_obj})

    





#https://podcastbuffs.com/wp-content/uploads/2022/12/Build-your-credibility.png
#https://www.consumeraffairs.com/static/img/rebrand/home/home-people-bg-desktop.webp







def automobiles(request): 
    # return response 
    all_reviews_list = Review.objects.filter(category='automobiles').order_by('rating')[:5]
    posts = Review.objects.all().filter(category='automobiles') # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    rating_reviews_list = Review.objects.filter(category='automobiles').distinct('company')
    cursor = connection.cursor()
    set1 = []
    my_set = cursor.execute("SELECT DISTINCT company FROM myapp_review WHERE category='automobiles' LIMIT 5")
    my_set = cursor.fetchall()
    for i in my_set:
        i = i[0]
        i = i
        set1.append(i)
    myd = {}
    li=[]
    company_name = []
    rating_avg = []
    for i in set1:
        u = cursor.execute(f"SELECT AVG(rating) FROM myapp_review WHERE company='{i}'")
        u = cursor.fetchall()
        listToStr = ' '.join([str(elem) for elem in u])
        listToStr = listToStr[10:11]
        listToStr = int(listToStr)
        myd.update({f"{i}": f"{u}"})
        li.append(listToStr)
        rating_avg.append(listToStr)
        company_name.append(i)
    final_ = []
    for c_name,r_avg in zip(company_name,rating_avg):
        final_.append(f"{c_name} - {r_avg}")

    return render(request, "automobiles.html",{'all_reviews_list':all_reviews_list,'rating_reviews_list':rating_reviews_list,'final_':final_,'page_obj': page_obj})


def real_estate(request): 
    # return response 
    all_reviews_list = Review.objects.filter(category='real_estate').order_by('rating')[:5]
    posts = Review.objects.all().filter(category='real_estate') # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    rating_reviews_list = Review.objects.filter(category='real_estate').distinct('company')
    cursor = connection.cursor()
    set1 = []
    my_set = cursor.execute("SELECT DISTINCT company FROM myapp_review WHERE category='real_estate' LIMIT 5")
    my_set = cursor.fetchall()
    for i in my_set:
        i = i[0]
        i = i
        set1.append(i)
    myd = {}
    li=[]
    company_name = []
    rating_avg = []
    for i in set1:
        u = cursor.execute(f"SELECT AVG(rating) FROM myapp_review WHERE company='{i}'")
        u = cursor.fetchall()
        listToStr = ' '.join([str(elem) for elem in u])
        listToStr = listToStr[10:11]
        listToStr = int(listToStr)
        myd.update({f"{i}": f"{u}"})
        li.append(listToStr)
        rating_avg.append(listToStr)
        company_name.append(i)
    final_ = []
    for c_name,r_avg in zip(company_name,rating_avg):
        final_.append(f"{c_name} - {r_avg}")

    return render(request, "real_estate.html",{'all_reviews_list':all_reviews_list,'rating_reviews_list':rating_reviews_list,'final_':final_,'page_obj': page_obj})

def travel(request): 
    # return response 
    all_reviews_list = Review.objects.filter(category='travel').order_by('rating')[:5]
    posts = Review.objects.all().filter(category='travel') # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    rating_reviews_list = Review.objects.filter(category='travel').distinct('company')
    cursor = connection.cursor()
    set1 = []
    my_set = cursor.execute("SELECT DISTINCT company FROM myapp_review WHERE category='travel' LIMIT 5")
    my_set = cursor.fetchall()
    for i in my_set:
        i = i[0]
        i = i
        set1.append(i)
    myd = {}
    li=[]
    company_name = []
    rating_avg = []
    for i in set1:
        u = cursor.execute(f"SELECT AVG(rating) FROM myapp_review WHERE company='{i}'")
        u = cursor.fetchall()
        listToStr = ' '.join([str(elem) for elem in u])
        listToStr = listToStr[10:11]
        listToStr = int(listToStr)
        myd.update({f"{i}": f"{u}"})
        li.append(listToStr)
        rating_avg.append(listToStr)
        company_name.append(i)
    final_ = []
    for c_name,r_avg in zip(company_name,rating_avg):
        final_.append(f"{c_name} - {r_avg}")

    return render(request, "travel.html",{'all_reviews_list':all_reviews_list,'rating_reviews_list':rating_reviews_list,'final_':final_,'page_obj': page_obj})

def fianance(request): 
    # return response 
    all_reviews_list = Review.objects.filter(category='fianance').order_by('rating')[:5]
    posts = Review.objects.all().filter(category='fianance') # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    rating_reviews_list = Review.objects.filter(category='fianance').distinct('company')
    cursor = connection.cursor()
    set1 = []
    my_set = cursor.execute("SELECT DISTINCT company FROM myapp_review WHERE category='fianance' LIMIT 5")
    my_set = cursor.fetchall()
    for i in my_set:
        i = i[0]
        i = i
        set1.append(i)
    myd = {}
    li=[]
    company_name = []
    rating_avg = []
    for i in set1:
        u = cursor.execute(f"SELECT AVG(rating) FROM myapp_review WHERE company='{i}'")
        u = cursor.fetchall()
        listToStr = ' '.join([str(elem) for elem in u])
        listToStr = listToStr[10:11]
        listToStr = int(listToStr)
        myd.update({f"{i}": f"{u}"})
        li.append(listToStr)
        rating_avg.append(listToStr)
        company_name.append(i)
    final_ = []
    for c_name,r_avg in zip(company_name,rating_avg):
        final_.append(f"{c_name} - {r_avg}")

    return render(request, "fianance.html",{'all_reviews_list':all_reviews_list,'rating_reviews_list':rating_reviews_list,'final_':final_,'page_obj': page_obj})

def food(request): 
    # return response 
    all_reviews_list = Review.objects.filter(category='food').order_by('rating')[:5]
    posts = Review.objects.all().filter(category='food') # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    rating_reviews_list = Review.objects.filter(category='food').distinct('company')
    cursor = connection.cursor()
    set1 = []
    my_set = cursor.execute("SELECT DISTINCT company FROM myapp_review WHERE category='food' LIMIT 5")
    my_set = cursor.fetchall()
    for i in my_set:
        i = i[0]
        i = i
        set1.append(i)
    myd = {}
    li=[]
    company_name = []
    rating_avg = []
    for i in set1:
        u = cursor.execute(f"SELECT AVG(rating) FROM myapp_review WHERE company='{i}'")
        u = cursor.fetchall()
        listToStr = ' '.join([str(elem) for elem in u])
        listToStr = listToStr[10:11]
        listToStr = int(listToStr)
        myd.update({f"{i}": f"{u}"})
        li.append(listToStr)
        rating_avg.append(listToStr)
        company_name.append(i)
    final_ = []
    for c_name,r_avg in zip(company_name,rating_avg):
        final_.append(f"{c_name} - {r_avg}")

    return render(request, "food.html",{'all_reviews_list':all_reviews_list,'rating_reviews_list':rating_reviews_list,'final_':final_,'page_obj': page_obj})

def education(request): 
    # return response 
    all_reviews_list = Review.objects.filter(category='education').order_by('rating')[:5]
    posts = Review.objects.all().filter(category='education') # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    rating_reviews_list = Review.objects.filter(category='education').distinct('company')
    cursor = connection.cursor()
    set1 = []
    my_set = cursor.execute("SELECT DISTINCT company FROM myapp_review WHERE category='education' LIMIT 5")
    my_set = cursor.fetchall()
    for i in my_set:
        i = i[0]
        i = i
        set1.append(i)
    myd = {}
    li=[]
    company_name = []
    rating_avg = []
    for i in set1:
        u = cursor.execute(f"SELECT AVG(rating) FROM myapp_review WHERE company='{i}'")
        u = cursor.fetchall()
        listToStr = ' '.join([str(elem) for elem in u])
        listToStr = listToStr[10:11]
        listToStr = int(listToStr)
        myd.update({f"{i}": f"{u}"})
        li.append(listToStr)
        rating_avg.append(listToStr)
        company_name.append(i)
    final_ = []
    for c_name,r_avg in zip(company_name,rating_avg):
        final_.append(f"{c_name} - {r_avg}")

    return render(request, "education.html",{'all_reviews_list':all_reviews_list,'rating_reviews_list':rating_reviews_list,'final_':final_,'page_obj': page_obj})

def other(request): 
    # return response 
    all_reviews_list = Review.objects.filter(category='other').order_by('rating')[:5]
    posts = Review.objects.all().filter(category='other') # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    rating_reviews_list = Review.objects.filter(category='other').distinct('company')
    cursor = connection.cursor()
    set1 = []
    my_set = cursor.execute("SELECT DISTINCT company FROM myapp_review WHERE category='other' LIMIT 5")
    my_set = cursor.fetchall()
    for i in my_set:
        i = i[0]
        i = i
        set1.append(i)
    myd = {}
    li=[]
    company_name = []
    rating_avg = []
    for i in set1:
        u = cursor.execute(f"SELECT AVG(rating) FROM myapp_review WHERE company='{i}'")
        u = cursor.fetchall()
        listToStr = ' '.join([str(elem) for elem in u])
        listToStr = listToStr[10:11]
        listToStr = int(listToStr)
        myd.update({f"{i}": f"{u}"})
        li.append(listToStr)
        rating_avg.append(listToStr)
        company_name.append(i)
    final_ = []
    for c_name,r_avg in zip(company_name,rating_avg):
        final_.append(f"{c_name} - {r_avg}")

    return render(request, "other.html",{'all_reviews_list':all_reviews_list,'rating_reviews_list':rating_reviews_list,'final_':final_,'page_obj': page_obj})


def index_cos(request):
    if request.method == "GET":
        searched = request.GET['searched']
        search_list_ent =Review.objects.all().filter(company=searched) & Review.objects.filter(category='cosmetics')
        my_set = Review.objects.all().filter(company=searched)
        stat = Review.objects.filter(company=searched).aggregate(Avg('rating'))['rating__avg']
        stat = int(stat)
        stat = str(stat)
        stat_ = []
        stat_.append(stat)
        c_name = []
        c_name.append(searched)
        my_set = []
        for c_name,r_avg in zip(c_name,stat_):
            my_set.append(f"{c_name} - {r_avg}")
    return render(request, "index_cos.html", {'search_list_ent':search_list_ent,'my_set':my_set})


def index_real_estate(request):
    if request.method == "GET":
        searched = request.GET['searched']
        search_list_ent =Review.objects.all().filter(company=searched) & Review.objects.filter(category='real_estate')
        my_set = Review.objects.all().filter(company=searched)
        stat = Review.objects.filter(company=searched).aggregate(Avg('rating'))['rating__avg']
        stat = int(stat)
        stat = str(stat)
        stat_ = []
        stat_.append(stat)
        c_name = []
        c_name.append(searched)
        my_set = []
        for c_name,r_avg in zip(c_name,stat_):
            my_set.append(f"{c_name} - {r_avg}")
    return render(request, "index_real_estate.html", {'search_list_ent':search_list_ent,'my_set':my_set})

def index_fianance(request):
    if request.method == "GET":
        searched = request.GET['searched']
        search_list_ent =Review.objects.all().filter(company=searched) & Review.objects.filter(category='fianance')
        my_set = Review.objects.all().filter(company=searched)
        stat = Review.objects.filter(company=searched).aggregate(Avg('rating'))['rating__avg']
        stat = int(stat)
        stat = str(stat)
        stat_ = []
        stat_.append(stat)
        c_name = []
        c_name.append(searched)
        my_set = []
        for c_name,r_avg in zip(c_name,stat_):
            my_set.append(f"{c_name} - {r_avg}")
    return render(request, "index_fianance.html", {'search_list_ent':search_list_ent,'my_set':my_set})

def index_food(request):
    if request.method == "GET":
        searched = request.GET['searched']
        search_list_ent =Review.objects.all().filter(company=searched) & Review.objects.filter(category='food')
        my_set = Review.objects.all().filter(company=searched)
        stat = Review.objects.filter(company=searched).aggregate(Avg('rating'))['rating__avg']
        stat = int(stat)
        stat = str(stat)
        stat_ = []
        stat_.append(stat)
        c_name = []
        c_name.append(searched)
        my_set = []
        for c_name,r_avg in zip(c_name,stat_):
            my_set.append(f"{c_name} - {r_avg}")
    return render(request, "index_food.html", {'search_list_ent':search_list_ent,'my_set':my_set})

def index_education(request):
    if request.method == "GET":
        searched = request.GET['searched']
        search_list_ent =Review.objects.all().filter(company=searched) & Review.objects.filter(category='education')
        my_set = Review.objects.all().filter(company=searched)
        stat = Review.objects.filter(company=searched).aggregate(Avg('rating'))['rating__avg']
        stat = int(stat)
        stat = str(stat)
        stat_ = []
        stat_.append(stat)
        c_name = []
        c_name.append(searched)
        my_set = []
        for c_name,r_avg in zip(c_name,stat_):
            my_set.append(f"{c_name} - {r_avg}")
    return render(request, "index_education.html", {'search_list_ent':search_list_ent,'my_set':my_set})

def index_other(request):
    if request.method == "GET":
        searched = request.GET['searched']
        search_list_ent =Review.objects.all().filter(company=searched) & Review.objects.filter(category='other')
        my_set = Review.objects.all().filter(company=searched)
        stat = Review.objects.filter(company=searched).aggregate(Avg('rating'))['rating__avg']
        stat = int(stat)
        stat = str(stat)
        stat_ = []
        stat_.append(stat)
        c_name = []
        c_name.append(searched)
        my_set = []
        for c_name,r_avg in zip(c_name,stat_):
            my_set.append(f"{c_name} - {r_avg}")
    return render(request, "index_other.html", {'search_list_ent':search_list_ent,'my_set':my_set})









def cosmetics(request): 
    # return response 
    all_reviews_list = Review.objects.filter(category='cosmetics').order_by('rating')[:5]
    posts = Review.objects.all().filter(category='cosmetics') # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    rating_reviews_list = Review.objects.filter(category='cosmetics').distinct('company')
    cursor = connection.cursor()
    set1 = []
    my_set = cursor.execute("SELECT DISTINCT company FROM myapp_review WHERE category='cosmetics' LIMIT 5")
    my_set = cursor.fetchall()
    for i in my_set:
        i = i[0]
        i = i
        set1.append(i)
    myd = {}
    li=[]
    company_name = []
    rating_avg = []
    for i in set1:
        u = cursor.execute(f"SELECT AVG(rating) FROM myapp_review WHERE company='{i}'")
        u = cursor.fetchall()
        listToStr = ' '.join([str(elem) for elem in u])
        listToStr = listToStr[10:11]
        listToStr = int(listToStr)
        myd.update({f"{i}": f"{u}"})
        li.append(listToStr)
        rating_avg.append(listToStr)
        company_name.append(i)
    final_ = []
    for c_name,r_avg in zip(company_name,rating_avg):
        final_.append(f"{c_name} - {r_avg}")

    return render(request, "cosmetics.html",{'all_reviews_list':all_reviews_list,'rating_reviews_list':rating_reviews_list,'final_':final_,'page_obj': page_obj})


def index_aut(request):
    if request.method == "GET":
        searched = request.GET['searched']
        search_list_ent =Review.objects.all().filter(company=searched) & Review.objects.filter(category='automobiles')
        my_set = Review.objects.all().filter(company=searched)
        stat = Review.objects.filter(company=searched).aggregate(Avg('rating'))['rating__avg']
        stat = int(stat)
        stat = str(stat)
        stat_ = []
        stat_.append(stat)
        c_name = []
        c_name.append(searched)
        my_set = []
        for c_name,r_avg in zip(c_name,stat_):
            my_set.append(f"{c_name} - {r_avg}")
    return render(request, "index_aut.html", {'search_list_ent':search_list_ent,'my_set':my_set})

def index_tech(request):
    if request.method == "GET":
        searched = request.GET['searched']
        search_list_ent =Review.objects.all().filter(company=searched) & Review.objects.filter(category='technology')
        my_set = Review.objects.all().filter(company=searched)
        stat = Review.objects.filter(company=searched).aggregate(Avg('rating'))['rating__avg']
        stat = int(stat)
        stat = str(stat)
        stat_ = []
        stat_.append(stat)
        c_name = []
        c_name.append(searched)
        my_set = []
        for c_name,r_avg in zip(c_name,stat_):
            my_set.append(f"{c_name} - {r_avg}")
    return render(request, "index_tech.html", {'search_list_ent':search_list_ent,'my_set':my_set})


def index_med(request):
    if request.method == "GET":
        searched = request.GET['searched']
        search_list_ent =Review.objects.all().filter(company=searched) & Review.objects.filter(category='medical')
        my_set = Review.objects.all().filter(company=searched)
        stat = Review.objects.filter(company=searched).aggregate(Avg('rating'))['rating__avg']
        stat = int(stat)
        stat = str(stat)
        stat_ = []
        stat_.append(stat)
        c_name = []
        c_name.append(searched)
        my_set = []
        for c_name,r_avg in zip(c_name,stat_):
            my_set.append(f"{c_name} - {r_avg}")
    return render(request, "index_med.html", {'search_list_ent':search_list_ent,'my_set':my_set})

def index_fashion(request):
    if request.method == "GET":
        searched = request.GET['searched']
        search_list_ent =Review.objects.all().filter(company=searched) & Review.objects.filter(category='fashion')
        my_set = Review.objects.all().filter(company=searched)
        stat = Review.objects.filter(company=searched).aggregate(Avg('rating'))['rating__avg']
        stat = int(stat)
        stat = str(stat)
        stat_ = []
        stat_.append(stat)
        c_name = []
        c_name.append(searched)
        my_set = []
        for c_name,r_avg in zip(c_name,stat_):
            my_set.append(f"{c_name} - {r_avg}")
    return render(request, "index_fashion.html", {'search_list_ent':search_list_ent,'my_set':my_set})

def index_cos(request):
    if request.method == "GET":
        searched = request.GET['searched']
        search_list_ent =Review.objects.all().filter(company=searched) & Review.objects.filter(category='cosmetics')
        my_set = Review.objects.all().filter(company=searched)
        stat = Review.objects.filter(company=searched).aggregate(Avg('rating'))['rating__avg']
        stat = int(stat)
        stat = str(stat)
        stat_ = []
        stat_.append(stat)
        c_name = []
        c_name.append(searched)
        my_set = []
        for c_name,r_avg in zip(c_name,stat_):
            my_set.append(f"{c_name} - {r_avg}")
    return render(request, "index_cos.html", {'search_list_ent':search_list_ent,'my_set':my_set})


def index_travel(request):
    if request.method == "GET":
        searched = request.GET['searched']
        search_list_ent =Review.objects.all().filter(company=searched) & Review.objects.filter(category='travel')
        my_set = Review.objects.all().filter(company=searched)
        stat = Review.objects.filter(company=searched).aggregate(Avg('rating'))['rating__avg']
        stat = int(stat)
        stat = str(stat)
        stat_ = []
        stat_.append(stat)
        c_name = []
        c_name.append(searched)
        my_set = []
        for c_name,r_avg in zip(c_name,stat_):
            my_set.append(f"{c_name} - {r_avg}")
    return render(request, "index_travel.html", {'search_list_ent':search_list_ent,'my_set':my_set})

