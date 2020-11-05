from tkinter import *

t = Tk()
import math
import locale
import tkinter as Tk

t.minsize(850, 600)

def login():
    f4= Frame(bg="black")
    f4.place(x=70, y=0, width=600, height=600)
    f3 = Frame(bg="pink")
    f3.place(x=100, y=0, width=750, height=600)
    u = Label(f3, text="LOGIN", bg="sky blue", fg="black")
    u.place(x=350, y=30)
    u1 = Label(f3, text="User Name", bg="black", fg="white")
    u1.place(x=250, y=90)

    e1 = Entry(f3, font=("", 12))
    e1.place(x=350, y=90, width=120)

    u2 = Label(f3, text="Password", bg="black", fg="white")
    u2.place(x=250, y=130)

    e1 = Entry(f3, font=("", 12),show="*")
    e1.place(x=350, y=130, width=120)

    
    b3 = Button(f3, text="Login", command=calculator)
    b3.place(x=310, y=190, width=100, height=40)

    b2 = Button(f3, text="I'm New User", command=detail)
    b2.place(x=310, y=250, width=100, height=40)

    b2 = Button(f3, text="Back", command=home)
    b2.place(x=310, y=310, width=100, height=40)
    
def detail():
    f4= Frame(bg="black")
    f4.place(x=70, y=0, width=600, height=600)
    f3 = Frame(bg="pink")
    f3.place(x=100, y=0, width=750, height=600)
    u = Label(f3, text="REGISTRATION DETAILS", bg="sky blue", fg="black")
    u.place(x=270, y=30)
    u1 = Label(f3, text="First Name", bg="black", fg="white")
    u1.place(x=250, y=90)

    e1 = Entry(f3, font=("", 12))
    e1.place(x=350, y=90, width=120)

    u2 = Label(f3, text="Last Name", bg="black", fg="white")
    u2.place(x=250, y=130)

    e1 = Entry(f3, font=("", 12))
    e1.place(x=350, y=130, width=120)

    u2 = Label(f3, text="Registration ID", bg="black", fg="white")
    u2.place(x=250, y=170)

    e1 = Entry(f3, font=("", 12))
    e1.place(x=350, y=170, width=120)

    u2 = Label(f3, text="Mobile no.", bg="black", fg="white")
    u2.place(x=250, y=210)

    e1 = Entry(f3, font=("", 12))
    e1.place(x=350, y=210, width=30, height=22)
    e1 = Entry(f3, font=("", 12))
    e1.place(x=390, y=210, width=120)

    u2 = Label(f3, text="Adress", bg="black", fg="white")
    u2.place(x=250, y=250)

    e1 = Entry(f3, font=("", 12))
    e1.place(x=350, y=250, width=120, height=30)

    u2 = Label(f3, text="Set Password", bg="black", fg="white")
    u2.place(x=250, y=290)

    e1 = Entry(f3, font=("", 12),show="*")
    e1.place(x=350, y=290, width=120, height=30)

    b3 = Button(f3, text="Register", command=calculator)
    b3.place(x=310, y=360, width=100, height=40)

    b2 = Button(f3, text="Back", command=home)
    b2.place(x=310, y=430, width=100, height=40)


