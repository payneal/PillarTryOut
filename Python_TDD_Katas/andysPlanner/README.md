# Andys Planner

## to run test 
* create virtualenv
* pip install -r requirements.txt
* python app/application.py 
* lettuce test/features

## Api must do the following
* POST - add customer(customer has address, first name, last name, balance, cost, special instruction)
* POST - assign customer to a day

* GET - grab individual customer and all info assoicated with said customer
* GET- must be able to grab a list of customers, just first name  and last name but returned in alphabetical order(by first name)
* GET - all customers that have negitive balance
* GET - Total amount paid for a day and Expected total
* GET - total amount paid for a month and expected Total 
* GET - Calender of month with all work (customer, customer status for that day

* DELETE - delete a customer from day
* DELETE - delete a customer from database

* PUT - update a  customers info
* PUT - update a customers balance for a paticular day

##  Files 
* steps.py = code which is executed by the .feature files 
* user.feature = the behavior test which describe the functionality of the users endpoint in application
* application.py = the entry point where our Flask application is created and the server is started 
* views.py = code to handle thr registration of views and defines the response to various HTTP request made on the view 

