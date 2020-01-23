from sphinx.cmd.build import main
from pathlib import Path

path = Path("./docs")
main(["-b", "html", str(path), str(path.joinpath("_build"))])
