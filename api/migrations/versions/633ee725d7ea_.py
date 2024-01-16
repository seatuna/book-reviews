"""Seed Genres table

Revision ID: 633ee725d7ea
Revises: 70a6a102e13e
Create Date: 2024-01-16 16:22:40.927138

"""
from alembic import op
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer
from api.seed_db_helpers import get_book_genres

# revision identifiers, used by Alembic.
revision = "633ee725d7ea"
down_revision = "70a6a102e13e"
branch_labels = None
depends_on = None


def upgrade():
    genres = get_book_genres()
    genres_table = table(
        "genre",
        column("id", Integer),
        column("genre_name", String),
    )

    table_data = [{"genre_name": genre} for genre in genres]

    op.bulk_insert(genres_table, table_data)


def downgrade():
    pass
