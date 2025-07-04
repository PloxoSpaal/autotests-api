from config import settings
import platform
import sys


def create_allure_environment_file():
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    os_data = f"os_info={platform.system()}"
    python_data = f"python_version={sys.version}"
    items.append(os_data)
    items.append(python_data)
    properties = '\n'.join(items)
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)