from os import getenv
from typing import Any, Self
from pypika import Query as PyPikaQuery
from psycopg_pool import AsyncConnectionPool
from pypika.queries import QueryBuilder as PyPikaQB

connection_pool = AsyncConnectionPool(conninfo=str(getenv('DB_DSN')), open=False)

class QueryBuilder(PyPikaQB):
    _params: dict[str, Any] = {}

    def set_param(self, name: str, value: Any) -> Self:
        self._params[name] = value

        return self

    def add_params(self, params: dict[str, Any]) -> Self:
        self._params = { **self._params, **params }

        return self

    async def execute(self):
        async with connection_pool.connection() as conn:
            async with conn.cursor() as c:
                await c.execute(query=self.get_sql().encode(), params=self._params)
                return c



class Query(PyPikaQuery):
    @classmethod
    def _builder(cls, **kvargs) -> 'QueryBuilder':
        return QueryBuilder(**kvargs)

