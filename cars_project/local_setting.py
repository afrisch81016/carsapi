# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3llu5ap=6ge1equcpb!n)s%k3e4*vy58*(e)a*t&te4e@04xw('

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "cars_database",
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password'
    }
}

