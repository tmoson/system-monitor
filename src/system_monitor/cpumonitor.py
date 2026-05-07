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

    def display_cores(self, term: Terminal) -> None:
        self._total_usage = psutil.cpu_percent(interval=0.1)
        cpus_string = f"Total CPU %: {self._total_usage}%"
        cpus = psutil.cpu_percent(interval=0.1, percpu=True)
        cpus_string += (
            f"\n| {self._standardize_width(cpu_num=0, cpu_percent=cpus[0])} |"
        )
        for i in range(1, self._num_cores):
            if i % 2 == 0:
                cpus_string += (
                    f"| {self._standardize_width(cpu_num=i, cpu_percent=cpus[i])} |"
                )
            else:
                cpus_string += (
                    f" {self._standardize_width(cpu_num=i, cpu_percent=cpus[i])} |\n"
                )
        print(term.home + term.clear + cpus_string)
