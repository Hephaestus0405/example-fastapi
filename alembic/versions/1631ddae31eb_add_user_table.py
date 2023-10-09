"""add user table

Revision ID: 1631ddae31eb
Revises: 8101d1e36cf9
Create Date: 2023-10-08 13:31:38.442312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1631ddae31eb'
down_revision: Union[str, None] = '8101d1e36cf9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False,  primary_key = True),
                    sa.Column('email', sa.String(), nullable=False,unique=True),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=False), server_default=sa.text('now()'), nullable=False)
                    
                    )

    pass


def downgrade():
    op.drop_table('users')
    pass
