from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'CoffeePI'}

@view_config(route_name='hello')
def hello(request):
    request.response.text = 'hello world'
    return request.response
