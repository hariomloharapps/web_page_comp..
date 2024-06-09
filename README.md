# web_page_comp..
c5y


def add_teacher(request):
    if 'principal_id' in request.session:
        if request.method == 'POST':
            form = TeacherForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('principal_dashboard')
        else:
            form = TeacherForm()
        return render(request, 'principal/add_teacher.html', {'form': form})
    else:
        return redirect('principal_login')