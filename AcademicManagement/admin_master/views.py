from django.shortcuts import render,redirect
from .models import AcademicClass,AcademicDepartment,AcademicDesignation,AcademicQualification,AcademicDivision,AcademicEmployeeCategory,AcademicSubject
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def department_manage(request):
    success_message=None
    error_message = None
    academic_department = AcademicDepartment.objects.all()
    if request.method == 'POST':
        department_name = request.POST.get('department_name','').strip()
        department_code = request.POST.get('department_code','').strip()
        
        # Server-side validation
        if not department_name or not department_code:
            error_message ='Both Department Name and Code are required.'
        elif AcademicDepartment.objects.filter(department_name__iexact=department_name).exists():
            error_message='Department Name already exists.'
        elif AcademicDepartment.objects.filter(department_code__iexact=department_code).exists():
            error_message='Department Code already exists.'
        else:
           
            # Create the department object
            AcademicDepartment.objects.create(
                department_name=department_name,
                department_code=department_code
            )
            success_message='Department added successfully.'

            
    context = {
        'errormessage': error_message,
        'successmessage': success_message,
        'academic_department': academic_department,
    }

    return render(request, 'department_manage.html',context)


def designation_manage(request):
    success_message=None
    error_message = None
    academic_designation = AcademicDesignation.objects.all()
    if request.method == 'POST':
        designation_name = request.POST.get('designation_name','').strip()
        designation_code = request.POST.get('designation_code','').strip()

        if not designation_name or not designation_code:
            error_message ='Both Designation Name and Code are required.'
        elif AcademicDesignation.objects.filter(designation_name__iexact=designation_name).exists():
            error_message='Designation Name already exists.'
        elif AcademicDesignation.objects.filter(designation_code__iexact=designation_code).exists():
            error_message='Designation Code already exists.'
        else:
           
            AcademicDesignation.objects.create(
                designation_name=designation_name,
                designation_code=designation_code
            )

            success_message='Designation added successfully.'

            
    context = {
        'errormessage': error_message,
        'successmessage': success_message,
        'academic_designation': academic_designation,
    }
    return render(request, 'designation_manage.html',context)


def qualification_manage(request):
    success_message=None
    error_message = None
    academic_qualification = AcademicQualification.objects.all()

    if request.method == 'POST':
        qualification_name = request.POST.get('qualification_name', '').strip()

        if not qualification_name:
            error_message = 'Qualification name cannot be empty.'
        else:
            if AcademicQualification.objects.filter(qualification_name=qualification_name).exists():
                error_message = 'Qualification name already exists.'
            else:
                AcademicQualification.objects.create(qualification_name=qualification_name)
                success_message = 'Qualification created successfully.'

    context = {
        'errormessage': error_message,
        'successmessage': success_message,
        'academic_qualifications': academic_qualification,
    }

    return render(request, 'qualification_manage.html', context)

def class_manage(request):
    success_message=None
    error_message = None
    academic_classes = AcademicClass.objects.all()

    if request.method == 'POST':
        class_name = request.POST.get('class_name', '').strip()

        if not class_name:
            error_message = 'Class name cannot be empty.'
        else:
            if AcademicClass.objects.filter(class_name=class_name).exists():
                error_message = 'Class name already exists.'
            else:
                AcademicClass.objects.create(class_name=class_name)
                success_message = 'Class created successfully.'
    
    context = {
        'errormessage': error_message,
        'successmessage': success_message,
        'academic_classes': academic_classes,
    }

    return render(request, 'class_manage.html', context)


def division_manage(request):
    success_message=None
    error_message = None
    academic_division = AcademicDivision.objects.all()

    if request.method == 'POST':
        division_name = request.POST.get('division_name', '').strip()

        if not division_name:
            error_message = 'Division name cannot be empty.'
        else:
            if AcademicDivision.objects.filter(division_name=division_name).exists():
                error_message = 'Division name already exists.'
            else:
                AcademicDivision.objects.create(division_name=division_name)
                success_message = 'Division created successfully.'

    context = {
        'errormessage': error_message,
        'successmessage': success_message,
        'academic_divisions': academic_division,
    }

    return render(request, 'division_manage.html', context)


