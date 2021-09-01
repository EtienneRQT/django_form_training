from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(
            request,
            "reviews/review.html",
            {
                "form": form,
            },
        )

    def post(self, request):
        form = ReviewForm(request.POST)


def thank_you(request):
    return render(request, "reviews/thank_you.html")
