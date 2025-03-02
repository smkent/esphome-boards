import os
import subprocess
from pathlib import Path

import pytest

from .conftest import PROJECT_DIR


@pytest.mark.parametrize(
    "board_file_path",
    (
        pytest.param(testfn, id=str(testfn))
        for testfn in [
            fn.relative_to(PROJECT_DIR)
            for fn in (PROJECT_DIR / "boards").rglob("*.yaml")
        ]
    ),
)
def test_render_board_config(board_file_path: Path, sandbox_dir: Path) -> None:
    for fn in (sandbox_dir / "boards").rglob("*.yaml"):
        device_temp_file = sandbox_dir / "device.yaml"
        try:
            with open(device_temp_file, "w") as f:
                print(
                    f"packages:{os.linesep}"
                    f"  board: !include {board_file_path}",
                    file=f,
                )
            subprocess.run(
                ["esphome", "config", str(device_temp_file)],
                cwd=sandbox_dir,
                check=True,
            )
        finally:
            if device_temp_file.exists():
                device_temp_file.unlink()
