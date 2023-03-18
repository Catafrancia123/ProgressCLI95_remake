from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from cls import clear

clear()


console = Console()
table = Table(title="My Table", show_header=True, header_style="bold magenta")
table.add_column("Column 1", justify="center", style="cyan", no_wrap=True)
table.add_column("Column 2", justify="center", style="green")
table.add_row("Value 1A", "Value 1B")
table.add_row("Value 2A", "Value 2B")
console.print(table)