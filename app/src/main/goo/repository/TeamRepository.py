from typing import List
from sqlalchemy.future import select
from models import Team  # models.py에서 Team 클래스 가져오기
from sqlalchemy.ext.asyncio import AsyncSession

class TeamRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def list_team(self) -> List[Team]:
        result = await self.session.execute(select(Team))
        return result.scalars().all()


    async def create_team(self, team: Team) -> Team:
        self.session.add(team)
        await self.session.commit()
        await self.session.refresh(team)
        return team
    
    # validation check
    async def get_team_by_name(self, name: str):
        result = await self.session.execute(select(Team).where(Team.t_name == name))
        return result.scalars().first()