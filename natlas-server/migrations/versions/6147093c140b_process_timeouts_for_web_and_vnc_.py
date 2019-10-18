"""process timeouts for web and vnc screenshots

Revision ID: 6147093c140b
Revises: d4685e98a91f
Create Date: 2019-10-17 20:50:25.905796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6147093c140b'
down_revision = 'd4685e98a91f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('agent_config', sa.Column('vncScreenshotTimeout', sa.Integer(), nullable=True))
    op.add_column('agent_config', sa.Column('webScreenshotTimeout', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('agent_config', 'webScreenshotTimeout')
    op.drop_column('agent_config', 'vncScreenshotTimeout')
    # ### end Alembic commands ###
