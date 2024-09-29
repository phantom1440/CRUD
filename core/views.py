from django.shortcuts import render, HttpResponse, redirect
from .models import Info

def main(request):

    if request.method == 'POST':

        f_name = request.POST['f_name']
        m_name = request.POST['m_name']
        l_name = request.POST['l_name']
        age = request.POST['age']
        gender = request.POST['gender']

        full_name = ''

        if m_name == '':
            full_name = f_name + ' ' + l_name
        else:
            full_name = f'{f_name} {m_name[0]}. {l_name}'

        if gender == '':
            return "Please select a gender"

        if m_name == '':
            user = Info(f_name = f_name, l_name = l_name, full_name = full_name, age = age, gender=gender)
            user.save()
        else:
            user = Info(f_name = f_name, m_name = m_name, l_name = l_name, full_name = full_name, age = age, gender=gender)
            user.save()
        
        return redirect('main')    
    else:
        users = Info.objects.all()
        return render(request, 'index.html', {'users': users})


def delete(request, pk):

    user = Info.objects.get(pk=pk)
    user.delete()

    return redirect('main')


def update(request, pk):

    user = Info.objects.get(pk=pk)

    if request.method == 'POST':

        f_name = request.POST['first']
        m_name = request.POST['middle']
        l_name = request.POST['last']
        age = request.POST['age']
        gender = request.POST['gender']

        full_name = ''

        if m_name == '':
            full_name = f'{f_name} {l_name}'
        else:
            full_name = f'{f_name} {m_name[0]}. {l_name}'

        user.f_name = f_name
        user.m_name = m_name
        user.l_name = l_name
        user.full_name = full_name
        user.age = age
        user.gender = gender

        user.save()

        return redirect('main')

    else:
        f_name = user.f_name 
        m_name = user.m_name 
        l_name = user.l_name
        full_name = user.full_name
        age = user.age 
        gender = user.gender 

        return render(request, 'update.html', {
            'pk': user.id,
            'f_name': f_name,
            'm_name': m_name,
            'l_name': l_name,
            'full_name': full_name,
            'age': age,
            'gender': gender
        })


