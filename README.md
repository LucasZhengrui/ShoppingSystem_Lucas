# Shopping System created by Rui Zheng, as known as Lucas
## Here is the solo assessment for Enterprise Software Programming.
### Well, here is the most important information about the open-data resource that I found for this project. I found this [Open data source](https://data.world/promptcloud/amazon-product-dataset-2020/workspace/file?filename=marketing_sample_for_amazon_com-ecommerce__20200101_20200131__10k_data.csv%2Fhome%2Fsdf%2Fmarketing_sample_for_amazon_com-ecommerce__20200101_20200131__10k_data.csv) in data-world platform.

#### 1. About this website application

#### 2. Main features

* View products list with page controller, which is a feature for all kinds of users
* View products details for each product
* Add product to cart on the detail page
* View cart
* Cancel order on the cart page
* Registration
* Login and Logout

#### 3. Database Overview

The structure model could be viewed in [model.py](https://github.com/LucasZhengrui/ShoppingSystem_Lucas/blob/main/models.py)

#### 4. Installation

##### 4.1 If you are using Codio:

###### 4.1.1 Create a virtual environment and activate it in the terminal of Codio
``` shell
    python3 -m venv .venv 
```

``` shell
    source .venv/bin/activate 
```

###### 4.1.2 Clone the repository or pull the code from GitHub
``` shell
    git clone git@github.com:LucasZhengrui/ShoppingSystem_Lucas.git
```
Or if you have cloned before

``` shell
    git pull origin main
```

###### 4.1.3 Changed the site details in **ALLOWED_HOSTS** of ```shopping_system/setting.py```

For example:

``` shell
    ALLOWED_HOSTS = ['127.0.0.1', 'lucass-toys-ecommerce.onrender.com', 'ricardobarbara-nissanventura-8000.codio-box.uk']
```

###### 4.1.4 Install Django in terminal

As for the Django installation

``` shell
    pip install django
```

###### 4.1.5 Run the website application

``` shell
    python3 manage.py runserver 0.0.0.0:8000
```

P.S **8000** is decided by what did you input in 4.1.3

##### 4.2 If you are using a local editor, such as Visual Studio Code, or Mac Terminal:

###### 4.2.1 Create a virtual environment and activate it in the terminal
``` shell
    python3 -m venv .venv 
```

``` shell
    source .venv/bin/activate 
```

###### 4.2.2 Clone the repository or pull the code from GitHub
``` shell
    git clone https://github.com/LucasZhengrui/ShoppingSystem_Lucas.git
```
Or if you have cloned before

``` shell
    git pull origin main
```

###### 4.2.3 Changed the site details in **ALLOWED_HOSTS** of ```shopping_system/setting.py```

For example:

``` shell
    ALLOWED_HOSTS = ['127.0.0.1', 'lucass-toys-ecommerce.onrender.com', 'ricardobarbara-nissanventura-8000.codio-box.uk']
```

###### 4.2.4 Install Django in terminal

As for the Django installation

``` shell
    pip install django
```

###### 4.2.5 Run the website application

``` shell
    python3 manage.py runserver
```

#### 5. Test

We have done unit testing for other apps, which were in the specific test.py files.

#### 6. Details of deploying the website application

The website application has been deployed to Render, here is its URL: https://lucass-toys-ecommerce.onrender.com/ .

Build command:

``` shell
    pip install --upgrade pip && pip install -r requirements.txt
```

Start command:

``` shell
    gunicorn shopping_system.wsgi:application --worker-class=gevent --worker-connections=1000 --workers=4 --bind=0.0.0.0:$PORT
```

#### 7. Development Log:

> * **15/4/2023** Started to do this Project.
> 
> * **19/4/2023** Added Open Source Data.
> 
> * **21/4/2023** Now, we could show the basic data structure on a web page.
> 
> * **22/4/2023** Now, we could show the image of the product.
> 
> * **23/4/2023** Fortunately, we now could link two tables and show them on the detail html page.
> 
> * **24/4/2023** Now, we may use css file to design our pages.
> 
> * **25/4/2023** Now, we added a cart feature with add and cancel, but we have bug at the moment.
> 
> * **30/4/2023** Now, cart feature with add and cancel could be used normally without bugs.
> 
> * **1/5/2023** Now, we started to handle the user part, including login, sign up, and log out.
> 
> * **2/5/2023** Now, we have added a register feature, which has users' database, and now, we could sign up.
> 
> * **2/5/2023** Now, we have added a login feature, and we could login if we have an account that we signed up.
> 
> * **3/5/2023** Now, we have added a logout button and a welcome message, and we could logout if we have logged in.
> 
> * **4/5/2023** We rebuild the user model, in order to connect with Django's user management. Here is a basic version at the moment.
> 
> * **5/5/2023** Search feature has been added, but it needs to be updated later.
> 
> * **5/5/2023** Search feature has been updated, and now, it can be used normally, but the page has some problems.
> 
> * **5/5/2023** Now, we have deployed the project in render, we could browse it at https://lucass-toys-ecommerce.onrender.com/.
> 
> * **5/5/2023** Login users have access to buy and cancel, and the test files have been added.