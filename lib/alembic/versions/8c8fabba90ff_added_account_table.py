"""Added account table

Revision ID: 8c8fabba90ff
Revises: 
Create Date: 2024-03-29 13:54:29.783837

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c8fabba90ff'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('doci')
    op.drop_table('patients')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patients',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('firstname', sa.VARCHAR(), nullable=True),
    sa.Column('lastname', sa.VARCHAR(), nullable=True),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.Column('gender', sa.VARCHAR(), nullable=True),
    sa.Column('address', sa.VARCHAR(), nullable=True),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('phone', sa.VARCHAR(), nullable=True),
    sa.Column('diabetes', sa.BOOLEAN(), nullable=True),
    sa.Column('family_history', sa.BOOLEAN(), nullable=True),
    sa.Column('hypertension', sa.BOOLEAN(), nullable=True),
    sa.Column('weight', sa.FLOAT(), nullable=True),
    sa.Column('height', sa.FLOAT(), nullable=True),
    sa.Column('smoking', sa.BOOLEAN(), nullable=True),
    sa.Column('heart_failure', sa.BOOLEAN(), nullable=True),
    sa.Column('risk_score', sa.INTEGER(), nullable=True),
    sa.Column('risk_category', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('doci',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('firstname', sa.VARCHAR(), nullable=True),
    sa.Column('lastname', sa.VARCHAR(), nullable=True),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.Column('gender', sa.VARCHAR(), nullable=True),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('address', sa.VARCHAR(), nullable=True),
    sa.Column('phone_number', sa.VARCHAR(), nullable=True),
    sa.Column('working_hours', sa.INTEGER(), nullable=True),
    sa.Column('salary', sa.FLOAT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
