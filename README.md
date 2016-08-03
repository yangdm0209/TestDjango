##　创建项目的步骤

1. 创建工程
django-admin startproject mysite
2. 创建app
python manage.py startapp polls
在setting中INSTALLED_APPS添加polls
3. 为Models修改创建迁移文件
python manage.py makemigrations polls
4. 将Models改变更新到数据库中
python manage.py migrate

5. 创建管理员用户
python manage.py createsuperuser

6. 启动服务器
python manage.py runserver


## 小技巧
#### 到出静态文件
`setting.py`添加`STATIC_ROOT = "D:\\web"`
```python
# 导出静态文件到`STATIC_ROOT`
python manage.py collectstatic
```