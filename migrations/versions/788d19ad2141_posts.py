"""posts

Revision ID: 788d19ad2141
Revises: 
Create Date: 2020-01-07 19:48:10.928354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '788d19ad2141'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('text', sa.String(length=10000), nullable=True),
    sa.Column('image', sa.String(length=10000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_image'), 'posts', ['image'], unique=True)
    op.create_index(op.f('ix_posts_text'), 'posts', ['text'], unique=True)
    op.create_index(op.f('ix_posts_title'), 'posts', ['title'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_title'), table_name='posts')
    op.drop_index(op.f('ix_posts_text'), table_name='posts')
    op.drop_index(op.f('ix_posts_image'), table_name='posts')
    op.drop_table('posts')
    # ### end Alembic commands ###
