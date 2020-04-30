from django.shortcuts import render, redirect
from .models import Data
import datetime
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from crud.forms import *
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def search(request):
    return render(request, 'search.html')

@login_required
def searchAjax(request):
    id_cilab=request.POST['id_cilab']
    nombres=request.POST['nombres']
    escolaridad=request.POST['escolaridad']
    fec_nac=request.POST['fec_nac']
    c_p_nac=request.POST['c_p_nac']
    empresa=request.POST['empresa']
    no_emp=request.POST['no_emp']
    apellido_p=request.POST['apellido_p']
    genero=request.POST['genero']
    edad=request.POST['edad']
    c_p_actual=request.POST['c_p_actual']
    depto=request.POST['depto']
    fecha=request.POST['fecha']
    apellido_m=request.POST['apellido_m']
    edo_civil=request.POST['edo_civil']
    c_p_trabajo=request.POST['c_p_trabajo']
    puesto=request.POST['puesto']

    datas = Data.objects.all()
    if id_cilab != '':
        datas = datas.filter(id_cilab=id_cilab)
    if nombres != '':
        datas = datas.filter(nombres__istartswith=nombres)
    if escolaridad != '0':
        datas = datas.filter(escolaridad=escolaridad)
    if fec_nac != '':
        datas = datas.filter(fec_nac=fec_nac)
    if c_p_nac != '':
        datas = datas.filter(c_p_nac=c_p_nac)
    if empresa != '':
        datas = datas.filter(empresa__istartswith=empresa)
    if no_emp != '':
        datas = datas.filter(no_emp=no_emp)
    if apellido_p != '':
        datas = datas.filter(apellido_p__istartswith=apellido_p)
    if genero != '0':
        datas = datas.filter(genero=genero)
    if edad != '':
        datas = datas.filter(edad=edad)
    if c_p_actual != '':
        datas = datas.filter(c_p_actual=c_p_actual)
    if depto != '':
        datas = datas.filter(depto__istartswith=depto)
    if fecha != '':
        datas = datas.filter(fecha=fecha)
    if apellido_m != '':
        datas = datas.filter(apellido_m__istartswith=apellido_m)
    if edo_civil != '0':
        datas = datas.filter(edo_civil=edo_civil)
    if c_p_trabajo != '':
        datas = datas.filter(c_p_trabajo=c_p_trabajo)
    if puesto != '':
        datas = datas.filter(puesto__istartswith=puesto)

    result = ''
    for data in datas:
        genero = "Masc"
        if data.genero == 2:
            genero = "Fem"
        result += '<tr id="'+ str(data.id) +'"><td>' + str(data.id_cilab) + '</td>'
        result += '<td>' + str(data.nombres) + '</td>'
        result += '<td>' + str(data.apellido_p) + '</td>'
        result += '<td>' + str(data.apellido_m) + '</td>'
        result += '<td>' + str(data.edad) + '</td>'
        result += '<td>' + genero + '</td>'
        result += '<td>' + str(data.empresa) + '</td>'
        result += '<td>' + str(data.fecha) + '</td>'
        result += '<td><a href="/edit/'+ str(data.id) +'" class="btn btn-primary mr-1">Edit</a><a href="/delete/'+ str(data.id) +'" class="btn btn-danger">Delete</a></td>'
    return JsonResponse({'data': result})

@login_required
def create(request):
    if request.method == 'POST':
        data = Data(
        id_cilab=request.POST['id_cilab'],
        nombres=request.POST['nombres'],
        escolaridad=request.POST['escolaridad'],
        fec_nac=request.POST['fec_nac'],
        c_p_nac=request.POST['c_p_nac'],
        empresa=request.POST['empresa'],
        no_emp=request.POST['no_emp'],
        apellido_p=request.POST['apellido_p'],
        genero=request.POST['genero'],
        edad=request.POST['edad'],
        c_p_actual=request.POST['c_p_actual'],
        depto=request.POST['depto'],
        fecha=request.POST['fecha'],
        apellido_m=request.POST['apellido_m'],
        edo_civil=request.POST['edo_civil'],
        c_p_trabajo=request.POST['c_p_trabajo'],
        puesto=request.POST['puesto'],
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(), )
        data.save()
        messages.success(request, 'Data was created successfully!')
        return redirect('/create')
    else:
        return render(request, 'create.html')

@login_required
def update(request, id):
    if request.method == 'POST':
        data = Data.objects.get(id=id)
        data.id_cilab=request.POST['id_cilab']
        data.nombres=request.POST['nombres']
        data.escolaridad=request.POST['escolaridad']
        data.fec_nac=request.POST['fec_nac']
        data.c_p_nac=request.POST['c_p_nac']
        data.empresa=request.POST['empresa']
        data.no_emp=request.POST['no_emp']
        data.apellido_p=request.POST['apellido_p']
        data.genero=request.POST['genero']
        data.edad=request.POST['edad']
        data.c_p_actual=request.POST['c_p_actual']
        data.depto=request.POST['depto']
        data.fecha=request.POST['fecha']
        data.apellido_m=request.POST['apellido_m']
        data.edo_civil=request.POST['edo_civil']
        data.c_p_trabajo=request.POST['c_p_trabajo']
        data.puesto=request.POST['puesto']
        data.created_at=datetime.datetime.now()
        data.updated_at=datetime.datetime.now()
        data.save()
        messages.success(request, 'Data was updated successfully!')
        return redirect('/edit/'+ str(id))
    else:
        return render(request, 'create.html')

