"""Add foreign key to Space in lists_in_clickup

Revision ID: 0ba3baf65677
Revises: effb046f44f8
Create Date: 2023-07-22 15:55:27.185402

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0ba3baf65677'
down_revision = 'effb046f44f8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('lists_in_clickup', 'space_id')
    op.add_column(
        'lists_in_clickup',
        sa.Column('clickup_space', sa.BigInteger(), nullable=False)
    )
    op.create_foreign_key(None, 'lists_in_clickup', 'spaces', ['clickup_space'], ['space_id'])
    op.add_column('spaces', sa.Column('name_space', sa.String(length=255), nullable=False, server_default='Faculdade'))

    op.drop_column('spaces', 'space_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spaces', sa.Column('space_name', mysql.VARCHAR(length=50), nullable=False))
    op.drop_column('spaces', 'name_space')
    op.drop_constraint(None, 'lists_in_clickup', type_='foreignkey')
    op.alter_column('lists_in_clickup', 'space_id',
                    existing_type=sa.BigInteger(),
                    type_=mysql.VARCHAR(length=50),
                    existing_nullable=False)
    # ### end Alembic commands ###