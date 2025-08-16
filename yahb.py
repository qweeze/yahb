from __future__ import annotations
import keyword
from dataclasses import dataclass, field
from html import escape
from typing import (
    Any,
    Generic,
    Literal,
    MutableSequence,
    Sequence,
    TypedDict,
    TypeVar,
    Unpack,
    cast,
)


class GlobalAttrs(TypedDict, total=False):
    # Can't make TypedDict to allow extra keys for now (see https://peps.python.org/pep-0728/)
    extra: dict[str, str]
    # https://html.spec.whatwg.org/multipage/#the-accesskey-attribute
    # An ordered set of unique space-separated tokens none of which are identical to
    # another token and each of which must be exactly one code point in length.
    accesskey: str
    # https://html.spec.whatwg.org/multipage/#attr-autocapitalize
    autocapitalize: Literal["off", "none", "on", "sentences", "words", "characters"]
    # https://html.spec.whatwg.org/multipage/interaction.html#attr-autocorrect
    autocorrect: Literal["on", "off"]
    # https://html.spec.whatwg.org/multipage/#attr-fe-autofocus
    autofocus: bool
    # https://html.spec.whatwg.org/multipage/#classes
    # A set of space-separated tokens representing the various classes that the element
    # belongs to.
    class_: str | Sequence[str]
    # https://html.spec.whatwg.org/multipage/#attr-contenteditable
    # A tristate attribute, not a boolean attribute.
    contenteditable: Literal["true", "false"]
    # https://html.spec.whatwg.org/multipage/#attr-dir
    dir: Literal["auto", "ltr", "rtl"]
    # https://html.spec.whatwg.org/multipage/#attr-draggable
    # A tristate attribute, not a bool attribute.
    draggable: Literal["true", "false"]
    # https://html.spec.whatwg.org/multipage/#attr-enterkeyhint
    enterkeyhint: Literal["enter", "done", "go", "next", "previous", "search", "send"]
    # https://html.spec.whatwg.org/multipage/#attr-hidden
    hidden: bool
    # https://html.spec.whatwg.org/multipage/#the-id-attribute
    # A unique value amount all id attributes of the HTML elements in your document. At
    # least one character in length and without ascii whitespace.
    id: str
    # https://html.spec.whatwg.org/multipage/interaction.html#the-inert-attribute
    inert: bool
    # https://html.spec.whatwg.org/multipage/#attr-inputmode
    inputmode: Literal[
        "none", "text", "tel", "url", "email", "numeric", "decimal", "search"
    ]
    # https://html.spec.whatwg.org/multipage/#attr-is
    # A valid custom element name.
    is_: str
    # https://html.spec.whatwg.org/multipage/#attr-itemid
    # A URL with optional surrounding whitespace.
    itemid: str
    # https://html.spec.whatwg.org/multipage/#names:-the-itemprop-attribute
    # A set of unique space-separated tokens. An empty value is not allowed.
    itemprop: str
    # https://html.spec.whatwg.org/multipage/#attr-itemref
    # A set of unique space-separated tokens referring to HTML element ids in the
    # current document.
    itemref: str
    # https://html.spec.whatwg.org/multipage/#attr-itemscope
    itemscope: bool
    # https://html.spec.whatwg.org/multipage/#attr-itemtype
    # A set of unique absolute URLs.
    itemtype: str
    # https://html.spec.whatwg.org/multipage/#attr-lang
    # A valid BCP 47 language tag or an empty string.
    lang: str
    # https://html.spec.whatwg.org/multipage/#attr-nonce
    # Any text is allowed.
    nonce: str
    # https://html.spec.whatwg.org/multipage/popover.html#attr-popover
    popover: Literal["auto", "manual", "hint"]
    # https://html.spec.whatwg.org/multipage/#handler-onabort
    onabort: str
    # https://html.spec.whatwg.org/multipage/#handler-onauxclick
    onauxclick: str
    # https://html.spec.whatwg.org/multipage/webappapis.html#handler-onbeforeinput
    onbeforeinput: str
    # https://html.spec.whatwg.org/multipage/webappapis.html#handler-onbeforematch
    onbeforematch: str
    # https://html.spec.whatwg.org/multipage/webappapis.html#handler-onbeforetoggle
    onbeforetoggle: str
    # https://html.spec.whatwg.org/multipage/#handler-onblur
    onblur: str
    # https://html.spec.whatwg.org/multipage/#handler-oncancel
    oncancel: str
    # https://html.spec.whatwg.org/multipage/#handler-oncanplay
    oncanplay: str
    # https://html.spec.whatwg.org/multipage/#handler-oncanplaythrough
    oncanplaythrough: str
    # https://html.spec.whatwg.org/multipage/#handler-onchange
    onchange: str
    # https://html.spec.whatwg.org/multipage/#handler-onclick
    onclick: str
    # https://html.spec.whatwg.org/multipage/#handler-onclose
    onclose: str
    # https://html.spec.whatwg.org/multipage/webappapis.html#handler-oncommand
    oncommand: str
    # https://html.spec.whatwg.org/multipage/webappapis.html#handler-oncontextlost
    oncontextlost: str
    # https://html.spec.whatwg.org/multipage/#handler-oncontextmenu
    oncontextmenu: str
    # https://html.spec.whatwg.org/multipage/webappapis.html#handler-oncontextlost
    oncontextrestored: str
    # https://html.spec.whatwg.org/multipage/#handler-oncopy
    oncopy: str
    # https://html.spec.whatwg.org/multipage/#handler-oncuechange
    oncuechange: str
    # https://html.spec.whatwg.org/multipage/#handler-oncut
    oncut: str
    # https://html.spec.whatwg.org/multipage/#handler-ondblclick
    ondblclick: str
    # https://html.spec.whatwg.org/multipage/#handler-ondrag
    ondrag: str
    # https://html.spec.whatwg.org/multipage/#handler-ondragend
    ondragend: str
    # https://html.spec.whatwg.org/multipage/#handler-ondragenter
    ondragenter: str
    # https://html.spec.whatwg.org/multipage/#handler-ondragleave
    ondragleave: str
    # https://html.spec.whatwg.org/multipage/#handler-ondragover
    ondragover: str
    # https://html.spec.whatwg.org/multipage/#handler-ondragstart
    ondragstart: str
    # https://html.spec.whatwg.org/multipage/#handler-ondrop
    ondrop: str
    # https://html.spec.whatwg.org/multipage/#handler-ondurationchange
    ondurationchange: str
    # https://html.spec.whatwg.org/multipage/#handler-onemptied
    onemptied: str
    # https://html.spec.whatwg.org/multipage/#handler-onended
    onended: str
    # https://html.spec.whatwg.org/multipage/#handler-onerror
    onerror: str
    # https://html.spec.whatwg.org/multipage/#handler-onfocus
    onfocus: str
    # https://html.spec.whatwg.org/multipage/#handler-onformdata
    onformdata: str
    # https://html.spec.whatwg.org/multipage/#handler-oninput
    oninput: str
    # https://html.spec.whatwg.org/multipage/#handler-oninvalid
    oninvalid: str
    # https://html.spec.whatwg.org/multipage/#handler-onkeydown
    onkeydown: str
    # https://html.spec.whatwg.org/multipage/#handler-onkeypress
    onkeypress: str
    # https://html.spec.whatwg.org/multipage/#handler-onkeyup
    onkeyup: str
    # https://html.spec.whatwg.org/multipage/#handler-onload
    onload: str
    # https://html.spec.whatwg.org/multipage/#handler-onloadeddata
    onloadeddata: str
    # https://html.spec.whatwg.org/multipage/#handler-onloadedmetadata
    onloadedmetadata: str
    # https://html.spec.whatwg.org/multipage/#handler-onloadstart
    onloadstart: str
    # https://html.spec.whatwg.org/multipage/#handler-onmousedown
    onmousedown: str
    # https://html.spec.whatwg.org/multipage/#handler-onmouseenter
    onmouseenter: str
    # https://html.spec.whatwg.org/multipage/#handler-onmouseleave
    onmouseleave: str
    # https://html.spec.whatwg.org/multipage/#handler-onmousemove
    onmousemove: str
    # https://html.spec.whatwg.org/multipage/#handler-onmouseout
    onmouseout: str
    # https://html.spec.whatwg.org/multipage/#handler-onmouseover
    onmouseover: str
    # https://html.spec.whatwg.org/multipage/#handler-onmouseup
    onmouseup: str
    # https://html.spec.whatwg.org/multipage/#handler-onpaste
    onpaste: str
    # https://html.spec.whatwg.org/multipage/#handler-onpause
    onpause: str
    # https://html.spec.whatwg.org/multipage/#handler-onplay
    onplay: str
    # https://html.spec.whatwg.org/multipage/#handler-onplaying
    onplaying: str
    # https://html.spec.whatwg.org/multipage/#handler-onprogress
    onprogress: str
    # https://html.spec.whatwg.org/multipage/#handler-onratechange
    onratechange: str
    # https://html.spec.whatwg.org/multipage/#handler-onreset
    onreset: str
    # https://html.spec.whatwg.org/multipage/#handler-onresize
    onresize: str
    # https://html.spec.whatwg.org/multipage/#handler-onscroll
    onscroll: str
    # https://html.spec.whatwg.org/multipage/webappapis.html#handler-onscrollend
    onscrollend: str
    # https://html.spec.whatwg.org/multipage/#handler-onsecuritypolicyviolation
    onsecuritypolicyviolation: str
    # https://html.spec.whatwg.org/multipage/#handler-onseeked
    onseeked: str
    # https://html.spec.whatwg.org/multipage/#handler-onseeking
    onseeking: str
    # https://html.spec.whatwg.org/multipage/#handler-onselect
    onselect: str
    # https://html.spec.whatwg.org/multipage/#handler-onslotchange
    onslotchange: str
    # https://html.spec.whatwg.org/multipage/#handler-onstalled
    onstalled: str
    # https://html.spec.whatwg.org/multipage/#handler-onsubmit
    onsubmit: str
    # https://html.spec.whatwg.org/multipage/#handler-onsuspend
    onsuspend: str
    # https://html.spec.whatwg.org/multipage/#handler-ontimeupdate
    ontimeupdate: str
    # https://html.spec.whatwg.org/multipage/#handler-ontoggle
    ontoggle: str
    # https://html.spec.whatwg.org/multipage/#handler-onvolumechange
    onvolumechange: str
    # https://html.spec.whatwg.org/multipage/#handler-onwaiting
    onwaiting: str
    # https://html.spec.whatwg.org/multipage/#handler-onwheel
    onwheel: str
    # https://html.spec.whatwg.org/#global-attributes:attr-aria-role
    role: str
    # https://html.spec.whatwg.org/multipage/#attr-slot
    # As far as I understand, any string is valid, since <slot name=?> is allowed to be
    # any string.
    slot: str
    # https://html.spec.whatwg.org/multipage/#attr-spellcheck
    # A tristate attribute, not a boolean attribute.
    spellcheck: Literal["true", "false"]
    # https://html.spec.whatwg.org/multipage/#attr-style
    # Valid CSS, see https://drafts.csswg.org/css-style-attr/ for more information.
    style: str
    # https://html.spec.whatwg.org/multipage/#attr-tabindex
    tabindex: int
    # https://html.spec.whatwg.org/multipage/#attr-title
    # Any text is allowed.
    title: str
    # https://html.spec.whatwg.org/multipage/#attr-translate
    translate: Literal["yes", "no"]
    # https://html.spec.whatwg.org/multipage/interaction.html#attr-writingsuggestions
    writingsuggestions: Literal["true", "false"]


