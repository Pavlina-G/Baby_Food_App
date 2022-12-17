from django.shortcuts import render, redirect
from django.views import generic as views



class IndexView(views.TemplateView):
    template_name = 'index4.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile home')
        return super(IndexView, self).dispatch(request, *args, **kwargs)

# def index(request):
#     profile = get_profile()
#
#     if profile is None:
#         return render(request, 'index4.html')
#
#     context = {
#         'profile': profile,
#     }
#
#     return render(request, 'profile_home.html', context)
#


    # return render(request, 'index4.html')



def locations_map(request):
    return render(request, 'common/../../templates/nicepage/locations.html')