def subject_manage(request):
    success_message=None
    error_message = None
    academic_classes = AcademicClass.objects.filter(is_enabled=True)
    academic_subject=AcademicSubject.objects.all()
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        class_ids = request.POST.getlist('classes')
        if not subject_name:
            error_message = 'Division name cannot be empty.'
        elif not class_ids:
            error_message = 'Select Class'
        else:
            if AcademicSubject.objects.filter(subject_name=subject_name).exists():
                error_message = 'Subject name already exists.'
            else:
                subject = AcademicSubject.objects.create(subject_name=subject_name)
                subject.classes.set(class_ids)
                subject.save()
                success_message = 'Subject created successfully.'
        


    context={
        'errormessage': error_message,
        'successmessage': success_message,
        "academic_classes":academic_classes,
        "academic_subject":academic_subject
    }
    return render(request,"subject_manage.html",context)

def employee_category_manage(request):
    success_message=None
    error_message = None
    academic_employee_category = AcademicEmployeeCategory.objects.all()

    if request.method == 'POST':
        employee_category_name = request.POST.get('category_name', '').strip()
        employee_category_area = request.POST.get('category_area', '').strip()
        print(type(employee_category_name))
        if not employee_category_name or not employee_category_area:
            error_message = 'Both Employee Name and Area are required.'
        elif AcademicEmployeeCategory.objects.filter(employee_category_name__iexact=employee_category_name).exists():
            error_message = 'Employee Name already exists.'
        elif AcademicEmployeeCategory.objects.exclude(employee_category_area=5).filter(employee_category_area__iexact=employee_category_area).exists():
            error_message = 'Employee Area already exists.'
        else:
            AcademicEmployeeCategory.objects.create(
                employee_category_name=employee_category_name,
                employee_category_area=employee_category_area
            )
            success_message = 'Employee added successfully.'

    context = {
        'errormessage': error_message,
        'successmessage': success_message,
        'academic_employee_categorys': academic_employee_category,
        'settings': settings
    }

    return render(request, 'employee_category_manage.html', context)


#edit view
def get_class_details(request):
    class_id = request.GET['class_id']
    cls_obj=AcademicClass.objects.get(id=class_id)
    print('Received class_id:', cls_obj)
    response_data = {
    'id': cls_obj.id,
    'name': cls_obj.class_name,
    'select': 1 if cls_obj.is_enabled else 0,
    }
    return JsonResponse(response_data)

def update_class_details(request):
    update_id = request.GET['updateId'].strip()
    update_class = request.GET['updateClass'].strip()
    update_Status = request.GET['updateStatus'].strip()
    error_message=None
    success_message=None
    if not update_class:
            error_message = 'Class name cannot be empty.'
    else:
        if AcademicClass.objects.exclude(id=update_id).filter(class_name=update_class).exists():
            error_message = 'Class name already exists.'
        else:
            obj= AcademicClass.objects.get(id=update_id)
            obj.class_name = update_class
            obj.is_enabled=int(update_Status)
            obj.save()
            success_message = 'Class updated successfully.'
    
    
    
    response_data = {
    'errormessage': error_message,
    'successmessage': success_message,
    }
    return JsonResponse(response_data)


def delete_class(request):
    delete_id = request.GET['id'].strip()
    q = AcademicClass.objects.get(id=delete_id)
    q.delete()
    return JsonResponse({"message":"deleted sucess fully"})




#department
def get_departments_details(request):
    department_id = request.GET['department_id']
    dep_obj=AcademicDepartment.objects.get(id=department_id)
    response_data = {
    'id': dep_obj.id,
    'name': dep_obj.department_name,
    'code':dep_obj.department_code,
    'select': 1 if dep_obj.is_active else 0,
    }
    return JsonResponse(response_data)


def update_departments_details(request):
    update_id = request.GET['updateId'].strip()
    update_name = request.GET['updateName'].strip()
    update_Status = request.GET['updateStatus'].strip()
    update_code = request.GET['updateCode'].strip()
    error_message=None
    success_message=None
    if not update_name or not update_code:
        error_message ='Both Department Name and Code are required.'
    elif AcademicDepartment.objects.exclude(id=update_id).filter(department_name=update_name).exists():
        error_message='Department Name already exists.'
    elif AcademicDepartment.objects.exclude(id=update_id).filter(department_code=update_code).exists():
        error_message='Department Code already exists.'
    else:
        obj= AcademicDepartment.objects.get(id=update_id)
        obj.department_name = update_name
        obj.department_code = update_code
        obj.is_active=int(update_Status)
        obj.save()
        success_message = 'Department updated successfully.'

    response_data = {
    'errormessage': error_message,
    'successmessage': success_message,
    }
    return JsonResponse(response_data)



