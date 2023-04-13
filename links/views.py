from django.http import HttpResponseNotFound
from django.urls import reverse_lazy

from main.utils import DataMixin
from .forms import LinkForm
from .models import Categories, Links
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


categories = Categories.objects.all()

class LinkDeleteView(DeleteView):
    model = Links
    template_name = 'links/delete_link.html'
    success_url = '/links/'

class LinkUpdateView(UpdateView):
    model = Links
    template_name = 'links/create_link.html'
    form_class = LinkForm

class LinkDetailView(DataMixin, DetailView):
    model = Links
    template_name = 'links/link_details.html'
    context_object_name = 'link'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Link view")
        context = dict(list(context.items()) + list(c_def.items()))
        context['categories'] = categories
        return context

class LinksHome(DataMixin, ListView):
    model = Links
    template_name = 'links/links_home.html'
    allow_empty = False
    # context_object_name = 'links'
    paginate_by = 12  # how may items per page

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Create, Update and Delete your links')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Links.objects.order_by('sub_category')

# def links_home(request):
#     links = Links.objects.order_by('sub_category')
#     data = {
#         'title': 'Create, Update and Delete your links',
#         'links': links,
#         'categories': categories
#     }
#     return render(request, 'links/links_home.html', data)

class CreateLink(LoginRequiredMixin, DataMixin, CreateView):
    form_class = LinkForm
    template_name = 'links/create_link.html'
    login_url = reverse_lazy('links_home')
    # raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Creat a new link')
        context = dict(list(context.items()) + list(c_def.items()))
        success_url = reverse_lazy('links_home')
        return context

# def create_link(request):
#     error = ''
#     if request.method == 'POST':
#         form = LinkForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('links_home')
#         else:
#             error = 'Undesirable data'
#     form = LinkForm()
#     data = {
#         'form': form,
#         'title': 'Create a new link',
#         'error': error,
#         'categories': categories
#     }
#     return render(request, 'links/create_link.html', data)


class CategoryListView(DataMixin, ListView):
    model = Links
    template_name = 'links/links_home.html'
    allow_empty = False
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(context['object_list'][0].category))
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Links.objects.filter(category_id=self.kwargs['category_id'])

# def show_links_by_category(request, category_id):
#     links = Links.objects.filter(category_id=category_id)
#     category = get_object_or_404(Categories, id=category_id)
#
#     context = {
#         'links': links,
#         'categories': categories,
#         'title': category,
#
#     }
#
#     return render(request, 'links/links_home.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
