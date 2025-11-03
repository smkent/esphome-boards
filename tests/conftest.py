import shutil
import tempfile
from collections.abc import Iterator
from pathlib import Path

import pytest

PROJECT_DIR = Path(__file__).parent.parent
SECRETS_YAML = """
wifi_ssid: "Captain's Log, Stardate 802.11"
wifi_password: deadbeef
wifi_domain: .local
api_encryption_key: ZGVhZGJlZWZkZWFkYmVlZmRlYWRiZWVmZGVhZGJlZQo=
ota_password: deadbeefdeadbeef
latitude: 51.4921513°
longitude: -0.19297°
"""


@pytest.fixture(autouse=True, scope="session")
def sandbox_dir() -> Iterator[Path]:
    with tempfile.TemporaryDirectory() as td:
        sandbox_path = Path(td) / "repo"
        shutil.copytree(
            PROJECT_DIR, sandbox_path, ignore=shutil.ignore_patterns(".git")
        )
        with open(sandbox_path / "secrets.yaml", "w") as f:
            f.write(SECRETS_YAML)
        yield sandbox_path
