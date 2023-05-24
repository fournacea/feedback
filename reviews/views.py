from django.shortcuts import render

from django.http import HttpResponseRedirect


# Create your views here.

def review(request):
    if request.method == "POST":
        entered_username = request.POST["username"]
        current_csrf_token = request.POST["csrfmiddlewaretoken"]
        print(f"USERNAME: {entered_username}")
        print(f"CSRF TOKEN: {current_csrf_token}")
        return HttpResponseRedirect("thank-you")
    
    return render(request, "reviews/review.html")

def thank_you(request):
    return render(request, "reviews/thank_you.html")