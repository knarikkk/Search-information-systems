from rich import print
from .data_visualization import primary_data_table


def sort_dict(old_dict):
    return dict(sorted(old_dict.items()))


def search(data):
    print(
        "\tFor exit type [bold red]EXIT[/]\
        \n\tFor multipe keyword search concate with [bold yellow]SPACE ( )[/]"
    )
    while True:
        user_data = input().strip()
        if user_data == "EXIT":
            print("[bold green]Bye!![/]")
            return
        user_data_low = user_data.lower()
        if " " not in user_data:
            if user_data_low in data:
                primary_data_table({user_data: data[user_data_low]}, "Results")
            else:
                print(f"\nCan't find [bold blue]{user_data}[/] in files\n")
        else:
            user_data_list = user_data_low.split()
            result = [v for k, v in data.items() if k in user_data_list]

            actual_files = result[0]
            for file_index in result[1:]:
                actual_files = [
                    index for index in file_index if index in actual_files
                ]
            if len(result) != len(user_data_list) or not actual_files:
                print(
                    f"\nCan't find [bold red]{user_data.replace(' ', ', ')}[/] in files\n"  # noqa
                )
            else:
                primary_data_table(
                    {", ".join(user_data.split()): actual_files},
                    "Result",
                )
