from fastmcp import FastMCP
import httpx
from typing import Any
# Create a server instance
mcp = FastMCP(name="MyAssistantServer")

base_url = "http://api.nationalize.io"

@mcp.tool()
async def predict_origin(self, name: str)->dict:
    """주어진 이름의 출신 국가를 예측

    Args:
        name (str): _description_

    Returns:
        dict: _description_
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{base_url}/?name={name}")
        return response.json()

@mcp.tool()
async def batch_predict(self, names: list[str])->dict:
    """여러개 이름 한번에 예측

    Args:
        names (list[str]): _description_

    Returns:
        dict: _description_
    """
    results = {}
    for name in names:
        result = await self.predict_origin(name)
        results[name] = result
    return results


if __name__ == "__main__":
    print('이름 출신 국가 서버 시작중...')
    mcp.run(transport='stdio')