_T_co = TypeVar("_T_co", bound=GlobalAttrs, covariant=True)

_SUFFIXED_KEYWORDS = frozenset(name + "_" for name in keyword.kwlist)


@dataclass
class Element(Generic[_T_co]):
    tag: str
    children: MutableSequence[Element[GlobalAttrs] | str] = field(default_factory=list)
    attrs: _T_co = field(default_factory=dict)  # type:ignore[assignment]
    selfclosing: bool = False

    def __str__(self) -> str:
        return self.to_html(indent=2, _level=0)

    def to_html(self, indent: int = 0, _level: int = 0) -> str:
        indent_str = " " * indent * _level
        sep = "\n" if indent > 0 else ""

        attrs_str = ""
        if self.attrs:
            _attrs = []
            all_attrs = self.attrs | cast(
                dict[str, Any], (self.attrs.get("extra") or {})
            )
            for k, v in all_attrs.items():
                if k == "extra":
                    continue

                if k in _SUFFIXED_KEYWORDS:
                    k = k.removesuffix("_")  # noqa:PLW2901

                k = k.replace("_", "-")  # noqa:PLW2901

                if k == "class" and isinstance(v, list):
                    v = " ".join(v)  # noqa:PLW2901

                if type(v) is bool and v:
                    _attrs.append(k)
                else:
                    _attrs.append(f'{k}="{escape(str(v))}"')

            attrs_str = " " + " ".join(_attrs)

        opening_tag = f"<{self.tag}{attrs_str}>"

        if self.selfclosing and not self.children:
            return f"{indent_str}{opening_tag.replace('>', '/>')}"

        if not self.children:
            return f"{indent_str}{opening_tag}</{self.tag}>"

        _children = []
        for child in self.children:
            match child:
                case Element():
                    _children.append(child.to_html(indent, _level + 1))
                case _:
                    child_indent = " " * indent * (_level + 1)
                    _children.append(f"{child_indent}{escape(str(child))}")
        children_str = sep.join(_children)
        return (
            f"{indent_str}{opening_tag}{sep}{children_str}"
            f"{sep}{indent_str}</{self.tag}>"
        )


@dataclass
class Document:
    root: Element[GlobalAttrs]

    def __str__(self) -> str:
        return f"<!DOCTYPE html>\n{self.root}"


def element(
    tag: str,
    /,
    *children: Element[GlobalAttrs] | str,
    selfclosing: bool = True,
    **attrs: Unpack[GlobalAttrs],
) -> Element[GlobalAttrs]:
    return Element(tag, children=list(children), attrs=attrs, selfclosing=selfclosing)


class _AAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-hyperlink-download
    # A valid file name.
    download: str
    # https://html.spec.whatwg.org/multipage/#attr-hyperlink-href
    # A URL potentially surrounded by spaces.
    href: str
    # https://html.spec.whatwg.org/multipage/#attr-hyperlink-hreflang
    # A valid BCP 47 language tag.
    hreflang: str
    # https://html.spec.whatwg.org/multipage/#ping
    # A space-separated list of http(s) urls.
    ping: str
    # https://html.spec.whatwg.org/multipage/#attr-hyperlink-referrerpolicy
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "same-origin",
        "origin",
        "strict-origin",
        "origin-when-cross-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    # https://html.spec.whatwg.org/multipage/#attr-hyperlink-rel
    # A space separated list of keywords. F.e. "next" or "license". See
    # https://html.spec.whatwg.org/multipage/links.html#linkTypes for more information.
    rel: str
    # https://html.spec.whatwg.org/multipage/#attr-hyperlink-target
    # A valid browsing context name, for example, "__blank", "__self" or "__parent". For
    # more see
    # https://html.spec.whatwg.org/multipage/browsers.html#valid-browsing-context-name-or-keyword.
    target: str
    # https://html.spec.whatwg.org/multipage/#attr-hyperlink-type
    # A MIME type string.
    type: str


def a(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_AAttrs]
) -> Element[_AAttrs]:
    return Element("a", list(children), attrs=attrs)


class _AbbrAttrs(GlobalAttrs, total=False): ...


def abbr(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_AbbrAttrs]
) -> Element[_AbbrAttrs]:
    return Element("abbr", list(children), attrs=attrs)


class _AddressAttrs(GlobalAttrs, total=False): ...


def address(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_AddressAttrs]
) -> Element[_AddressAttrs]:
    return Element("address", list(children), attrs=attrs)


class _AreaAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-area-alt
    # Any text which is an adequate replacement for the missing image.
    alt: str
    # https://html.spec.whatwg.org/multipage/#attr-area-coords
    # A list of comma separated floating point numbers.
    coords: str
    # https://html.spec.whatwg.org/multipage/#attr-hyperlink-download
    # A valid file name.
    download: str
    # https://html.spec.whatwg.org/multipage/#attr-hyperlink-href
    # A URL potentially surrounded by spaces.
    href: str
    # https://html.spec.whatwg.org/multipage/#ping
    # A space-separated list of http(s) urls.
    ping: str
    # https://html.spec.whatwg.org/multipage/#attr-hyperlink-referrerpolicy
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "same-origin",
        "origin",
        "strict-origin",
        "origin-when-cross-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    # https://html.spec.whatwg.org/multipage/#attr-hyperlink-rel
    # A space separated list of keywords. F.e. "next" or "license". See
    # https://html.spec.whatwg.org/multipage/links.html#linkTypes for more information.
    rel: str
    # https://html.spec.whatwg.org/multipage/#the-area-element:attr-area-shape
    shape: Literal["circle", "default", "poly", "rect"]
    # https://html.spec.whatwg.org/multipage/#attr-hyperlink-target
    # A valid browsing context name, for example, "__blank", "__self" or "__parent". For
    # more see
    # https://html.spec.whatwg.org/multipage/browsers.html#valid-browsing-context-name-or-keyword.
    target: str


