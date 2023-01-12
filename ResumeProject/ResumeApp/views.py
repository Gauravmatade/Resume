from django.shortcuts import render,redirect
from . forms import ResumeForm
from django.views import View
from . models import ResumeModel
# Create your views here.

# def home_view(request):
#     forms = ResumeForm()
#     context = {'forms':forms}
#     return render(request,'ResumeApp/home.html',context)

class home(View):
    def get(self,request):
        forms = ResumeForm()
        context = {'forms':forms}
        return render(request,'ResumeApp/home.html',context)

    def post(self,request):
        forms = ResumeForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('home')
        return redirect('home')

class all_candidates(View):
    def get(self,request):
        data = ResumeModel.objects.all()
        context = {'data':data}
        return render(request,'ResumeApp/all_candidates.html',context)

class candidate(View):
    def get(self,request,id):
        # print('id is :',id)
        data = ResumeModel.objects.get(id=id)
        context = {'data':data}
        return render(request,'ResumeApp/candidate.html',context)
        # return redirect('all_candidates')

