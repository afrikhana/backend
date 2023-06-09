"""update

Revision ID: 5905ea4b224a
Revises: 6b3a74686a86
Create Date: 2023-06-08 21:08:38.618744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5905ea4b224a'
down_revision = '6b3a74686a86'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=20), nullable=False))
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
