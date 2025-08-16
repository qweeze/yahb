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
