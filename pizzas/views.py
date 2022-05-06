from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Pizza
from django.contrib.auth.decorators import login_required 


# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

#@login_required
def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
   
    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html', context)

#@login_required 
def pizza(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    toppings = pizza.topping_set.all()
    
    comments = pizza.comment_set.all().order_by('-date_added')

    context = {'pizza':pizza, 'toppings':toppings, 'comments':comments}

    return render(request, 'pizzas/pizza.html', context)

#@login_required 
def new_comment(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            #new_comment.owner = request.user
            new_comment.save()

            return redirect('pizzas:pizza', pizza_id=pizza_id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/new_comment.html',context)