import os
import sys
import transaction

from sqlalchemy import engine_from_config
from alembic.config import Config
from alembic import command

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from ..models import (
    DBSession,
    MyModel,
    Base,
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    alembic_cfg = Config(config_uri)
    command.stamp(alembic_cfg, "head")
    with transaction.manager:
        model = MyModel(name='one', value=1)
        DBSession.add(model)
