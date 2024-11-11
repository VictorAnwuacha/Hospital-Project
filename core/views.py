from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Patient, Doctor, Appointment
from .forms import AppointmentForm
from .models import Notification

# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'core/doctor_list.html', {'doctors': doctors})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'core/doctor_detail.html', {'doctor': doctor})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'core/patient_list.html', {'patients': patients})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'core/patient_detail.html', {'patient': patient})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'core/appointment_list.html', {'appointments': appointments})

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'core/appointment_detail.html', {'appointment': appointment})

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment created successfully!")
            return redirect('core/appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'core/create_appointment.html', {'form': form})

def update_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment updated successfully!")
            return redirect('core/appointment_detail', pk=appointment.pk)
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'core/update_appointment.html', {'form': form, 'appointment': appointment})

def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, "Appointment deleted successfully!")
        return redirect('core/appointment_list')
    return render(request, 'core/delete_appointment.html', {'appointment': appointment})


def notification_list(request, patient_id):
    notifications = Notification.objects.filter(recipient_id=patient_id)
    return render(request, 'core/notification_list.html', {'notifications': notifications})
