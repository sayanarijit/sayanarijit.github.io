from htmldoom import elements as e
from htmldoom.url import https


def external_url(href: str, display: str) -> bytes:
    return e.a(href=href, target="_blank", rel="noopener noreferrer")(display)


def linked_image(url: str, alt: str, height: str, width: str) -> bytes:
    return external_url(
        href=url, display=e.img(src=url, alt=alt, height=height, width=width)
    )


def wikipedia(display: str) -> bytes:
    return external_url(
        href=https("en.wikipedia.org/wiki", display.replace(" ", "_")), display=display
    )


def heading(txt: str):
    return e.b()(txt, e.hr())