def calculator():
    locale.setlocale(locale.LC_ALL, '')
    root = Tk.Tk()
    root.title("Income Tax Calculator")
    root.geometry("900x300")
    TaxFreeNum = 250000

    def callback():
        GetGrossTax = GrossTaxIn.get()
        GrossYear = float(GetGrossTax)
        GrossMonth = GrossYear / 12
        GrossWeek = GrossYear / 52
        GrossDay = GrossYear / 365
        Yearli = Tk.Label(RightFrame, text='₹{:,.2f}'.format(GrossYear))
        Yearli.grid(row=1, column=1)
        Monthli = Tk.Label(RightFrame, text='₹{:,.2f}'.format(GrossMonth))
        Monthli.grid(row=1, column=2)
        Weekli = Tk.Label(RightFrame, text='₹{:,.2f}'.format(GrossWeek))
        Weekli.grid(row=1, column=3)
        Dayli = Tk.Label(RightFrame, text='₹{:,.2f}'.format(GrossDay))
        Dayli.grid(row=1, column=4)

        TaxFreeYear = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TaxFreeNum))
        TaxFreeYear.grid(row=2, column=1)
        TaxFreeMonth = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TaxFreeNum / 12))
        TaxFreeMonth.grid(row=2, column=2)
        TaxFreeWeek = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TaxFreeNum / 52))
        TaxFreeWeek.grid(row=2, column=3)
        TaxFreeDay = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TaxFreeNum / 365))
        TaxFreeDay.grid(row=2, column=4)

        if GrossYear > 250000:
            TotalTaxableYear = Tk.Label(RightFrame, text='₹{:,.2f}'.format(GrossYear - TaxFreeNum))
            TotalTaxableYear.grid(row=3, column=1)
            TotalTaxableMonth = Tk.Label(RightFrame, text='₹{:,.2f}'.format(GrossMonth - TaxFreeNum / 12))
            TotalTaxableMonth.grid(row=3, column=2)
            TotalTaxableWeekly = Tk.Label(RightFrame, text='₹{:,.2f}'.format(GrossWeek - TaxFreeNum / 52))
            TotalTaxableWeekly.grid(row=3, column=3)
            TotalTaxableDaily = Tk.Label(RightFrame, text='₹{:,.2f}'.format(GrossDay - TaxFreeNum / 365))
            TotalTaxableDaily.grid(row=3, column=4)
        else:
            TotalTaxableYear = Tk.Label(RightFrame, text='₹0.00')
            TotalTaxableYear.grid(row=3, column=1)
            TotalTaxableMonth = Tk.Label(RightFrame, text='₹0.00')
            TotalTaxableMonth.grid(row=3, column=2)
            TotalTaxableWeekly = Tk.Label(RightFrame, text='₹0.00')
            TotalTaxableWeekly.grid(row=3, column=3)
            TotalTaxableDaily = Tk.Label(RightFrame, text='₹0.00')
            TotalTaxableDaily.grid(row=3, column=4)

        if GrossYear > 1500000:
            AdditionalRate = GrossYear - 1500000
            AdditionalRateTax = Tk.Label(RightFrame, text='₹{:,.2f}'.format(AdditionalRate * 0.30))
            AdditionalRateTax.grid(row=6, column=1)
            HigherRate = Tk.Label(RightFrame, text='₹{:,.2f}'.format(500000 * 0.25))
            HigherRate.grid(row=5, column=1)
            BasicRate = Tk.Label(RightFrame, text='₹{:,.2f}'.format(750000 * 0.10))
            BasicRate.grid(row=4, column=1)
            TotalIn = (150000 * 0.10) + (200000 * 0.25) + (AdditionalRate * 0.30)

        elif GrossYear <= 1500000 and GrossYear >= 1000000:
            HigherRate = GrossYear - 1000000
            HigherRateTax = Tk.Label(RightFrame, text='₹{:,.2f}'.format(HigherRate * 0.25))
            HigherRateTax.grid(row=5, column=1)
            BasicRate = Tk.Label(RightFrame, text='₹{:,.2f}'.format(150000 * 0.10))
            BasicRate.grid(row=4, column=1)
            AdditionalRateTax = Tk.Label(RightFrame, text='₹0.00')
            AdditionalRateTax.grid(row=6, column=1)
            TotalIn = (34449 * 0.10) + (HigherRate * 0.25)

        elif GrossYear <= 999999 and GrossYear >= 250001:
            BasicRate = GrossYear - 250001
            BasicRateTax = Tk.Label(RightFrame, text='₹{:,.2f}'.format(BasicRate * 0.10))
            BasicRateTax.grid(row=4, column=1)
            HigherRateTax = Tk.Label(RightFrame, text='₹0.00')
            HigherRateTax.grid(row=5, column=1)
            AdditionalRateTax = Tk.Label(RightFrame, text='₹0.00')
            AdditionalRateTax.grid(row=6, column=1)
            TotalIn = (BasicRate * 0.10)

        else:
            TotalIn = 0

        TotalNetTax = round(TotalIn)
        TotalNetTaxLi = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TotalNetTax))
        TotalNetTaxLi.grid(row=9, column=1)

        TotalNetWages = GrossYear - TotalNetTax
        TotalNetWagesMonthly = TotalNetWages / 12
        TotalNetWagesWeekly = TotalNetWages / 52
        TotalNetWagesDaily = TotalNetWages / 365
        TotalNetWagesLi = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TotalNetWages))
        TotalNetWagesLi.grid(row=10, column=1)
        TotalNetWagesMonthlyLi = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TotalNetWagesMonthly))
        TotalNetWagesMonthlyLi.grid(row=10, column=2)
        TotalNetWagesWeeklyLi = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TotalNetWagesWeekly))
        TotalNetWagesWeeklyLi.grid(row=10, column=3)
        TotalNetWagesDailyLi = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TotalNetWagesDaily))
        TotalNetWagesDailyLi.grid(row=10, column=4)

    LeftFrame = Tk.Frame(root, width=300, height=200, pady=3)
    RightFrame = Tk.Frame(root, width=400, height=200, pady=3)

    LeftFrame.grid(sticky="n", row=0, column=0)
    RightFrame.grid(sticky="n", row=0, column=1)

    TaxYearOp = Tk.StringVar()
    TaxYearOp.set("2020/2021")

    TaxYear = Tk.Label(LeftFrame, text="Select tax year")
    TaxYear.grid(row=1, column=0)

    Placeholder = Tk.Label(LeftFrame, text="")
    Placeholder.grid(row=1, column=1)

    TaxYearLi = Tk.OptionMenu(Placeholder, TaxYearOp, "2020/2021")
    TaxYearLi.grid(row=1, column=1)
    Placeholder2 = Tk.Label(LeftFrame, text="")
    Placeholder2.grid(row=2, column=1)
    Pension = Tk.Label(LeftFrame, text="Pension contributions (₹)")
    Pension.grid(row=3, column=0)
    PensionEn = Tk.Entry(LeftFrame)
    PensionEn.grid(row=3, column=1)
    GrossTaxLa = Tk.Label(LeftFrame, text="annual earnings here! >")
    GrossTaxLa.grid(row=4, column=0)
    GrossTaxIn = Tk.Entry(LeftFrame)
    GrossTaxIn.grid(row=4, column=1)
    TaxCalGo = Tk.Button(LeftFrame, text="Calculate My Wage", command=callback)
    TaxCalGo.grid(row=5, column=1)

    Summary = Tk.Label(RightFrame, text="Salary Summary", width=15)
    Summary.grid(row=0, column=0)
    Yearly = Tk.Label(RightFrame, text="Year", width=10)
    Yearly.grid(row=0, column=1)
    Monthly = Tk.Label(RightFrame, text="Monthly", width=10)
    Monthly.grid(row=0, column=2)
    Weekly = Tk.Label(RightFrame, text="Weekly", width=10)
    Weekly.grid(row=0, column=3)
    Daily = Tk.Label(RightFrame, text="Daily", width=10)
    Daily.grid(row=0, column=4)

    Summary = Tk.Label(RightFrame, text="Salary Summary", width=15)
    Summary.grid(row=0, column=0)
    GrossPay = Tk.Label(RightFrame, text="Gross Pay", width=15)
    GrossPay.grid(row=1, column=0)
    TaxFree = Tk.Label(RightFrame, text="Tax Free Allowance", width=15)
    TaxFree.grid(row=2, column=0)
    TotalTaxable = Tk.Label(RightFrame, text="Total Taxable", width=15)
    TotalTaxable.grid(row=3, column=0)
    Tax20 = Tk.Label(RightFrame, text="10% rate", width=15)
    Tax20.grid(row=4, column=0)
    Tax40 = Tk.Label(RightFrame, text="25% rate", width=15)
    Tax40.grid(row=5, column=0)
    Tax45 = Tk.Label(RightFrame, text="30% rate", width=15)
    Tax45.grid(row=6, column=0)
    TotalDeductions = Tk.Label(RightFrame, text="Total Deductions", width=15)
    TotalDeductions.grid(row=9, column=0)
    NetWage = Tk.Label(RightFrame, text="Net Wage", width=15)
    NetWage.grid(row=10, column=0)

