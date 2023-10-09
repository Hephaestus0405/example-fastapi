"""add last few columns to the post table

Revision ID: 289b757498bc
Revises: 75af40360ed3
Create Date: 2023-10-09 11:05:13.590450

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '289b757498bc'
down_revision: Union[str, None] = '75af40360ed3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts_one', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'), )
    op.add_column('posts_one', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default = sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts_one', 'published')
    op.drop_column('posts_one', 'created_at')
    pass
