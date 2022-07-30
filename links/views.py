from django.shortcuts import render, redirect
from .models import Links, Categories
from .forms import LinkForm, CategoryForm
from .models import Categories, Links
from django.views.generic import DetailView, UpdateView, DeleteView

categories = Categories.objects.all()

class LinkDeleteView(DeleteView):
    model = Links
    template_name = 'links/delete_link.html'
    success_url = '/links/'

class LinkUpdateView(UpdateView):
    model = Links
    template_name = 'links/create_link.html'
    form_class = LinkForm

class LinkDetailView(DetailView):
    model = Links
    template_name = 'links/link_details.html'
    context_object_name = 'link'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = categories
        return context

class CategoryDetailView(DetailView):
    model = Categories
    template_name = 'links/link_details.html'
    context_object_name = 'category'


class LinkUpdateView(UpdateView):
    model = Links
    template_name = 'links/create_link.html'
    form_class = LinkForm


def links_home(request):
    links = Links.objects.order_by('sub_category')
    data = {
        'title': 'Links',
        'links': links,
        'categories': categories
    }
    return render(request, 'links/links_home.html', data)


def create_link(request):
    error = ''
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('links_home')
        else:
            error = 'Undesirable data'
    form = LinkForm()
    data = {
        'form': form,
        'title': 'Create a new link',
        'error': error,
        'categories': categories
    }
    return render(request, 'links/create_link.html', data)


def show_category(request, category_id):
    links = Links.objects.filter(category_id=category_id)
    category = Categories.objects.get(id=category_id)

    # if len(links) == 0:
    #     raise Http404()

    context = {
        'links': links,
        'categories': categories,
        'title': category,
        'cat_selected': category_id,
    }

    return render(request, 'links/links_home.html', context=context)
