前端 appfront
    cd appfront
    cnpm install
    cnpm install  vue-resource
    cnpm install element-ui
    npm install -g vue-cli
    vue-init webpack appfront
    cd appfront
    npm install
    npm run dev

创建后端 myproject
  （1）pip install Django
  （2）django-admin startproject myproject
   (3) cd myproject   进入项目根目录，创建一个app：myapp
       python manage.py startapp myapp
   (4)数据库 myproject/settings.py
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'helloworld',
        'USER': 'kaihua',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        }
    }
    在app目录下的models.py里我们简单写一个mode  在views.py添加view 在 urls.py中添加api/

    (5) 把app加入到installed_apps列表里
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
         'myapp',
    ]
    (6)同步
    python manage.py makemigrations myapp
    python manage.py migrate
    (7)运行
    python manage.py runserver

1.前后端分离
参考 https://cloud.tencent.com/developer/article/1005607
    https://blog.csdn.net/lantian_123/article/details/103750347



2.整合
  1.cd appfront
    npm run build
    生成 dist

  2. myproject/settings.py

  (1)添加:
# Add for vuejs
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "appfront/dist/static"),
]
   (2)TEMPLATES路径
   'DIRS': ['appfront/dist'],

   (3)urls.py
     url(r'^$', TemplateView.as_view(template_name="index.html")),


3.不整合下运行
  (1) cd appfront
      npm run dev

      访问:http://localhost:8080/#/

  (2) cd myproject
      python manage.py runserver

      访问: http://127.0.0.1:8000/api/show_user

4.解决跨域
(1)安装 pip install django-cors-headers
(2)myproject/settings.py中添加,注意顺序
   'corsheaders.middleware.CorsMiddleware',

   CORS_ORIGIN_ALLOW_ALL = True

