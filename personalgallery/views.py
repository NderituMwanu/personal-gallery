from django.http import HttpResponse
import datetime as dt
from django.shortcuts import render,redirect


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
    return render(request, 'all-pictures/todays-post.html', {"date": date,})

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
            
    return render(request, 'all-pictures/past-post.html', {"date": date})

    
