"""empty message

Revision ID: 30b091260689
Revises: 251a7638da78
Create Date: 2018-07-30 12:52:52.845202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "30b091260689"
down_revision = "251a7638da78"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("is_expert", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "is_expert")
    # ### end Alembic commands ###
