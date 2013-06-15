from coffeepi.model          import DBSession, init_DBSession, init_db, commit
from pyramid.paster  import get_appsettings

settings = get_appsettings('development.ini')

from coffeepi.model.model_test import Member

init_DBSession(settings)
init_db()

#create members

m = Member()
m.name = 'bob'
DBSession.add(m)

m = Member()
m.name = 'james'
DBSession.add(m)

m = Member()
m.name = 'sally'
DBSession.add(m)

commit()
