import os
import sys
import sqlalchemy as sa

from enum import Enum
from datetime import date

from alembic.config import Config
from alembic import command

from smp_backend.app.core.config import dconf

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from smp_backend.app.models import license_usage, license, contract

original_db_type = dconf.DB_TYPE
dconf.DB_TYPE = "postgresql"

engine = sa.create_engine(dconf.DB_URL, echo=True)

Session = sessionmaker(bind=engine)
session = Session()
