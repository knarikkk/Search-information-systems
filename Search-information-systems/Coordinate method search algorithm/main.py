from rich import print
from rich.table import Table
import re

data = {
    "hello": {1: [36, 78, 170, 251, 458, 1000], 4: [12, 22, 64, 102], 8: [17]},
    "to": {
        1: [47, 86, 234, 999],
        4: [14, 24, 774, 944, 2],
        8: [199, 319, 589, 608],
    },
    "world": {
        1: [53, 87, 704, 722, 901],
        4: [8, 23, 43, 68, 103],
        8: [19, 189, 618],
    },
    "where": {1: [5, 19, 46, 147, 201, 341, 387], 4: [7, 24, 58, 111, 321]},
    "full": {
        1: [1, 17, 74, 158, 222],
        4: [8, 74, 106, 287, 450],
        8: [5, 78, 188],
    },
    "go": {1: [2, 13, 25, 46, 96, 307], 4: [58, 96, 108, 368], 8: [69, 421]},
    "school": {
        1: [10, 31, 48, 135, 768],
        4: [21, 47, 87, 99],
        8: [8, 41, 198, 318, 487],
    },
}


print("[bold blue]Enter your words---> [/]", end=" ")
words = input().replace("\\", "/")
regex = r"\/-?\d+"
digit = re.search(regex, words)
digit = abs(int((digit.group() if digit else "/0")[1:]))
new_str = re.sub(regex, " ", words).split()
if len(new_str) != 2:
    print(f"[bold red]We need 2  word you have {len(new_str)}[/]")
    exit(0)
print(f"{digit=}, {new_str=}")

dict1 = data.get(new_str[0], {})
dict2 = data.get(new_str[1], {})

result = {}
for filename in set(dict1.keys()) & set(dict2.keys()):
    for x in dict1[filename]:
        if x + digit in dict2[filename]:
            result[filename] = [*result.get(filename, []), (x, x + digit)]
        if x - digit in dict2[filename]:
            result[filename] = [*result.get(filename, []), (x, x - digit)]
print(result)


def draw_table(filename, data):
    table = Table(title=f"File {filename}")
    table.add_column(new_str[0], justify="center", style="magenta")
    table.add_column(new_str[1], justify="center", style="green")
    for i in data:
        table.add_row(str(i[0]), str(i[1]))
    print(table)


if not result:
    print("[bold]There is not matches[/]")
else:
    for filename, data in result.items():
        draw_table(filename, data)
