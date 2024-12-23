from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets =  {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={"class": "form-control mb-5"})
        }
        labels = {
            'title': 'Title of your note:',
            'text': 'Write your thoughts here:',
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        
        # List of aerospace-related terms
        aerospace_terms = [
            'Aerospace', 'Aviation', 'Aircraft', 'Jet', 'Rocket', 
            'Space', 'Satellite', 'Flight', 'Helicopter', 'Drone',
            'Propulsion', 'Wing', 'Cockpit', 'Turbine', 'Fuselage',
            'Aerodynamics', 'Mach', 'Runway', 'Orbit', 'Payload',
            'Landing', 'Takeoff', 'Navigation', 'UAV', 'Engine', 
            'Altitude', 'Throttle', 'Gyroscope', 'Supersonic'
        ]

        # Check if any term is in the title
        if not any(term in title for term in aerospace_terms):
            raise ValidationError('We only accept notes about Aerospace or related topics!')
        return title
