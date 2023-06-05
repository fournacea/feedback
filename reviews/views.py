from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


from .forms import ReviewForm

from .models import Review

# Create your views here.

class AddFavoriteReview(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        fav_review = Review.objects.get(pk=review_id)
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


    # def post(self, request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("thank-you")
        
    #     else:
    #         return render(request, "reviews/review.html",{
    #             "form": form
    #         })


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
   
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data= base_query.filter(rating__gt=4)
    #     return data


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context
    


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        context["message2"] = "This works too!"
        return context





    




# def thank_you(request):
#     return render(request, "reviews/thank_you.html")



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

