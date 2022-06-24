from django.shortcuts import render
import requests
from . import API

# Create your views here.
def get_area(request):
    response = requests.get(API.LOCATION_GET_POST)
    location_data = response.json()
    if request.method=="POST":
        get_loction = request.POST.get('city')
        user_detail=requests.get(API.USER_ROLE+ str(get_loction))
        user_detail_json=user_detail.json()
        return render(request, 'pgpGlass/select_role.html',{'data':user_detail_json})
    return render(request,'pgpGlass/location.html',{'all_area':location_data})

def get_filtered_name(request):
    if request.method == "POST":
        ddl1 = request.POST['ddl1']
        ddl2 = request.POST['ddl2']
        ddl3 = request.POST['ddl3']
        response = requests.get(API.LOCATION_GET_POST)
        data = response.json()
        return render(request,'pgpGlass/add_new_task.html',{'person':ddl1,'person1':ddl2,'person2':ddl3,'location':data})
    return render(request, 'pgpGlass/select_role.html')

def addTask(request):
    if request.method == "POST":
        person=request.POST['person']
        person1 = request.POST['person1']
        person2 = request.POST['person2']
        date = request.POST['date']
        equipment = request.POST["txtequipment"]
        number_of_person=request.POST['txtnop']
        start_time = request.POST['txtstarttime']
        end_time = request.POST['txtendtime']
        location = request.POST['city']
        print("LOCATION++++++++",location)
        tool=request.POST['txtTool']
        agency = request.POST['txtagency']
        description = request.POST['txtdesc']
        type_of_work=request.POST.getlist('checks[]')
        worktype_listToStr = ' , '.join([str(elem) for elem in type_of_work])

        ppe_required= request.POST.getlist('ppe[]')
        ppe_listToStr = ' , '.join([str(elem) for elem in ppe_required])

        postFormData = {
            "loggedPerson":person, "date":date, "typeOfWork":worktype_listToStr, "numberOfPerson":number_of_person,
            "startTime":start_time, "endTime":end_time, "location":location, "equipment":equipment,
            "toolRequired":tool, "workingAgency":agency, "workDescription":description, "ppeRequired":ppe_listToStr,
            "person1":person1, "person2":person2, "newFlag":True, "oldFlag" : False, "closeFlag":False,
            "completedFlag":False,"":True
        }
        print("*************FORMDATA=", postFormData)
        a=requests.post(url=API.FORM_GET_POST, data=postFormData)
        # return render(request,'pgpGlass/location.html')
    return render(request, 'pgpGlass/add_new_task.html')

def newTask(request):
    response = requests.get(API.NEW_TASK+str('Aman Pandey'))
    print(response)
    data = response.json()
    print(data)
    return render(request, 'pgpGlass/new_task.html',{'data':data})

def oldTask(request):
    response = requests.get(API.OLD_FLAG+str('Roshani'))
    data = response.json()
    return render(request, 'pgpGlass/new_task.html',{'data':data})

def closeTask(request):
    response = requests.get(API.CLOSE_FLAG+str('Roshani'))
    data = response.json()
    return render(request, 'pgpGlass/new_task.html',{'data':data})

def completeTask(request):
    response = requests.get(API.COMPLETE_FLAG+str('Roshani'))
    data = response.json()
    return render(request, 'pgpGlass/new_task.html',{'data':data})

def notification(request):
    response = requests.get(API.NOTIFICATION+str('Roshani Kale'))
    data = response.json()
    return render(request, 'pgpGlass/new_task.html',{'data':data})


def toClose(request):
    response = requests.get(API.CHANGE_CLOSE_FLAG)
    data=response.json()
    return render(request,'pgpGlass/to_close.html',{'data':data})