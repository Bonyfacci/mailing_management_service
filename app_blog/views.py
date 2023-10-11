from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from app_blog.models import Blog


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': f'Блог Castellsefels'
    }


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'app_blog/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


# class BlogCreateView(CreateView):
#     model = Blog
#     template_name = 'app_blog/blog_form.html'
#     success_url = reverse_lazy('app_blog:blog_list')


# class BlogUpdateView(UpdateView):
#     model = Blog
#     fields = ('title', 'content', 'photo', 'created_date')
#     template_name = 'app_blog/blog_form.html'
#     success_url = reverse_lazy('app_blog:blog_list')


# class BlogDeleteView(DeleteView):
#     model = Blog
#     template_name = 'app_blog/blog_delete_confirm.html'
#     success_url = reverse_lazy('app_blog:blog_list')


