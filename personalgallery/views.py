from django.http import HttpResponse
import datetime as dt
from django.shortcuts import render,redirect
from .models import Image, Category, Location

#my views
# def welcome(request):
#     return render(request, 'welcome.html')


def post_time(request):
    date = dt.date.today()

    #function to convert date object to find the exact date
    day = date
    html = f'''
        <html>
            <body>
                <h1> Date: {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''

    return HttpResponse(html)


def post_of_today(request):
    date = dt.date.today()
    post = Image.post_of_today()
    return render(request, 'all-pictures/todays-post.html', {"date": date, "post":post})

def past_day_post(request,past_date):
        # Converts data from the string Url
    
    try:
        # converts data from the string URL
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        #Raise 404 error when ValueError is thrown
        raise Http404()
        assert False


    if date == dt.date.today():
        return redirect(post_of_day)

    post = Image.post_of_day(date)         
    return render(request, 'all-pictures/past-post.html', {"date": date})

    
def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("article")
        searched_images = Article.search_by_location(search_term)
        message = f"{search_term}"

        return render(request, 'all-pictures/search.html',{"message":message,"images": searched_images})

    else:
        message = "Sorry You haven't searched for any term"
        return render(request, 'all-pictures/search.html',{"message":message})


def location(request,location_id):
    gallery = Image.objects.filter(location__name=location_id)
    location = Location.objects.all()
    category= Category.objects.all()

    return render(request,"all-pictures/images.html", {"gallery":gallery,"location":location,'category':category})


def image(request,image_id):
    print('/images')
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "all-pictures/image.html", {"image":image})  

def category_image(request,category_id):
    images=Image.objects.filter(category__name=category_id)
    category= Categorys.objects.all()
    location= Location.objects.all()
    return render(request,'all-pictures/image.html',{'gallery':images,'category':category,'location':location})