def area(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_AreaAttrs]
) -> Element[_AreaAttrs]:
    return Element("area", list(children), attrs=attrs, selfclosing=True)


class _ArticleAttrs(GlobalAttrs, total=False): ...


def article(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_ArticleAttrs]
) -> Element[_ArticleAttrs]:
    return Element("article", list(children), attrs=attrs)


class _AsideAttrs(GlobalAttrs, total=False): ...


def aside(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_AsideAttrs]
) -> Element[_AsideAttrs]:
    return Element("aside", list(children), attrs=attrs)


class _AudioAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-media-autoplay
    autoplay: bool
    # https://html.spec.whatwg.org/multipage/#attr-media-controls
    controls: bool
    # https://html.spec.whatwg.org/multipage/#attr-media-crossorigin
    crossorigin: Literal["anonymous", "use-credentials"]
    # https://html.spec.whatwg.org/multipage/#attr-media-loop
    loop: bool
    # https://html.spec.whatwg.org/multipage/#attr-media-muted
    muted: bool
    # https://html.spec.whatwg.org/multipage/#attr-media-preload
    preload: Literal["none", "metadata", "auto"]
    # https://html.spec.whatwg.org/multipage/#attr-media-src
    # A URL potentially surrounded by spaces.
    src: str


def audio(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_AudioAttrs]
) -> Element[_AudioAttrs]:
    return Element("audio", list(children), attrs=attrs)


class _BAttrs(GlobalAttrs, total=False): ...


def b(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_BAttrs]
) -> Element[_BAttrs]:
    return Element("b", list(children), attrs=attrs)


class _BaseAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-base-href
    # A URL potentially surrounded by spaces.
    href: str
    # https://html.spec.whatwg.org/multipage/#attr-base-target
    # A valid browsing context name, for example, "__blank", "__self" or "__parent". For
    # more see
    # https://html.spec.whatwg.org/multipage/browsers.html#valid-browsing-context-name-or-keyword.
    target: str


def base(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_BaseAttrs]
) -> Element[_BaseAttrs]:
    return Element("base", list(children), attrs=attrs, selfclosing=True)


class _BdiAttrs(GlobalAttrs, total=False): ...


def bdi(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_BdiAttrs]
) -> Element[_BdiAttrs]:
    return Element("bdi", list(children), attrs=attrs)


class _BdoAttrs(GlobalAttrs, total=False): ...


def bdo(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_BdoAttrs]
) -> Element[_BdoAttrs]:
    return Element("bdo", list(children), attrs=attrs)


class _BlockquoteAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-blockquote-cite
    # A URL potentially surrounded by spaces.
    cite: str


def blockquote(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_BlockquoteAttrs]
) -> Element[_BlockquoteAttrs]:
    return Element("blockquote", list(children), attrs=attrs)


class _BodyAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#handler-window-onafterprint
    onafterprint: str
    # https://html.spec.whatwg.org/multipage/#handler-window-onbeforeprint
    onbeforeprint: str
    # https://html.spec.whatwg.org/multipage/#handler-window-onbeforeunload
    onbeforeunload: str
    # https://html.spec.whatwg.org/multipage/#handler-window-onhashchange
    onhashchange: str
    # https://html.spec.whatwg.org/multipage/#handler-window-onlanguagechange
    onlanguagechange: str
    # https://html.spec.whatwg.org/multipage/#handler-window-onmessage
    onmessage: str
    # https://html.spec.whatwg.org/multipage/#handler-window-onmessageerror
    onmessageerror: str
    # https://html.spec.whatwg.org/multipage/#handler-window-onoffline
    onoffline: str
    # https://html.spec.whatwg.org/multipage/#handler-window-ononline
    ononline: str
    # https://html.spec.whatwg.org/multipage/#handler-window-onpagehide
    onpagehide: str
    # https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onpagereveal
    onpagereveal: str
    # https://html.spec.whatwg.org/multipage/#handler-window-onpageshow
    onpageshow: str
    # https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onpageswap
    onpageswap: str
    # https://html.spec.whatwg.org/multipage/#handler-window-onpopstate
    onpopstate: str
    # https://html.spec.whatwg.org/multipage/#handler-window-onrejectionhandled
    onrejectionhandled: str
    # https://html.spec.whatwg.org/multipage/#handler-window-onstorage
    onstorage: str
    # https://html.spec.whatwg.org/multipage/#handler-window-onunhandledrejection
    onunhandledrejection: str
    # https://html.spec.whatwg.org/multipage/#handler-window-onunload
    onunload: str


def body(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_BodyAttrs]
) -> Element[_BodyAttrs]:
    return Element("body", list(children), attrs=attrs)


class _BrAttrs(GlobalAttrs, total=False): ...


def br(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_BrAttrs]
) -> Element[_BrAttrs]:
    return Element("br", list(children), attrs=attrs, selfclosing=True)


class _ButtonAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command
    # Valid options include: toggle-popover, show-popover, hide-popover, close,
    # request-close, show-modal, and a custom command keyword of your choosing
    command: str
    # https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-commandfor
    # A valid id of the element on which to perform the command
    commandfor: str
    # https://html.spec.whatwg.org/multipage/#attr-fe-disabled
    disabled: bool
    # https://html.spec.whatwg.org/multipage/#attr-fae-form
    # A valid id of a form element in the same tree.
    form: str
    # https://html.spec.whatwg.org/multipage/#attr-fs-formaction
    # A non-empty valid URL, potentially surrounded by whitespace.
    formaction: str
    # https://html.spec.whatwg.org/multipage/#attr-fs-formenctype
    formenctype: Literal[
        "application/x-www-form-urlencoded", "multipart/form-data", "text/plain"
    ]
    # https://html.spec.whatwg.org/multipage/#attr-fs-formmethod
    formmethod: Literal["dialog", "get", "post"]
    # https://html.spec.whatwg.org/multipage/#attr-fs-formnovalidate
    formnovalidate: bool
    # https://html.spec.whatwg.org/multipage/#attr-fs-formtarget
    # A valid browsing context name, for example, "__blank", "__self" or "__parent". For
    # more see
    # https://html.spec.whatwg.org/multipage/browsers.html#valid-browsing-context-name-or-keyword.
    formtarget: str
    # https://html.spec.whatwg.org/multipage/#attr-fe-name
    # Any name except for the empty string and isindex.
    name: str
    # https://html.spec.whatwg.org/multipage/popover.html#attr-popovertarget
    # A valid id of the popovertarget
    popovertarget: str
    # https://html.spec.whatwg.org/multipage/popover.html#attr-popovertargetaction
    popovertargetaction: Literal["toggle", "show", "hide"]
    # https://html.spec.whatwg.org/multipage/#attr-button-type
    type: Literal["submit", "reset", "button"]
    # https://html.spec.whatwg.org/multipage/#attr-button-value
    # Any text is allowed.
    value: str


def button(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_ButtonAttrs]
) -> Element[_ButtonAttrs]:
    return Element("button", list(children), attrs=attrs)


class _CanvasAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-canvas-height
    height: int
    # https://html.spec.whatwg.org/multipage/#attr-canvas-width
    width: int


def canvas(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_CanvasAttrs]
) -> Element[_CanvasAttrs]:
    return Element("canvas", list(children), attrs=attrs)


class _CaptionAttrs(GlobalAttrs, total=False): ...


def caption(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_CaptionAttrs]
) -> Element[_CaptionAttrs]:
    return Element("caption", list(children), attrs=attrs)


class _CiteAttrs(GlobalAttrs, total=False): ...


def cite(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_CiteAttrs]
) -> Element[_CiteAttrs]:
    return Element("cite", list(children), attrs=attrs)


class _CodeAttrs(GlobalAttrs, total=False): ...


def code(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_CodeAttrs]
) -> Element[_CodeAttrs]:
    return Element("code", list(children), attrs=attrs)


class _ColAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-col-span
    span: int


def col(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_ColAttrs]
) -> Element[_ColAttrs]:
    return Element("col", list(children), attrs=attrs, selfclosing=True)


class _ColgroupAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-colgroup-span
    span: int


def colgroup(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_ColgroupAttrs]
) -> Element[_ColgroupAttrs]:
    return Element("colgroup", list(children), attrs=attrs)


