import os
import random
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','todolist.settings') 
django.setup()

# FAKE POP SCRIPT
from todo.models import *
from faker import Faker

fakegen = Faker()
todos = ['Tittle', 'poster', 'art', 'flashmob']

def add_todo():
    q = Todo.objects.get_or_create(name=random.choice(todos))[0]
    q.save()
    return q

def populate(N=5):
    for entry in range(N):
        top = add_todo()

        fake_name = fakegen.name()
        fake_address = fakegen.address()
        fakephone_number = fakegen.msisdn()

        fake_list = List.objects.get_or_create(name =fake_name, address = fake_address, phone_number= fakephone_number)[0]

if __name__ == '__main__':
    print('populating fake_data')
    populate(40)
    print('populating complated!')