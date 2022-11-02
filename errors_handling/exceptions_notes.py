import requests


def exception_notes():
    try:
        r = requests.get('http://www.google.comx')
    except requests.exceptions.RequestException as e:
        e.add_note("Couldn't fetch Google...")
        raise


exception_notes()
