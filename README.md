

# DB user
you need to change mysql db meta info in setting.py if download to local for test
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LittleLemon',
        'USER': 'root',
        'PASSWORD': 'pwd@1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```


# Super user: change to your local username/password
```
username: admin
email: admin@littlelemon.com
password: admin@123
login url: http://127.0.0.1:8000/admin/login/?next=/admin/
```


# Review criteria

**Does the web application use Django to serve static HTML content?**

YES

![](./README/1.1.jpg)
![](./README/1.jpg)


**Has the learner committed the project to a Git repository?**
YES
https://github.com/AlexanderLv/LittleLemon.git
git@github.com:AlexanderLv/LittleLemon.git

**Does the application connect the backend to a MySQL database?**
YES

![](./README/3.jpg)

**Are the menu and table booking APIs implemented?**

YES
![](./README/4.jpg)
![](./README/4.1.jpg)
![](./README/4.2.jpg)

**Is the application set up with user registration and authentication?**

YES
![](./README/5.1.jpg)
![](./README/5.2.jpg)
![](./README/5.3.jpg)

**Does the application contain unit tests?**
YES
![](./README/6.1.jpg)
![](./README/6.2.jpg)

**Can the API be tested with the Insomnia REST client?**

YES, see above


thanks.