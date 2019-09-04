from htmldoom import doctype
from htmldoom import elements as e
from htmldoom import functions as fn
from htmldoom import renders
from htmldoom.url import https

gravatar_avartar = "secure.gravatar.com/avatar/260b78495c933d0b932ea23ccffa44dd"


def external_url(href, text):
    return e.a(href=href, target="_blank", rel="noopener noreferrer")(text)


def linked_image(url, alt, height, width):
    return e.a(href=url, target="_blank", rel="noreferrer")(
        e.img(src=url, alt=alt, height=height, width=width)
    )


@renders(e.li()("{before}", external_url(href="{href}", text="{text}"), "{after}"))
def render_social_link(link, before="", after=""):
    return {"href": https(link), "text": link, "before": before, "after": after}


@renders(
    doctype("html"),
    e.html()(
        e.head()(
            e.meta(charset="utf-8"),
            e.meta(
                name="viewport",
                content="width=device-width, initial-scale=1, shrink-to-fit=no",
            ),
            *fn.foreach((("apple-touch-icon", "180"), ("icon", "32"), ("icon", "16")))(
                lambda x: e.link(
                    rel=x[0],
                    sizes=f"{x[1]}x{x[1]}",
                    href=https(gravatar_avartar, size=x[1]),
                )
            ),
            e.link(
                rel="stylesheet",
                href=https(
                    "stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
                ),
                integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T",
                crossorigin="anonymous",
            ),
            e.title()("Arijit Basu"),
        ),
        e.body()(
            e.div(class_="container")(
                e.p()(" "),
                e.div(class_="row")(
                    e.div(class_="col-sm-1 col-md-2 col-lg-3")(" "),
                    e.div(class_="col-sm-10 col-md-8 col-lg-6")(
                        e.p()(
                            linked_image(
                                url=https(gravatar_avartar, size=640),
                                alt="Arijit Basu's gravatar picture",
                                height="128",
                                width="128",
                            ),
                            e.br(),
                            "↑ this guy right here is ",
                            e.b()("Arijit Basu"),
                            " (sayan)",
                        ),
                        e.p()(
                            "He's kinda busy conquering the world of ",
                            external_url(
                                href=https("en.wikipedia.org/wiki/Computer_science"),
                                text="Computer Science",
                            ),
                            ".",
                        ),
                        e.p()(
                            "Here's a list of few places where you can find him these days:",
                            "{social_links}",
                            "And of course, ",
                            e.code()("(@ sayanarijit (. gmail com))"),
                        ),
                    ),
                    e.div(class_="col-sm-1 col-md-2 col-lg-3")(" "),
                ),
            )
        ),
    ),
)
def render_document():
    return {
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
        )
    }


if __name__ == "__main__":
    print(render_document())
