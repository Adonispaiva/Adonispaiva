"""Bootstrap de desenvolvimento."""

from app.infrastructure.db.models import Base
from app.infrastructure.db.session import engine

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Banco inicializado")
