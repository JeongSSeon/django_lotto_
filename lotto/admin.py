from django.contrib import admin
# from lotto.models import GuessNumbers
from .models import GuessNumbers
# adimn.py랑 import 하려는 class 들어있는 modles.py 같은 파일에 있을 때


# Register your models here.
admin.site.register(GuessNumbers)