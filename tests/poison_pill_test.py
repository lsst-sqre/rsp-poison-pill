"""Test the RSP startup poison pill."""

import subprocess


def test_poison_pill() -> None:
    result = subprocess.run("launch-rubin-jupyterlab", check=False)
    assert result.returncode == 4