def feed():
    f5= Frame(bg="sky blue")
    f5.place(x=70, y=0, width=700, height=600)
    
    u1= Label(f5, text="Leave Feedback", bg="pink", fg="brown")
    u1.place(x=100, y=20)
    e1 = Entry(f5, font=("",20))
    e1.place(x=100, y=50, width=450,height=200)
    
    b2 = Button(f5, text="Submit", command=home)
    b2.place(x=150, y=280, width=100, height=40)
    b2 = Button(f5, text="Back", command=home)
    b2.place(x=150, y=325, width=100, height=40)

def contact():
    
    f6= Frame(bg="sky blue")
    f6.place(x=70, y=0, width=600, height=600)
    
    u1= Label(f6, text="OUR INFO :", bg="pink", fg="brown")
    u1.place(x=100, y=20)

    u2= Label(f6, text="EMAIL : taxcal@gmail.com", bg="white", fg="brown")
    u2.place(x=100, y=50)

    u3= Label(f6, text="PHONE NO. : 987654", bg="white", fg="brown")
    u3.place(x=100, y=80)
    
    u4= Label(f6, text="SERVICE CENTER : Gandhi Market, Phagwara, Punjab", bg="white", fg="brown")
    u4.place(x=100, y=110)

    
    u4= Label(f6, text="OTHER WEBSITE : www.taxmanage.com", bg="white", fg="brown")
    u4.place(x=100, y=140)


    b2 = Button(f6, text="Back", command=home)
    b2.place(x=100, y=180, width=100, height=36)

