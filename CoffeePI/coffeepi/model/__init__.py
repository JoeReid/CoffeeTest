import logging
log = logging.getLogger(__name__)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy.orm             import scoped_session, sessionmaker
from zope.sqlalchemy            import ZopeTransactionExtension      # AllanC - Apparently, the recomended way to use Pyramid is with a transaction manager
DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))

engine = None

#-------------------------------------------------------------------------------
# DB Setup
#-------------------------------------------------------------------------------

def init_DBSession(settings):
   """
   To be called from Pyramid _init_ to setup SQLA from settings
   This binds inits DBSession and Base
   
   To be called AFTER all extentisons to Base have been imported/setup
   Import the files with your datamodel, before calling this.
   Upon this call is the SQLa tables are build/linked
   """
   global engine
   log.info("Bind DBSession to engine")
   from sqlalchemy import engine_from_config
   engine = engine_from_config(settings, 'sqlalchemy.')
   DBSession.configure(bind=engine)

#def init_DBSession(transactional=False):
   #connection = engine.connect()
   #if transactional:
   #    transaction = connection.begin()
   #return DBSession.configure(bind=connection), transaction
   #transaction.rollback() # can roll back with

def init_db():
   """
   Clears and Creates all DB tables associated with Base
   
   To be called AFTER init_DBSession
   """
   log.info("Drop all existing tables")
   Base.metadata.drop_all  (bind=DBSession.bind, checkfirst=True)
   log.info("Create all tables bound to Base")
   Base.metadata.create_all(bind=DBSession.bind                 ) #, checkfirst=True
   
import transaction

def commit():
   """
   Commits the db session regardless of if it was setup with the zope transaction manager
   """
   try:
       DBSession.commit()
   except AssertionError as ae:
       transaction.commit()