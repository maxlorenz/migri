import json


async def migrate(conn) -> bool:
    await conn.execute("INSERT INTO abc (tags) VALUES ($1)", json.dumps({"hey": "true"}))
    return True