class _DataAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-data-value
    # Data in any machine-readable format.
    value: str


def data(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_DataAttrs]
) -> Element[_DataAttrs]:
    return Element("data", list(children), attrs=attrs)


class _DatalistAttrs(GlobalAttrs, total=False): ...


def datalist(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_DatalistAttrs]
) -> Element[_DatalistAttrs]:
    return Element("datalist", list(children), attrs=attrs)


class _DdAttrs(GlobalAttrs, total=False): ...


def dd(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_DdAttrs]
) -> Element[_DdAttrs]:
    return Element("dd", list(children), attrs=attrs)


class _DelAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-mod-cite
    # A URL.
    cite: str
    # https://html.spec.whatwg.org/multipage/#attr-mod-datetime
    # Valid date string with optional time. See
    # https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-date-string-with-optional-time
    # for more information.
    datetime: str


def del_(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_DelAttrs]
) -> Element[_DelAttrs]:
    return Element("del_", list(children), attrs=attrs)


class _DetailsAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-details-name
    # Name of group of mutually-exclusive details elements
    name: str
    # https://html.spec.whatwg.org/multipage/#attr-details-open
    open: bool


def details(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_DetailsAttrs]
) -> Element[_DetailsAttrs]:
    return Element("details", list(children), attrs=attrs)


class _DfnAttrs(GlobalAttrs, total=False): ...


def dfn(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_DfnAttrs]
) -> Element[_DfnAttrs]:
    return Element("dfn", list(children), attrs=attrs)


class _DialogAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-dialog-closedby
    closedby: Literal["any", "closerequest", "none"]
    # https://html.spec.whatwg.org/multipage/#attr-dialog-open
    open: bool


def dialog(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_DialogAttrs]
) -> Element[_DialogAttrs]:
    return Element("dialog", list(children), attrs=attrs)


class _DivAttrs(GlobalAttrs, total=False): ...


def div(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_DivAttrs]
) -> Element[_DivAttrs]:
    return Element("div", list(children), attrs=attrs)


class _DlAttrs(GlobalAttrs, total=False): ...


def dl(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_DlAttrs]
) -> Element[_DlAttrs]:
    return Element("dl", list(children), attrs=attrs)


class _DtAttrs(GlobalAttrs, total=False): ...


def dt(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_DtAttrs]
) -> Element[_DtAttrs]:
    return Element("dt", list(children), attrs=attrs)


class _EmAttrs(GlobalAttrs, total=False): ...


def em(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_EmAttrs]
) -> Element[_EmAttrs]:
    return Element("em", list(children), attrs=attrs)


class _EmbedAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-dim-height
    height: int
    # https://html.spec.whatwg.org/multipage/#attr-embed-src
    # A URL potentially surrounded by spaces.
    src: str
    # https://html.spec.whatwg.org/multipage/#attr-embed-type
    # A MIME type string.
    type: str
    # https://html.spec.whatwg.org/multipage/#attr-dim-width
    width: int


def embed(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_EmbedAttrs]
) -> Element[_EmbedAttrs]:
    return Element("embed", list(children), attrs=attrs, selfclosing=True)


class _FieldsetAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-fieldset-disabled
    disabled: bool
    # https://html.spec.whatwg.org/multipage/#attr-fae-form
    # A valid id of a form element in the same tree.
    form: str
    # https://html.spec.whatwg.org/multipage/#attr-fe-name
    # Any name except for the empty string and isindex.
    name: str


def fieldset(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_FieldsetAttrs]
) -> Element[_FieldsetAttrs]:
    return Element("fieldset", list(children), attrs=attrs)


class _FigcaptionAttrs(GlobalAttrs, total=False): ...


def figcaption(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_FigcaptionAttrs]
) -> Element[_FigcaptionAttrs]:
    return Element("figcaption", list(children), attrs=attrs)


class _FigureAttrs(GlobalAttrs, total=False): ...


def figure(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_FigureAttrs]
) -> Element[_FigureAttrs]:
    return Element("figure", list(children), attrs=attrs)


class _FooterAttrs(GlobalAttrs, total=False): ...


def footer(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_FooterAttrs]
) -> Element[_FooterAttrs]:
    return Element("footer", list(children), attrs=attrs)


class _FormAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-form-accept-charset
    # The only valid value is a case insensitive "utf-8".
    accept: str
    # https://html.spec.whatwg.org/multipage/#attr-fs-action
    # A non-empty valid URL, potentially surrounded by whitespace.
    action: str
    # https://html.spec.whatwg.org/multipage/#attr-form-autocomplete
    autocomplete: Literal["on", "off"]
    # https://html.spec.whatwg.org/multipage/#attr-fs-enctype
    enctype: Literal[
        "application/x-www-form-urlencoded", "multipart/form-data", "text/plain"
    ]
    # https://html.spec.whatwg.org/multipage/#attr-fs-method
    method: Literal["dialog", "get", "post"]
    # https://html.spec.whatwg.org/multipage/#attr-form-name
    # A name which is not the empty string. It must be unique within the context of the
    # current form.
    name: str
    # https://html.spec.whatwg.org/multipage/#attr-fs-novalidate
    novalidate: bool
    # https://html.spec.whatwg.org/multipage/#attr-form-rel
    # A space separated list of keywords. F.e. "next" or "license". See
    # https://html.spec.whatwg.org/multipage/links.html#linkTypes for more information.
    rel: str
    # https://html.spec.whatwg.org/multipage/#attr-fs-target
    # A valid browsing context name, for example, "__blank", "__self" or "__parent". For
    # more see
    # https://html.spec.whatwg.org/multipage/browsers.html#valid-browsing-context-name-or-keyword.
    target: str


def form(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_FormAttrs]
) -> Element[_FormAttrs]:
    return Element("form", list(children), attrs=attrs)


class _H1Attrs(GlobalAttrs, total=False): ...


def h1(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_H1Attrs]
) -> Element[_H1Attrs]:
    return Element("h1", list(children), attrs=attrs)


class _H2Attrs(GlobalAttrs, total=False): ...


def h2(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_H2Attrs]
) -> Element[_H2Attrs]:
    return Element("h2", list(children), attrs=attrs)


class _H3Attrs(GlobalAttrs, total=False): ...


def h3(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_H3Attrs]
) -> Element[_H3Attrs]:
    return Element("h3", list(children), attrs=attrs)


class _H4Attrs(GlobalAttrs, total=False): ...


def h4(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_H4Attrs]
) -> Element[_H4Attrs]:
    return Element("h4", list(children), attrs=attrs)


class _H5Attrs(GlobalAttrs, total=False): ...


def h5(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_H5Attrs]
) -> Element[_H5Attrs]:
    return Element("h5", list(children), attrs=attrs)


class _H6Attrs(GlobalAttrs, total=False): ...


def h6(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_H6Attrs]
) -> Element[_H6Attrs]:
    return Element("h6", list(children), attrs=attrs)


class _HeadAttrs(GlobalAttrs, total=False): ...


def head(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_HeadAttrs]
) -> Element[_HeadAttrs]:
    return Element("head", list(children), attrs=attrs)


class _HeaderAttrs(GlobalAttrs, total=False): ...


def header(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_HeaderAttrs]
) -> Element[_HeaderAttrs]:
    return Element("header", list(children), attrs=attrs)


class _HgroupAttrs(GlobalAttrs, total=False): ...


def hgroup(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_HgroupAttrs]
) -> Element[_HgroupAttrs]:
    return Element("hgroup", list(children), attrs=attrs)


class _HrAttrs(GlobalAttrs, total=False): ...


def hr(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_HrAttrs]
) -> Element[_HrAttrs]:
    return Element("hr", list(children), attrs=attrs, selfclosing=True)


class _HtmlAttrs(GlobalAttrs, total=False): ...


def html(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_HtmlAttrs]
) -> Element[_HtmlAttrs]:
    return Element("html", list(children), attrs=attrs)


class _IAttrs(GlobalAttrs, total=False): ...


def i(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_IAttrs]
) -> Element[_IAttrs]:
    return Element("i", list(children), attrs=attrs)


