from htmlbuilder import (
    Document,
    a,
    body,
    br,
    button,
    div,
    element,
    h1,
    head,
    html,
    img,
    label,
    link,
    meta,
    p,
    title,
)


def test_simple_element() -> None:
    assert str(p()) == "<p></p>"


def test_element_with_text_child() -> None:
    assert str(p("Hello, World!")) == "<p>\n  Hello, World!\n</p>"


def test_element_with_attributes() -> None:
    result = str(div(id="main", class_="container"))
    assert result == '<div id="main" class="container"></div>'


def test_nested_elements() -> None:
    result = str(div(p("This is a paragraph.")))
    expected = """
<div>
  <p>
    This is a paragraph.
  </p>
</div>
    """.strip()
    assert result.strip() == expected


def test_self_closing_tag() -> None:
    result = str(img(src="image.jpg", alt="An image"))
    assert result == '<img src="image.jpg" alt="An image"/>'


def test_self_closing_tag_with_children() -> None:
    # This is an edge case. <br> shouldn't have children.
    result = str(br("some text"))
    expected = """
<br>
  some text
</br>
    """.strip()
    assert result.strip() == expected


def test_multiple_children() -> None:
    result = str(div(p("First paragraph."), "Just some text.", p("Second paragraph.")))
    expected = """
<div>
  <p>
    First paragraph.
  </p>
  Just some text.
  <p>
    Second paragraph.
  </p>
</div>
    """.strip()
    assert result.strip() == expected


def test_a_href() -> None:
    result = str(a("Click here", href="https://example.com", target="_blank"))
    assert (
        result == '<a href="https://example.com" target="_blank">\n  Click here\n</a>'
    )


def test_boolean_attribute_rendering() -> None:
    result = button("Click me", autofocus=True).to_html()
    assert result == "<button autofocus>Click me</button>"


def test_multiple_classes() -> None:
    result = str(p("paragraph", class_="class1"))
    assert result.strip() == '<p class="class1">\n  paragraph\n</p>'
    result = str(p("paragraph", class_=["class1", "class2"]))
    assert result.strip() == '<p class="class1 class2">\n  paragraph\n</p>'


def test_deeply_nested() -> None:
    result = str(
        div(div(p("Deeply nested text.")), div(p("Another nested paragraph.")))
    )
    expected = """
<div>
  <div>
    <p>
      Deeply nested text.
    </p>
  </div>
  <div>
    <p>
      Another nested paragraph.
    </p>
  </div>
</div>
    """.strip()
    assert result.strip() == expected


def test_custom_element() -> None:
    result = element("custom-tag", "Content", extra={"custom_attr": "value"}).to_html()
    assert result == '<custom-tag custom-attr="value">Content</custom-tag>'


def test_py_keywords() -> None:
    assert (
        label("Login:", for_="login").to_html() == '<label for="login">Login:</label>'
    )


def test_escaping() -> None:
    escaped = "&lt;script&gt;alert(&#x27;xxx&#x27;)&lt;/script&gt;"
    assert div("<script>alert('xxx')</script>").to_html() == f"<div>{escaped}</div>"
    assert (
        div(itemprop="<script>alert('xxx')</script>").to_html()
        == f'<div itemprop="{escaped}"></div>'
    )
    assert (
        div(extra={"mytag": "<script>alert('xxx')</script>"}).to_html()
        == f'<div mytag="{escaped}"></div>'
    )


def test_document() -> None:
    doc = Document(
        html(
            head(
                meta(charset="UTF-8"),
                meta(name="viewport", content="width=device-width, initial-scale=1.0"),
                title("Awesome document"),
                link(rel="stylesheet", href="https://cdn.simplecss.org/simple.css"),
            ),
            body(
                h1("Hello world"),
            ),
            lang="en",
        )
    )
    assert (
        str(doc)
        == """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>
      Awesome document
    </title>
    <link rel="stylesheet" href="https://cdn.simplecss.org/simple.css"/>
  </head>
  <body>
    <h1>
      Hello world
    </h1>
  </body>
</html>
""".strip()
    )
