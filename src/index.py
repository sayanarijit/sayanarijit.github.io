import typing as t

from htmldoom import doctype, renders
from htmldoom.url import https
from htmldoom.yaml_loader import loadyaml as ly

from academics import render_academics
from common import (
    COMPONENTS,
    GRAVARTER_AVARTER,
    render_external_url,
    render_heading,
    render_icon,
    render_linked_image,
    render_social_link,
    render_wikipedia,
)
from experience import render_experience
from interests import render_interests

ICONS = "".join(
    render_icon(rel=x[0], size=x[1])
    for x in [("apple-touch-icon", "180"), ("icon", "32"), ("icon", "16")]
)


@renders(doctype("html"), "{html}")
def render_document() -> t.Dict[str, str]:
    return {"html": render_html()}


@renders(ly(COMPONENTS, "html"))
def render_html() -> t.Dict[str, str]:
    return {"head": render_head(), "body": render_body()}


@renders(ly(COMPONENTS, "head"))
def render_head() -> t.Dict[str, str]:
    return {"icons": ICONS}


@renders(ly(COMPONENTS, "body"))
def render_body() -> t.Dict[str, str]:
    return {
        "profile_pic": render_linked_image(
            url=https(GRAVARTER_AVARTER, size=640),
            alt="Arijit Basu's gravatar picture",
            height="128",
            width="128",
        ),
        "wiki_computer_science": render_wikipedia("computer science"),
        "interests": render_interests(),
        "experience": render_experience(),
        "academics": render_academics(),
        "this_site": render_external_url(
            link="github.com/sayanarijit/sayanarijit.github.io", display="This site"
        ),
        "htmldoom_url": render_external_url(
            link="github.com/sayanarijit/htmldoom", display="htmldoom"
        ),
        "social_links": "".join(
            (
                render_social_link(
                    link="github.com/sayanarijit", after=" (most active)"
                ),
                render_social_link(link="dev.to/sayanarijit"),
                render_social_link(link="fb.com/sayansprofile"),
                render_social_link(link="blog.niteo.co/author/sayanarijit"),
                render_social_link(link="pyslackers.com", after=" (@sayanarijit)"),
                render_social_link(link="twitter.com/sayansprofile"),
                render_social_link(link="hackerrank.com/sayanarijit"),
                render_social_link(link="hackerearth.com/@sayanarijit"),
                render_social_link(link="linkedin.com/in/sayanarijit"),
            )
        ),
    }


if __name__ == "__main__":
    print(render_document())
