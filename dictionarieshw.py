# Lesson 1: Assignments | Dictionaries
# 1. Real-World Python Dictionary Applications
# Task 1: Restaurant Menu Update
#-------------------------------------------------------------
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu.update({'Beverage': {'Sparkling Water': 0.78, 'Minute Maid': 2.08}})
restaurant_menu['Main Course'].update({'Steak': 17.99})
restaurant_menu['Starters'].pop('Bruschetta')
print(restaurant_menu)

#-------------------------------------------------------------


# 2. Python Programming Challenges for Customer Service Data Handling
# Task 1: Customer Service Ticket Tracker

service_ticket = {
        'Ticket#1': {'Customer': 'Samantha', 'Issue': 'Login In', 'Status':'Closed'}, 
        'Ticket#2': {'Customer': 'Larry', 'Issue': 'Password Rest', 'Status': 'Open'},
        'Ticket#3': {'Customer': 'Keisha', 'Issue': 'Data Loss', 'Status': 'Open'}
            }
ticket = {}

def open_new(ticket):
    ticket_number = 'Ticket#' + str(len(service_ticket) + 1)
    customer = input('Enter customer name: ')
    issue = input('Enter issue description: ')
    status = 'Open'
    service_ticket[ticket_number] = {'Customer': customer, 'Issue': issue, 'Status': status}
    print(service_ticket)


def update (ticket):
    user_input = input('Enter ticket number for the ticket you want to update?')
  
    if user_input in service_ticket:
          if  service_ticket[user_input]['Status'] == 'Closed': 
            service_ticket[user_input]['Status'] = 'Open' 
            print(service_ticket)
          elif  service_ticket[user_input]['Status'] == 'Open':
            service_ticket[user_input]['Status'] = 'Closed' 
            print(service_ticket)
    
    else:
        print('Please enter a valid ticket')


def view (ticket):
    print(service_ticket)

def track (ticket):
    while True:
        user_input = input ('''
            How can I help ypu today? 
            1. Open a new ticket
            2. Update the status of an existing ticket
            3. Display all tickets
                ''')
        if user_input == '1':
            open_new(ticket)

        elif user_input == '2':
            update(ticket)

        elif user_input == '3':
            view(ticket)
        else:
            print('Please enter a number ')

track (ticket)   











