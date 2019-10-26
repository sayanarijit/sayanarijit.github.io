import typing as t

from htmldoom import renders
from htmldoom.yaml_loader import loadyaml as ly

from common import COMPONENTS, render_external_url, render_heading, render_wikipedia


@renders(ly(COMPONENTS, "academics"))
def render_academics() -> t.Dict[str, str]:
    return {
        "heading": render_heading("Academics"),
        "wiki_diploma": render_wikipedia("diploma"),
        "wiki_electrical_engineering": render_wikipedia("electrical engineering"),
        "wiki_computer_programming": render_wikipedia("computer programming"),
        "mit_ocw": render_external_url(
            link="ocw.mit.edu", display="MIT OpenCourseWare"
        ),
    }


if __name__ == "__main__":
    print(render_academics())
