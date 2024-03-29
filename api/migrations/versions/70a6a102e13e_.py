"""empty message

Revision ID: 70a6a102e13e
Revises: ba76a3b89a75
Create Date: 2024-01-10 16:15:30.114150

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '70a6a102e13e'
down_revision = 'ba76a3b89a75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_column('result_all')

    with op.batch_alter_table('genre', schema=None) as batch_op:
        batch_op.add_column(sa.Column('book_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'book', ['book_id'], ['id'])
        batch_op.drop_column('result_all')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('genre', schema=None) as batch_op:
        batch_op.add_column(sa.Column('result_all', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('book_id')

    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('result_all', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
