# Technical Assay - Dev Program

## Before you start
* Try not to read ahead.
* Do one task at a time. The trick is to learn to work incrementally.
* Make sure you only test for correct inputs, there is no need to test for invalid inputs for this kata.
* Test First!

## Application Description
The current application is oriented to handle a contacts list and the messages you could send to one or many contacts.
It provides the following functionality:

  - User Registration. By opening the URL {server}/signup, you can register in the application. When you enter your email, the app will create a termporal code. You will need to use this temporal code to complete the registration process. Once you enter the temporal code, you will be able to set you username and password.

  - List Contacts. Once you are signed-in in the app, the list contacts page should be displayed.

  - Create a Contact. Within your session, the "Create Contact" option will be visible so you can create a new contact.

  - Send Message. This option lets you to send a single text message to any of your contacts. In the form to create the message, the app should display an option to pick the contact or contacts to send the message to. Also the form will show the "Cancel" button, in case you decided to discard your message.

## Application Structure
This is a REST application, so this repository provides two applications: API and Client.

## Application Requirements
In order to run both applications you will need:

### Database
- Sqlite 3.37.0

### API
- Python 3.1 or higher
- Django 4.0
- Python IDE 

### Client 
- NodeJS 12.18 or higher 
- NPM 6.14

The application is implemented with React.

## How to Run Server
- Run setup.py to install requirement libraries: python ./setup.py install
- Migrate the database using command: python manage.py migrate
- Seed the database: python manage.py loaddata .\contacts\data\seeds\default_users.json
- Run the applicacion with command: python manage.py runserver

## How to Run Client
- Run `npm install` to install node modules
- After that run `npm start` to run the applications

## Problem Description
Once you will be able to run the app, you will notice there are several incomplete features, as follow:

#### User Registration. 
  - **Task 1 (FE):** Add a functionality to logout to the current user so any other user will be able to sing in.

#### Contacts List.
  - **Task 2 (FE):** The landing page for contacts list already exists, however the list of contacts is not being displayed. Detect the problem and fix it.
  - **Task 3 (BE):** Introduce a service class, so the ContactController should use it instead a repository. Also, ensure all unit tests are passing.
  - **Task 4 (BE):** Complete the required logic for the `shouldReturnOkWhenSavingContact` test method.
  - **Task 5 (BE):** Create a new test class for UserController. Add as many tests as you can for the controller.
  - **Task 6 (BE/FE):** 
    * Add a new field in the `Contact` entity class. This new field should be used to store the phone number of the contact. 
    * Update the ContactController in order to validate the phone number when saving a contact. 
    * Update the `Contact` form so the phone number can be added.
    * (Optional) Display the error message(s) in the form when some required fields are missing.
  - **Task 7 (BE/FE):** 
    * Add new funtionality to search contacts by using the email of the contact.
    * Add new funtionality to search contacts by using the phone number of the contact.
    * Implement validation for the input accordingly.
    * Refactor your search functionalities to use a generic logic in the endpoint (BE), so we could use only one endpoint to search any visible contact field.

#### Messages.
  - **Task 8 (BE/FE):**
    * Create a UI form to create a message. The message should be able to send to one or multiple contacts.
    * Ensure the required fields are validated on backend. Display the errors on UI when needed.
    * We already have some endpoitn running on backend
