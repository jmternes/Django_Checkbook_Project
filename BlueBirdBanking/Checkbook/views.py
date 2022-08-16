from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# homepage here
def home(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['account'] #if form is submitted retreive the acct that user wants to view
        return balance(request, pk)
    content = {'form': form}
    return render(request, 'checkbook/index.html', content)


# create new account page here
def create_account(request):
    form = AccountForm(data=request.POST or None) #retrieves the account form
    #checks if request method is post
    if request.method == 'POST':
        if form.is_valid():
            form.save() #saves the new account if submitted form is valid
            return redirect('index')
    content = {'form': form} #saves the content to the template as a dir
    #adds content of form to the page
    return render(request, 'checkbook/CreateNewAccount.html', content)


# balance page here
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) #retrieve account using pk
    transactions = Transaction.Transactions.filter(account=pk)
    current_total = account.initial_deposit #create account total var, starting with initial value
    table_contents = {} #dict into which transaction info will be placed
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount #if deposit add to balance
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# transaction page
def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account']
            form.save()
            return balance(request, pk)
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
