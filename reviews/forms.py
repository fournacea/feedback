from django import forms

from .models import Review
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name:", max_length=100, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Name must be less than 100 characters",
#     })

#     review_text = forms.CharField(label="Feedback:", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Rating:", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            "user_name": "Name:",
            "review_text": "Feedback:",
            "rating": "Rating:",

        }

        error_messages = {
            "user_name": {
                "required": "Your name must not be empty",
                "max_length": "Name must be less than 100 characters",
            }

        }