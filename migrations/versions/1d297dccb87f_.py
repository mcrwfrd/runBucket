"""empty message

Revision ID: 1d297dccb87f
Revises: 641c17b0b920
Create Date: 2018-05-02 21:01:52.332874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d297dccb87f'
down_revision = '641c17b0b920'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('run', sa.Column('distance', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('run', 'distance')
    # ### end Alembic commands ###