class _IframeAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-iframe-allow
    # A serialized permission policy. See
    # https://w3c.github.io/webappsec-permissions-policy/#ascii-serialization for more
    # information.
    allow: str
    # https://html.spec.whatwg.org/multipage/#attr-iframe-allowfullscreen
    allowfullscreen: bool
    # https://html.spec.whatwg.org/multipage/#attr-dim-height
    height: int
    # https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-loading
    loading: Literal["lazy", "eager"]
    # https://html.spec.whatwg.org/multipage/#attr-iframe-name
    # A valid browsing context name, for example, "__blank", "__self" or "__parent". For
    # more see
    # https://html.spec.whatwg.org/multipage/browsers.html#valid-browsing-context-name-or-keyword.
    name: str
    # https://html.spec.whatwg.org/multipage/#attr-iframe-referrerpolicy
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "same-origin",
        "origin",
        "strict-origin",
        "origin-when-cross-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    # https://html.spec.whatwg.org/multipage/#attr-iframe-sandbox
    # A set of unique space-separated tokens. Examples of valid values are
    # "allow-forms", "allow-modals", "allow-orientation-lock" and more may be added. See
    # https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-sandbox
    # for more information.
    sandbox: str
    # https://html.spec.whatwg.org/multipage/#attr-iframe-src
    # A URL potentially surrounded by spaces.
    src: str
    # https://html.spec.whatwg.org/multipage/#attr-iframe-srcdoc
    # Any number of comments and whitespace, optional doctype, any number of comments
    # and whitespace, an html document, any number of comments and whitespace.
    srcdoc: str
    # https://html.spec.whatwg.org/multipage/#attr-dim-width
    width: int


def iframe(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_IframeAttrs]
) -> Element[_IframeAttrs]:
    return Element("iframe", list(children), attrs=attrs)


class _ImgAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-img-alt
    # Any text which is an adequate replacement for the missing image.
    alt: str
    # https://html.spec.whatwg.org/multipage/#attr-img-crossorigin
    crossorigin: Literal["anonymous", "use-credentials"]
    # https://html.spec.whatwg.org/multipage/#attr-img-decoding
    decoding: Literal["sync", "async", "auto"]
    # https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-fetchpriority
    # A modern way to increase (or decrease) the priority with which the browser fetches
    # a resource. See
    # https://html.spec.whatwg.org/multipage/urls-and-fetching.html#fetch-priority-attribute
    fetchpriority: Literal["high", "low", "auto"]
    # https://html.spec.whatwg.org/multipage/#attr-dim-height
    height: int
    # https://html.spec.whatwg.org/multipage/#attr-img-ismap
    ismap: bool
    # https://html.spec.whatwg.org/multipage/#attr-img-loading
    loading: Literal["lazy", "eager"]
    # https://html.spec.whatwg.org/multipage/#attr-img-referrerpolicy
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "same-origin",
        "origin",
        "strict-origin",
        "origin-when-cross-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    # https://html.spec.whatwg.org/multipage/#attr-img-sizes
    # Complex syntax requirement, see
    # https://html.spec.whatwg.org/multipage/images.html#sizes-attribute.
    sizes: str
    # https://html.spec.whatwg.org/multipage/#attr-img-src
    # A URL potentially surrounded by spaces.
    src: str
    # https://html.spec.whatwg.org/multipage/#attr-img-srcset
    # Any number of image candidate strings. See
    # https://html.spec.whatwg.org/multipage/images.html#srcset-attribute for more
    # information.
    srcset: str
    # https://html.spec.whatwg.org/multipage/#attr-hyperlink-usemap
    # A hash-name reference to a map element.
    usemap: str
    # https://html.spec.whatwg.org/multipage/#attr-dim-width
    width: int


def img(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_ImgAttrs]
) -> Element[_ImgAttrs]:
    return Element("img", list(children), attrs=attrs, selfclosing=True)


class _InputAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-input-accept
    # A comma separated list of "audio/", "video/", "image/", a valid MIME type
    # string with no parameters, file extensions starting with a ".".
    accept: str
    # https://html.spec.whatwg.org/multipage/input.html#attr-input-alpha
    # If present, it indicates the CSS color's alpha component can be manipulated by the
    # end user and does not have to be fully opaque.
    alpha: bool
    # https://html.spec.whatwg.org/multipage/#attr-input-alt
    # Any text which is an adequate replacement for the missing image.
    alt: str
    # https://html.spec.whatwg.org/multipage/#attr-fe-autocomplete
    # Either "on" or "off", or autofill detail tokens.
    autocomplete: str
    # https://html.spec.whatwg.org/multipage/#attr-input-checked
    checked: bool
    # https://html.spec.whatwg.org/multipage/input.html#attr-input-colorspace
    colorspace: Literal["limited-srgb", "display-p3"]
    # https://html.spec.whatwg.org/multipage/#attr-fe-dirname
    # Any name that is not an empty string. The browser will implicitly append `.dir` in
    # the urlencoded parameters sent to the server.
    dirname: str
    # https://html.spec.whatwg.org/multipage/#attr-fe-disabled
    disabled: bool
    # https://html.spec.whatwg.org/multipage/#attr-fae-form
    # A valid id of a form element in the same tree.
    form: str
    # https://html.spec.whatwg.org/multipage/#attr-fs-formaction
    # A non-empty valid URL, potentially surrounded by whitespace.
    formaction: str
    # https://html.spec.whatwg.org/multipage/#attr-fs-formenctype
    formenctype: Literal[
        "application/x-www-form-urlencoded", "multipart/form-data", "text/plain"
    ]
    # https://html.spec.whatwg.org/multipage/#attr-fs-formmethod
    formmethod: Literal["dialog", "get", "post"]
    # https://html.spec.whatwg.org/multipage/#attr-fs-formnovalidate
    formnovalidate: bool
    # https://html.spec.whatwg.org/multipage/#attr-fs-formtarget
    # A valid browsing context name, for example, "__blank", "__self" or "__parent". For
    # more see
    # https://html.spec.whatwg.org/multipage/browsers.html#valid-browsing-context-name-or-keyword.
    formtarget: str
    # https://html.spec.whatwg.org/multipage/#attr-dim-height
    height: int
    # https://html.spec.whatwg.org/multipage/#attr-input-list
    # The id of a datalist element.
    list: str
    # https://html.spec.whatwg.org/multipage/#attr-input-max
    # Acceptable values are defined by the type attribute.
    max: str
    # https://html.spec.whatwg.org/multipage/#attr-input-maxlength
    maxlength: int
    # https://html.spec.whatwg.org/multipage/#attr-input-min
    # Acceptable values are defined by the type attribute.
    min: str
    # https://html.spec.whatwg.org/multipage/#attr-input-minlength
    minlength: int
    # https://html.spec.whatwg.org/multipage/#attr-input-multiple
    multiple: bool
    # https://html.spec.whatwg.org/multipage/#attr-fe-name
    # Any name except for the empty string and isindex.
    name: str
    # https://html.spec.whatwg.org/multipage/#attr-input-pattern
    # A JS regex pattern.
    pattern: str
    # https://html.spec.whatwg.org/multipage/#attr-input-placeholder
    # A string without a linefeed (\n) or carriage return (\r).
    placeholder: str
    # https://html.spec.whatwg.org/multipage/popover.html#attr-popovertarget
    # A valid id of the popovertarget
    popovertarget: str
    # https://html.spec.whatwg.org/multipage/popover.html#attr-popovertargetaction
    popovertargetaction: Literal["toggle", "show", "hide"]
    # https://html.spec.whatwg.org/multipage/#attr-input-readonly
    readonly: bool
    # https://html.spec.whatwg.org/multipage/#attr-input-required
    required: bool
    # https://html.spec.whatwg.org/multipage/#attr-input-size
    size: int
    # https://html.spec.whatwg.org/multipage/#attr-input-src
    # A URL potentially surrounded by spaces.
    src: str
    # https://html.spec.whatwg.org/multipage/#attr-input-step
    # A positive non-zero floating point number or the literal string "any".
    step: str
    # https://html.spec.whatwg.org/multipage/#attr-input-type
    type: Literal[
        "hidden",
        "text",
        "search",
        "tel",
        "url",
        "email",
        "password",
        "date",
        "month",
        "week",
        "time",
        "datetime",
        "number",
        "range",
        "color",
        "checkbox",
        "radio",
        "file",
        "submit",
        "image",
        "reset",
        "button",
    ]
    # https://html.spec.whatwg.org/multipage/#attr-input-value
    # Any text is allowed.
    value: str
    # https://html.spec.whatwg.org/multipage/#attr-dim-width
    width: int


def input_(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_InputAttrs]
) -> Element[_InputAttrs]:
    return Element("input", list(children), attrs=attrs, selfclosing=True)


class _InsAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-mod-cite
    # A URL potentially surrounded by spaces.
    cite: str
    # https://html.spec.whatwg.org/multipage/#attr-mod-datetime
    # Valid date string with optional time. See
    # https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-date-string-with-optional-time
    # for more information.
    datetime: str


