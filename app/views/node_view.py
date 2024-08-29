from ..models.node_model import Node


def data_from_node(node):
    """ Get the Nodo and Options """
    if not node:
        return []

    options = [
        {
            "next_node_id": option.next_node_id,
            "description": option.option_description
        }
        for option in node.options
        if option.next_node_id
    ]

    result = {
        "Nodo": {
            "id": node.id,
            "description": node.description
        },
        "Options": options
    }

    return result


def first_option():
    """ First option """
    first_node = Node.query.first()

    result = data_from_node(first_node)

    return result


def search_option(data):
    """ Search option from data """
    node_id = data.get("node_id")

    node = Node.query.filter(Node.id == node_id).first()

    result = data_from_node(node)

    return result
