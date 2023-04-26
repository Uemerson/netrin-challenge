from typing import Any, Dict

from api.data.interfaces import LoggingInterface


class Logging(LoggingInterface):
    def log(self, time: str | float, q: str) -> None:
        with open("app.log", "a") as f:
            f.seek(0, 2)
            if f.tell() != 0:
                f.write("\n")
            f.write(f"{q}\n")
            f.write(str(time))

    def generate_metrics(self) -> Dict[str, Any]:
        with open("app.log", "r") as f:
            querys = []
            average_time = 0.0
            for i, row in enumerate(f):
                if i % 2 == 0:
                    querys.append(row)
                else:
                    average_time = average_time + float(row)
            return {"average_time": average_time / len(querys), "querys": querys}
