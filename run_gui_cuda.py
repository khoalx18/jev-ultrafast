"""Windows entry for jev_gui_agent: pin the local CUDA engine, then run.

Usage (from C:/Users/ADMIN/jev-spike):
    .venv/Scripts/python.exe run_gui_cuda.py --pid <pid> --window-id <wid> --goal "..." --expect "..." --json

Why this exists: the shell-wide env forces OPENJEV_DEVICE=cpu (other flows
depend on it), but the GUI loop needs CUDA. This wrapper scopes cuda + local
to the GUI run only. TYPESAFE/OPENROUTER keys are dummies: the local path
never sends them anywhere; they only skip the macOS `security` keychain
lookup that would crash on Windows.
"""

import importlib.util
import os
import sys

os.environ.setdefault("OPENJEV_LOCAL", "1")
os.environ["OPENJEV_DEVICE"] = "cuda"
os.environ.setdefault("TYPESAFE_API_KEY", "local-unused")
os.environ.setdefault("OPENROUTER_API_KEY", "local-unused")
os.environ.setdefault(
    "CUA_DRIVER_BIN",
    "C:/Users/ADMIN/AppData/Local/hermes/tools/cua-driver-0.21.0-win32-x64/cua-driver.exe",
)
sys.path.insert(0, "C:/Users/ADMIN/hermes-jev-skills")
sys.path.insert(0, "C:/Users/ADMIN/openJev-verdict-2.0")

_AGENT = "C:/Users/ADMIN/hermes-jev-skills/skills/jev-computer-use/scripts/jev_gui_agent.py"


def main(argv=None):
    spec = importlib.util.spec_from_file_location("jev_gui_agent", _AGENT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    raise SystemExit(mod.main(argv if argv is not None else sys.argv[1:]))


if __name__ == "__main__":
    main()
