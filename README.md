# FriendShop-Api

<a href="https://github.com/edufvicentini/pokedex-react-js/blob/master/LICENSE">
   <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="React Pokédex is released under the MIT license." />
 </a>

## 💻 About the project

<p>This is an e-commerce API REST that offers functionalities for both admin and customer users.</p>

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

## Author

<a href="https://https://www.linkedin.com/in/eduardofvicentini/">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/95220802?s=400&u=55c93f56de0ea7dfee88bfe5d75a8f795ef89f4b&v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Eduardo Frota Vicentini</b></sub></a> <a href="https://https://www.linkedin.com/in/eduardofvicentini/" title="Rocketseat">🚀</a>


Made with ❤️ by Eduardo Frota Vicentini 👋🏽 Contact me!

[![Linkedin Badge](https://img.shields.io/badge/-Eduardo-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://https://www.linkedin.com/in/eduardofvicentini/)](https://www.linkedin.com/in/eduardofvicentini/) 
[![Gmail Badge](https://img.shields.io/badge/-eduardofvicentini@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:eduardofvicentini@gmail.com)](mailto:tgmarinho@gmail.com)