def ins(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_InsAttrs]
) -> Element[_InsAttrs]:
    return Element("ins", list(children), attrs=attrs)


class _KbdAttrs(GlobalAttrs, total=False): ...


def kbd(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_KbdAttrs]
) -> Element[_KbdAttrs]:
    return Element("kbd", list(children), attrs=attrs)


class _LabelAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-label-for
    # The id of a labelable element.
    for_: str


def label(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_LabelAttrs]
) -> Element[_LabelAttrs]:
    return Element("label", list(children), attrs=attrs)


class _LegendAttrs(GlobalAttrs, total=False): ...


def legend(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_LegendAttrs]
) -> Element[_LegendAttrs]:
    return Element("legend", list(children), attrs=attrs)


class _LiAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-li-value
    value: int


def li(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_LiAttrs]
) -> Element[_LiAttrs]:
    return Element("li", list(children), attrs=attrs)


class _LinkAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-link-as
    # Common values are: "script" and "style". See
    # https://fetch.spec.whatwg.org/#concept-request-destination for more information.
    as_: str
    # https://html.spec.whatwg.org/multipage/semantics.html#attr-link-blocking
    # Not very useful at this time. It is not possible to use this attribute to make
    # something that was render-blocking not render-blocking.
    blocking: Literal["render"]
    # https://html.spec.whatwg.org/multipage/#attr-link-color
    # A CSS color value.
    color: str
    # https://html.spec.whatwg.org/multipage/#attr-link-crossorigin
    crossorigin: Literal["anonymous", "use-credentials"]
    # https://html.spec.whatwg.org/multipage/#attr-link-disabled
    disabled: bool
    # https://html.spec.whatwg.org/multipage/semantics.html#attr-link-fetchpriority
    # A modern way to increase (or decrease) the priority with which the browser fetches
    # a resource. See
    # https://html.spec.whatwg.org/multipage/urls-and-fetching.html#fetch-priority-attribute
    fetchpriority: Literal["high", "low", "auto"]
    # https://html.spec.whatwg.org/multipage/#attr-link-href
    # A URL potentially surrounded by spaces.
    href: str
    # https://html.spec.whatwg.org/multipage/#attr-link-hreflang
    # A valid BCP 47 language tag.
    hreflang: str
    # https://html.spec.whatwg.org/multipage/#attr-link-imagesizes
    # Complex syntax requirement, see
    # https://html.spec.whatwg.org/multipage/images.html#sizes-attribute.
    imagesizes: str
    # https://html.spec.whatwg.org/multipage/#attr-link-imagesrcset
    # Any number of image candidate strings. See
    # https://html.spec.whatwg.org/multipage/images.html#srcset-attribute for more
    # information.
    imagesrcset: str
    # https://html.spec.whatwg.org/multipage/#attr-link-integrity
    # Commonly a hash algorithm a "-" and a base64 encoded value of the hash. See
    # https://w3c.github.io/webappsec-subresource-integrity/#the-integrity-attribute for
    # more information.
    integrity: str
    # https://html.spec.whatwg.org/multipage/semantics.html#attr-link-media
    # A valid media query list. See
    # https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-media-query-list
    # for more information.
    media: str
    # https://html.spec.whatwg.org/multipage/#attr-link-referrerpolicy
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "same-origin",
        "origin",
        "strict-origin",
        "origin-when-cross-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    # https://html.spec.whatwg.org/multipage/#attr-link-rel
    # A space separated list of keywords. F.e. "next" or "license". See
    # https://html.spec.whatwg.org/multipage/links.html#linkTypes for more information.
    rel: str
    # https://html.spec.whatwg.org/multipage/#attr-link-sizes
    # Either the string "any" or two pixel values, separated by an "x"
    sizes: str
    # https://html.spec.whatwg.org/multipage/#attr-link-type
    # A MIME type string.
    type: str


def link(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_LinkAttrs]
) -> Element[_LinkAttrs]:
    return Element("link", list(children), attrs=attrs, selfclosing=True)


class _MainAttrs(GlobalAttrs, total=False): ...


def main(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_MainAttrs]
) -> Element[_MainAttrs]:
    return Element("main", list(children), attrs=attrs)


class _MapAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-map-name
    # Any name.
    name: str


def map_(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_MapAttrs]
) -> Element[_MapAttrs]:
    return Element("map", list(children), attrs=attrs)


class _MarkAttrs(GlobalAttrs, total=False): ...


def mark(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_MarkAttrs]
) -> Element[_MarkAttrs]:
    return Element("mark", list(children), attrs=attrs)


class _MenuAttrs(GlobalAttrs, total=False): ...


def menu(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_MenuAttrs]
) -> Element[_MenuAttrs]:
    return Element("menu", list(children), attrs=attrs)


class _MetaAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-meta-charset
    # The only valid value is a case insensitive "utf-8".
    charset: str
    # https://html.spec.whatwg.org/multipage/#attr-meta-content
    # Valid values are defined based on the value of the "name" attribute.
    content: str
    # https://html.spec.whatwg.org/multipage/#attr-meta-http-equiv
    http: Literal[
        "content-type",
        "default-style",
        "refresh",
        "x-ua-compatible",
        "content-security-policy",
    ]
    # https://html.spec.whatwg.org/multipage/semantics.html#attr-meta-media
    # Unless the name is theme-color, the media attribute has no effect on the
    # processing model and must not be used by authors.
    media: str
    # https://html.spec.whatwg.org/multipage/#attr-meta-name
    # Any name.
    name: str


def meta(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_MetaAttrs]
) -> Element[_MetaAttrs]:
    return Element("meta", list(children), attrs=attrs, selfclosing=True)


class _MeterAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-meter-high
    high: float
    # https://html.spec.whatwg.org/multipage/#attr-meter-low
    low: float
    # https://html.spec.whatwg.org/multipage/#attr-meter-max
    max: float
    # https://html.spec.whatwg.org/multipage/#attr-meter-min
    min: float
    # https://html.spec.whatwg.org/multipage/#attr-meter-optimum
    optimum: float
    # https://html.spec.whatwg.org/multipage/#attr-meter-value
    value: float


def meter(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_MeterAttrs]
) -> Element[_MeterAttrs]:
    return Element("meter", list(children), attrs=attrs)


class _NavAttrs(GlobalAttrs, total=False): ...


def nav(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_NavAttrs]
) -> Element[_NavAttrs]:
    return Element("nav", list(children), attrs=attrs)


class _NoscriptAttrs(GlobalAttrs, total=False): ...


def noscript(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_NoscriptAttrs]
) -> Element[_NoscriptAttrs]:
    return Element("noscript", list(children), attrs=attrs)


class _ObjectAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-object-data
    # A URL potentially surrounded by spaces.
    data: str
    # https://html.spec.whatwg.org/multipage/#attr-dim-height
    height: int
    # https://html.spec.whatwg.org/multipage/#attr-fae-form
    # A valid id of a form element in the same tree.
    form: str
    # https://html.spec.whatwg.org/multipage/#attr-object-name
    # A valid browsing context name, for example, "__blank", "__self" or "__parent". For
    # more see
    # https://html.spec.whatwg.org/multipage/browsers.html#valid-browsing-context-name-or-keyword.
    name: str
    # https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-object-type
    # A MIME type string.
    type: str
    # https://html.spec.whatwg.org/multipage/#attr-hyperlink-usemap
    # A hash-name reference to a map element.
    usemap: str
    # https://html.spec.whatwg.org/multipage/#attr-dim-width
    width: int


def object_(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_ObjectAttrs]
) -> Element[_ObjectAttrs]:
    return Element("object", list(children), attrs=attrs)


class _OlAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-ol-reversed
    reversed: bool
    # https://html.spec.whatwg.org/multipage/#attr-ol-start
    start: int
    # https://html.spec.whatwg.org/multipage/#attr-ol-type
    type: Literal["1", "a", "A", "i", "I"]


def ol(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_OlAttrs]
) -> Element[_OlAttrs]:
    return Element("ol", list(children), attrs=attrs)


class _OptgroupAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-optgroup-disabled
    disabled: bool
    # https://html.spec.whatwg.org/multipage/#attr-optgroup-label
    # Any text is allowed.
    label: str


def optgroup(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_OptgroupAttrs]
) -> Element[_OptgroupAttrs]:
    return Element("optgroup", list(children), attrs=attrs)


class _OptionAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-option-disabled
    disabled: bool
    # https://html.spec.whatwg.org/multipage/#attr-option-label
    # Any non empty string.
    label: str
    # https://html.spec.whatwg.org/multipage/#attr-option-selected
    selected: bool
    # https://html.spec.whatwg.org/multipage/#attr-option-value
    # Any text is allowed.
    value: str


