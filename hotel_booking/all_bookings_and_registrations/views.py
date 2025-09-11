from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Member, Teachers  # Import both models
from django.db import transaction
import html
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.db import IntegrityError
from .models import (
    Teachers, Member, Properties, Users, Districts, 
    PropertyCategories, PropertyPictures, Excursions,
    PropertyRoomCategories
)

def home(request):
  if request.method == 'POST':  
    title = request.POST.get('title', '').strip()
    short_description = request.POST.get('short_description', '').strip()
    long_description = request.POST.get('long_description', '').strip()
    property_category = request.POST.get('property_category', '').strip()
    address = request.POST.get('address', '').strip()
    GoogleMapPin = request.POST.get('GoogleMapPin', '').strip()
   
    new_hotel = Properties.objects.create(
        title=title,
        short_description=short_description,
        long_description=long_description,
        property_category=property_category,
        address=address,
        districtid=1,  # Default district ID; modify as needed
        defaultpictureid = '1000',  # Default picture ID; modify as needed
        googlemappin=GoogleMapPin,
        verified='No',
        verifiedby='',  
        verifiedtimestamp='',
        verifiednotes='',
        enabled='Yes',
        nextverification='',

    )
    
  
  return render(request, 'home.html')




def hotel_registration(request):
  return render(request, 'hotel_registration.html')



   
    
















# # 01) Insert data into table
#     # Teachers.objects.create(
#     #     reg_no=10,
#     #     name='nimal',
#     #     address='horana',
#     #     gender='male',
#     #     salary=20000,
#     #     subject="ICT"
#     # )

#     # 02) Database එකේ සියලුම විස්තර දර්ශනය කිරීම
#     Teachers_Table = Teachers.objects.all()

#     # 03) හොරණ ජිවත් වන ගුරුවරුන්ගේ, ගුරු අංකය හා විෂය ලබා ගැනීම
#     horana_teachers = Teachers.objects.filter(address='horana').values('reg_no', 'subject', 'name')

#     # 04) ගම්පහ නොවන වෙනත් ප්‍රදේශ වල ජිවත් වන ගුරුවරුන්ගේ නම හා ලිපිනය තෝරා ගැනීම
#     non_gampaha_teachers = Teachers.objects.exclude(address='gampaha').values('name', 'address')
    
#     # 05) වැටුප 25,000 ට වැඩි ගුරුවරුන්ගේ, ගුරු අංකය, නම, විෂය හා වැටුප තේරීම
#     high_salary_teachers = Teachers.objects.filter(salary__gt=25000).values('reg_no', 'name', 'subject', 'salary')

#     # 06) kaluගේ ලිපිනය කළුතර බවට වෙනස් කිරීම
#     try:
#         teacher = Teachers.objects.get(name='kalu')
#         teacher.address = 'kaluthara'
#         teacher.save()
#         update_status = "Updated successfully"
#     except Teachers.DoesNotExist:
#         update_status = "Teacher 'kalu' not found"

#     # 07) වැටුප 25,000ට අඩු ගුරුවරුන්ගේ සියලුම දත්ත මැකීම
#     teachers_to_delete = Teachers.objects.filter(salary__lt=25000).delete()
    