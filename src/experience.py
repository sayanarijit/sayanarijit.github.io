import typing as t

from htmldoom import renders
from htmldoom.url import https

from common import external_url, wikipedia


@renders(
    "He started his career as an Associate System Engineer at ",
    external_url(href=https("techmahindra.com"), display="Tech Mahindra"),
    " in Feb 2016, and eventually converted to a Junior Software Engineer.",
    " After 3 years of working alongside the infrastructure operations team,"
    " contributing to automation based projects, he joined ",
    external_url(href=https("niteo.co"), display="Niteo"),
    " in March 2019 as a trialist Python developer and became permanent in June 2019.",
)
def render_experience() -> t.Dict[str, str]:
    return {}
