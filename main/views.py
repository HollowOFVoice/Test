from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Book
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from users.models import CustomUser


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book_list.html'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'genre', 'condition']
    template_name = 'add_book.html'
    success_url = reverse_lazy('book-list')  # Добавьте эту строку

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

@staff_member_required
def custom_admin_panel(request):
    return render(request, 'admin_panel.html', {
        'users_count': CustomUser.objects.count(),
        'books_count': Book.objects.count(),
        'last_books': Book.objects.order_by('-id')[:5]
    })