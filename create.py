from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os

eng= create_engine(os.getenv('DB_URI'))
db=scoped_session(sessionmaker(bind=eng))

def main():
    db.execute("CREATE TABLE movies (id serial PRIMARY KEY, name text NOT NULL, year INT NOT NULL, description text NOT NULL, image text);")
    db.commit()

if __name__ == "__main__":
    main()