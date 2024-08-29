import unittest

from app import create_app, db
from app.models.node_model import Node, Option
from app.views.node_view import data_from_node


class TestNodeAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app("config.TestConfig")
        cls.app.testing = True
        cls.client = cls.app.test_client()

        with cls.app.app_context():
            cls.db = db
            cls.db.create_all()

            cls.node1 = Node(
                id=1,
                description="Inicio de aventura."
            )
            cls.node2 = Node(
                id=2,
                description="Descripción 1."
            )
            cls.option1 = Option(
                id=1,
                node_id=1,
                next_node_id=2,
                option_description="Opción 1"
            )
            cls.option2 = Option(
                id=2,
                node_id=1,
                next_node_id=3,
                option_description="Opción 2"
            )
            cls.option3 = Option(
                id=3,
                node_id=2,
                next_node_id=4,
                option_description="Opción 3"
            )
            cls.option4 = Option(
                id=4,
                node_id=2,
                next_node_id=5,
                option_description="Opción 4"
            )
            cls.db.session.add(cls.node1)
            cls.db.session.add(cls.node2)
            cls.db.session.add(cls.option1)
            cls.db.session.add(cls.option2)
            cls.db.session.add(cls.option3)
            cls.db.session.add(cls.option4)
            cls.db.session.commit()

            cls.data_node1 = data_from_node(cls.node1)
            cls.data_node2 = data_from_node(cls.node2)

            cls.node2_id = cls.node2.id

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            cls.db.drop_all()

    def test_start_route(self):
        """Test /start route"""

        response = self.client.post("/start")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, self.data_node1)

    def test_choose_route(self):
        """Test /choose route"""

        response = self.client.post("/choose", json={
            "node_id": self.node2.id
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, self.data_node2)


if __name__ == "__main__":
    unittest.main()
