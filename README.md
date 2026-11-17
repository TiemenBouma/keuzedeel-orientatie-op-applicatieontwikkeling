# Webdevelopment – Keuzedeel Oriëntatie op applicatieontwikkeling

Lesmateriaal voor mbo niveau 2: zes modules over HTML, CSS en JavaScript.
De site staat op GitHub Pages:
https://tiemenbouma.github.io/keuzedeel-orientatie-op-applicatieontwikkeling/

## Inhoud aanpassen

De tekst van de site staat in de map `bron`, één bestand per module (`module-1.md` t/m `module-6.md`).
De HTML-pagina's in de mappen `module-1` t/m `module-6` worden daaruit gemaakt. Pas die dus niet met de hand aan.

1. Pas het bestand in `bron` aan.
2. Bouw de site opnieuw (eenmalig eerst `pip install markdown pymdown-extensions`):

   ```
   python bron/build.py
   ```

3. Commit en push. GitHub Pages zet de nieuwe versie vanzelf online.

## Zo werkt een modulebestand

- Bovenaan staan de gegevens van de module (`nr`, `titel`, `kort`, `tags`).
- Een nieuwe pagina begint met een regel als `=== blok-2 | display: flex`.
- Kaders: `!!! tip "Titel"`, `!!! onthoud`, `!!! let-op`, `!!! klaar`, `!!! opdracht`.
- Uitklapvelden: `??? check "Titel"`, `??? antwoord`, `??? hint`.
- Een echt voorbeeld dat in de pagina getekend wordt: een codeblok met ```` ```demo titel="..." ````.
