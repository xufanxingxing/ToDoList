"""empty message

Revision ID: 6c6b63878c92
Revises: 19b5eb84e425
Create Date: 2019-10-24 20:59:59.979603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c6b63878c92'
down_revision = '19b5eb84e425'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plans', sa.Column('priority', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('plans', 'priority')
    # ### end Alembic commands ###