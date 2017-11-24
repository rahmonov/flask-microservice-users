

class BaseConfig:
    """ Base Configuration """
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """ Development configuration """
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    DEBUG = False
