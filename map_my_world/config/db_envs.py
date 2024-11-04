import os


def envs_postgres() -> str:
    POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: int = os.environ.get("POSTGRES_PORT", 5432)
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER", "Test")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD", "Test")
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB", "map-my-world")

    return f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"  # noqa
