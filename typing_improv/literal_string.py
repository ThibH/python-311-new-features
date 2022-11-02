import os
from typing import LiteralString


def run(command: LiteralString) -> None:
    os.system(command)


file_name = input("Enter file name: ")
run(f"Echo {file_name}")

# Exemple Django
django.utils.safestring.mark_safe(f"<script>{user_input}</script>")

# This vulnerability could be prevented by updating mark_safe to only accept LiteralString:
def mark_safe(s: LiteralString) -> str: ...
