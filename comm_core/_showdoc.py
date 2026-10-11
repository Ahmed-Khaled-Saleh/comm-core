"""The docs' `show_doc` renderer (`renderer` in `[tool.nbdev]`); hand-written, not exported from a notebook.

nbdev's renderer prints every signature as `def Name(...)`, classes included; this one prints `class Name(...)` for classes.
"""
import inspect, re

from nbdev.showdoc import BasicMarkdownRenderer


class ShowDocRenderer(BasicMarkdownRenderer):
    "nbdev's markdown renderer, with `class` instead of `def` in the signature of a class."

    def _repr_markdown_(self):
        md = super()._repr_markdown_()
        if inspect.isclass(self.sym):
            md = re.sub(r'(```python\s*)def ', r'\1class ', md, count=1)
        return md
