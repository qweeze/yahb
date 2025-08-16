# Yet Another Python HTML Builder

A single-file, zero-dependency, fully-typed HTML builder library

### Usage:

```python
from yahb import (
    Document,
    Element,
    body,
    h1,
    head,
    html,
    img,
    link,
    main,
    meta,
    p,
    title,
)


def app() -> Element:
    return main(
        h1("Welcome to HTML Builder"),
        p(
            "Here's a cat for you:",
            img(src="https://cataas.com/cat"),
        ),
    )


doc = Document(
    html(
        head(
            meta(charset="UTF-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            title("My Awesome Page"),
            link(rel="stylesheet", href="https://cdn.simplecss.org/simple.css"),
        ),
        body(app()),
        lang="en",
    )
)
print(doc)
```

Output:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>
      My Awesome Page
    </title>
    <link rel="stylesheet" href="https://cdn.simplecss.org/simple.css"/>
  </head>
  <body>
    <main>
      <h1>
        Welcome to HTML Builder
      </h1>
      <p>
        Here&#x27;s a cat for you:
        <img src="https://cataas.com/cat"/>
      </p>
    </main>
  </body>
</html>
```

### Installation

```bash
pip install yahb
# or uv/poetry/pdm/next-shiny-thing add yahb
```

### Features

- Elements and their attrubutes are parsed from [WHATWG site](https://html.spec.whatwg.org/) so we have nice IDE / typechecker support:

```python
button(type="circle")
# mypy: Argument "type" to "button" has incompatible type "Literal['circle']";
# expected "Literal['submit', 'reset', 'button']"

a(href=None)
# mypy: Argument "href" to "a" has incompatible type "None"; expected "str"
```

- String content is auto-escaped:
```python
print(div("<script>alert('XSS')</script>"))
# <div>&lt;script&gt;alert(&#x27;XSS&#x27;)&lt;/script&gt;</div>
```

- Indentation levels support:
```python
print(div("Hello").to_html())
# <div>Hello</div>

print(div("Hello").to_html(indent=4))
# <div>
#     Hello
# </div>
```


### Inspired by
 - https://github.com/tvst/htbuilder
 - https://github.com/jaimevp54/htmlBuilder
