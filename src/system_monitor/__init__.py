from .cpumonitor import CpuMonitor


def main() -> None:
    cpu_monitor = CpuMonitor()
    cpu_monitor.display_cores()