def option(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_OptionAttrs]
) -> Element[_OptionAttrs]:
    return Element("option", list(children), attrs=attrs)


class _OutputAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-output-for
    # A set of unique space-separated tokens. Each of which is an id of an element in
    # the same document.
    for_: str
    # https://html.spec.whatwg.org/multipage/#attr-fae-form
    # A valid id of a form element in the same tree.
    form: str
    # https://html.spec.whatwg.org/multipage/#attr-fe-name
    # Any name except for the empty string and isindex.
    name: str


def output(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_OutputAttrs]
) -> Element[_OutputAttrs]:
    return Element("output", list(children), attrs=attrs)


class _PAttrs(GlobalAttrs, total=False): ...


def p(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_PAttrs]
) -> Element[_PAttrs]:
    return Element("p", list(children), attrs=attrs)


class _ParamAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-param-name
    # Any name.
    name: str
    # https://html.spec.whatwg.org/multipage/#attr-param-value
    # Any text is allowed.
    value: str


def param(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_ParamAttrs]
) -> Element[_ParamAttrs]:
    return Element("param", list(children), attrs=attrs)


class _PictureAttrs(GlobalAttrs, total=False): ...


def picture(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_PictureAttrs]
) -> Element[_PictureAttrs]:
    return Element("picture", list(children), attrs=attrs)


class _PreAttrs(GlobalAttrs, total=False): ...


def pre(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_PreAttrs]
) -> Element[_PreAttrs]:
    return Element("pre", list(children), attrs=attrs)


class _ProgressAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-progress-value
    max: float
    # https://html.spec.whatwg.org/multipage/#attr-progress-max
    value: float


def progress(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_ProgressAttrs]
) -> Element[_ProgressAttrs]:
    return Element("progress", list(children), attrs=attrs)


class _QAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-q-cite
    # A URL potentially surrounded by spaces.
    cite: str


def q(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_QAttrs]
) -> Element[_QAttrs]:
    return Element("q", list(children), attrs=attrs)


class _RpAttrs(GlobalAttrs, total=False): ...


def rp(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_RpAttrs]
) -> Element[_RpAttrs]:
    return Element("rp", list(children), attrs=attrs)


class _RtAttrs(GlobalAttrs, total=False): ...


def rt(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_RtAttrs]
) -> Element[_RtAttrs]:
    return Element("rt", list(children), attrs=attrs)


class _RubyAttrs(GlobalAttrs, total=False): ...


def ruby(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_RubyAttrs]
) -> Element[_RubyAttrs]:
    return Element("ruby", list(children), attrs=attrs)


class _SAttrs(GlobalAttrs, total=False): ...


def s(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_SAttrs]
) -> Element[_SAttrs]:
    return Element("s", list(children), attrs=attrs)


class _SampAttrs(GlobalAttrs, total=False): ...


def samp(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_SampAttrs]
) -> Element[_SampAttrs]:
    return Element("samp", list(children), attrs=attrs)


class _ScriptAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-script-async
    async_: bool
    # https://html.spec.whatwg.org/multipage/scripting.html#attr-script-blocking
    # Not very useful at this time. It is not possible to use this attribute to make an
    # inline script not render-blocking.
    blocking: Literal["render"]
    # https://html.spec.whatwg.org/multipage/#attr-script-crossorigin
    crossorigin: Literal["anonymous", "use-credentials"]
    # https://html.spec.whatwg.org/multipage/#attr-script-defer
    defer: bool
    # https://html.spec.whatwg.org/multipage/scripting.html#attr-script-fetchpriority
    # A modern way to increase (or decrease) the priority with which the browser fetches
    # a resource. See
    # https://html.spec.whatwg.org/multipage/urls-and-fetching.html#fetch-priority-attribute
    fetchpriority: Literal["high", "low", "auto"]
    # https://html.spec.whatwg.org/multipage/#attr-script-integrity
    # Commonly a hash algorithm a "-" and a base64 encoded value of the hash. See
    # https://w3c.github.io/webappsec-subresource-integrity/#the-integrity-attribute for
    # more information.
    integrity: str
    # https://html.spec.whatwg.org/multipage/#attr-script-nomodule
    nomodule: bool
    # https://html.spec.whatwg.org/multipage/#attr-script-referrerpolicy
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "same-origin",
        "origin",
        "strict-origin",
        "origin-when-cross-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    # https://html.spec.whatwg.org/multipage/#attr-script-src
    # A URL potentially surrounded by spaces.
    src: str
    # https://html.spec.whatwg.org/multipage/#attr-script-type
    # An empty string or a javascript MIME type for non module javascript. "module" for
    # module javascript. Any other value makes this script tag a data block.
    type: str


def script(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_ScriptAttrs]
) -> Element[_ScriptAttrs]:
    return Element("script", list(children), attrs=attrs)


class _SearchAttrs(GlobalAttrs, total=False): ...


def search(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_SearchAttrs]
) -> Element[_SearchAttrs]:
    return Element("search", list(children), attrs=attrs)


class _SectionAttrs(GlobalAttrs, total=False): ...


def section(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_SectionAttrs]
) -> Element[_SectionAttrs]:
    return Element("section", list(children), attrs=attrs)


class _SelectAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-fe-autocomplete
    # Either "on" or "off", or autofill detail tokens.
    autocomplete: str
    # https://html.spec.whatwg.org/multipage/#attr-fe-disabled
    disabled: bool
    # https://html.spec.whatwg.org/multipage/#attr-fae-form
    # A valid id of a form element in the same tree.
    form: str
    # https://html.spec.whatwg.org/multipage/#attr-select-multiple
    multiple: bool
    # https://html.spec.whatwg.org/multipage/#attr-fe-name
    # Any name except for the empty string and isindex.
    name: str
    # https://html.spec.whatwg.org/multipage/#attr-select-required
    required: bool
    # https://html.spec.whatwg.org/multipage/#attr-select-size
    size: int


def select(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_SelectAttrs]
) -> Element[_SelectAttrs]:
    return Element("select", list(children), attrs=attrs)


class _SlotAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-slot-name
    # Any name.
    name: str


def slot(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_SlotAttrs]
) -> Element[_SlotAttrs]:
    return Element("slot", list(children), attrs=attrs)


class _SmallAttrs(GlobalAttrs, total=False): ...


def small(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_SmallAttrs]
) -> Element[_SmallAttrs]:
    return Element("small", list(children), attrs=attrs)


class _SourceAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/embedded-content-other.html#attr-dim-height
    height: int
    # https://html.spec.whatwg.org/multipage/#attr-source-media
    # A valid media query list. See
    # https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-media-query-list
    # for more information.
    media: str
    # https://html.spec.whatwg.org/multipage/#attr-source-sizes
    # Complex syntax requirement, see
    # https://html.spec.whatwg.org/multipage/images.html#sizes-attribute.
    sizes: str
    # https://html.spec.whatwg.org/multipage/#attr-source-src
    # A URL potentially surrounded by spaces.
    src: str
    # https://html.spec.whatwg.org/multipage/#attr-source-srcset
    # Any number of image candidate strings. See
    # https://html.spec.whatwg.org/multipage/images.html#srcset-attribute for more
    # information.
    srcset: str
    # https://html.spec.whatwg.org/multipage/#attr-source-type
    # A MIME type string.
    type: str
    # https://html.spec.whatwg.org/multipage/embedded-content-other.html#attr-dim-width
    width: int


def source(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_SourceAttrs]
) -> Element[_SourceAttrs]:
    return Element("source", list(children), attrs=attrs, selfclosing=True)


class _SpanAttrs(GlobalAttrs, total=False): ...


def span(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_SpanAttrs]
) -> Element[_SpanAttrs]:
    return Element("span", list(children), attrs=attrs)


class _StrongAttrs(GlobalAttrs, total=False): ...


def strong(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_StrongAttrs]
) -> Element[_StrongAttrs]:
    return Element("strong", list(children), attrs=attrs)


class _StyleAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/semantics.html#attr-style-blocking
    # Not very useful at this time. It is not possible to use this attribute to make an
    # inline stylesheet not render-blocking.
    blocking: Literal["render"]
    # https://html.spec.whatwg.org/multipage/#attr-style-media
    # A valid media query list. See
    # https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-media-query-list
    # for more information.
    media: str


def style(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_StyleAttrs]
) -> Element[_StyleAttrs]:
    return Element("style", list(children), attrs=attrs)


class _SubAttrs(GlobalAttrs, total=False): ...


