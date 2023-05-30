from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm

from .models import Review

# Create your views here.

def review(request):
    ##-- To update instead of create new review --##
    # if request.method == "POST":
    # existing_data = Review.objects.get(pk=4)
    # form = ReviewForm(request.POST, instance=existing_data)

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("thank-you")
        
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html",{
        "form": form
    })

def thank_you(request):
    return render(request, "reviews/thank_you.html")