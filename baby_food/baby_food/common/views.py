from django.shortcuts import render, redirect
from django.views import generic as views



class IndexView(views.TemplateView):
    template_name = 'common/home.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile home')
        return super(IndexView, self).dispatch(request, *args, **kwargs)


def locations_map(request):
    return render(request, 'common/../../templates/nicepage/locations.html')

class GalleryView(views.TemplateView):
    template_name = 'common/gallery.html'
