"""add content column to posts_one table

Revision ID: 8101d1e36cf9
Revises: d630f8847bc2
Create Date: 2023-10-08 12:33:46.561580

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8101d1e36cf9'
down_revision: Union[str, None] = 'd630f8847bc2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts_one', sa.Column('content',sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_column('posts_one', 'content')
    pass
