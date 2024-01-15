from django.shortcuts import render
from admin_master.models import AcademicClass,AcademicQualification,AcademicDivision,AcademicDepartment,AcademicDesignation,AcademicEmployeeCategory,AcademicSubject
from .models import adminemp,empdesig,empdpt,salary,scd
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json
import qrcode
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


# Create your views here.
def employee_register(request):
    qualification_data=AcademicQualification.objects.filter(is_active=True)
    designation_data=AcademicDesignation.objects.filter(is_active=True)
    department_data=AcademicDepartment.objects.filter(is_active=True)
    employee_data=AcademicEmployeeCategory.objects.filter(is_active=True)
    class_data=AcademicClass.objects.filter(is_enabled=True)
    division_data=AcademicDivision.objects.filter(is_active=True)
    subject_data=AcademicSubject.objects.filter(is_active=True)


    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        dob = request.POST.get('dob')
        department = request.POST.get('department')
        jdate = request.POST.get('jdate')

        qr_data = f"Name: {fname} {lname}\nDOB: {dob}\nDepartment: {department}\nJoin Date: {jdate}"

        # Generate QR code image
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image to a BytesIO object
        qr_image_io = BytesIO()
        img.save(qr_image_io, format='PNG')
        qr_image_io.seek(0)

        # Create an InMemoryUploadedFile from BytesIO
        qr_image = InMemoryUploadedFile(
            file=qr_image_io,
            field_name=None,
            name=f'qr_code_{fname}_{lname}.png',
            content_type='image/png',
            size=qr_image_io.tell(),
            charset=None,
        )



        employee = adminemp.objects.create(
            empcatid_id=json.loads(request.POST.get('EmployeeCategory')).get('id'),
            empname=fname + ' ' + lname,
            dob=request.POST.get('dob'),
            mobile=request.POST.get('phone'),
            email=request.POST.get('email'),
            address=request.POST.get('Locality'),
            joindate=request.POST.get('jdate'),
            photo=request.FILES.get('photo'),
            qualifid_id=request.POST.get('qualification'),
            desigid_id=request.POST.get('designation'),
            dptid_id=request.POST.get('department'),
            salary=request.POST.get('snumber'),
            gender=request.POST.get('gender'),
            barcode=qr_image,
        )

        # Handle empdesig
        empdesig.objects.create(
            empid=employee,
            desigid_id=request.POST.get('designation'),
            from_date=request.POST.get('jdate'),

        )

        # Handle empdpt
        empdpt.objects.create(
            empid=employee,
            dptid_id=request.POST.get('department'),
            from_date=request.POST.get('jdate'),
        
        )

        # Handle salary
        salary.objects.create(
            empid=employee,
            salary=request.POST.get('snumber'),
            from_date=request.POST.get('jdate'),
        )

        # Handle scd
        class_ids = request.POST.getlist('class_ids[]')
        division_ids = request.POST.getlist('division_ids[]')
        subject_ids = request.POST.getlist('subject_ids[]')


        for class_id, division_id, subject_id in zip(class_ids, division_ids, subject_ids):
            scd.objects.create(
                empid=employee,
                classid_id=class_id,
                divid_id=division_id,
                subid_id=subject_id
            )

    context={
        'qualification_data':qualification_data,
        'designation_data':designation_data,
        'department_data':department_data,
        'employee_data':employee_data,
        'class_data':class_data,
        'division_data':division_data,
        'subject_data':subject_data,

    }
    return render(request,"employee_register.html",context)

def get_register_subjects(request):
    class_id = request.GET['classId']
    academic_class = get_object_or_404(AcademicClass, id=class_id, is_enabled=True)
    subjects = list(AcademicSubject.objects.filter(classes=academic_class, is_active=True).values('id', 'subject_name'))
    print(subjects)
    response_data={"subjects":subjects}
    return JsonResponse(response_data)


def get_employee_details(request):
    return render(request,'get_employee_details.html')