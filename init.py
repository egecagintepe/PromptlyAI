# init_db.py
from database import Base, engine, SessionLocal
import models
from auth import register_user
import traceback

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Veritabanı tabloları oluşturuldu.")

    # Create admin/admin user if not exists
    db = SessionLocal()
    try:
        admin_user = db.query(models.User).filter_by(username="admin").first()
        if not admin_user:
            register_user(
                db, 
                username="admin", 
                password="admin", 
                email="admin@promptly.ai", 
                gender="Diger"
            )
            print("Varsayılan admin hesabı oluşturuldu: admin / admin")
        else:
            print("admin hesabı zaten mevcut.")
    except Exception as e:
        print("Admin hesabı oluşturulurken hata:")
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    init_db()