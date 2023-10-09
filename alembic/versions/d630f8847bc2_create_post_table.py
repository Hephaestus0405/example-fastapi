"""Create post table

Revision ID: d630f8847bc2
Revises: 
Create Date: 2023-10-08 11:53:26.995308

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd630f8847bc2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Handle the changes.
def upgrade():
    op.create_table('posts_one', sa.Column('id', sa.Integer(), nullable = False, primary_key = True), sa.Column('title', sa.String(), nullable = False))
    pass

# Handle the roll back if you want it.
def downgrade():
    op.drop_table('posts_one')
    pass
