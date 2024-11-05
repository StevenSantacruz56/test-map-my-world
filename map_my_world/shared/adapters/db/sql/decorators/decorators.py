from functools import wraps


def atomic(func):
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        async with self.session.begin():
            try:
                result = await func(self, *args, **kwargs)
                await self.session.commit()
                return result
            except Exception as e:
                await self.session.rollback()
                raise e
            finally:
                await self.session.close()
    return wrapper
