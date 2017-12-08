import  os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'first_Django_project.settings')

import django
django.setup()

##FAKE POP SCRIPT

import random
from first_Django_app.models import AccessRecord, Topic, Webpage
from faker import  Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Maketplace', 'New', 'Game']

def add_topic():
    t = Topic.objects.get_or_create(top_name= random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        #get topic for entry
        top = add_topic()

        #create the fake data for entry
        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()

        #create the webpage for entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #create a fake access record for the webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date= fake_date)[0]

if __name__ == "__main__":
    print('populating scripts!')
    populate(20)
    print('populating complete!')

