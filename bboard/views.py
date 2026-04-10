from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.models import User

from bboard.forms import BbForm
from bboard.models import Bb, Rubric

from django.shortcuts import render
from .models import Bb

from django.core.paginator import Paginator

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from bboard.models import IceCream
from bboard.forms import IceCreamForm
from django.shortcuts import render, redirect

TAGS = ["sale", "new", "cheap", "popular"]

def get_rubrics():
    return Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)


def index(request):
    bb_list = Bb.objects.all().order_by('-published')

    paginator = Paginator(bb_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {
        'page_obj': page_obj,
        'rubrics': get_rubrics()
    })

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    current_rubric = get_object_or_404(Rubric, pk=rubric_id)

    return render(request, 'by_rubric.html', {
        'bbs': bbs,
        'rubrics': get_rubrics(),
        'current_rubric': current_rubric
    })


class BbCreateView(CreateView):
    template_name = 'create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_rubrics()
        return context


def select_columns(request):
    bbs = Bb.objects.values('title', 'price')

    return render(request, 'select_columns.html', {
        'bbs': bbs,
        'rubrics': get_rubrics()
    })


def exclude_values(request):
    bbs = Bb.objects.exclude(price=0)

    return render(request, 'exclude_values.html', {
        'bbs': bbs,
        'rubrics': get_rubrics()
    })


def bb_list(request):
    bbs = Bb.objects.all()

    return render(request, 'index.html', {
        'bbs': bbs,
        'rubrics': get_rubrics()
    })


def bb_detail(request, id):
    bb = get_object_or_404(Bb, pk=id)

    return render(request, 'bb_detail.html', {
        'bb': bb,
        'rubrics': get_rubrics()
    })


def bb_delete(request, id):
    bb = get_object_or_404(Bb, pk=id)

    if request.method == "POST":
        bb.delete()
        return redirect('index')

    return render(request, 'bb_confirm_delete.html', {
        'bb': bb,
        'rubrics': get_rubrics()
    })


class UserListView(ListView):
    model = User
    template_name = 'users_list.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_rubrics()
        return context


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_rubrics()
        return context


def tags_demo(request):
        bbs = Bb.objects.all()

        return render(request, 'tags_demo.html', {
            'bbs': bbs
        })

class IceCreamListView(ListView):
    model = IceCream
    template_name = 'icecream/list.html'
    context_object_name = 'icecreams'


class IceCreamCreateView(CreateView):
    model = IceCream
    form_class = IceCreamForm
    template_name = 'icecream/create.html'
    success_url = reverse_lazy('icecream_list')


class IceCreamUpdateView(UpdateView):
    model = IceCream
    form_class = IceCreamForm
    template_name = 'icecream/create.html'
    success_url = reverse_lazy('icecream_list')


class IceCreamDeleteView(DeleteView):
    model = IceCream
    template_name = 'icecream/delete.html'
    success_url = reverse_lazy('icecream_list')

def icecream_create(request):

        if request.method == "GET":
            form = IceCreamForm()
            return render(request, "icecream/create.html", {"form": form})

        form = IceCreamForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("icecream_list")  # успех

        return render(request, "icecream/create.html", {
            "form": form
        })