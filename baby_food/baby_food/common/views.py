from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import generic as views

from baby_food.common.models import Gallery


class IndexView(views.TemplateView):
    template_name = 'common/home.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile home')
        return super(IndexView, self).dispatch(request, *args, **kwargs)


def locations_map(request):
    return render(request, 'common/locations.html')


class GalleryView(views.TemplateView):
    template_name = 'common/gallery.html'

    def get(self, request, *args, **kwargs):
        paginator = Paginator(Gallery.objects.all().order_by('-upload_date'), 3)
        page = request.GET.get('page')
        paginated_photos = paginator.get_page(page)

        context = super().get_context_data(**kwargs)
        try:
            photos = Gallery.objects.all().order_by('-upload_date')
        except Gallery.DoesNotExist():
            photos = None
        context['photos'] = photos
        context['paginated_photos'] = paginated_photos
        return self.render_to_response(context)



