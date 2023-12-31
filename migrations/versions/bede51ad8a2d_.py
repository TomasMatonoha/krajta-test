"""empty message

Revision ID: bede51ad8a2d
Revises: d902df8633e7
Create Date: 2023-10-24 09:01:34.185897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bede51ad8a2d'
down_revision = 'd902df8633e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sklad', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pocet_kusu', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sklad', schema=None) as batch_op:
        batch_op.drop_column('pocet_kusu')

    # ### end Alembic commands ###
