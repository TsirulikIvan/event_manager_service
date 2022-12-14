"""Add equipment table and car field

Revision ID: 83587b9e8c49
Revises: 8560e9ff0b12
Create Date: 2022-08-29 01:13:38.191046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83587b9e8c49'
down_revision = '8560e9ff0b12'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('have_car', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'have_car')
    # ### end Alembic commands ###
