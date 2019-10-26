import typing as t

from htmldoom import renders
from htmldoom.yaml_loader import loadyaml as ly

from common import COMPONENTS, render_heading, render_wikipedia


@renders(ly(COMPONENTS, "interests"))
def render_interests() -> t.Dict[str, str]:
    return {
        "heading": render_heading("Interests"),
        "wiki_soccer": render_wikipedia("soccer"),
        "wiki_tennis": render_wikipedia("tennis"),
        "wiki_trekking": render_wikipedia("trekking"),
    }


if __name__ == "__main__":
    print(render_interests())
