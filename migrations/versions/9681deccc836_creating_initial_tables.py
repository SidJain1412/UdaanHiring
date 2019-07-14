"""Creating initial tables:

Revision ID: 9681deccc836
Revises: 
Create Date: 2019-07-14 15:31:17.452214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9681deccc836'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('asset',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=96), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_asset_count'), 'asset', ['count'], unique=False)
    op.create_index(op.f('ix_asset_created_at'), 'asset', ['created_at'], unique=False)
    op.create_index(op.f('ix_asset_name'), 'asset', ['name'], unique=False)
    op.create_table('worker',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=96), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('email', sa.String(length=96), nullable=True),
    sa.Column('phonenum', sa.String(length=96), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_worker_created_at'), 'worker', ['created_at'], unique=False)
    op.create_index(op.f('ix_worker_email'), 'worker', ['email'], unique=False)
    op.create_index(op.f('ix_worker_name'), 'worker', ['name'], unique=False)
    op.create_index(op.f('ix_worker_phonenum'), 'worker', ['phonenum'], unique=False)
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=96), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('freq', sa.Integer(), nullable=True),
    sa.Column('timeofalloc', sa.DateTime(), nullable=True),
    sa.Column('taskToBePerformedBy', sa.DateTime(), nullable=True),
    sa.Column('workerId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['workerId'], ['worker.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_created_at'), 'task', ['created_at'], unique=False)
    op.create_index(op.f('ix_task_freq'), 'task', ['freq'], unique=False)
    op.create_index(op.f('ix_task_name'), 'task', ['name'], unique=False)
    op.create_index(op.f('ix_task_taskToBePerformedBy'), 'task', ['taskToBePerformedBy'], unique=False)
    op.create_index(op.f('ix_task_timeofalloc'), 'task', ['timeofalloc'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_timeofalloc'), table_name='task')
    op.drop_index(op.f('ix_task_taskToBePerformedBy'), table_name='task')
    op.drop_index(op.f('ix_task_name'), table_name='task')
    op.drop_index(op.f('ix_task_freq'), table_name='task')
    op.drop_index(op.f('ix_task_created_at'), table_name='task')
    op.drop_table('task')
    op.drop_index(op.f('ix_worker_phonenum'), table_name='worker')
    op.drop_index(op.f('ix_worker_name'), table_name='worker')
    op.drop_index(op.f('ix_worker_email'), table_name='worker')
    op.drop_index(op.f('ix_worker_created_at'), table_name='worker')
    op.drop_table('worker')
    op.drop_index(op.f('ix_asset_name'), table_name='asset')
    op.drop_index(op.f('ix_asset_created_at'), table_name='asset')
    op.drop_index(op.f('ix_asset_count'), table_name='asset')
    op.drop_table('asset')
    # ### end Alembic commands ###