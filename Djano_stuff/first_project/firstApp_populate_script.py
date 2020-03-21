import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

#Now use faker to genrate fake databases
import random
from faker import Faker
from first_app.models import AccessRecord,Topic,Webpage

fakegen = Faker()
topics = ['search','social network','marketPlace','news','sports']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N = 5):

    for entry in range(N):
        #get the topic for the entry
        top = add_topic()

        #create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create new web page entry

        webpg = Webpage.objects.get_or_create(topic = top,url=fake_url,name = fake_name)[0]

        # create AccessRecord for the entry
        accessRecord = AccessRecord.objects.get_or_create(name = webpg,date = fake_date)[0]

if __name__ == '__main__':
    print("populating data")
    populate(10)
    print("population complete")