def sub(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_SubAttrs]
) -> Element[_SubAttrs]:
    return Element("sub", list(children), attrs=attrs)


class _SummaryAttrs(GlobalAttrs, total=False): ...


def summary(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_SummaryAttrs]
) -> Element[_SummaryAttrs]:
    return Element("summary", list(children), attrs=attrs)


class _SupAttrs(GlobalAttrs, total=False): ...


def sup(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_SupAttrs]
) -> Element[_SupAttrs]:
    return Element("sup", list(children), attrs=attrs)


class _TableAttrs(GlobalAttrs, total=False): ...


def table(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_TableAttrs]
) -> Element[_TableAttrs]:
    return Element("table", list(children), attrs=attrs)


class _TbodyAttrs(GlobalAttrs, total=False): ...


def tbody(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_TbodyAttrs]
) -> Element[_TbodyAttrs]:
    return Element("tbody", list(children), attrs=attrs)


class _TdAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-tdth-colspan
    colspan: int
    # https://html.spec.whatwg.org/multipage/#attr-tdth-headers
    # A set of unique space-separated tokens. Each of which is an id of a th element in
    # the same table.
    headers: str
    # https://html.spec.whatwg.org/multipage/#attr-tdth-rowspan
    rowspan: int


def td(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_TdAttrs]
) -> Element[_TdAttrs]:
    return Element("td", list(children), attrs=attrs)


class _TemplateAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/scripting.html#attr-template-shadowrootmode
    shadowrootmode: Literal["open", "closed"]
    # https://html.spec.whatwg.org/multipage/scripting.html#attr-template-shadowrootdelegatesfocus
    shadowrootdelegatesfocus: bool
    # https://html.spec.whatwg.org/multipage/scripting.html#attr-template-shadowrootclonable
    shadowrootclonable: bool
    # https://html.spec.whatwg.org/multipage/scripting.html#attr-template-shadowrootserializable
    shadowrootserializable: bool
    # https://html.spec.whatwg.org/multipage/scripting.html#attr-template-shadowrootcustomelementregistry
    shadowrootcustomelementregistry: bool


def template(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_TemplateAttrs]
) -> Element[_TemplateAttrs]:
    return Element("template", list(children), attrs=attrs)


class _TextareaAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-fe-autocomplete
    # Either "on" or "off", or autofill detail tokens.
    autocomplete: str
    # https://html.spec.whatwg.org/multipage/#attr-textarea-cols
    cols: int
    # https://html.spec.whatwg.org/multipage/#attr-fe-dirname
    # Any name that is not an empty string. The browser will implicitly append `.dir` in
    # the urlencoded parameters sent to the server.
    dirname: str
    # https://html.spec.whatwg.org/multipage/#attr-fe-disabled
    disabled: bool
    # https://html.spec.whatwg.org/multipage/#attr-fae-form
    # A valid id of a form element in the same tree.
    form: str
    # https://html.spec.whatwg.org/multipage/#attr-textarea-maxlength
    maxlength: int
    # https://html.spec.whatwg.org/multipage/#attr-textarea-minlength
    minlength: int
    # https://html.spec.whatwg.org/multipage/#attr-fe-name
    # Any name except for the empty string and isindex.
    name: str
    # https://html.spec.whatwg.org/multipage/#attr-textarea-placeholder
    # Any string is allowed. Line feeds and carriage represent are line breaks.
    placeholder: str
    # https://html.spec.whatwg.org/multipage/#attr-textarea-readonly
    readonly: bool
    # https://html.spec.whatwg.org/multipage/#attr-textarea-required
    required: bool
    # https://html.spec.whatwg.org/multipage/#attr-textarea-rows
    rows: int
    # https://html.spec.whatwg.org/multipage/#attr-textarea-wrap
    wrap: Literal["hard", "soft"]


def textarea(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_TextareaAttrs]
) -> Element[_TextareaAttrs]:
    return Element("textarea", list(children), attrs=attrs)


class _TfootAttrs(GlobalAttrs, total=False): ...


def tfoot(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_TfootAttrs]
) -> Element[_TfootAttrs]:
    return Element("tfoot", list(children), attrs=attrs)


class _ThAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-th-abbr
    # An alternative label.
    abbr: str
    # https://html.spec.whatwg.org/multipage/#attr-tdth-colspan
    colspan: int
    # https://html.spec.whatwg.org/multipage/#attr-tdth-headers
    # A set of unique space-separated tokens. Each of which is an id of a th element in
    # the same table.
    headers: str
    # https://html.spec.whatwg.org/multipage/#attr-tdth-rowspan
    rowspan: int
    # https://html.spec.whatwg.org/multipage/#attr-th-scope
    scope: Literal["col", "colgroup", "row", "rowgroup"]


def th(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_ThAttrs]
) -> Element[_ThAttrs]:
    return Element("th", list(children), attrs=attrs)


class _TheadAttrs(GlobalAttrs, total=False): ...


def thead(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_TheadAttrs]
) -> Element[_TheadAttrs]:
    return Element("thead", list(children), attrs=attrs)


class _TimeAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-time-datetime
    # Valid date string with optional time. See
    # https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-date-string-with-optional-time
    # for more information.
    datetime: str


def time(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_TimeAttrs]
) -> Element[_TimeAttrs]:
    return Element("time", list(children), attrs=attrs)


class _TitleAttrs(GlobalAttrs, total=False): ...


def title(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_TitleAttrs]
) -> Element[_TitleAttrs]:
    return Element("title", list(children), attrs=attrs)


class _TrAttrs(GlobalAttrs, total=False): ...


def tr(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_TrAttrs]
) -> Element[_TrAttrs]:
    return Element("tr", list(children), attrs=attrs)


class _TrackAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-track-default
    default: bool
    # https://html.spec.whatwg.org/multipage/#attr-track-kind
    kind: Literal["subtitles", "captions", "descriptions", "chapters", "metadata"]
    # https://html.spec.whatwg.org/multipage/#attr-track-label
    # Any non empty string.
    label: str
    # https://html.spec.whatwg.org/multipage/#attr-track-src
    # A URL potentially surrounded by spaces.
    src: str
    # https://html.spec.whatwg.org/multipage/#attr-track-srclang
    # A valid BCP 47 language tag.
    srclang: str


def track(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_TrackAttrs]
) -> Element[_TrackAttrs]:
    return Element("track", list(children), attrs=attrs, selfclosing=True)


class _UAttrs(GlobalAttrs, total=False): ...


def u(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_UAttrs]
) -> Element[_UAttrs]:
    return Element("u", list(children), attrs=attrs)


class _UlAttrs(GlobalAttrs, total=False): ...


def ul(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_UlAttrs]
) -> Element[_UlAttrs]:
    return Element("ul", list(children), attrs=attrs)


class _VarAttrs(GlobalAttrs, total=False): ...


def var(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_VarAttrs]
) -> Element[_VarAttrs]:
    return Element("var", list(children), attrs=attrs)


class _VideoAttrs(GlobalAttrs, total=False):
    # https://html.spec.whatwg.org/multipage/#attr-media-autoplay
    autoplay: bool
    # https://html.spec.whatwg.org/multipage/#attr-media-controls
    controls: bool
    # https://html.spec.whatwg.org/multipage/#attr-media-crossorigin
    crossorigin: Literal["anonymous", "use-credentials"]
    # https://html.spec.whatwg.org/multipage/#attr-dim-height
    height: int
    # https://html.spec.whatwg.org/multipage/#attr-media-loop
    loop: bool
    # https://html.spec.whatwg.org/multipage/#attr-media-muted
    muted: bool
    # https://html.spec.whatwg.org/multipage/#attr-video-playsinline
    playsinline: bool
    # https://html.spec.whatwg.org/multipage/#attr-video-poster
    # A URL potentially surrounded by spaces.
    poster: str
    # https://html.spec.whatwg.org/multipage/#attr-media-preload
    preload: Literal["none", "metadata", "auto"]
    # https://html.spec.whatwg.org/multipage/#attr-media-src
    # A URL potentially surrounded by spaces.
    src: str
    # https://html.spec.whatwg.org/multipage/#attr-dim-width
    width: int


def video(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_VideoAttrs]
) -> Element[_VideoAttrs]:
    return Element("video", list(children), attrs=attrs)


class _WbrAttrs(GlobalAttrs, total=False): ...


def wbr(
    *children: Element[GlobalAttrs] | str, **attrs: Unpack[_WbrAttrs]
) -> Element[_WbrAttrs]:
    return Element("wbr", list(children), attrs=attrs, selfclosing=True)
