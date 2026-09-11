from django import forms
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError
from .models import Exam, Question, Choice

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'description']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'score']

class BaseChoiceFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        if any(self.errors):
            return
        
        correct_count = 0
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_correct'):
                    correct_count += 1
        
        if correct_count != 1:
            raise ValidationError("Exactly one choice must be marked as correct.")

ChoiceFormSet = inlineformset_factory(
    Question, 
    Choice, 
    fields=['text', 'is_correct'], 
    extra=4, 
    can_delete=True,
    formset=BaseChoiceFormSet
)