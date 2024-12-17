from database import engine
from lib.models.student import Base


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Database and tables created successfully!")