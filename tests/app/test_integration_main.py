from tests import IntegrationTest

from flask import Flask
from app.main import main
from app.services import ServicesExtension
from app.models import ModelsExtension


class MainTestCase(IntegrationTest):

    def setUp(self) -> None:
        self.app = Flask(__name__)

    def test_main_injects_dependencies(self):
        # given
        app = Flask(__name__)

        # when
        main(app)

        # then
        self.assertEqual(type(app), Flask)
        self.assertIsNotNone(app.extensions[ServicesExtension.KEY])
        self.assertIsNotNone(app.extensions[ModelsExtension.KEY])

    def test_main_registers_blueprints(self):
        # given
        app = Flask(__name__)

        # when
        main(app)

        # then
        self.assertNotEqual(len(app.blueprints.keys()), 0)
