# FriendShop-Api

<a href="https://github.com/edufvicentini/pokedex-react-js/blob/master/LICENSE">
   <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="React Pokédex is released under the MIT license." />
 </a>

## 💻 About the project

<p>This is an e-commerce API REST that offers functionalities for both admin and customer users.</p>

## ⚙️ Routes List

### Authentication
| HTTP METHOD | URI               |  Authentication |DESCRIPTION     
| ----------- | ---------------   | --------------| --------------------------      |
|  POST       | api/auth/register    | Customer only | Sign up as a Customer           |
|  POST       | api/auth/login       | Any           | Login as a Costumer or Admin    |
|  POST       | api/auth/logout      |  Any          | Logout as a Costumer or Admin   |
|  GET        | api/auth/login/admin |  Admin only   | Tests if user is Admin          |

### Products
| HTTP METHOD | URI                               | Authentication |        DESCRIPTION     
| ----------- | ---------------                   | -------------- | --------------------------     |
|  GET        | api/products                      | Any            | List all products              |
|  POST       | api/products/create               | Admin only     | Create a new product           |
|  PUT        | api/auth/update/{product-id}      |  Admin only    | Update an existing product     |
|  DELETE     | api/products/delete/{product-id}  |  Admin only    | Delete an existing product     |
|  GET        | api/products/{product-id}         |  Admin only    | Detail a single product        |

---

## Author

<a href="https://https://www.linkedin.com/in/eduardofvicentini/">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/95220802?s=400&u=55c93f56de0ea7dfee88bfe5d75a8f795ef89f4b&v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Eduardo Frota Vicentini</b></sub></a> <a href="https://https://www.linkedin.com/in/eduardofvicentini/" title="Rocketseat">🚀</a>


Made with ❤️ by Eduardo Frota Vicentini 👋🏽 Contact me!

[![Linkedin Badge](https://img.shields.io/badge/-Eduardo-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://https://www.linkedin.com/in/eduardofvicentini/)](https://www.linkedin.com/in/eduardofvicentini/) 
[![Gmail Badge](https://img.shields.io/badge/-eduardofvicentini@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:eduardofvicentini@gmail.com)](mailto:tgmarinho@gmail.com)
