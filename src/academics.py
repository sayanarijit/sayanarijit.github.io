import typing as t

from htmldoom import renders
from htmldoom.url import https

from common import external_url, wikipedia


@renders(
    "As for academics, he doesn't have anything to brag about. After three year ",
    wikipedia("diploma"),
    " in ",
    wikipedia("electrical engineering"),
    ", he wandered into the field of ",
    wikipedia("computer programming"),
    " on his own and graduated from the need of graduation certificates.",
    " He's still pursuing his own learning path via online courses such as ",
    external_url(href=https("ocw.mit.edu"), display="MIT OpenCourseWare"),
    ".",
)
def render_academics() -> t.Dict[str, str]:
    return {}
