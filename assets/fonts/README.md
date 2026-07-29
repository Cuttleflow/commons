# Self-hosted fonts

**Done — the files are here.** Seven woff2 files, no external font requests anywhere
on the estate, no dependency on conference wifi or a corporate proxy.

    spectral-400.woff2     body serif, pull-quotes
    spectral-400i.woff2    italic
    spectral-600.woff2     display headings (.disp)
    inter-400.woff2        body sans
    inter-600.woff2        semibold sans
    plexmono-400.woff2     eyebrows, labels, meta
    plexmono-500.woff2     emphasis in mono

The `@font-face` block near the top of `assets/meridian.css` loads them with
relative paths (`url('fonts/…')`), so the same stylesheet works from the web root,
from a subfolder, and from a local file.

Three copies of this folder exist, one per deployed site: `site/assets/fonts/`,
`holding/assets/fonts/` and `commons/assets/fonts/`. Keep them identical.

## Optional: preload the two faces above the fold

Not done, deliberately — it would mean the same two `<link>` tags in 37 pages, and
`font-display:swap` already prevents invisible text. If you want the extra ~100ms on
first paint, add to `<head>` after the stylesheet link:

    <link rel="preload" href="/assets/fonts/spectral-600.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="/assets/fonts/inter-400.woff2" as="font" type="font/woff2" crossorigin>

Note the leading slash: those paths only resolve when served over HTTP, not when
opening a file locally.

## Licences

Spectral, Inter and IBM Plex Mono are all under the SIL Open Font License 1.1.
Self-hosting and redistribution are permitted. Keep an `OFL.txt` alongside these
files if you redistribute the repository publicly.
