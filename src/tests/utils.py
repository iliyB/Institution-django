from typing import Dict


def get_auth_header(token: str) -> Dict:
    return {"Authorization": f"Bearer {token}"}
