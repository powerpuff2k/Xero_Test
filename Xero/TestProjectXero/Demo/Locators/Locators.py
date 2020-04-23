class Locators(object):

#Login button locator
    btn_login = "//a[@href='https://login.xero.com/']"

#Sign In locators

    Username = "//input[@name='userName']"
    Password = "//input[@name='password']"
    SignIn = "//button[@id='submitButton']"

#Add bank account
    Search_For_ANZ = '//input[@role="textbox"]'
    Select_ANZ = 'ba-banklist-1023'
    Acct_Name_Field = 'input[id^="accountname"]'
    Bank = "//input[@type='search']"
    Results = "//dive[@data-automationid='searchBanksList']"
    AccountName = "//input[@componentid='accountname-1037']"
    # AccountType = "//input('input[id^="accounttype"]')"
    Select_account_type = "//div[@role='presentation']"

#homepage
    Current_Org= 'xrh-appmenucontainer'
    OrgName = 'xrh-appbutton--text'
    Accounting_link = "//button[@name ='navigation-menu/accounting']"
    BankAccount_link = "Bank accounts"
    Chart_Of_bank_Acc = "Chart of accounts"
    Add_bank_account = "//a[@href='/Banking/Account/#find']"


#ChartOfAccounts
    SearchBox = '//input[@id="SearchTermsText"]'
    CheckboxToSelect = '//input[@name="selectedAccounts"]'
    ConfirmDelete = '//div[@class="button-container"]//a[@id="popupOK"]'
    DeleteConfirmButton = '//div[@id="notify01"]//div[@class="message"]'







