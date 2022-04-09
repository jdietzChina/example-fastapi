"""add content column to posts table

Revision ID: 611e1700414b
Revises: 8bb948dd1952
Create Date: 2022-04-08 09:36:26.585430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '611e1700414b'
down_revision = '8bb948dd1952'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
