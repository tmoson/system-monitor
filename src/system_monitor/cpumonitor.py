import psutil
from blessed import Terminal


class CpuMonitor:
    def __init__(self):
        num_cores = psutil.cpu_count()
        if num_cores is None:
            raise SystemError(
                "ERROR: Cannot read cpu count, so CPU monitor cannot be initialized"
            )
        self._num_cores = num_cores
        self._total_usage = psutil.cpu_percent(interval=0.01)

    def _standardize_width(self, cpu_num: int, cpu_percent: float) -> str:
        cpu_string = "CPU "
        if cpu_num < 10:
            cpu_string += " "
        cpu_string += f"{cpu_num}: "
        percent_int = 100 - int(cpu_percent / 10)
        while percent_int != 0:
            cpu_string += " "
            percent_int = int(percent_int / 10)
        cpu_string += f"{cpu_percent}%"
        return cpu_string

    def _cpu_color(self, term: Terminal, percent: float) -> str:
        match percent:
            case _ if percent < 26:
                return term.darkolivegreen2
            case _ if percent < 51:
                return term.yellow
            case _ if percent < 76:
                return term.orange
            case _ if percent < 91:
                return term.orangered
            case _:
                return term.red

    def display_cores(self, term: Terminal) -> None:
        self._total_usage = psutil.cpu_percent(interval=0.1)
        cpus_string = f"Total CPU %: {self._total_usage}%\n"
        cpus = psutil.cpu_percent(interval=0.1, percpu=True)
        for i in range(0, self._num_cores):
            if i % 2 == 0:
                cpus_string += f"| {self._cpu_color(term=term, percent=cpus[i])}{self._standardize_width(cpu_num=i, cpu_percent=cpus[i])}{term.normal} |"
            else:
                cpus_string += f" {self._cpu_color(term=term, percent=cpus[i])}{self._standardize_width(cpu_num=i, cpu_percent=cpus[i])}{term.normal} |\n"
        print(term.home + term.clear + cpus_string)
