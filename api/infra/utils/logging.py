from api.data.interfaces import LoggingInterface


class Logging(LoggingInterface):
    def log(self, time: str | float, q: str) -> None:
        with open("app.log", "a") as f:
            f.seek(0, 2)
            if f.tell() != 0:
                f.write("\n")
            f.write(f"{q}\n")
            f.write(str(time))
