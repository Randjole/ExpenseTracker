import json



list_exp = []


class Expense(): 


    def activate_exp(self): 
    

        while True:

            question = input('Do you want to add your expense? [y/n]: ')

            if question == 'y':

                while True:

                    iD = input('Your ID: ')
                    date = input('Enter date: ')
                    description = input('Enter description: ')
                    amount = input ('Enter amount: ')

                    list_exp.append({'ID': iD ,'Date': date, 'Description': description })
                    breaking = input('Do you want to add more?: [y/n]')

                    if breaking == 'y':
                        continue

                    elif breaking == 'n':
                        break



            elif question =='n':
                if len(list_exp) == 0:
                    print('Sorry your list is empty')

                else:
                    print('Thank you this is your list')
                    print(list_exp)
                    break
            else:
                print('Try again')


    def view_exp(self):

        if len(list_exp) == 0:
            print('Sorry your list is empty')


        else:
            print('ID Date Desription amount')
            for list_e in list_exp:
                for key, value in list_e.items():
                    print(f'{key} {value}')
                    



    


    def main(self):
        exp = Expense()


        while True:
    
            print('**** Expense Task ****')
            print('1. Add expense')
            print('2. View expenses')

            enter = input('Enter your choise: ')

            if enter == '1':
                exp.activate_exp()
            if enter == '2':
                exp.view_exp()








        











if __name__ == '__main__':
    activate = Expense()
    work = activate.main()
    












        
            # try:
            #     with open (save +''+ '.json','w') as f:
            #         json.dump(list_exp, f)

            # except FileExistsError:
            #     print('Sorry')  

   
