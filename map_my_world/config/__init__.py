import os
from .config_envs import ConfigEnv

os.environ['ROOT_PATH'] = os.path.dirname(os.path.realpath(__file__))
SETUP = ConfigEnv().more_settings