def delete_department(request):
    delete_id = request.GET['id'].strip()
    q = AcademicDepartment.objects.get(id=delete_id)
    q.delete()
    return JsonResponse({"message":"deleted sucess fully"})



#designation


def get_designation_details(request):
    designation_id = request.GET['designation_id']
    dep_obj=AcademicDesignation.objects.get(id=designation_id)
    response_data = {
    'id': dep_obj.id,
    'name': dep_obj.designation_name,
    'code':dep_obj.designation_code,
    'select': 1 if dep_obj.is_active else 0,
    }
    return JsonResponse(response_data)


def update_designation_details(request):
    update_id = request.GET['updateId'].strip()
    update_name = request.GET['updateName'].strip()
    update_Status = request.GET['updateStatus'].strip()
    update_code = request.GET['updateCode'].strip()
    error_message=None
    success_message=None
    if not update_name or not update_code:
        error_message ='Both Designation Name and Code are required.'
    elif AcademicDesignation.objects.exclude(id=update_id).filter(designation_name=update_name).exists():
        error_message='Designation Name already exists.'
    elif AcademicDesignation.objects.exclude(id=update_id).filter(designation_code=update_code).exists():
        error_message='Designation Code already exists.'
    else:
        obj= AcademicDesignation.objects.get(id=update_id)
        obj.designation_name = update_name
        obj.designation_code = update_code
        obj.is_active=int(update_Status)
        obj.save()
        success_message = 'Designation updated successfully.'

    response_data = {
    'errormessage': error_message,
    'successmessage': success_message,
    }
    return JsonResponse(response_data)

def delete_designation(request):
    delete_id = request.GET['id'].strip()
    q = AcademicDesignation.objects.get(id=delete_id)
    q.delete()
    return JsonResponse({"message":"deleted sucess fully"})


#Qualification

def get_qualification_details(request):
    qualification_id = request.GET['qualification_id']
    qualification_obj=AcademicQualification.objects.get(id=qualification_id)
    response_data = {
    'id': qualification_obj.id,
    'name': qualification_obj.qualification_name,
    'select': 1 if qualification_obj.is_active else 0,
    }
    return JsonResponse(response_data)

def update_qualification_details(request):
    update_id = request.GET['updateId'].strip()
    update_name = request.GET['updateName'].strip()
    update_Status = request.GET['updateStatus'].strip()
    error_message=None
    success_message=None
    if not update_name:
            error_message = 'Class name cannot be empty.'
    else:
        if AcademicQualification.objects.exclude(id=update_id).filter(qualification_name=update_name).exists():
            error_message = 'Class name already exists.'
        else:
            obj= AcademicQualification.objects.get(id=update_id)
            obj.qualification_name = update_name
            obj.is_active=int(update_Status)
            obj.save()
            success_message = 'Class updated successfully.'
    
    
    
    response_data = {
    'errormessage': error_message,
    'successmessage': success_message,
    }
    return JsonResponse(response_data)


def delete_qualification(request):
    delete_id = request.GET['id'].strip()
    q = AcademicQualification.objects.get(id=delete_id)
    q.delete()
    return JsonResponse({"message":"deleted sucess fully"})



def get_division_details(request):
    division_id = request.GET['division_id']
    qualification_obj=AcademicDivision.objects.get(id=division_id)
    response_data = {
    'id': qualification_obj.id,
    'name': qualification_obj.division_name,
    'select': 1 if qualification_obj.is_active else 0,
    }
    return JsonResponse(response_data)

def update_division_details(request):
    update_id = request.GET['updateId'].strip()
    update_name = request.GET['updateName'].strip()
    update_Status = request.GET['updateStatus'].strip()
    error_message=None
    success_message=None
    if not update_name:
            error_message = 'Division name cannot be empty.'
    else:
        if AcademicDivision.objects.exclude(id=update_id).filter(division_name=update_name).exists():
            error_message = 'Division name already exists.'
        else:
            obj= AcademicDivision.objects.get(id=update_id)
            obj.division_name = update_name
            obj.is_active=int(update_Status)
            obj.save()
            success_message = 'Division updated successfully.'
    
    
    
    response_data = {
    'errormessage': error_message,
    'successmessage': success_message,
    }
    return JsonResponse(response_data)


