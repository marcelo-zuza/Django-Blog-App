from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .models import Blog
from .forms import BlogModelForm


class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['posts'] = Blog.objects.order_by('-id').all()
        return context


class BlogViewForm(FormView):
    template_name = 'blogform.html'
    form_class = BlogModelForm
    success_url = reverse_lazy('blog')

    def get_context_data(self, **kwargs):
        form = BlogModelForm
        context = {
            'form': form
        }
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
