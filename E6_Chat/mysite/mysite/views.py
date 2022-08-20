from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.mail import send_mail
from myapi.models import Author


def start(request):
    return render(request, 'chat/start.html')


def room_select(request):
    return render(request, 'chat/room_select.html')


class Author_List(ListView):
    model = Author
    template_name = 'chat/mailing.html'
    context_object_name = 'mass_mailing'

    def get_context_data (self, **kwargs):
        id = self.kwargs.get('room_name')
        id1 = self.kwargs.get('user_email')
        context = super().get_context_data(**kwargs)
        context['val'] = id
        context['val1'] = id1
        return context


    def post(self, request, *args, **kwargs):
        id = self.kwargs.get('room_name')
        id1 = self.kwargs.get('user_email')
        id_author = request.POST.getlist("Участники")  # доделать что бы можно было несколько подписок оформлять сразу
        #print(f'id_author- {id_author}')
        mass_cat=''
        for id_sel in id_author:
            #print (Author.objects.get(id=id_sel))
            abonent=Author.objects.get(id=id_sel)
            #print (abonent.name)
            send_mail(
                 subject=f'{id1} Вас в чат ',
                 message=f'{id1} приглашает Вас присоединиться к беседе в чате в комнате {id}',
                 from_email='Umba.dog@yandex.ru',
                 recipient_list=[abonent.name],
            )
        #print (id)
        return redirect(f'/chat/{id}')