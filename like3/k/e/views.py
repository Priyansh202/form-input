from django.shortcuts import render, redirect
from .forms import ExampleForm
from .models import MyModel

def example_view(request):
    count_1 = MyModel.objects.first().count_1
    count_2= MyModel.objects.first().count_2
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            selected_option = form.cleaned_data['select_field']
            if selected_option == 'option1':
                # Do something for option 1
                # ...
                count_1 += 1
                MyModel.objects.update(count_1=count_1)
                
            elif selected_option == 'option2':
                # Do something for option 2
                # ...
                count_2 += 1
                MyModel.objects.update(count_2=count_2)
    else:
        form = ExampleForm()

   
    return render(request, 'e/base.html', {'form':form, 'count_1':count_1,'count_2':count_2})
    