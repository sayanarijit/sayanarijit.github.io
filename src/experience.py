import typing as t

from htmldoom import renders
from htmldoom.yaml_loader import loadyaml as ly

from common import COMPONENTS, render_external_url, render_heading


@renders(ly(COMPONENTS, "experience"))
def render_experience() -> t.Dict[str, str]:
    return {
        "heading": render_heading("Experience"),
        "niteo": render_external_url(link="niteo.co", display="Niteo"),
        "techm": render_external_url(link="techmahindra.com", display="Tech Mahindra"),
    }


if __name__ == "__main__":
    print(render_experience())
