import typing as t

from htmldoom import renders
from htmldoom.url import https
from htmldoom.yaml_loader import loadyaml as ly

GRAVARTER_AVARTER = "secure.gravatar.com/avatar/260b78495c933d0b932ea23ccffa44dd"
COMPONENTS = "src/components.yml"


@renders(ly(COMPONENTS, "icon"))
def render_icon(rel: str, size: str) -> t.Dict[str, str]:
    return {"href": https(GRAVARTER_AVARTER, size=size), "size": size, "rel": rel}


@renders(ly(COMPONENTS, "heading"))
def render_heading(txt: str) -> t.Dict[str, str]:
    return {"txt": txt}


@renders(ly(COMPONENTS, "social_link"))
def render_social_link(link, before="", after="") -> t.Dict[str, str]:
    return {"href": https(link), "text": link, "before": before, "after": after}


@renders(ly(COMPONENTS, "external_url"))
def render_external_url(link, display) -> t.Dict[str, str]:
    return {"href": https(link), "display": display}


@renders(ly(COMPONENTS, "linked_image"))
def render_linked_image(
    url: str, alt: str, height: str, width: str
) -> t.Dict[str, str]:
    return {"url": url, "href": url, "alt": alt, "height": height, "width": width}


@renders(ly(COMPONENTS, "wikipedia"))
def render_wikipedia(display: str) -> t.Dict[str, str]:
    return {
        "display": display,
        "href": https("en.wikipedia.org/wiki", display.replace(" ", "_")),
    }
