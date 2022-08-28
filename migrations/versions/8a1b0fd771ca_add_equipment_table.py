"""add equipment table

Revision ID: 8a1b0fd771ca
Revises: 83587b9e8c49
Create Date: 2022-08-29 01:15:32.025583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a1b0fd771ca'
down_revision = '83587b9e8c49'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('equipment',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('class', sa.Enum('tent', 'sleeping_bag', 'tourist_foam', name='equipmentclass'), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('equipment')
    # ### end Alembic commands ###
