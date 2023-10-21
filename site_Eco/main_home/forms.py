from django import forms
from .models import *

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)
        for question in questions:
            answers = Answer.objects.filter(question=question)
            answer_choices = [(answer.id, answer.answer) for answer in answers]
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                widget=forms.RadioSelect(attrs={'class': 'quiz-form-radio'}),
                choices=answer_choices,
                label=question.question,
            )
            self.fields[f'question_{question.id}'].img_bg = question.img_bg
