import json 

collection_exp = {'ID': 1,
                  'Date': '13.03.2025',
                  'Description':'Lunch',
                  'Amount': 20}

# def add_exp():
#     expense = input('Add your type of expense: ')
#     bill = input('Enter your bill: ')


#     collection_exp = json.dumps({})
    




def view_exp():
    print('*** View of all your expenses *** ') 
    print('ID  Date  Description  Amount')   
    for k,v in collection_exp.items():
        print(v, end = "   ")






view_exp()