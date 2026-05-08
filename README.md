# Notes

Math notes by Eric Laurence — a [Quarto](https://quarto.org) blog deployed to GitHub Pages.

## Local setup

Install [Quarto](https://quarto.org/docs/get-started/), then:

```bash
pip install -r requirements.txt
quarto preview
```

Quarto caches executed chunks in `_freeze/` (committed to the repo) so unchanged code isn't re-run on every build.

## Writing a post

Create a folder under `posts/`:

```
posts/your-post/
└── index.qmd
```

Front matter:

```yaml
---
title: "Your title"
description: "One-line summary for the listing."
date: "2026-05-07"
categories: [topology, analysis]
---
```

Inline math: `$f(x) = x^2$`. Display math: `$$ ... $$`.

Theorem-style blocks (CSS classes defined in `styles.css`):

````markdown
::: {.theorem}
**Theorem.** ...
:::

::: {.proof}
...
:::
````

Available classes: `theorem`, `proposition`, `lemma`, `corollary`, `definition`, `example`, `remark`, `proof`.

For runnable Python in a post, add `jupyter: python3` to the front matter:

````markdown
```{python}
import numpy as np
...
```
````

For R, the default `knitr` engine handles `{r}` chunks — see Quarto's [R computations docs](https://quarto.org/docs/computations/r.html).

## Deployment

Pushing to `main` triggers `.github/workflows/publish.yml`, which renders the site and pushes the output to the `gh-pages` branch.

**One-time setup:** in **Settings → Pages**, switch the source from `main` to the `gh-pages` branch (root). The workflow creates that branch on its first successful run.
