from pyramid.view import view_config

from pyramid.renderers import render_to_response

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'CoffeePI'}

@view_config(route_name='hello')
def hello(request):
    request.response.text = 'hello world'
    #import pdb; pdb.set_trace()
    return request.response

@view_config(route_name='mako')
def mako(request):
    data = {'a': 1, 'b': 2}
    request.response = render_to_response('test.mako', data, request=request)
    return request.response
