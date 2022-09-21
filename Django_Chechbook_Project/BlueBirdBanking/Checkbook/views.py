from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction
# This function will render the homepage when requested

def home(request):
    form = TransactionForm(data=request.POST or None)
    # check if request method is POST
    if request.method == 'POST':
        pk = request.POST['account'] # if the form is submitte, retrive which account the user wants to view
        return balance(request, pk) #call balance function to render that accounts balance sheet
    content = {'form' : form} # pass content to the template in a dictionary
    # Adds content of form to page
    return render(request, 'checkbook/index.html', content)

# this function will render the Create New account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None) # Retrieve the Account form
    # check if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # check tp see if the submitted form is valid and if so, saves the form
            form.save()  #saves new account
            return redirect('index') #Returns user back to the home page
    content = {'form': form} #saves content to the template as a dictionary
    # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


# This function will render the Balance page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) # retrive the requested account using its primary key
    transactions = Transaction.Transactions.filter(account=pk) #retrive all of that accounts transactions
    current_total = account.initial_deposit # creates account total variable, starting with initial deposit value
    table_contents = {} # creates a dictionary into which transaction information will be placed
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount #if deposit add amount to the balance
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount # if withdrawal subtract amount from deposit
            table_contents.update({t: current_total}) # add transaction and total to the dictionary

        # pass acount , account total balance, and transaction information to the template
        content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)

# This function will render the Transaction Page when requested

def transaction(request):
    form = TransactionForm(data=request.POST or None) #Retrieve the Transaction form
    # checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): #check to see if the submitted form is valid and if so, will save it
            pk = request.POST['account']# retrive which account the transaction was for
            form.save() # saves the Transaction form
            return balance(request, pk) #renders balance of the accounts balance sheet
    # passcontent to the template in a dictionary
    content = {'form': form}
    # Adds content of form to the page
    return render(request, 'checkbook/AddTransaction.html', content)
