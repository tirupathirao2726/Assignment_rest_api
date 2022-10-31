## setting django environment
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Assignment.settings')

## django setup
import django
django.setup()


# import Faker
from faker import Faker
from webapp.models import user_info

fakegen=Faker()

def populate_user(N=10):
    emails=[fakegen.unique.email() for i in range(N)]
    for each in range(N):
        firstname=fakegen.first_name()
        lastname=fakegen.last_name()
        email=fakegen.unique.email()
        new_user,created=user_info.objects.get_or_create(First_Name=firstname,Last_Name=lastname,Email=email)
        new_user.save()
if __name__=='__main__':
    print('populating script')
    #populate(30)
    populate_user(50)
    print('population completed')
