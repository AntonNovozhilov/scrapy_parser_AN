import datetime
import pathlib

RES = "results"
TIME = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
RESULT_DIR = pathlib.Path(__file__).parent.parent / f"{RES}"
RESULT_DIR.mkdir(exist_ok=True)
LOG_DIR = pathlib.Path(__file__).parent.parent / "logging"
LOG_DIR.mkdir(exist_ok=True)
