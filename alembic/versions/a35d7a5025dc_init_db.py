"""init_db

Revision ID: a35d7a5025dc
Revises: 
Create Date: 2024-07-04 22:23:47.223765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a35d7a5025dc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categoria',
    sa.Column('pk_id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('pk_id'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('centros_treinamento',
    sa.Column('pk_id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=20), nullable=False),
    sa.Column('endereco', sa.String(length=60), nullable=False),
    sa.Column('proprietario', sa.String(length=30), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('pk_id'),
    sa.UniqueConstraint('nome')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('centros_treinamento')
    op.drop_table('categoria')
    # ### end Alembic commands ###