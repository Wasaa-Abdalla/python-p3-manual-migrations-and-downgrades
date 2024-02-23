"""Renaming students to scholars

Revision ID: b678271110be
Revises: ccd443902577
Create Date: 2024-02-23 07:32:05.542452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b678271110be'
down_revision = 'ccd443902577'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
