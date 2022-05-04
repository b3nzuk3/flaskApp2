class Config:

    NEWS_BASE_URL ='https://newsapi.org/v2/everything?q={}&from=2022-04-04&sortBy=publishedAt&apiKey={}'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
    Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
    Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