def delete_division(request):
    delete_id = request.GET['id'].strip()
    q = AcademicDivision.objects.get(id=delete_id)
    q.delete()
    return JsonResponse({"message":"deleted sucess fully"})



def get_employee_category_details(request):
    employee_category_id = request.GET['employee_category_id']
    employee_category_obj=AcademicEmployeeCategory.objects.get(id=employee_category_id)
    response_data = {
    'id': employee_category_obj.id,
    'name': employee_category_obj.employee_category_name,
    'area':employee_category_obj.employee_category_area,
    'select': 1 if employee_category_obj.is_active else 0,
    }
    return JsonResponse(response_data)

def update_employee_category_details(request):
    update_id = request.GET['updateId'].strip()
    update_name = request.GET['updateName'].strip()
    update_Area = request.GET['updateArea'].strip()
    update_Status = request.GET['updateStatus'].strip()
    error_message=None
    success_message=None

    if not update_name or not update_Area:
        error_message = 'Both Employee Name and Area are required.'
    elif AcademicEmployeeCategory.objects.exclude(id=update_id).filter(employee_category_name__iexact=update_name).exists():
            error_message = 'Employee Name already exists.'
    elif AcademicEmployeeCategory.objects.exclude(id=update_id).exclude(employee_category_area=5).filter(employee_category_area__iexact=update_Area).exists():
            error_message = 'Employee Area already exists.'
    else:
        obj= AcademicEmployeeCategory.objects.get(id=update_id)
        obj.employee_category_name = update_name
        obj.employee_category_area=update_Area
        obj.is_active=int(update_Status)
        obj.save()
        success_message = 'Employee updated successfully.'
    
    response_data = {
    'errormessage': error_message,
    'successmessage': success_message,
    }
    return JsonResponse(response_data)


def delete_employee_category(request):
    delete_id = request.GET['id'].strip()
    q = AcademicEmployeeCategory.objects.get(id=delete_id)
    q.delete()
    return JsonResponse({"message":"deleted sucess fully"})



def get_subject_details(request):
    subject_id = request.GET['subject_id']
    subject_obj=AcademicSubject.objects.get(id=subject_id)
    classes = list(subject_obj.classes.values('id', 'class_name'))
    other_classes_queryset = AcademicClass.objects.filter(is_enabled=True).exclude(id__in=subject_obj.classes.values_list('id', flat=True))
    other_classes = list(other_classes_queryset.values('id', 'class_name'))

    response_data = {
    'id': subject_obj.id,
    'name': subject_obj.subject_name,
    "classes":classes,
    "other_classes":other_classes,
    'select': 1 if subject_obj.is_active else 0,
    }
    return JsonResponse(response_data)

def update_subject_details(request):
    update_id = request.GET['updateId'].strip()
    update_name = request.GET['updateName'].strip()
    update_Status = request.GET['updateStatus'].strip()
    class_ids = request.GET.get('selectedClassIds').split(',')
    print(class_ids)
    error_message = None
    success_message = None

    if not update_name or not class_ids:
        error_message = 'Both Subject and Class are required.'
    elif AcademicSubject.objects.exclude(id=update_id).filter(subject_name__iexact=update_name).exists():
        error_message = 'Subject Name already exists.'
    else:
        if not any(class_ids):
            error_message = 'At least one class must be selected.'
        else:
            obj = AcademicSubject.objects.get(id=update_id)
            obj.subject_name = update_name
            obj.is_active = int(update_Status)  
            obj.classes.set(class_ids)
            obj.save()
            success_message = 'Employee updated successfully.'

    response_data = {
        'errormessage': error_message,
        'successmessage': success_message,
    }
    return JsonResponse(response_data)


def get_subject_view(request):
    subject_id = request.GET['subject_id']
    subject_obj=AcademicSubject.objects.get(id=subject_id)
    classes = list(subject_obj.classes.values('id', 'class_name'))
    print(subject_obj.classes)
    response_data = {
    'id': subject_obj.id,
    'name': subject_obj.subject_name,
    "classes":classes,
    'select': "Active" if subject_obj.is_active else "Deactive",
    }
    return JsonResponse(response_data)



def delete_subject(request):
    delete_id = request.GET['id'].strip()
    q = AcademicSubject.objects.get(id=delete_id)
    q.delete()
    return JsonResponse({"message":"deleted sucess fully"})