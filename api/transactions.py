from fastapi import APIRouter
from pypika import Table

from lib.models import Transaction
import lib.database as db

r = APIRouter(
    prefix='/transactions',
)


@r.post(path='/')
async def create_transaction(transaction: Transaction):
    transactions = Table('transactions')


@r.get(path='/')
async def list_transactions():
    return (await db.Query.from_('transations').select('*').execute()).fetchall()

