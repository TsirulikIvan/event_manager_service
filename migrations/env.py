from os import environ
from alembic import context
from app.models import users, events, groups


config = context.config

section = config.config_ini_section
config.set_section_option(section, "DB_USER", "user")
config.set_section_option(section, "DB_PASS", "password")
config.set_section_option(section, "DB_NAME", "postgres")
config.set_section_option(section, "DB_HOST", "localhost")


target_metadata = [users.metadata, events.metadata, groups.metadata]