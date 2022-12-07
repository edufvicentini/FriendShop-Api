# FriendShop-Api

<a href="https://github.com/edufvicentini/FriendShop-Api/blob/master/LICENSE">
   <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="React Pokédex is released under the MIT license." />
 </a>

## 💻 About the project

<p>This is an e-commerce API REST that offers functionalities for both admin and customer users.</p>

## Structure

### Project Structure
```bash
├── .vscode
├── api
   ├── auth                   # Authentication Module
   ├── logs                   
      ├── admin_logs          # Admin Logs Module
      └── user_logs           # User Logs Module
   ├── migrations         # Database migrations
   ├── modules            # Main Operational modules
      ├── categories          # Category Module
      ├── products            # Products Module
      ├── sells               # Sells Module
      └── userCartProducts    # Cart Module
├── .gitignore
├── manage.py             # Main Project file
└── FriendShop
    ├── __init__.py
    ├── asgi.py
    ├── settings.py           # Configuration file
    ├── urls.py               # Available URLs in project
    └── wsgi.py
```

### Module Structure
```bash
Module
├── model.py         # Database model file. Defines the modeling of the entity.
├── serializer.py    # Configuration of serializers. They are responsible for converting django objects to JSON.
├── urls.py          # Endpoints configuration.
├── views.py         # File containing the module useCases and business rules.
└── utils.py         # Optional file with module utilities.
```

## ⚙️ Routes List
<a href="https://github.com/edufvicentini/pokedex-react-js/blob/master/LICENSE">
   <img src="https://img.shields.io/badge/GET-INSOMNIA%20FILE-purple" />
 </a>


### Authentication
| HTTP METHOD | URI               |  Authentication |DESCRIPTION     
| ----------- | ---------------   | --------------| --------------------------      
|  POST       | api/auth/register    | Free | Sign up as a Customer          
|  POST       | api/auth/login       | Free           | Login as a Costumer or Admin   
|  POST       | api/auth/logout      |  Authenticated           | Logout as a Costumer or Admin  
|  GET        | api/auth/login/admin |  Admin    | Tests if user is Admin          

### Products
| HTTP METHOD | URI                               | Authentication |        DESCRIPTION     
| ----------- | ---------------                   | -------------- | --------------------------    
|  GET        | api/products                      | Free           | List all products              
|  POST       | api/products/create               | Admin          | Create a new product          
|  PUT        | api/products/update/{product-id}  |  Admin         | Update an existing product    
|  DELETE     | api/products/delete/{product-id}  |  Admin         | Delete an existing product    
|  GET        | api/products/{product-id}         |  Admin         | Detail a single product        

### Categories
| HTTP METHOD | URI                                 | Authentication |        DESCRIPTION     
| ----------- | ---------------                     | -------------- | --------------------------     
|  GET        | api/categories                      | Free           | List all categories             
|  POST       | api/categories/create               | Admin          | Create a new category           
|  PUT        | api/categories/update/{category-id} |  Admin         | Update an existing category    
|  DELETE     | api/categories/delete/{category-id} |  Admin         | Delete an existing category    
|  GET        | api/categories/{category-id}        |  Admin         | Detail a single category       

### Cart
| HTTP METHOD | URI                                         | Authentication      |        DESCRIPTION     
| ----------- | ---------------                             | --------------     | --------------------------     
|  GET        | api/cart/products                           | Authenticated      | List all products in logged user's cart           
|  POST       | api/cart/products/add                       | Authenticated      | Add a new product in logged user's cart      
|  PUT        | api/cart/products/update/{cart-product-id}  |  Authenticated     | Update quantity of a product in logged user's cart    
|  DELETE     | api/cart/products/delete/{cart-product-id}  |  Authenticated     | Remove a product off logged user's cart   

### Sells
| HTTP METHOD | URI               | Authentication      |        DESCRIPTION     
| ----------- | ---------------   | --------------     | --------------------------     
|  POST       | api/sells/create  | Authenticated      | Finish the cart and create a new sell         
|  GET        | api/sells         | Authenticated      | List all current user's sells  

### Logs
| HTTP METHOD | URI              | Authentication  |        DESCRIPTION     
| ----------- | ---------------  | --------------  | --------------------------     
|  GET        | api/admin/logs   | Admin           | List logs from admin's activity         
|  GET        | api/user/logs    | Admin           | List users activities


---
## 🚀 How to execute the project

### Prerequisites
Before starting, you will need to have the following tools installed on your machine:
- [Git](https://git-scm.com)
- [Python v3.8>=](https://www.python.org/)
- Any SQL Database System like [PostgreSQL](https://www.postgresql.org/) or [Docker](https://www.docker.com/) for running database images. 
- Also it's nice to have an editor to work with the code like [VSCode](https://code.visualstudio.com/).

If you don't have Django installed, run these following lines in your Terminal:

```bash
pip install django
pip install django_rest_framework
```

### Configuring Database
Having Django installed:

```bash
# Clone this repository
git clone git@github.com:edufvicentini/FriendShop-Api.git

# Access the folder in terminal
cd FriendShop-Api

# Open in your editor
code .
```

Inside the project you will have:

```bash
├── .vscode
├── api
├── .gitignore
├── manage.py
└── FriendShop
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

Open settings.py and find the following lines:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # keep this if you are using postgresql
        'NAME': 'postgres',         # your database name
        'USER': 'myusername',       # your database user
        'PASSWORD': 'mypassword',   # your database pasword
        'HOST': 'localhost',        # your database host
        'PORT': '8001',             # your database port
    }
}
```
[Here](https://commandprompt.com/education/how-to-download-and-install-postgresql/) your can find more information about installing PostgreSQL in your computer. If you want to use Docker, follow this [Link](https://imasters.com.br/banco-de-dados/postgresql-docker-executando-uma-instancia-e-o-pgadmin-4-partir-de-containers) instead.

### Running the project

After setting up, open the project folder in your Terminal and execute the following:

```bash
   # Access the folder in terminal
   cd FriendShop-Api
   
   # Make any undone database migrations
   python manage.py makemigrations     
   
   # Run migrations into database
   python manage.py migrate         
   
   # Creates the Admin user. Requires a login and password
   python manage.py createsuperuser
   
   # And finally, run the server
   python manage.py runserver
```

## 

## Author

<a href="https://https://www.linkedin.com/in/eduardofvicentini/">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/95220802?s=400&u=55c93f56de0ea7dfee88bfe5d75a8f795ef89f4b&v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Eduardo Frota Vicentini</b></sub></a> <a href="https://https://www.linkedin.com/in/eduardofvicentini/" title="Rocketseat">🚀</a>


Made with ❤️ by Eduardo Frota Vicentini 👋🏽 Contact me!

[![Linkedin Badge](https://img.shields.io/badge/-Eduardo-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://https://www.linkedin.com/in/eduardofvicentini/)](https://www.linkedin.com/in/eduardofvicentini/) 
[![Gmail Badge](https://img.shields.io/badge/-eduardofvicentini@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:eduardofvicentini@gmail.com)](mailto:tgmarinho@gmail.com)
