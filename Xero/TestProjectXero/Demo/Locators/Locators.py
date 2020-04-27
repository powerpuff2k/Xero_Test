class Locators(object):

#Login button locator
    btn_login = "//a[@href='https://login.xero.com/']"

#Sign In locators

    Username = "//input[@name='userName']"
    Password = "//input[@name='password']"
    SignIn = "//button[@id='submitButton']"

#Add bank account
    Search_For_ANZ = '//input[@role="textbox"]'
    Select_Result = 'ba-banklist-1023'
    Acct_Name_Field = 'input[id^="accountname"]'
    Bank_Name = "//input[@type='search']"
    Results = "//dive[@data-automationid='searchBanksList']"
    AccountName = "//input[@componentid='accountname-1037']"
    # AccountType = "//input('input[id^="accounttype"]')"
    # Select_account_type = "//div[@role='presentation']"
    AccountNumber = "//input[@componentid='accountnumber-1068']"
    success_message = "//div[@id='notify01']//div[@class='message']"
    prompt_alert = '//div[@id="accountname-1037-errorEl"]'
    Account_type_dropdown = 'input[id^="accounttype"]'
    Account_type_selection = "li.ba-combo-list-item"
    Continue_button = 'a[data-automationid="continueButton"]'

#homepage
    Current_Org= 'xrh-appmenucontainer'
    OrgName = 'xrh-appbutton--text'
    Accounting_link = "//button[@name ='navigation-menu/accounting']"
    BankAccount_link = "Bank accounts"
    Chart_Of_bank_Acc = "Chart of accounts"
    Add_bank_account = "//a[@href='/Banking/Account/#find']"
    page_title = '//h1[@class="ba-page-title"]'


#ChartOfAccounts
    SearchBox = '//input[@id="SearchTermsText"]'
    CheckboxToSelect = '//input[@name="selectedAccounts"]'
    ConfirmDelete = '//div[@class="button-container"]//a[@id="popupOK"]'
    DeleteConfirmButton = '//div[@id="notify01"]//div[@class="message"]'