from pyramid.config import Configurator

from .model import init_DBSession


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    init_DBSession(settings)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('hello', '/helloworld')
    config.add_route('mako', '/mako')
    config.scan()
    return config.make_wsgi_app()
