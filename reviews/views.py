from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

from .forms import ReviewForm

# from .models import Review

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html",{
            "form": form
        })


    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("thank-you")
        
        else:
            return render(request, "reviews/review.html",{
                "form": form
            })


def thank_you(request):
    return render(request, "reviews/thank_you.html")



# def review(request):
#     ##-- To update instead of create new review --##
#     # if request.method == "POST":
#     # existing_data = Review.objects.get(pk=4)
#     # form = ReviewForm(request.POST, instance=existing_data)

#     if request.method == "POST":
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("thank-you")
        
#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html",{
#         "form": form
#     })

