import logging
from mercurius.core.application import MercuriusApplication

from .config import RootConfig

# change this as needed
logging.basicConfig(level=logging.INFO)

app = MercuriusApplication({{ project_name }}, RootConfig, config_path="{{ project_name }}.toml", controllers_module="controllers")

{% for module_name in selected_modules %}
app.install({{module_name}})
{% endfor %}

# This if is important! Only this way the app can be started with an external application server
if __name__ == "__main__":
    app.start()
