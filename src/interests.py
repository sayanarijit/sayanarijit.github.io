import typing as t

from htmldoom import renders

from common import heading, wikipedia


@renders(
    heading("Interests"),
    "Other than computer science & tech stuffs, he likes outdoor sports, specifically ",
    wikipedia("soccer"),
    ", and adventurous sports such as ",
    wikipedia("trekking"),
    ". Fitness is important to him, both physical and mental.",
)
def render_interests() -> t.Dict[str, str]:
    return {}
