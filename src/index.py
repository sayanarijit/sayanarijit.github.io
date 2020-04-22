import typing as t
from textwrap import dedent

from htmldoom import doctype
from htmldoom import elements as e
from htmldoom import functions as fn
from htmldoom import renders
from htmldoom.url import https


gravatar_avartar = "secure.gravatar.com/avatar/260b78495c933d0b932ea23ccffa44dd"
gravatar_brands = (
    "gravatar.com/userimage/78986357/9d4ecf96126df0ccd63d2ade607d92b0?size=640"
)
current_city = "Pune"
links = (
    "github.com/sayanarijit",
    "dev.to/sayanarijit",
    "blog.niteo.co/author/sayanarijit",
)


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
            e.link(
                href=https(
                    "fonts.googleapis.com/css", family="Share Tech Mono", display="swap"
                ),
                rel="stylesheet",
            ),
            e.title()("This is Arijit Basu"),
        ),
        e.body()(
            e.div(
                class_="container", style="font-family: 'Share Tech Mono', monospace"
            )(
                e.div(class_="row justify-content-md-center")(
                    e.div(class_="col-sm-10 col-md-8")(
                        e.p(),
                        e.p()("This is Arijit Basu."),
                        e.p()("I do coding for a living and for time-pass."),
                        e.p()(
                            "I like science & tech, outdoor sports, adventure",
                            " activities, all things fitness and a minimalist",
                            " lifestyle..",
                        ),
                        e.hr(),
                        e.p()(
                            "I joined ",
                            e.a(href=https("techmahindra.com"))("Tech Mahindra"),
                            " after I finished college and worked for about 3 years.",
                        ),
                        e.p()(
                            "Now I develop software with the ",
                            e.a(href=https("niteo.co/team"))("Niteans"),
                            f", remotely from India (currently {current_city}, India).",
                        ),
                        e.hr(),
                        e.p()("Find me here:"),
                        e.ul()(
                            *fn.foreach(links)(
                                lambda link: e.li()(e.a(href=https(link))(link))
                            )
                        ),
                        e.p()(
                            "Or email me at: ",
                            e.code()("(@ sayanarijit (. gmail com))"),
                        ),
                        e.hr(),
                        e.p()(
                            e.a(
                                href=https(
                                    "github.com/sayanarijit/sayanarijit.github.io"
                                )
                            )("This site"),
                            " was built using ",
                            e.a(href=https("github.com/sayanarijit/htmldoom"))(
                                "htmldoom"
                            ),
                            ", one of my side projects.",
                        ),
                    )
                )
            )
        ),
    ),
)
def render_document() -> t.Dict[str, str]:
    return {}


if __name__ == "__main__":
    print(render_document())
