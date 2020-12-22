import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'saladpet.settings'
import django
django.setup()
from ../accounts.models import User
import csv
import uuid

UUID = "".join(str(uuid.uuid4()).split('-')) ## Generating random UUID value
PASSWORD = 1
OWNER_NAME = 'test'
OWNER_BIRTHDAY = '1999-09-09'
STATUS = 'ACTIVE'
IS_ACTIVE = 1
IS_STAFF = 0
IS_SUPERUSER = 0
PET_TYPE = (
        (1, '개'),
        (2, '고양이'),
        (3, '둘다'),
)

TROUBLE_TYPE = (
        (0, ''), 
        (1, '알러지'),
        (2, '장'),
        (3, '치아/구강'),
        (4, '비만'),
        (5, '뼈/관절'),
        (6, '피부/모질'),
        (7, '노령'),
        (8, '신장/요로'),
        (9, '호흡기'),
        (10, '심장'),
        (11, '당뇨'),
        (12, '눈/귀'),
        (13, '행동'),
)
PET_TYPE = {v:k for k,v in dict(PET_TYPE).items()}
TROUBLE_TYPE = {v:k for k,v in dict(TROUBLE_TYPE).items()}

idx = 0
with open('users.csv', 'r', encoding='utf-8-sig') as f:
    rdr = csv.reader(f)
    for line in rdr:
        if idx == 0:
            cursor = {v:k for k,v in enumerate(line)}
            print(cursor)
        else:
            query_arg = {}
            query_arg['password'] = PASSWORD
            query_arg['email'] = str(idx) + '@foo.bar'
            query_arg['owner_name'] = OWNER_NAME
            query_arg['owner_birthday'] = OWNER_BIRTHDAY
            query_arg['nickname'] = line[cursor['nickname']]
            query_arg['pet_name'] = line[cursor['pet_name']]
            query_arg['pet_type2'] = line[cursor['pet_type2']]
            query_arg['pet_type1'] = line[cursor['pet_type1']]
            query_arg['pet_weight'] = line[cursor['pet_weight']]
            query_arg['pet_age'] = line[cursor['pet_age']]
            query_arg['trouble1'] = TROUBLE_TYPE[line[cursor['trouble1']]]
            query_arg['trouble2'] = TROUBLE_TYPE[line[cursor['trouble2']]]
            query_arg['trouble3'] = TROUBLE_TYPE[line[cursor['trouble3']]]
            query_arg['status'] = STATUS
            query_arg['is_active'] = IS_ACTIVE
            query_arg['is_staff'] = IS_STAFF
            query_arg['is_superuser'] = IS_SUPERUSER
            query_arg['secret'] = UUID
            User.objects.create(**query_arg)
            Userinstance = User.objects.create(**query_arg)
            print(i, 'th customer inserted')
        idx += 1
        
    print(query_arg)

        
        
