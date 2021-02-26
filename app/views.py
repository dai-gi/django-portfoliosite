from django.views.generic import View
from django.shortcuts import render
from .models import Profile


class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.order_by("-id")
        return render(request, 'app/index.html', {
            'profile_data': profile_data,
        })