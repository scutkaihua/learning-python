前端 appfront

cd appfront
cnpm install
cnpm install  vue-resource
cnpm install element-ui


后端 myapp

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

