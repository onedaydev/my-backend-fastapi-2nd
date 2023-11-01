from database import SessionLocal

def get_db():
    sessionlocal = SessionLocal()
    try:
        yield sessionlocal
    finally:
        sessionlocal.close()

        

