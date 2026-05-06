import psutil


class CpuMonitor:
    def __init__(self):
        num_cores = psutil.cpu_count()
        if num_cores is None:
            raise SystemError(
                "ERROR: Cannot read cpu count, so CPU monitor cannot be initialized"
            )
        self._num_cores = num_cores
        self._total_usage = psutil.cpu_percent(interval=0.01)

    def display_cores(self):
        self._total_usage = psutil.cpu_percent(interval=0.1)
        print(f"CPU %: {self._total_usage}%")
        cpus = psutil.cpu_percent(interval=0.1, percpu=True)
        cpus_string = f"CPU 0: {cpus[0]}%, "
        for i in range(1, self._num_cores):
            if i % 2 == 0:
                cpus_string += f"CPU {i}: {cpus[i]}%,"
            else:
                cpus_string += f" CPU {i}: {cpus[i]}%\n"
        print(cpus_string)
