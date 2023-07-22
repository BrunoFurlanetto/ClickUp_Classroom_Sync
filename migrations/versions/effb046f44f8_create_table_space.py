"""Create table space

Revision ID: effb046f44f8
Revises: 5de48337e056
Create Date: 2023-07-22 15:46:28.921442

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'effb046f44f8'
down_revision = '5de48337e056'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'spaces',
        sa.Column('space_id', sa.BigInteger(), autoincrement=False, nullable=False),
        sa.Column('space_name', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('space_id')
    )


def downgrade() -> None:
    op.drop_table('spaces')
