# """Create initial tables

# Revision ID: 001
# Revises:
# Create Date: 2024-07-16 10:00:00.000000

# """

# from uuid import uuid4

# import sqlalchemy as sa

# from alembic import op

# # revision identifiers, used by Alembic.
# revision = "001"
# down_revision = None
# branch_labels = None
# depends_on = None


# def upgrade():
#     op.create_table(
#         "bot",
#         sa.Column("uuid", sa.UUID(), primary_key=True, default=uuid4),
#         sa.Column("integration_uuid", sa.UUID(), unique=True, nullable=False),
#         sa.Column("api_key", sa.UUID(), nullable=False, unique=True),
#         sa.Column("api_secret", sa.String(length=250), nullable=False, unique=True),
#         sa.Column("bot_token", sa.String(length=250), nullable=False, unique=True),
#     )


# def downgrade():
#     op.drop_table("bot")
