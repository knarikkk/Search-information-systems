from rich.console import Console
from rich.table import Table


def primary_data_table(data, title="Words"):
    table = Table(title=title)

    table.add_column("Word", style="blue")
    table.add_column("Files count", style="#f92672", justify="center")
    table.add_column("DocId", style="green", justify="right")

    for word, doc in data.items():
        table.add_row(word, str(len(doc)), ", ".join([str(_) for _ in doc]))

    console = Console()
    console.print(table)