@login_required    
def edit(request, id):
    data = Data.objects.get(id=id)
    return render(request, 'edit.html', {'data': data})

@login_required
def delete(request, id):
    data = Data.objects.get(id=id)
    data.delete()
    messages.error(request, 'Data was deleted successfully!')
    return redirect('/search')

@login_required
def fileupload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        document = Document(
        description=request.POST['description'],
        document=myfile.name, 
        uploaded_at=datetime.datetime.now(),)
        document.save()
        messages.success(request, 'Member was created successfully!')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return redirect('fileupload')
    else:
        documents = Document.objects.order_by('-uploaded_at')[:3]
        context = {'documents': documents}
    return render(request, 'fileupload.html', context)

@login_required
def ajax(request):
    if request.method == 'POST':
        if request.is_ajax():
            data = Ajax(
            text=request.POST['text'],
            search=request.POST['search'],
            email=request.POST['email'],
            telephone=request.POST['telephone'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), 
            )
            data.save()
            astr = "<html><b> you sent an ajax post request </b> <br> returned data: %s</html>" % data
            return JsonResponse({'data': 'success'})
    else:
        ajax_list = Ajax.objects.order_by('-created_at')
        context = {'ajax_list': ajax_list}
    return render(request, 'ajax.html',  {'ajax_list': ajax_list})

@csrf_protect
def getajax(request):
    if request.method == 'GET':
        if request.is_ajax():
            data = Ajax.objects.order_by('-created_at').first()
            created = data.created_at.strftime('%m-%d-%Y %H:%M:%S')
            datas = {"id": data.id, "text": data.text, "search": data.search, "email": data.email, "telephone": data.telephone, "created_at": created}
            return JsonResponse(datas)
    else:
        return JsonResponse({'data': 'failure'})
  
@csrf_protect
def ajax_delete(request):
    if request.method == 'GET':
        if request.is_ajax():
            id=request.GET['id']
            ajax = Ajax.objects.get(id=id)
            ajax.delete()
            return JsonResponse({'data': 'success'})
    else:
        return JsonResponse({'data': 'failure'})
  

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            is_staff=True,
            is_active=True,
            is_superuser=True,
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
 
def register_success(request):
    return render_to_response(
    'success.html',
    )

@login_required
def users(request):
    users_list = User.objects.all()
    paginator = Paginator(users_list, 5)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'users.html', {'users': users})

@login_required
def user_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    messages.error(request, 'User was deleted successfully!')
    return redirect('/users')

@login_required
def upload_csv(request):
    if 'GET' == request.method:
        csv_list = CsvUpload.objects.all()
        paginator = Paginator(csv_list, 7)
        page = request.GET.get('page')
        try:
            csvdata = paginator.page(page)
        except PageNotAnInteger:
            csvdata = paginator.page(1)
        except EmptyPage:
            csvdata = paginator.page(paginator.num_pages)
        return render(request, 'upload_csv.html', {'csvdata': csvdata})
    try:
        csv_file = request.FILES["csv_file"]

        if len(csv_file) == 0:
            messages.error(request, 'Empty File')
            return render(request, 'upload_csv.html')

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return render(request, 'upload_csv.html')

        if csv_file.multiple_chunks():
            messages.error(request, 'Uploaded file is too big (%.2f MB).' % (csv_file.size / (1000 * 1000),))
            return render(request, 'upload_csv.html')

        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split("\n")
        for index, line in enumerate(lines):
            fields = line.split(",")
            if index == 0:
                if (fields[0] == 'name') and (fields[1] == 'description') and (fields[2] == 'end_date') and (fields[3] == 'notes'):
                    pass
                else:
                    messages.error(request, 'File is not Correct Headers')
                    return render(request, 'upload_csv.html')
                    break
            else:
                print(index)
                if (len(fields[0]) != 0) and (len(fields[1]) != 0) and (len(fields[2]) != 0) and (len(fields[3]) != 0):
                    data = CsvUpload(
                        name=fields[0],
                        description=fields[1],
                        end_date=datetime.datetime.now(),
                        notes=fields[3]
                    )
                    data.save()
        messages.success(request, "Successfully Uploaded CSV File")
        return redirect('/upload/csv/')

    except Exception as e:
        messages.error(request, "Unable to upload file")
        return redirect('/upload/csv/')

@login_required
def changePassword(request):
    print('changepasword')
    return render(request, 'change_password.html')