def about():
    
    f10= Frame(bg="black")
    f10.place(x=00, y=0, width=600, height=600)
    f7= Frame(bg="sky blue")
    f7.place(x=80, y=0, width=600, height=600)
    
    u1= Label(f7, text="OUR FUNCTIONALITY :", bg="grey", fg="white")
    u1.place(x=100, y=20)
    
    u1= Label(f7, text="~  We calculate tax for salaried employer over his over all income", bg="pink", fg="brown")
    u1.place(x=100, y=60)
    
    u3= Label(f7, text="~  We keep track of your pension", bg="pink", fg="brown")
    u3.place(x=100, y=100)
    
    u3= Label(f7, text="~  We help you calculating tax on monthly yearly weekly and daily basis", bg="pink", fg="brown")
    u3.place(x=100, y=140)
    
    u3= Label(f7, text="~  This website helps you know your tax free allowance", bg="pink", fg="brown")
    u3.place(x=100, y=180)
    
    u3= Label(f7, text="~  It create a chart of all the taxes", bg="pink", fg="brown")
    u3.place(x=100, y=220)
    
    u3= Label(f7, text="~  It tells your net wages", bg="pink", fg="brown")
    u3.place(x=100, y=260)
    b2 = Button(f7, text="Back", command=home)
    b2.place(x=100, y=300, width=100, height=36)

def chart():
    
    f9= Frame(bg="yellow")
    f9.place(x=0, y=0, width=940, height=600)

    
    f8= Frame(bg="sky blue")
    f8.place(x=150, y=0, width=600, height=350)
    
    u1= Label(f8, text="TAX RATES", bg="PINK", fg="black")
    u1.place(x=280, y=10)
    
    u1= Label(f8, text="For salary>1500000        :", bg="grey", fg="white")
    u1.place(x=140, y=50)
    
    u1= Label(f8, text="tax is 30%", bg="white", fg="grey")
    u1.place(x=440, y=50)


    
    u1= Label(f8, text="For salary <= 1500000 and salary >= 1000000   :", bg="grey", fg="white")
    u1.place(x=140, y=100)
    
    u1= Label(f8, text="tax is 25%", bg="white", fg="grey")
    u1.place(x=440, y=100)

    
    u1= Label(f8, text="For salary>2500000        :", bg="grey", fg="white")
    u1.place(x=140, y=150)
    
    u1= Label(f8, text="tax is negotiable", bg="white", fg="grey")
    u1.place(x=440, y=150)

    
    
    u1= Label(f8, text="For salary <= 999999 and salary >= 250001  :", bg="grey", fg="white")
    u1.place(x=140, y=200)
    
    u1= Label(f8, text="tax is 10%", bg="white", fg="grey")
    u1.place(x=440, y=200)

    b2 = Button(f8, text="Back", command=home)
    b2.place(x=250, y=240, width=90, height=30)
    
    b2 = Button(f8, text="Query", command=feed)
    b2.place(x=250, y=275, width=90, height=30)


    
def home():
    f1 = Frame(bg="sky blue")
    f1.place(x=0, y=0, width=850, height=600)
    u7= Label(f1, text="TAX  CALCULATOR", font=("", 25), bg="white", fg="brown")
    u7.place(x=270, y=50,width=320, height=80)
    
    b3 = Button(f1, text="LOGIN ", font=("", 12),fg="white",bg="black",command=login)
    b3.place(x=200, y=150, width=220, height=60)
    u1= Label(f1, text="if already user", bg="white", fg="grey")
    u1.place(x=270, y=200)
    
    b2 = Button(f1, text="REGISTER ", font=("", 12),bg="black",fg="white",command=detail)
    b2.place(x=200, y=250, width=220, height=60)
    
    u1= Label(f1, text="if new user", bg="white",fg="grey")
    u1.place(x=276, y=300)
    

    b4 = Button(f1, text="Tax Chart",bg="purple",fg="white",command=chart)
    b4.place(x=520, y=170, width=120, height=30)

    b5 = Button(f1, text="About Website",bg="green",fg="white",command=about)
    b5.place(x=520, y=205, width=120, height=30)

    b7 = Button(f1, text="Contact Us",bg="blue",fg="white",command=contact)
    b7.place(x=520, y=240, width=120, height=30)
    
    b6 = Button(f1, text="Feedback",bg="orange",fg="white",command=feed)
    b6.place(x=520, y=275, width=120, height=30)


home()
t.mainloop()
