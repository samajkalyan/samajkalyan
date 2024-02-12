from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FormData
import uuid
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def home(request):
    if request.method == 'POST':
        # Extract form data
        salutation = request.POST.get('salutation')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        taluka = request.POST.get('taluka')
        district = request.POST.get('district')
        postal_code = request.POST.get('postal_code')
        age = request.POST.get('age')
        contact = request.POST.get('contact')
        whatsapp_no = request.POST.get('whatsapp_no')
        num_family_members = request.POST.get('num_family_members')
        aadhar_no = request.POST.get('aadhar_no')
        Type_of_members = request.POST.get('Type_of_members')

        # Generate unique ID and serial number
        unique_id = uuid.uuid4().hex[:6].upper()
        serial_no = FormData.objects.count() + 1

        # Save data to the database
        profile = FormData.objects.create(
            unique_id=unique_id,
            serial_no=serial_no,
            first_name=first_name,
            salutation=salutation,
            middle_name=middle_name,
            last_name=last_name,
            address=address,
            taluka=taluka,
            district=district,
            postal_code=postal_code,
            age=age,
            contact=contact,
            whatsapp_no=whatsapp_no,
            num_family_members=num_family_members,
            aadhar_no=aadhar_no,
            Type_of_members=Type_of_members,
        )
        profile.save()

        # Append data to Google Sheets
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials/vskp-data-968e6fd53b63.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open('VSKP').sheet1  # Change to your sheet name
        row = [salutation, first_name, middle_name, last_name, address, taluka, district, postal_code, age, contact, whatsapp_no, num_family_members, aadhar_no, Type_of_members]
        sheet.append_row(row)

        # Success message
        messages.success(request, 'Profile created successfully')

        # Redirect to profile page
        return redirect('modal', unique_id)

    return render(request, 'create_profile.html')



def profile(request,unique_id):
    profile = FormData.objects.filter(unique_id=unique_id)
    return render(request,'profile.html',{'profile':profile})


def modal(request,unique_id):
    profile = FormData.objects.filter(unique_id=unique_id)
    return render(request,'modal.html',{'profile':profile})