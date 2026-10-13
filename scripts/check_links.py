"""Check links, images, and local assets in a generated Jekyll site."""

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.anchors = set()
        self.canonical = None
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and "canonical" in attrs.get("rel", "").split():
            self.canonical = attrs.get("href")
        if "id" in attrs:
            self.anchors.add(attrs["id"])
        if tag == "a" and "name" in attrs:
            self.anchors.add(attrs["name"])
        for attr in ("href", "src"):
            if attrs.get(attr):
                self.links.append((attrs[attr], self.getpos()[0]))


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    files = sorted(root.rglob("*.html"))
    if not files:
        sys.exit(f"No HTML files found in {root}")
    pages = {path: Page(path) for path in files}
    home = pages.get(root / "index.html")
    if home is None:
        sys.exit("Missing index.html")
    # Jekyll's canonical URL identifies absolute links back to this site.
    canonical = urlsplit(home.canonical or "https://localhost/")
    origin = f"{canonical.scheme}://{canonical.netloc}"
    errors = []
    for path, page in pages.items():
        relative = path.relative_to(root).as_posix()
        page_url = "/" + relative
        if page_url.endswith("index.html"):
            page_url = page_url[:-len("index.html")]
        for link, line in page.links:
            parsed = urlsplit(urljoin(origin + page_url, link))
            if parsed.scheme not in ("http", "https") or parsed.netloc != canonical.netloc:
                continue
            target = (root / unquote(parsed.path).lstrip("/")).resolve()
            if not target.is_relative_to(root):
                errors.append(f"{relative}:{line}: path escapes site: {link}")
                continue
            if target.is_dir():
                target /= "index.html"
            elif not target.is_file() and not target.suffix:
                target = target.with_suffix(".html")
            if not target.is_file():
                errors.append(f"{relative}:{line}: missing target: {link}")
            elif parsed.fragment and target in pages:
                if unquote(parsed.fragment) not in pages[target].anchors:
                    errors.append(f"{relative}:{line}: missing anchor: {link}")
    if errors:
        sys.exit("\n".join(errors))
    print(f"Checked internal links and assets in {len(pages)} HTML pages.")


if __name__ == "__main__":
    main()
