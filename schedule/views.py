from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from schedule.forms import ScheduleForm
from schedule.models import Schedule
# Create your views here.


def diary(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ScheduleForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    schedules = Schedule.objects.all()
    return render(request, "show.html", {'schedules': schedules})


def edit(request, id):
    schedule = Schedule.objects.get(id=id)
    return render(request, 'edit.html', {'schedule': schedule})


def update(request, id):
    schedule = Schedule.objects.get(id=id)
    form = ScheduleForm(request.POST, instance=schedule)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'schedule': schedule})


def destroy(request, id):
    schedule = Schedule.objects.get(id=id)
    schedule.delete()
    return redirect("/show")
