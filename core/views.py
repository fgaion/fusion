# from django.shortcuts import render

# como temos formulários no projeto, trocou-se TemplateView por FormView
#from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils import translation


from core.models import Servico, Funcionario, Recurso
from core.forms import ContatoForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        lang = translation.get_language()
        context['servicos'] = Servico.objects.order_by('?').all()  #ordena aleatoriamente
        #context['servicos'] = Servico.objects.all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        #context['funcionarios'] = Funcionario.objects.all()
        meio_rec = int(Recurso.objects.all().count() / 2)
        context['recursos1'] = Recurso.objects.filter(id__lt=meio_rec+1)
        context['recursos2'] = Recurso.objects.filter(id__gt=meio_rec)
        context['lang'] = lang
        translation.activate(lang)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('E-mail enviado com sucesso'))
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar e-mail'))
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

'''
class TesteView(TemplateView):
    template_name = '500.html'
'''