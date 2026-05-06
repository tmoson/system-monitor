# system monitor

In an attempt to explore how the wonderful tool [btop](https://github.com/aristocratos/btop) works, I'm setting out to build a simpler python-based version. The current goals are as such:

1. Get CPU/RAM usage levels
2. Browse a list of running processes
3. Organize processed by the amount of CPU/memory that they're using
4. Select and kill processes in the application

## Tools

Currently, I'm just setting this up to be used with [uv](https://docs.astral.sh/uv/), so if you want to use this tool, go ahead and follow the install instructions on their site and run `uv run system-monitor`
