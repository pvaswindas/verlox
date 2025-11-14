import httpx
import json
from .utils import sign_payload


async def post_event(
    endpoint: str,
    api_key: str,
    api_secret: str,
    event: dict,
):
    headers = {"Content-Type": "application/json", "X-Verlox-Key": api_key}
    body = json.dumps(event, separators=(",", ":"), sort_keys=True)
    headers["X-Verlox-Signature"] = f"sha256={sign_payload(api_secret, event)}"
    async with httpx.AsyncClient(timeout=5) as client:
        response = await client.post(endpoint, content=body, headers=headers)
        response.raise_for_status()
        return response
