from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request,'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(
                        username = request.POST['username'],
                        password = request.POST['password1'])
                    user.save()
                    login(request,user)
                    return redirect('tasks')
                except IntegrityError:
                    return render(request,'signup.html', {
                            'form': UserCreationForm,
                            'error': 'User already exists'
                    })
        return render(request,'signup.html', {
                     'form': UserCreationForm,
                    'error': 'Password do not match'
        })
