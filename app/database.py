from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://todo_user:password@localhost:5432/todo_db")

with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS todos (
            id SERIAL PRIMARY KEY,
            name TEXT
        )
    """))

    conn.execute(text("INSERT INTO users (name) VALUES ('Alice')"))
    conn.commit()