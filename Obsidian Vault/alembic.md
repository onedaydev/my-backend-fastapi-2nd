1. install
```
pip install alembic
```

2. init
```
alembic init migrations
```

alembic.ini 파일에서 sqlalchemy.url 값을 database.py에서 설정한 db url과 동일하게 설정
migrations 폴더 내 env.py에서 target_metadata = models.Base.metadata 설정

3. generate revision file
```
alembic revision --autogenerate
```

4. execute revision file
```
alembic upgrade head
```

