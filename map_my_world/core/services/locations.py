from sqlmodel.ext.asyncio.session import AsyncSession


class LocationService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session