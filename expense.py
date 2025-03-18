import json
from datetime import datetime


list_exp = [{'ID': 1 ,'Date': '2025-01-15', 'Description': 'pizza', 'amount': 290},
            {'ID': 2 ,'Date': '2025-03-18', 'Description': 'burek','amount': 290,},
            {'ID': 3 ,'Date': '2025-03-18', 'Description': 'pljeskavica', 'amount': 310},
            {'ID': 4 ,'Date': '2025-05-18', 'Description': 'cevapi', 'amount': 400}]

allExpenses = {}
monthExpense = {}

class Expense(): 


    def activate_exp(self): 
    

        while True:

            question = input('Do you want to add your expense? [y/n]: ')

            if question == 'y':

                while True:

                    iD = int(input('Your ID: '))
                    date = input('Enter date\nIf you want today date type[t] or create new[n]: ')
                    if date == 't':
                        t = datetime.today().strftime('%Y-%m-%d')
                        description = input('Enter description: ')
                        amount = int(input('Enter amount: '))
                        list_exp.append({'ID': iD ,'Date': t,'Description': description, 'amount': amount })
                        print('Expense added successfully!')
                        breaking = input('Do you want to add more?: [y/n]')
                    elif date == 'n':
                        newDate = input('Enter date: ')
                        description = input('Enter description: ')
                        amount = int(input('Enter amount: '))
                        list_exp.append({'ID': iD ,'Date': newDate,'Description': description, 'amount': amount })
                        print('Expense added successfully!')
                        breaking = input('Do you want to add more?: [y/n]')
                            

                    if breaking == 'y':
                        continue

                    elif breaking == 'n':
                        print('Thank you')
                        break
                    break
                    



            elif question =='n':
                if len(list_exp) == 0:
                    print('Sorry your list is empty')

                else:
                    print('Thank you')
                    break
            else:
                print('Try again')




    def view_exp(self):

        if len(list_exp) == 0:
            print('Sorry your list is empty')


        else:
            print('*** Total Expenses ***\n')
            for list_e in list_exp:
                for key, value in list_e.items():      
                        print(f'{value}', end = '    ')               
                print('   ')    
                
                
                
    def updat(self):
        
        while True:
            print('*** Update Expense ***\n')
            print('1. Update ID')
            print('2. Update Date')
            print('3. Update Description')
            print('4. Update Amount')
            print('5. Quit')
            upd = int(input('Enter number: : '))  
            
            if upd == 1:
                print('All ID-s we have in arhive')
                for list_e in list_exp:
                    keep = list_e['ID']
                    desc = list_e['Description']
                    print(f'Id ~ {keep} {desc}')
                upd_id = int(input('Enter ID you want to change: '))
                for list_e in list_exp:
                    if upd_id in list_e.values():
                        new_id = int(input('Enter a new ID: '))
                        list_e.update({'ID': new_id})
                        
                    
       
       
            elif upd == 2:
                upd_id = int(input('Enter ID for date you want to change: '))
                for list_e in list_exp:
                    if upd_id in list_e.values():
                        keep = list_e['Date']
                        print(f'The current date ~ {keep}')
                        new_date = input('Enter your new date: ')
                        list_e.update({'Date': new_date})
        
            elif upd == 3:
                upd_desc = int(input('Enter ID for description you want to change: '))
                for list_e in list_exp:
                    if upd_desc in list_e.values():
                        keep = list_e['Description']
                        print(f'The current date ~ {keep}')
                        new_desc = input('Enter your new description: ')
                        list_e.update({'Description': new_desc})
                        
            elif upd == 4:
                upd_am = int(input('Enter ID for amount you want to change: '))
                for list_e in list_exp:
                    if upd_am in list_e.values():
                        keep = list_e['amount']
                        print(f'The current date ~ {keep}')
                        new_desc = input('Enter new amount: ')
                        list_e.update({'amount': new_desc})            
                         
            elif upd == 5:
                break  
            
            
            
    def summary_exp(self):
        
        spec_month = {'Jan':'2025-01',
                      'Feb':'2025-02',
                      'Mar':'2025-03',
                      'Apr':'2025-04',
                      'May':'2025-05',
                      'Jun':'2025-06',
                      'Jul':'2025-07',
                      'Aug':'2025-08',
                      'Sep':'2025-09',
                      'Oct':'2025-10',
                      'Nov':'2025-11',
                      'Dec':'2025-12',}
        list = []
        month_list = []
        
        print('*** Summary of your expeses ***\n')
        print('1. View summary of all expenses')
        print('2. View summay of specific month')
        
        choice = int(input('Enter you choise: '))
        
        if choice == 1:
            for list_e in list_exp:
                keep = list_e['amount']
                list.append(keep)
                sum_list = sum(list)
                
            print(f'Total summary of all your expenses is\n[{sum_list}]')
        
        elif choice == 2:
            for list_e in list_exp:
                keep = list_e['Date']
                
  
            choice = input('Enter month: ')
            if choice in spec_month.keys():
                for key, value in spec_month.items():
                    if choice == key:
                        for list_e in list_exp:
                            keep = list_e['Date']
                            if value in keep:
                                am = list_e['amount']
                                month_list.append(am)
                                suming = sum(month_list)
                print(f'Total summary of your choisen month is [{suming}]')
            else:
                print('Error')    

                    
    def save_exp(self):
        count = 0
        while True:
            print('\n==== Tasks to Save ===== ')
            print('1. Save all expenses')
            print('2. Back')
            
            save = int(input('Enter number: '))
            if save == 1:
                if len(list_exp) == 0:
                    print('Your dont have any expense') 
                else: 
                    count +=1     
                    with open(f'allEpenses{count}.json','w') as file:
                        json.dump(list_exp, file)
                                           
            elif save == 2:
                print('Thank you!')
                break
            else:
                print('Sorry we dont have that option. Please try again!')              
   
                    

                    
                   

            
    def delete_exp(self):
        print('*** Delete your Expense ***\n')

        for list_e in list_exp:
            for key, value in list_e.items():      
                    print(f'{value}', end = '    ')               
            print('   ')   
             
        choice = int(input('Enter ID of expense you want to delete: '))
        for list_e in list_exp:
            if choice in list_e.values():
                list_exp.remove(list_e)
 




                
    def main(self):
        exp = Expense()


        while True:
    
            print('**** Expense Task ****')
            print('1. Add expense')
            print('2. View expenses')
            print('3. Update expenses')
            print('4. Summary')
            print('5. Save your expenses')
            print('6. Delete your expense')

            enter = input('Enter your choise: ')

            if enter == '1':
                exp.activate_exp()
            elif enter == '2':
                exp.view_exp()
            elif enter == '3':
                exp.updat()
            elif enter == '4':
                exp.summary_exp()     
            elif enter == '5':
                exp.save_exp()
            elif enter == '6':
                exp.delete_exp()    
            else:
                print('We dont have that option. Please try again!')
               
                



    

                     

                        
                        
                
                


if __name__ == '__main__':
    activate = Expense()
    work = activate.main()
    












        
            # try:
            #     with open (save +''+ '.json','w') as f:
            #         json.dump(list_exp, f)

            # except FileExistsError:
            #     print('Sorry')  

   
