from django.shortcuts import render
from .models import Fee,FeeStructure
from landing_page.models import Candidate
from django.http import JsonResponse
# Create your views here.
def fee(request):
    context = {}
    return render(request,"fee.html",context)

def fetch_student_details(request):
    if request.method == 'POST':
        student_id = int(request.POST["student_id"])
        print(student_id)
        row = Fee.objects.filter(student_id = student_id).values()
        if len(row)==0:
            row_c = Candidate.objects.filter(student_id = student_id).values()
            if len(row_c)!=0:
                new_fee = Fee.objects.create(student_id=student_id)
                return JsonResponse({'status': [0]*12,"payable":"12"})
            return JsonResponse({'status': 'Invalid request'}, status=400)      
        print(row) 
        return JsonResponse({'status': [1]*row[0]["fee_paid_months"]+[0]*(12-row[0]["fee_paid_months"]),"payable":str(12-row[0]["fee_paid_months"])})
        
def fee_payment(request):
    if request.method == 'POST':
        student_id = int(request.POST["student_id"])
        months = int(request.POST["months"])
        print(student_id)
        row = Fee.objects.get(student_id = student_id)
        
        if row==None or row.fee_paid_months+months>12:
            return JsonResponse({'status': 'Invalid request'}, status=400)  
        row.fee_paid_months += months
        row.save()
        return JsonResponse({'status': [1]*row.fee_paid_months+[0]*(12-row.fee_paid_months),"payable":str(12-row.fee_paid_months)})   

def fee_structure(request):
    context = {}
    return render(request,"fee_structure.html",context)


def  enter_fee_structure(request):
    if request.method == 'POST':
        class_ = int(request.POST["class"])
        name = request.POST["name"]
        value = float(request.POST["value"])
        row = FeeStructure.objects.create(student_class=class_,fee_name=name,fee_value=value)
        row = FeeStructure.objects.filter(student_class=class_)
        data = {}
        for r in row:
            data[r["fee_name"]] = r["fee_value"]
        return JsonResponse(data)


def fee_structure_by_class(request):
    if request.method == 'POST':
        class_ = int(request.POST["class"])
        row = FeeStructure.objects.filter(student_class=class_)
        data = {}
        for r in row:
            data[r["fee_name"]] = r["fee_value"]
        return JsonResponse(data)
        
            
        