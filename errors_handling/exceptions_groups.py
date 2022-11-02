import requests


def test_links(urls: list) -> None:
    exceptions = []
    for url in urls:
        try:
            requests.get(url)
        except Exception as e:
            e.add_note(url)
            exceptions.append(e)

    if exceptions:
        raise ExceptionGroup("Couldn't fetch some URLs", exceptions)


def write_to_file(exceptions, file_name):
    with open(f"log/{file_name}.txt", "w") as f:
        for exception in exceptions:
            f.write(f"{exception.__notes__[0]}\n")


try:
    test_links(
            urls=[
                "ht://www.google.com",
                "http://www.google.comx",
                "http://www.google.coms",
                "http://www.google.coma",
                "www.google.com",
            ]
    )
except* requests.exceptions.InvalidSchema as e:
    write_to_file(e.exceptions, "invalid_schema")
except* requests.exceptions.MissingSchema as e:
    write_to_file(e.exceptions, "missing_schema")
except* requests.exceptions.ConnectionError as e:
    write_to_file(e.exceptions, "connection_error")
else:
    print("All links are valid")
