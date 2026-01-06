```python
from pathlib import Path
import importlib.util
import sys


def load_module_from_path(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_rolldice_range(monkeypatch):
    repo_root = Path(__file__).resolve().parent.parent
    app_path = repo_root / "src" / "app.py"
    app = load_module_from_path(app_path, "app_for_test_rolldice")

    # Force randint to a deterministic value
    monkeypatch.setattr(app.random, "randint", lambda a, b: 4)
    assert app.rolldice() == 4


def test_main_writes_result(tmp_path, monkeypatch):
    """
    Run main for a single iteration (sleep_time=0) and ensure resultado.txt is created and contains the expected text.
    """
    repo_root = Path(__file__).resolve().parent.parent
    app_path = repo_root / "src" / "app.py"
    app = load_module_from_path(app_path, "app_for_test_main")

    # Avoid actual sleeping
    monkeypatch.setattr(app.time, "sleep", lambda s: None)

    # Run a single iteration, writing into tmp_path
    app.main(iterations=1, sleep_time=0, pvc_mount_path=str(tmp_path))

    result_file = tmp_path / "resultado.txt"
    assert result_file.exists(), "resultado.txt should be created in the pvc_mount_path"
    text = result_file.read_text()
    assert "Rolando o dado... Resultado" in text
