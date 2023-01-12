from django import forms
from . models import ResumeModel

gender_choices = [('Male','Male'),('Female','Female'),('Others','Others')]
city_choices = [('Mulund','Mulund'),('Thane','Thane'),('Kalyan','Kalyan')]
state_choices = [('Maharashtra','Maharashtra'),('GOA','GOA'),('Punjab','Punjab'),('UttaraKhand','UttaraKhand')]
language_choice = [('Marathi','Marathi'),('Hindi','Hindi'),('English','English'),('Tamil','Tamil')]
prolanguage_choice = [('Python','Python'),('Java','Java'),('Html','Html'),('CSS','CSS'),('Dot Net','Dot Net')]
prefloc_choice = [('Mumbai','Mumbai'),('Thane','Thane'),('Banglore','Banglore'),('Delhi','Delhi')]
class ResumeForm(forms.ModelForm):

    Gender = forms.ChoiceField(choices= gender_choices,label="Gender",widget=forms.RadioSelect())
    City = forms.ChoiceField(choices = city_choices,label='Select City',widget = forms.Select(attrs={'class':'form-control'}))
    State = forms.ChoiceField(choices = state_choices, label = 'State',widget = forms.Select(attrs={'class':'form-control'}))
    Language = forms.MultipleChoiceField(choices = language_choice,label = 'Select Language',widget = forms.CheckboxSelectMultiple)
    Programming_Language = forms.MultipleChoiceField(choices = prolanguage_choice, label = 'Select Programming Language ',
    widget = forms.CheckboxSelectMultiple)
    Prefered_loc = forms.ChoiceField(choices = prefloc_choice,label = "Prefered Location", widget = forms.RadioSelect())

    class Meta:
        model = ResumeModel
        fields = ['FirstName','LastName','Email','ContactNo','Gender','DOB','City','State','Language','Programming_Language','Education','Prefered_loc','Prof_image','Project']

        labels = {
            'FirstName':'First Name',
            'LastName': 'Last Name',
            'Email': 'Email-Id',
            'ContactNo':'Contact Number',
            'Gender':'Gender',
            'DOB':'Date Of Birth',
            'City':'CITY',
            'State':'State',
            'Language':'Language',
            'Programming_Language':'Programming Language',
            'Education':'Education/Qualification',
            'Prefered_loc':'Location Prefered',
            'Prof_image':'Upload your Image',
            'Project':'Project Done'
        }

        widgets ={
            'FirstName':forms.TextInput(attrs={'class':'form-control'}),
            'LastName':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'ContactNo':forms.TextInput(attrs={'class':'form-control'}),
            'DOB':forms.DateInput(attrs={'class':'form-control'}),
            'Education':forms.TextInput(attrs = {'class':'form-control'}),
            
        }
