from flask import Blueprint

from .platforms import platforms_controller
from .operating_systems import operating_systems_controller
from .profiles import profiles_controller
from .products import products_controller
from .tags import tags_controller
from .service_profiles import service_profiles_controller

admin_controller = Blueprint('admin', __name__, url_prefix='/admin')

admin_controller.register_blueprint(platforms_controller)
admin_controller.register_blueprint(operating_systems_controller)
admin_controller.register_blueprint(profiles_controller)
admin_controller.register_blueprint(products_controller)
admin_controller.register_blueprint(tags_controller)
admin_controller.register_blueprint(service_profiles_controller)
