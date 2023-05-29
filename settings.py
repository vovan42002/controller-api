from envparse import Env

env = Env()

DB_HOST: str = env.str("DB_HOST", default="localhost")
DB_USERNAME: str = env.str("DB_USERNAME", default="postgres")
DB_PASSWORD: str = env.str("DB_PASSWORD", default="postgres")
DB_NAME: str = env.str("DB_NAME", default="controller")

DATABASE_URL = env.str(
    "DATABASE_URL",
    default=f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}",
)

SECRET_KEY: str = env.str("SECRET_KEY", default="secret_key")
ALGORITHM: str = env.str("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", default=30)
