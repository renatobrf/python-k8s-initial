```python
from pathlib import Path
import importlib.util


def load_module_from_path(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_welcome_message_returns_text():
    repo_root = Path(__file__).resolve().parent.parent
    welcome_path = repo_root / "src" / "welcome.py"
    welcome = load_module_from_path(welcome_path, "welcome_for_test")

    msg = welcome.welcome_message()
    assert isinstance(msg, str)
    assert "Bem-vindo" in msg
