from django.forms import ModelForm
from .models import Account, Transaction


# Creates Account Form base on Account Model
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


# Creates Transaction Form based on Transaction Model
class TransactionForm(ModelForm):
    class Mate:
        model = Transaction
        fields = '__all__'