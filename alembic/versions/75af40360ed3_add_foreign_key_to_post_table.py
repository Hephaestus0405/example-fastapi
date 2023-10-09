"""add foreign key to post table

Revision ID: 75af40360ed3
Revises: 1631ddae31eb
Create Date: 2023-10-09 10:44:04.228507

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75af40360ed3'
down_revision: Union[str, None] = '1631ddae31eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts_one', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('posts_users_fk', source_table= "posts_one", referent_table = "users", local_cols=['owner_id'], remote_cols =['id'], ondelete ="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name = "posts_one")
    op.drop_column('posts_one', 'owner_id')
    pass
