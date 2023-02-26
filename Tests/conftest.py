import os
import sys
import pytest

from configparser import ConfigParser


def get_root_dir():
    root_dir = sys.path[0]
    print("Root Dir: ", root_dir)
    return root_dir


def get_config_file_path():
    config_path = os.path.join(get_root_dir(), 'app-config.ini')
    print("CONFIG_PATH: ", config_path)
    return config_path


def get_config():
    configure = ConfigParser()
    return configure


@pytest.fixture(scope='module')
def base_url():
    configure = get_config()
    configure.read(get_config_file_path())
    base_url = configure['DEV']['base_url']
    print(base_url)
    return base_url


@pytest.fixture(scope='module')
def api_version():
    configure = get_config()
    configure.read(get_config_file_path())
    get_version = configure['DEV']['version']
    print(get_version)
    return "/" + get_version


def get_end_point(end_point_name):
    configure = ConfigParser()
    end_points_path = os.path.join(sys.path[0], 'endpoints.ini')
    configure.read(end_points_path)
    get_end_point_name = configure['END_POINTS'][end_point_name]
    print(get_end_point_name)
    return get_end_point_name


@pytest.fixture(scope='module')
def users_end_point():
    return get_end_point("USERS_LIST")
