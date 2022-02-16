
from sqlalchemy import select, insert
from core.middleware import g
from core.schema import paginate_handler
from core.utils.api_exception import NotFoundException
from core.i18n import gettext
from app.app01.models import App01


async def list_app01(page: int, limit: int):
    stmt = select(App01)
    return await paginate_handler(page=page, limit=limit, db=g.db, stmt=stmt)

async def create_app01(name: str, description: str):
    return await g.db.execute(insert(App01).values({"name": name, "description": description}))

async def delete_app01(record_id: str):
    obj = await g.db.get(App01, record_id)
    if not obj:
        raise NotFoundException(gettext("record not found"))
    await obj.delete()
    return

