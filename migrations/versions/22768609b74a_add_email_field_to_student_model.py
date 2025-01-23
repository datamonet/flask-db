"""Add email field to Student model

Revision ID: 22768609b74a
Revises: 
Create Date: 2025-01-23 11:31:25.000000

"""
from alembic import op
import sqlalchemy as sa
from alembic.operations import ops


# revision identifiers, used by Alembic.
revision = '22768609b74a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create a temporary table with the new schema
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=120), nullable=True))
        batch_op.create_unique_constraint('unique_email', ['email'])


def downgrade() -> None:
    # Remove the email column
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_constraint('unique_email', type_='unique')
        batch_op.drop_column('email')
