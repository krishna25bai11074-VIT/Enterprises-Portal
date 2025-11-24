print('|----------------------------------------Somika Enterprises------------------------------------|')
print('|---------------------------------------------Portal-------------------------------------------|')


import statistics
from Data import *
import random
ans='y'
while ans in 'yY':
    print('Dashboard:- 1) GST Information 📃')
    print('            2) GST Invoice Generator 💸')
    print('            3) Aniversary Special 🎁')
    print('            4) Enter More Information 📝')
    print('            5) Exit              ')
    opt=int(input('Enter Any Option'))
    if opt==1:
        print('Menu:-  1) Sale Price')
        print('        2) GST Percentage')
        print('        3) GST Rate')
        opt1=int(input('Choose:- '))
        if opt1==1:
            def option(l):
                print('Menu:-   1) Highest Sale Price')
                print('         2) Lowest Sale Price')
                print('         3) Average Sale Price')
                print('         4) Total Sale Price')
                print('         5) Most Frequent Sale Price')
                opt2=int(input('Choose:-'))
                if opt2==1:
                    print('Highest Sale Price :- ₹',max(l))
                elif opt2==2:
                    print('Lowest Sale Price :- ₹',min(l))
                elif opt2==3:
                    print('Average Sale Price :- ₹',statistics.mean(l))
                elif opt2==4:
                    print('Total Sale Price :- ₹',sum(l))
                elif opt2==5:
                    print('Most Frequent Sale Price :- ₹',statistics.mode(l))
            P=[]
            for i in Info:
                 P.append(i['Price'])
            option(P)
        elif opt1==2:
            def option(l):
                print('Menu:-   1) Highest GST Percentage Applied')
                print('         2) Lowest GST Percentage Applied')
                print('         3) Total GST Percentage Applied')
                print('         4) Most Frequent GST Percentage Applied')
                opt2=int(input('Choose:-'))
                if opt2==1:
                    print('Highest GST Percentage Applied :- ',max(l),'%')
                elif opt2==2:
                    print('Lowest GST Percentage Applied :- ',min(l),'%')
                elif opt2==3:
                    print('Total GST Percentage Applied :- ',sum(l),'%')
                elif opt2==4:
                    print('Most Frequent GST Percentage Applied :- ',statistics.mode(l),'%')
            G=[]
            for i in Info:
                G.append(i['GST_P'])
            option(G)
        elif opt1==3:
            def option(l):
                print('Menu:-   1) Highest GST Rate Applied')
                print('         2) Lowest GST Rate Applied')
                print('         3) Total GST Rate Applied')
                print('         4) Most Frequent GST Rate Applied')
                opt2=int(input('Choose:-'))
                if opt2==1:
                    print('Highest GST Rate Applied :- ₹',max(l))
                elif opt2==2:
                    print('Lowest GST Rate Applied :- ₹',min(l))
                elif opt2==3:
                    print('Total GST Rate Applied :- ₹',sum(l))
                elif opt2==4:
                    print('Most Frequent GST Rate Applied :- ₹',statistics.mode(l))
            R=[]
            for i in Info:
                R.append(i['GST_R'])
            option(R)
        else:
            print('Enter Valid Option')
    elif opt==2:


        print('|--------------------------------🪙💵 GST Invoice Generator 🪙💵-------------------------------|')
        print('')
        print('')
                                                                             # Please Enter only Given Data in Inputs for Proper Functioning :)
        Enterprise_Name=input('Enter Name of Your Enterprise')               # Swades Enterprises
        H_No=input('Enter  House Number/Plot Number')                        # 6478
        Gali_No=input('Enter Gali Number/Street Number/Lane Number')         # 4
        Locality=input('Enter Locality')                                     # Holyground
        City=input('Enter City')                                             # Gurugram
        State=input('Enter State')                                           # Haryana
        sh_tof=input('Enter Shipping House No./Flat No.')                    # Flat No.-267,Tower-2
        sh_toa=input('Enter Shipping Locality/Appartments')                  # PUS-2,Sector-86
        sh_toc=input('Enter Shipping City')                                  # Gurugram
        sh_tos=input('Enter Shipping State')                                 # Haryana
        Des_Go=input('Enter Name of Good')                                   # HP Omnibook
        Qty=int(input('Enter Quantity of Item'))                             # 1
        Rate=input('Enter Rate of Item')                                     # 86,100
        GST_Rate=input('Enter GST Amount')                                   # 18,900
        GST_Per=int(input('Enter GST Percentage'))                           # 1,05,000


        def invoice_Our():
                    print('')
                    print('|---------------------------------------------------------------------------------------------|')
                    print('|                                       ',Enterprise_Name,'                                  |',)
                    print('|                                       ',H_No,Gali_No,Locality,'                                   |')
                    print('|                                       ',City,State,'                                    |')
                    print('|---------------------------------------------------------------------------------------------|')
                    print('| Shipping Address --',sh_tof,'                                                   |')
                    print('|                    ',sh_toa,'                                                        |')
                    print('|                    ',sh_toc,sh_tos,'                                                       |')
                    print('|---------------------------------------------------------------------------------------------|')
                    print('|                                                                                             |')
                    print('| Invoice No.-ACP/25-48/0013567','                                           ','Dated-21-Nov-2025 |')
                    print('|---------------------------------------------------------------------------------------------|')
                    print('| S No. |','    Description of Goods    |',' Quantity |','   Rate   |','  GST Rate  |',' GST Percentage |')
                    print('|   1   |','        HP Omnibook         |','    1     |',' 86,100/- |','  18,900/-  |','       18%      |')
                    print('|       |','                            |','          |','          |','            |','                |')
                    print('|       |','                            |','          |','          |','            |','                |')
                    print('|       |','                            |','          |','          |','            |','                |')
                    print('|       |','                            |','          |','          |','            |','                |')
                    print('|       |','                            |','          |','          |','            |','                |')
                    print('|       |','                            |','          |','          |','            |','                |')
                    print('|       |','                            |','          |','          |','            |','                |')
                    print('|       |','                            |','          |','          |','            |','                |')
                    print('|       |','                            |','          |','          |','            |','                |')
                    print('|       |','                            |','          |','          |','            |','                |')
                    print('|       |','                            |','          |','          |','            |','                |')
                    print('|       |','                            |','          |','          |','            |','                |')
                    print('|       |','                            |','          |','          |','            |','                |')
                    print('|       |','                            |','          |','          |','            |','                |')
                    print('|       |','                            |','          |','          |','            |','                |')
                    print('|       |','                            |','          |','          |','            |','                |')
                    print('|_______|_____________________________|___________|___________|____Total -__|____1,05,000/-___|')
                    print('')
        invoice_Our()
    elif opt==3:
        n=[]
        for i in Info:
             n.append(i['Name'])
        print('|-----------------Winner of the Prize form our Past Customer is-',random.choice(n),'🎉🥳')
    elif opt==4:
        new_n=input('Enter Name')
        new_p=input('Enter Product Sold')
        new_pr=int(input('Enter Sale Price'))
        new_GST_p=input('Enter GST Percentage Applied')
        new_GST_r=int(input('Enter GST Rate Applied'))
        new_info={new_n,new_p,new_pr,new_GST_p,new_GST_r}
        Info.append(new_info)
        print('New Data Added Succesfully 🎉:)')   
    elif opt==5:
        exit()
    else:
        print('Please Enter Valid Option')
    ans=input('Do U Want to Work More{y/n}')

print('Hope U Liked Our Portal')
print('Thank You :)')