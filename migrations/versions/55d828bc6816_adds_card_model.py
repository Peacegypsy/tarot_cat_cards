"""adds Card model

Revision ID: 55d828bc6816
Revises: 
Create Date: 2021-07-20 16:16:15.837269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55d828bc6816'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('card_id', sa.Integer(), nullable=False),
    sa.Column('card_name', sa.String(length=100), nullable=False),
    sa.Column('card_general', sa.Text(), nullable=False),
    sa.Column('card_upright', sa.Text(), nullable=False),
    sa.Column('card_reversed', sa.Text(), nullable=False),
    sa.Column('card_image_location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('card_id')
    )
    # op.drop_table('cards')
    # op.drop_table('cards_dataset-2')
    # op.drop_table('posts')
    # op.drop_table('posts_tags')
    # op.drop_table('cards_new')
    # op.drop_table('reviews')
    # op.drop_table('tags')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('tags',
    # sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('tagname', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    # sa.PrimaryKeyConstraint('id', name='tags_pkey'),
    # postgresql_ignore_search_path=False
    # )
    # op.create_table('reviews',
    # sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('title', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    # sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('body', sa.TEXT(), autoincrement=False, nullable=True),
    # sa.Column('creator_id', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('stars', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.PrimaryKeyConstraint('id', name='reviews_pkey')
    # )
    # op.create_table('cards_new',
    # sa.Column('card_id', sa.INTEGER(), autoincrement=True, nullable=False),
    # sa.Column('card', sa.TEXT(), autoincrement=False, nullable=True),
    # sa.Column('general', sa.TEXT(), autoincrement=False, nullable=True),
    # sa.Column('upright', sa.TEXT(), autoincrement=False, nullable=True),
    # sa.Column('reversed', sa.TEXT(), autoincrement=False, nullable=True),
    # sa.PrimaryKeyConstraint('card_id', name='cards_new_pkey')
    # )
    # op.create_table('posts_tags',
    # sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('tag_id', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name='posts_tags_post_id_fkey'),
    # sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], name='posts_tags_tag_id_fkey'),
    # sa.PrimaryKeyConstraint('post_id', 'tag_id', name='posts_tags_pkey')
    # )
    # op.create_table('posts',
    # sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('title', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    # sa.Column('body', sa.TEXT(), autoincrement=False, nullable=True),
    # sa.PrimaryKeyConstraint('id', name='posts_pkey')
    # )
    # op.create_table('cards_dataset-2',
    # sa.Column('ACE OF WANDS', sa.TEXT(), autoincrement=False, nullable=True),
    # sa.Column('Creativity is in the air- along with a rainbow of possibilities', sa.TEXT(), autoincrement=False, nullable=True),
    # sa.Column('Beware of letting ambition cause you to reach for too much. New', sa.TEXT(), autoincrement=False, nullable=True),
    # sa.Column("If you can't quite seem to reach your creative goals or find a ", sa.TEXT(), autoincrement=False, nullable=True)
    # )
    # op.create_table('cards',
    # sa.Column('card', sa.TEXT(), autoincrement=False, nullable=True),
    # sa.Column('general', sa.TEXT(), autoincrement=False, nullable=True),
    # sa.Column('upright', sa.TEXT(), autoincrement=False, nullable=True),
    # sa.Column('reversed', sa.TEXT(), autoincrement=False, nullable=True),
    # sa.Column('image', sa.TEXT(), autoincrement=False, nullable=True),
    # sa.Column('card_id', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('card_id', name='cards_pkey')
    # )
    op.drop_table('card')
    # ### end Alembic commands ###
