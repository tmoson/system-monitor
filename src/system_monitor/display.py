from .cpumonitor import CpuMonitor
from blessed import Terminal
import time


class Display:
    def __init__(
        self, title: str = "CPU Monitor", cpu_monitor: CpuMonitor | None = None
    ):
        self.term = Terminal()
        self.term.set_window_title(title)
        if cpu_monitor is None:
            self.cpu_monitor = CpuMonitor()
        else:
            self.cpu_monitor = cpu_monitor

    async def run(self) -> None:
        with self.term.cbreak():
            while True:
                key = await self.term.async_inkey(0.5)
                if key == "q":
                    return
                self.cpu_monitor.display_cores(term=self.term)
                time.sleep(1)
