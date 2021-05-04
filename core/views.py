# from django.shortcuts import render

# como temos formulários no projeto, trocou-se TemplateView por FormView
#from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from core.models import Servico, Funcionario, Recurso
from core.forms import ContatoForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()  #ordena aleatoriamente
        #context['servicos'] = Servico.objects.all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        #context['funcionarios'] = Funcionario.objects.all()
        meioRec = int(Recurso.objects.all().count() / 2)
        context['recursos1'] = Recurso.objects.filter(id__lt=meioRec+1)
        context['recursos2'] = Recurso.objects.filter(id__gt=meioRec)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

'''
class TesteView(TemplateView):
    template_name = '500.html'
'''