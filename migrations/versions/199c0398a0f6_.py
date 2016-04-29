"""empty message

Revision ID: 199c0398a0f6
Revises: b3f73178cee6
Create Date: 2016-04-28 17:10:39.468718

"""

# revision identifiers, used by Alembic.
revision = '199c0398a0f6'
down_revision = 'b3f73178cee6'

from alembic import op
import sqlalchemy as sa
import doorman.database


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('config', doorman.database.JSONB(), nullable=True),
    sa.Column('query_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['query_id'], ['query.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('query_id', 'name', name='_query_name_uc')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rule')
    ### end Alembic commands ###
