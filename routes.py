from views import index
from views import comment

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_post('/comment', comment, name='comment')