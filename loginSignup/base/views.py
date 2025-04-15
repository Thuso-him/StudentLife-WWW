from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReminderForm
from .models import Reminder
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("base:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})

@login_required
def home(request):
    reminders = Reminder.objects.all()

    for reminder in reminders:
        today = timezone.now().date()
        due = reminder.due_date

        if due < today:
            days_overdue = (today - due).days
            if days_overdue > 7:
                reminder.delete()
                continue
            elif days_overdue <= 7:
                reminder.due_color = "overdue"
        else:
            days_left = (due - today).days
            if days_left <= 3:
                reminder.due_color = "urgent"
            elif 4 <= days_left <= 20:
                reminder.due_color = "warning"
            else:
                reminder.due_color = "safe"

    reminders = sorted(reminders, key=lambda x: x.due_date)

    context = {
        "reminders": reminders,
    }
    return render(request, "home.html", context)

@login_required
def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            form.save()
            return redirect('base:home')
    else:
        form = ReminderForm()
    return render(request, 'registration/create_reminder.html', {'form': form})

@login_required
def edit_reminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, id=reminder_id)

    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('base:home')
    else:
        form = ReminderForm(instance=reminder)

    return render(request, 'edit_reminder.html', {'form': form})

def delete_reminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, id=reminder_id)
    if request.method == 'POST':
        reminder.delete()
        return redirect('base:home')



