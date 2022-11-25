"""add to many relation in user and posts

Revision ID: 2c45ba9873ce
Revises: fb61bfe69c87
Create Date: 2022-11-21 01:32:09.017851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c45ba9873ce'
down_revision = 'fb61bfe69c87'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("userid",sa.Integer(),nullable = False))


def downgrade() -> None:
    pass
