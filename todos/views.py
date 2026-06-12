from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Todo, Category
from .forms import TodoForm, CategoryForm, SignUpForm, LoginForm


# ---------------- AUTH VIEWS ----------------

def register_view(request):
    if request.user.is_authenticated:
        return redirect('todo_list')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully! Welcome.")
            return redirect('todo_list')
    else:
        form = SignUpForm()
    return render(request, 'todos/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('todo_list')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo_list')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'todos/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')


# ---------------- TODO VIEWS ----------------

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)

    # Filters
    status = request.GET.get('status', '')
    priority = request.GET.get('priority', '')
    category_id = request.GET.get('category', '')
    search = request.GET.get('search', '')

    if status == 'completed':
        todos = todos.filter(completed=True)
    elif status == 'pending':
        todos = todos.filter(completed=False)

    if priority:
        todos = todos.filter(priority=priority)

    if category_id:
        todos = todos.filter(category_id=category_id)

    if search:
        todos = todos.filter(Q(title__icontains=search) | Q(description__icontains=search))

    categories = Category.objects.filter(user=request.user)

    total = Todo.objects.filter(user=request.user).count()
    completed_count = Todo.objects.filter(user=request.user, completed=True).count()
    pending_count = total - completed_count

    context = {
        'todos': todos,
        'categories': categories,
        'status': status,
        'priority': priority,
        'category_id': category_id,
        'search': search,
        'total': total,
        'completed_count': completed_count,
        'pending_count': pending_count,
    }
    return render(request, 'todos/todo_list.html', context)


@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, user=request.user)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, "Task added successfully!")
            return redirect('todo_list')
    else:
        form = TodoForm(user=request.user)
    return render(request, 'todos/todo_form.html', {'form': form, 'title': 'Add Task'})


@login_required
def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo, user=request.user)
    return render(request, 'todos/todo_form.html', {'form': form, 'title': 'Edit Task'})


@login_required
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, "Task deleted.")
        return redirect('todo_list')
    return render(request, 'todos/todo_confirm_delete.html', {'todo': todo})


@login_required
def toggle_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')


# ---------------- CATEGORY VIEWS ----------------

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, "Category added!")
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'todos/category_list.html', {'categories': categories, 'form': form})


@login_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        category.delete()
        messages.success(request, "Category deleted.")
        return redirect('category_list')
    return render(request, 'todos/category_confirm_delete.html', {'category': category})
