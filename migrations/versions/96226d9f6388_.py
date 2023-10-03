"""empty message

Revision ID: 96226d9f6388
Revises: 
Create Date: 2023-10-03 08:32:00.320621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96226d9f6388'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('gender',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('vyrobce',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('address', sa.String(length=564), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('personal_phone', sa.String(length=20), nullable=True),
    sa.Column('personal_celphone', sa.String(length=20), nullable=True),
    sa.Column('contact_group_id', sa.Integer(), nullable=False),
    sa.Column('gender_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contact_group_id'], ['contact_group.id'], ),
    sa.ForeignKeyConstraint(['gender_id'], ['gender.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('typ_vozidla',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('vyrobce_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['vyrobce_id'], ['vyrobce.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('typ_vozidla')
    op.drop_table('contact')
    op.drop_table('vyrobce')
    op.drop_table('gender')
    op.drop_table('contact_group')
    # ### end Alembic commands ###