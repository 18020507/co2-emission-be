"""empty message

Revision ID: 3942c0671d2c
Revises: f9a075ca46e9
Create Date: 2023-03-29 15:51:13.646930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3942c0671d2c'
down_revision = 'f9a075ca46e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('companies', sa.Column('created_by', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'companies', 'users', ['created_by'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'companies', type_='foreignkey')
    op.drop_column('companies', 'created_by')
    # ### end Alembic commands ###
