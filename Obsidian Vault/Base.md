## Structure
```
.
├── __init__.py
├── __pycache__
│   ├── main.cpython-311.pyc
│   ├── test.cpython-311.pyc
│   └── upload_test.cpython-311.pyc
├── database.py
├── dependencies.py
├── domain
│   ├── post
│   │   ├── crud.py
│   │   ├── router.py
│   │   └── schema.py
│   └── user
│       ├── __init__.py
│       ├── crud.py
│       ├── router.py
│       └── schema.py
├── internal
│   ├── __init__.py
│   └── admin.py
├── main.py
├── models.py
└── test
    ├── test.py
    └── upload_test.py
```

## 라이브러리(requirements.txt)
```
python3 -m pip install --upgrade pip

pip install fastapi
pip install "uvicorn[standard]" 
pip install "python-jose[cryptography]" # to generate and verifiy the JWT tokens
pip install "passlib[bcrypt]" # to handle password hash(Bcrypt).
pip install python-multipart # to use forms and receive uploaded files
pip install sqlalchemy # database
pip instsall alembic # database
```