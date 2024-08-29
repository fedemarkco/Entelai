"""Added data

Revision ID: 256189a98f03
Revises: c6ad8fe583ed
Create Date: 2024-08-28 19:04:36.901351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '256189a98f03'
down_revision = 'c6ad8fe583ed'
branch_labels = None
depends_on = None


def upgrade():
    nodes_table = sa.table('node',
                           sa.column('id', sa.Integer),
                           sa.column('description', sa.String))

    op.bulk_insert(
        nodes_table,
        [
            {'id': 1, 'description': 'Inicio de aventura.'},
            {'id': 2, 'description': 'Descripción 1.'},
            {'id': 3, 'description': 'Descripción 2.'},
            {'id': 4, 'description': 'Descripción 3.'},
            {'id': 5, 'description': 'Descripción 4.'},
            {'id': 6, 'description': 'Descripción 5.'},
            {'id': 7, 'description': 'Descripción 6.'},
            {'id': 8, 'description': 'Fin de la aventura.'},
            {'id': 9, 'description': 'Descripción 7.'},
            {'id': 10, 'description': 'Fin de la aventura.'},
            {'id': 11, 'description': 'Fin de la aventura.'},
            {'id': 12, 'description': 'Fin de la aventura.'},
            {'id': 13, 'description': 'Fin de la aventura.'},
            {'id': 14, 'description': 'Fin de la aventura.'},
            {'id': 15, 'description': 'Fin de la aventura.'},
            {'id': 16, 'description': 'Fin de la aventura.'},
            {'id': 17, 'description': 'Fin de la aventura.'},
            {'id': 18, 'description': 'Fin de la aventura.'},
            {'id': 19, 'description': 'Fin de la aventura.'},
            {'id': 20, 'description': 'Fin de la aventura.'},
            {'id': 21, 'description': 'Fin de la aventura.'}
        ]
    )

    options_table = sa.table('option',
                             sa.column('id', sa.Integer),
                             sa.column('node_id', sa.Integer),
                             sa.column('next_node_id', sa.Integer),
                             sa.column('option_description', sa.String))

    op.bulk_insert(
        options_table,
        [
            {'id': 1, 'node_id': 1, 'next_node_id': 2, 'option_description': 'Opción 1'},
            {'id': 2, 'node_id': 1, 'next_node_id': 3, 'option_description': 'Opción 2'},
            {'id': 3, 'node_id': 1, 'next_node_id': 4, 'option_description': 'Opción 3'},
            {'id': 4, 'node_id': 2, 'next_node_id': 5, 'option_description': 'Opción 4'},
            {'id': 5, 'node_id': 2, 'next_node_id': 6, 'option_description': 'Opción 5'},
            {'id': 6, 'node_id': 3, 'next_node_id': 7, 'option_description': 'Opción 6'},
            {'id': 7, 'node_id': 3, 'next_node_id': 8, 'option_description': 'Opción 7'},
            {'id': 8, 'node_id': 4, 'next_node_id': 9, 'option_description': 'Opción 8'},
            {'id': 9, 'node_id': 4, 'next_node_id': 10, 'option_description': 'Opción 9'},
            {'id': 10, 'node_id': 5, 'next_node_id': 11, 'option_description': 'Opción 10'},
            {'id': 11, 'node_id': 5, 'next_node_id': 12, 'option_description': 'Opción 11'},
            {'id': 12, 'node_id': 5, 'next_node_id': 13, 'option_description': 'Opción 12'},
            {'id': 13, 'node_id': 6, 'next_node_id': 14, 'option_description': 'Opción 13'},
            {'id': 14, 'node_id': 6, 'next_node_id': 15, 'option_description': 'Opción 14'},
            {'id': 15, 'node_id': 8, 'next_node_id': None, 'option_description': None},
            {'id': 16, 'node_id': 9, 'next_node_id': 16, 'option_description': 'Opción 15'},
            {'id': 17, 'node_id': 9, 'next_node_id': 19, 'option_description': 'Opción 16'},
            {'id': 18, 'node_id': 10, 'next_node_id': None, 'option_description': None},
            {'id': 19, 'node_id': 11, 'next_node_id': None, 'option_description': None},
            {'id': 20, 'node_id': 12, 'next_node_id': None, 'option_description': None},
            {'id': 21, 'node_id': 13, 'next_node_id': None, 'option_description': None},
            {'id': 22, 'node_id': 14, 'next_node_id': None, 'option_description': None},
            {'id': 23, 'node_id': 15, 'next_node_id': None, 'option_description': None},
            {'id': 24, 'node_id': 16, 'next_node_id': None, 'option_description': None},
            {'id': 25, 'node_id': 17, 'next_node_id': None, 'option_description': None},
            {'id': 26, 'node_id': 18, 'next_node_id': None, 'option_description': None},
            {'id': 27, 'node_id': 19, 'next_node_id': None, 'option_description': None},
            {'id': 28, 'node_id': 20, 'next_node_id': None, 'option_description': None},
            {'id': 29, 'node_id': 21, 'next_node_id': None, 'option_description': None}
        ]
    )


def downgrade():
    pass
