from os import environ
from alembic import context
from app.models import users


config = context.config

section = config.config_ini_section
config.set_section_option(section, "DB_USER", environ.get("POSTGRES_PASSWORD"))
config.set_section_option(section, "DB_PASS", environ.get("POSTGRES_USER"))
config.set_section_option(section, "DB_NAME", environ.get("POSTGRES_DB"))
config.set_section_option(section, "DB_HOST", environ.get("DEFAULT_HOST"))


target_metadata = [users.metadata]