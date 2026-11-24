---
nr: 4
titel: Layout met flexbox
kort: Kaarten in een rij, je naam links en je menu rechts, en op een telefoon alles onder elkaar.
tags: display: flex | gap | justify-content | @media
---

=== start | Start
## Dit ga je maken

Aan het eind van deze module staan onderdelen van je site naast elkaar, en werkt hij ook op een telefoon.

| Wat zie je? | Hoe doe je dat? |
|---|---|
| Je naam links, je menu rechts | `display: flex` en `justify-content` |
| Kaarten naast elkaar | `display: flex` en `gap` |
| Een foto naast je tekst | `align-items: center` |
| Onder elkaar op je telefoon | een media query |

```demo titel="Zo kan je site eruitzien"
<style>
header{display:flex;justify-content:space-between;align-items:center;background:#1B1F3B;color:#fff;padding:10px 16px;border-radius:8px}
header h1{margin:0;font-size:18px}
nav{display:flex;gap:6px}
nav a{color:#fff;text-decoration:none;padding:4px 10px;border-radius:6px;font-size:14px}
nav a.actief{background:#E44D26}
.kaarten{display:flex;gap:12px;margin:14px 0}
.kaart{flex:1;background:#E8EAF6;border-radius:8px;padding:10px}
.kaart h2{font-size:15px;margin:0 0 4px}.kaart p{margin:0;font-size:13px}
.profiel{display:flex;align-items:center;gap:14px}
.foto{width:90px;height:70px;background:#c5cae9;border-radius:8px;display:grid;place-items:center;font-size:12px}
footer{display:flex;justify-content:space-between;margin-top:14px;font-size:13px;color:#5b6075}
</style>
<header><h1>Sam Jansen</h1><nav><a class="actief">Home</a><a>Hobby's</a><a>Contact</a></nav></header>
<div class="kaarten"><div class="kaart"><h2>Gamen</h2><p>Elke vrijdag</p></div><div class="kaart"><h2>Fietsen</h2><p>Rondje Utrecht</p></div><div class="kaart"><h2>School</h2><p>ICT niveau 2</p></div></div>
<div class="profiel"><div class="foto">foto</div><p>Ik ben Sam. Ik woon in Utrecht en fiets elke dag naar school.</p></div>
<footer><span>sam@mail.nl</span><span>Utrecht</span><span>© 2026 Sam Jansen</span></footer>
```

## Dit kun je al

Alles in deze module bouwt verder op wat je al gemaakt hebt.

- **HTML:** een `div` of `section` als doos, met een class zoals `.kaart`. Nesten: een doos in een doos.
- **CSS:** een palet, een Google Font, schaduw, `:hover` en `transition`. `main` in het midden met `max-width`.
- **Site:** drie pagina's (index, hobbys en contact) met één style.css, een menubalk en een map images.

!!! tip "Iets kwijt?"
    De naslag van module 1 t/m 3 mag je er de hele tijd bij houden.

## Zo werk je

In opdracht 1 maak je in Documenten de map `module4-jouwnaam`, met daarin de mappen `opdracht-1` tot en met `opdracht-8` en `eindopdracht`. In `opdracht-1` zet je een kopie van je eindopdracht van module 3. Bij elke volgende opdracht kopieer je alle bestanden en mappen uit de vorige opdrachtmap naar de volgende. In je HTML verander je weinig: een div om je kaarten, twee extra alinea's in je footer en een div om je foto en tekst. De rest doe je in style.css.

Elk blok werkt hetzelfde: eerst de **uitleg**, dan een **check** om te kijken of je het snapt, en daarna een **mini-opdracht** die je meteen in VS Code maakt.

| Blok | Onderwerp |
|---|---|
| 1 | Opfrissen: block en inline, de flex-knoppen in Chrome |
| 2 | display: flex |
| 3 | gap en richting |
| 4 | justify-content |
| 5 | align-items |
| 6 | Kaarten in een rij |
| 7 | Header en menu |
| 8 | Op je telefoon |

=== blok-1 | Opfrissen
## Je nieuwe gereedschap: de flex-knoppen

Chrome laat je precies zien wat flexbox doet.
{: .sub}

1. **Open je pagina.** Met Live Server. Druk daarna op F12.
2. **Zoek het label flex.** In Elements staat een label `flex` achter elk element met `display: flex`.
3. **Klik op flex.** Op je pagina zie je paarse lijnen om elk item en de ruimte ertussen.
4. **Klik op het icoontje.** Bij Styles staat naast `display: flex` een klein icoontje met blokjes.
5. **Probeer de knoppen.** Je ziet knoppen voor `justify-content` en `align-items`. Klik en kijk wat er gebeurt.

Zo ziet het stukje Elements eruit:

```html
<main>
  <div class="kaarten">   flex
    <div class="kaart">
    <div class="kaart">
  </div>
</main>
```

!!! tip "Wat heb je eraan?"
    Je ziet de ruimte die flexbox verdeelt. Zonder die lijnen is dat lastig te zien.

!!! let-op "Zie je geen label flex?"
    Nu zie je dit label nog nergens, want je gebruikt `display: flex` pas vanaf blok 2. Kijk er in opdracht 2 opnieuw naar.

## Waar waren we gebleven?

Je site van module 3 is het startpunt.
{: .sub}

1. **Mooie opmaak.** Een palet, een Google Font, een foto achter je header en schaduw op je kaarten.
2. **main in het midden.** Met `max-width` en `margin: 0 auto` staat je inhoud netjes in het midden.
3. **Alles staat onder elkaar.** Je kaarten staan nog onder elkaar. In deze module zet je ze naast elkaar.

```css
main {
  max-width: 800px;
  margin: 0 auto;
}
.kaart {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transition: all 0.3s;
}
```

## Block en inline

Waarom staan sommige dingen onder elkaar, en andere naast elkaar?
{: .sub}

1. **block** neemt de hele breedte. Het volgende element begint op een nieuwe regel. Bijvoorbeeld `div`, `p`, `h1` en `section`.
2. **inline** is zo breed als de inhoud en staat naast andere inline-elementen. Bijvoorbeeld `a`, `img` en `span`.
3. **display** verandert dat. In module 2 zette `display: inline-block` je menu naast elkaar.

```demo titel="block: onder elkaar · inline: naast elkaar"
<style>.b{background:#E8EAF6;padding:6px 10px;margin:4px 0;border-radius:6px}.i{background:#ffe0d6;padding:4px 8px;border-radius:6px}</style>
<div class="b">div</div><div class="b">p</div><div class="b">section</div>
<p><span class="i">a</span> <span class="i">img</span> <span class="i">span</span></p>
```

!!! tip "Kijk het zelf na"
    Klik in de DevTools op een element. Typ bij Computed in het zoekvak (Filter) het woord display. Dan zie je of het block of inline is.

??? check "Check: block en inline"
    **1. Je hebt drie div's met een kaart erin. Hoe staan ze op je pagina?**

    - A. Naast elkaar
    - B. Onder elkaar
    - C. Over elkaar heen
    - D. Schuin

    **2. Welk element is inline?**

    - A. div
    - B. p
    - C. a
    - D. section

    ??? antwoord "Bekijk de antwoorden"
        **1. B – onder elkaar.** Een div is een block: hij pakt de hele breedte, dus de volgende begint op een nieuwe regel. Naast elkaar kan wel, maar daar heb je CSS voor nodig.

        **2. C – a.** Een link staat midden in een zin, dus is hij inline. div, p en section zijn blokken die de hele breedte pakken.

!!! opdracht "1. Zet je werkmap klaar en kijk rond"
    Ongeveer 10 minuten · Je werkt in: `opdracht-1`
    {: .meta}

    1. Maak in Documenten een map `module4-jouwnaam`. Maak daarin de mappen `opdracht-1` tot en met `opdracht-8` en de map `eindopdracht`.
    2. Kopieer alle bestanden en mappen uit de map `eindopdracht` van module 3 naar `opdracht-1`.
    3. Open `module4-jouwnaam` in VS Code en start Live Server op index.html.
    4. Druk op F12 en klik met het pijltje op een kaart. Typ bij Computed in het zoekvak (Filter) het woord display en kijk wat er staat.
    5. Doe hetzelfde bij een link in je menu en bij je foto.
    6. Schrijf bovenaan in style.css tussen `/*` en `*/` een opmerking met drie voorbeelden van block-elementen en drie voorbeelden van inline-elementen.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        /* block: div, ...
           inline: ... */
        ```

    !!! klaar "Klaar als..."
        Je site van module 3 werkt in `opdracht-1`. Bovenin style.css staat een opmerking met minstens drie blokken en drie inline-elementen.

=== blok-2 | display: flex
## Dingen naast elkaar met flexbox

Met één regel CSS zet je blokken naast elkaar.
{: .sub}

1. **Een doos om je blokken.** Zet een div om de elementen die naast elkaar moeten staan. Die div heet de container.
2. **display: flex op de container.** Niet op de kaarten zelf, maar op de doos eromheen.
3. **De kinderen worden items.** Alles wat direct in de container staat, heet een kind van de container. In flexbox noem je die kinderen items. Ze schuiven naast elkaar. De container zelf is de ouder.

```html
<div class="kaarten">
  <div class="kaart">Gamen</div>
  <div class="kaart">Fietsen</div>
</div>
```

```css
.kaarten {
  display: flex;
}
```

<div class="naast" markdown>

```demo titel="Zonder flex"
<style>.kaart{background:#E8EAF6;padding:8px 12px;border-radius:6px;margin:4px;font-weight:bold}</style>
<div class="kaarten"><div class="kaart">Gamen</div><div class="kaart">Fietsen</div></div>
```

```demo titel="Met display: flex"
<style>.kaarten{display:flex}.kaart{background:#E8EAF6;padding:8px 12px;border-radius:6px;margin:4px;font-weight:bold}</style>
<div class="kaarten"><div class="kaart">Gamen</div><div class="kaart">Fietsen</div></div>
```

</div>

!!! onthoud "Onthoud: flex zet je op de ouder"
    De doos met `display: flex` is de container. Wat erin staat, zijn de items.

## Alleen de kinderen doen mee

Flexbox werkt op de items die direct in de container staan.
{: .sub}

1. **Direct erin = item.** De kaarten staan direct in `.kaarten`. Zij zijn de items en staan naast elkaar.
2. **Wat dieper staat, verandert niet.** De h2 en de p in een kaart zijn geen items. Die staan nog gewoon onder elkaar.
3. **Vanzelf even hoog.** Items worden even hoog als het hoogste item. Handig voor kaarten met veel en weinig tekst.

```demo titel=".kaarten is de container, de kaarten zijn de items. De h2 en p in een kaart doen niet mee."
<style>.kaarten{display:flex;gap:10px;border:2px dashed #2965F1;padding:8px;border-radius:8px}.kaart{flex:1;background:#E8EAF6;border:2px solid #E44D26;padding:8px;border-radius:6px}h2{font-size:15px;margin:0 0 4px}p{margin:0;font-size:13px}</style>
<div class="kaarten"><div class="kaart"><h2>Gamen</h2><p>Elke vrijdag met vrienden online.</p></div><div class="kaart"><h2>Fietsen</h2><p>Kort.</p></div></div>
```

!!! tip "Zie je het label flex?"
    In Elements staat nu `flex` achter je container. Klik erop: je ziet paarse lijnen om elk item.

??? check "Check: display: flex"
    **1. Waar zet je display: flex?**

    - A. Op elke kaart
    - B. Op de doos om de kaarten
    - C. In de head
    - D. Op de footer

    **2. In een kaart staan een h2 en een p. De doos om de kaarten heeft display: flex. Hoe staan de h2 en de p?**

    - A. Naast elkaar
    - B. Onder elkaar
    - C. Ze verdwijnen
    - D. Over elkaar

    ??? antwoord "Bekijk de antwoorden"
        **1. B – op de doos om de kaarten.** Flex zet je op de ouder, de container. Die zet zijn kinderen naast elkaar. Zet je het op een kaart, dan komt de inhoud van díe kaart naast elkaar.

        **2. B – onder elkaar.** Alleen de kaarten zijn items. De h2 en de p staan een laag dieper, dus daar verandert niets.

!!! opdracht "2. Zet je kaarten naast elkaar"
    Ongeveer 15 minuten · Je werkt in: `opdracht-2`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit `opdracht-1` naar `opdracht-2`.
    2. Zet in index.html een div met class `kaarten` om je kaarten heen.
    3. Doe hetzelfde op hobbys.html en contact.html.
    4. Geef `.kaarten` in style.css `display: flex`.
    5. Sla op en kijk: staan je kaarten naast elkaar?
    6. Klik in de DevTools op het label flex achter je div.

    ??? hint "Codehint (niet het antwoord)"
        ```html
        <footer class="rij">
          <p>...</p>
          <p>...</p>
        </footer>
        ```
        ```css
        .rij {
          display: ...;
        }
        ```

    !!! klaar "Klaar als..."
        Op alle drie je pagina's staan je kaarten naast elkaar. Ze plakken nog tegen elkaar aan. Dat los je op in opdracht 3.

=== blok-3 | gap en richting
## Ruimte ertussen met gap

`gap` zet ruimte tussen de items, niet aan de buitenkant.
{: .sub}

1. **gap op de container.** Net als `display: flex` zet je `gap` op de doos eromheen.
2. **Alleen tussen de items.** Aan de randen komt geen extra ruimte. Dat is het verschil met margin.
3. **Eén getal is genoeg.** `gap: 20px` zet 20 pixels tussen elk item.

```css
.kaarten {
  display: flex;
  gap: 20px;
}
```

<div class="naast" markdown>

```demo titel="Zonder gap"
<style>.k{display:flex;border:2px dashed #b8bddc}.k div{flex:1;background:#E8EAF6;border:1px solid #b8bddc;padding:10px;text-align:center}</style>
<div class="k"><div>kaart</div><div>kaart</div><div>kaart</div></div>
```

```demo titel="Met gap: 20px"
<style>.k{display:flex;gap:20px;border:2px dashed #b8bddc}.k div{flex:1;background:#E8EAF6;border:1px solid #b8bddc;padding:10px;text-align:center}</style>
<div class="k"><div>kaart</div><div>kaart</div><div>kaart</div></div>
```

</div>

!!! tip "Waarom geen margin?"
    Met margin krijgen ook de eerste en de laatste kaart ruimte aan de buitenkant. Met gap komt de ruimte alleen tussen de kaarten. Je hoeft niets weg te halen bij de eerste of de laatste kaart.

## Rij of kolom: flex-direction

Je bepaalt zelf of de items naast of onder elkaar staan.
{: .sub}

1. **row is de standaard.** Zonder `flex-direction` staan de items naast elkaar, van links naar rechts.
2. **column zet ze onder elkaar.** Handig op een telefoon. Daar kom je in blok 8 op terug.
3. **De hoofdrichting.** Bij row loopt de hoofdrichting van links naar rechts. Bij column van boven naar beneden.

```css
.kaarten {
  display: flex;
  flex-direction: column;
}
```

<div class="naast" markdown>

```demo titel="flex-direction: row"
<style>.k{display:flex;gap:8px}.k div{background:#E8EAF6;padding:8px 14px;border-radius:6px;font-weight:bold}</style>
<div class="k"><div>1</div><div>2</div><div>3</div></div>
```

```demo titel="flex-direction: column"
<style>.k{display:flex;flex-direction:column;gap:8px}.k div{background:#E8EAF6;padding:8px 14px;border-radius:6px;font-weight:bold}</style>
<div class="k"><div>1</div><div>2</div><div>3</div></div>
```

</div>

!!! tip "Waarom dan flex met column?"
    Met `column` ziet het er hetzelfde uit als zonder flex. Maar met flex kun je ook `gap` gebruiken en de items uitlijnen.

??? check "Check: gap en richting"
    **1. Wat doet gap: 20px op een flex-container?**

    - A. 20px om de container
    - B. 20px tussen de items
    - C. Items 20px breed
    - D. Tekst 20px groot

    **2. Welke regel zet de items onder elkaar?**

    - A. `flex-direction: row;`
    - B. `flex-direction: column;`
    - C. `display: column;`
    - D. `direction: down;`

    ??? antwoord "Bekijk de antwoorden"
        **1. B – 20px tussen de items.** gap werkt alleen tussen de items. Ruimte om de hele container geef je met margin of padding.

        **2. B – flex-direction: column;** row is naast elkaar, en dat is de standaard. `display: column` en `direction: down` bestaan niet. De DevTools laten dan een geel driehoekje zien.

!!! opdracht "3. Geef je kaarten ruimte"
    Ongeveer 10 minuten · Je werkt in: `opdracht-3`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit `opdracht-2` naar `opdracht-3`.
    2. Geef `.kaarten` een gap van 20px.
    3. Zet in je footer nog twee alinea's, zoals je stad en © 2026 jouw naam. Doe dit op alle drie je pagina's.
    4. Zet de drie onderdelen in je footer (je mailadres en de twee nieuwe alinea's) met flexbox naast elkaar, met een gap.
    5. Zet in de DevTools `flex-direction: column` op `.kaarten`. Wat gebeurt er?
    6. Haal die regel in de DevTools weer weg.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        .rij {
          display: flex;
          gap: 40px;
        }
        ```

    !!! klaar "Klaar als..."
        Tussen je kaarten zit ruimte. De drie onderdelen in je footer staan naast elkaar.

=== blok-4 | justify-content
## Items verdelen met justify-content

Met justify-content bepaal je waar de lege ruimte in de rij komt.
{: .sub}

1. **flex-start:** alles links. Dit is de standaard.
2. **center:** alles in het midden.
3. **flex-end:** alles rechts.
4. **space-between:** eerste links, laatste rechts, de rest gelijk verdeeld ertussen.

```demo titel="Dezelfde drie items met vier waarden van justify-content"
<style>.r{display:flex;gap:6px;background:#f6f7fc;border:1px dashed #b8bddc;border-radius:6px;padding:6px;margin-bottom:8px}.r div{background:#2965F1;color:#fff;width:34px;text-align:center;border-radius:4px;padding:3px 0}small{display:block;font-family:Consolas,monospace;font-size:12px;color:#5b6075;margin-bottom:2px}</style>
<small>flex-start</small><div class="r" style="justify-content:flex-start"><div>1</div><div>2</div><div>3</div></div>
<small>center</small><div class="r" style="justify-content:center"><div>1</div><div>2</div><div>3</div></div>
<small>flex-end</small><div class="r" style="justify-content:flex-end"><div>1</div><div>2</div><div>3</div></div>
<small>space-between</small><div class="r" style="justify-content:space-between"><div>1</div><div>2</div><div>3</div></div>
```

!!! tip "Alleen als er ruimte over is"
    Vullen je items de hele rij al, dan valt er niets te verdelen. Dan zie je geen verschil.

## justify-content in je site

Twee waarden die je vaak ziet.
{: .sub}

1. **space-between.** Het eerste item helemaal links, het laatste helemaal rechts. Goed voor een naam links en een menu rechts.
2. **center.** Alles in het midden. Bijvoorbeeld een rij knoppen of één kaart.
3. **Op de container.** Ook `justify-content` zet je op de doos met `display: flex`.

```css
footer {
  display: flex;
  justify-content: space-between;
}
```

```demo titel="Zo ziet je footer eruit"
<style>footer{display:flex;justify-content:space-between;background:#1B1F3B;color:#fff;padding:10px 14px;border-radius:6px;font-size:14px}</style>
<footer><span>sam@mail.nl</span><span>Utrecht</span><span>© 2026 Sam Jansen</span></footer>
```

!!! tip "Probeer het met de flex-knop"
    Klik bij Styles op het icoontje naast `display: flex`. Klik op de knoppen bij justify-content en kijk wat er gebeurt.

??? check "Check: justify-content"
    **1. Je wilt je naam links en je menu rechts. Welke waarde kies je?**

    - A. center
    - B. flex-start
    - C. space-between
    - D. flex-end

    **2. Waar zet je justify-content?**

    - A. Op de container
    - B. Op elk item
    - C. In de HTML
    - D. Bij :hover

    ??? antwoord "Bekijk de antwoorden"
        **1. C – space-between.** De lege ruimte komt tussen de items. Het eerste gaat helemaal naar links, het laatste helemaal naar rechts. Bij flex-start staan ze allebei links, bij flex-end allebei rechts.

        **2. A – op de container.** Alles wat de rij regelt, zet je op de container: `display: flex`, `gap` en `justify-content`.

!!! opdracht "4. Verdeel de ruimte"
    Ongeveer 10 minuten · Je werkt in: `opdracht-4`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit `opdracht-3` naar `opdracht-4`.
    2. Probeer in de DevTools met de flex-knop alle waarden van justify-content op je footer.
    3. Kies de waarde die de drie onderdelen van je footer over de hele breedte verdeelt. Typ die over in style.css.
    4. Zet de kaarten in `.kaarten` in het midden van de rij.
    5. Kijk op contact.html: je ene kaart staat nu in het midden.
    6. Kijk op index.html: verandert er iets aan je kaarten? Waarom niet?

    ??? hint "Codehint (niet het antwoord)"
        ```css
        .knoppen {
          display: flex;
          justify-content: ...;
        }
        ```

    !!! klaar "Klaar als..."
        De drie onderdelen in je footer zijn verdeeld over de hele breedte. De kaart op je contactpagina staat in het midden.

=== blok-5 | align-items
## Uitlijnen met align-items

Bij een rij verdeelt `justify-content` de items van links naar rechts. `align-items` zet ze van boven naar beneden goed.
{: .sub}

1. **stretch:** even hoog. De standaard. Alle items rekken uit tot het hoogste.
2. **flex-start:** bovenaan. Elk item houdt zijn eigen hoogte en staat bovenaan.
3. **center:** in het midden. Elk item staat in het midden van de hoogte.
4. **flex-end:** onderaan. Elk item staat onderaan de rij.

```demo titel="Drie items van verschillende hoogte"
<style>.w{display:flex;gap:10px}.w>div{flex:1}.r{display:flex;gap:4px;height:80px;background:#f6f7fc;border:1px dashed #b8bddc;border-radius:6px;padding:4px}.r div{background:#2965F1;color:#fff;flex:1;text-align:center;border-radius:4px}.a{height:30px}.b{height:50px}.c{height:20px}small{display:block;font-family:Consolas,monospace;font-size:12px;color:#5b6075;margin-bottom:2px}</style>
<div class="w"><div><small>stretch</small><div class="r" style="align-items:stretch"><div>1</div><div>2</div><div>3</div></div></div>
<div><small>flex-start</small><div class="r" style="align-items:flex-start"><div class="a">1</div><div class="b">2</div><div class="c">3</div></div></div>
<div><small>center</small><div class="r" style="align-items:center"><div class="a">1</div><div class="b">2</div><div class="c">3</div></div></div>
<div><small>flex-end</small><div class="r" style="align-items:flex-end"><div class="a">1</div><div class="b">2</div><div class="c">3</div></div></div></div>
```

!!! onthoud "Twee richtingen"
    `justify-content` werkt in de hoofdrichting: bij row van links naar rechts. `align-items` werkt in de andere richting: bij row van boven naar beneden.

## Een foto naast tekst

Het bekendste voorbeeld van `align-items: center`.
{: .sub}

1. **Een div om foto en tekst.** De div wordt de container. De img en de p zijn de items.
2. **align-items: center.** De tekst staat netjes in het midden naast de foto, niet bovenaan.
3. **Maak de foto kleiner.** Met `max-width: 40%` pakt de foto niet de hele rij.

```html
<div class="profiel">
  <img src="images/sam.jpg" alt="Sam op de fiets">
  <p>Ik ben Sam ...</p>
</div>
```

```css
.profiel {
  display: flex;
  align-items: center;
  gap: 20px;
}
.profiel img {
  max-width: 40%;
}
```

```demo titel="Een foto links met de tekst in het midden van de hoogte ernaast"
<style>.profiel{display:flex;align-items:center;gap:20px}.foto{width:40%;height:110px;background:#c5cae9;border-radius:8px;display:grid;place-items:center;color:#5b6075}</style>
<div class="profiel"><div class="foto">foto</div><p>Ik ben Sam. Ik woon in Utrecht en fiets elke dag naar school.</p></div>
```

!!! tip "Waarom zijn je kaarten even hoog?"
    Zonder `align-items` is de waarde `stretch`. Daarom zijn je kaarten sinds opdracht 2 even hoog.

??? check "Check: align-items"
    **1. Kaarten in een rij zijn even hoog, ook met weinig tekst. Hoe komt dat?**

    - A. Door gap
    - B. Door stretch
    - C. Door justify-content
    - D. Door max-width

    **2. Tekst moet in de hoogte in het midden naast een foto staan. Wat gebruik je?**

    - A. `justify-content: center;`
    - B. `text-align: center;`
    - C. `align-items: center;`
    - D. `margin: 0 auto;`

    ??? antwoord "Bekijk de antwoorden"
        **1. B – door stretch.** `align-items: stretch` is de standaard. De items rekken uit tot het hoogste item. gap en justify-content gaan over de ruimte in de rij, niet over de hoogte.

        **2. C – align-items: center;** align-items werkt in de hoogte. `justify-content: center` zet de items in het midden van links naar rechts, en `text-align` zet alleen de tekst in het midden.

!!! opdracht "5. Zet een foto naast je tekst"
    Ongeveer 15 minuten · Je werkt in: `opdracht-5`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit `opdracht-4` naar `opdracht-5`.
    2. Zet op index.html een div met een eigen class om je foto en een nieuwe alinea over jezelf.
    3. Geef die div `display: flex` en een gap.
    4. Zet de tekst in de hoogte in het midden naast de foto.
    5. Maak de foto in die div kleiner met `max-width: 40%`.
    6. Zet in de DevTools `align-items: flex-start` op `.kaarten`. Wat zie je? Haal het daarna weer weg.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        .rij {
          display: flex;
          align-items: ...;
        }
        .rij img {
          max-width: ...;
        }
        ```

    !!! klaar "Klaar als..."
        Op je homepagina staat je foto met de tekst in het midden ernaast. En je weet waarom je kaarten even hoog zijn.

=== blok-6 | Kaarten in een rij
## Te veel kaarten voor één rij

Met `flex-wrap` schuiven items door naar de volgende regel.
{: .sub}

1. **Standaard: alles op één regel.** Flexbox propt alle items in één rij. Bij veel kaarten worden ze heel smal.
2. **flex-wrap: wrap.** Past het niet meer, dan gaat het volgende item naar een nieuwe regel.
3. **gap werkt ook tussen de regels.** De ruimte tussen de rijen is net zo groot als tussen de kaarten.

```css
.kaarten {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
```

<div class="naast" markdown>

```demo titel="Zonder wrap: te smal"
<style>.k{display:flex;gap:8px}.k div{background:#E8EAF6;padding:10px 0;min-width:0;flex:1;text-align:center;border-radius:6px;font-weight:bold}</style>
<div class="k"><div>1</div><div>2</div><div>3</div><div>4</div><div>5</div></div>
```

```demo titel="Met wrap: door naar de volgende regel"
<style>.k{display:flex;flex-wrap:wrap;gap:8px}.k div{background:#E8EAF6;padding:10px 0;width:28%;text-align:center;border-radius:6px;font-weight:bold}</style>
<div class="k"><div>1</div><div>2</div><div>3</div><div>4</div><div>5</div></div>
```

</div>

!!! tip "Maak je venster smaller"
    Pas bij een smal venster zie je wrap aan het werk. Sleep je Chrome-venster smaller en kijk hoe de kaarten doorschuiven.

## Even breed met flex: 1

Laat de items de ruimte eerlijk verdelen.
{: .sub}

1. **flex: 1 op de items.** Nu op de kaart zelf, niet op de container. Elke kaart krijgt een even groot deel van de rij.
2. **min-width als grens.** Met `min-width: 200px` wordt een kaart nooit smaller. Past het niet, dan schuift hij door.
3. **flex: 2 is dubbel.** Een item met `flex: 2` wordt twee keer zo breed als een item met `flex: 1`.

```css
.kaart {
  flex: 1;
  min-width: 200px;
}
```

```demo titel="Boven: alle drie flex: 1. Onder: de eerste flex: 2"
<style>.r{display:flex;gap:8px;margin-bottom:8px}.r div{background:#E8EAF6;padding:8px;text-align:center;border-radius:6px;font-family:Consolas,monospace;font-size:13px}</style>
<div class="r"><div style="flex:1">flex: 1</div><div style="flex:1">flex: 1</div><div style="flex:1">flex: 1</div></div>
<div class="r"><div style="flex:2;background:#ffe0d6">flex: 2</div><div style="flex:1">flex: 1</div><div style="flex:1">flex: 1</div></div>
```

!!! onthoud "Container of item?"
    `display`, `gap`, `justify-content`, `align-items` en `flex-wrap` zet je op de container. `flex` en `min-width` zet je op het item.

??? check "Check: kaarten in een rij"
    **1. Wat doet flex-wrap: wrap?**

    - A. Items even breed
    - B. Naar een nieuwe regel
    - C. Een rand om de items
    - D. Tekst afbreken

    **2. Drie kaarten hebben flex: 1. Hoe breed worden ze?**

    - A. Allemaal even breed
    - B. 1 pixel breed
    - C. De eerste het breedst
    - D. Zo breed als het scherm

    ??? antwoord "Bekijk de antwoorden"
        **1. B – naar een nieuwe regel.** wrap betekent: laat het doorlopen. Items die niet meer passen, gaan naar de volgende regel. Even breed maken doe je met `flex: 1`, een rand met `border`.

        **2. A – allemaal even breed.** `flex: 1` betekent: neem een even groot deel van de ruimte. Het is geen maat in pixels.

!!! opdracht "6. Laat je kaarten meeschuiven"
    Ongeveer 15 minuten · Je werkt in: `opdracht-6`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit `opdracht-5` naar `opdracht-6`.
    2. Maak main breder: een max-width van 1000px.
    3. Laat de kaarten in `.kaarten` doorschuiven naar een nieuwe regel.
    4. Geef `.kaart` `flex: 1` en een min-width.
    5. Rijen te ver uit elkaar? Haal margin-top en margin-bottom weg bij `.kaart`. Geef `.kaarten` `margin: 20px 0`.
    6. Maak je Chrome-venster smaller en kijk op hobbys.html hoe de kaarten doorschuiven.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        .foto {
          flex: 1;
          min-width: 150px;
        }
        ```

    !!! klaar "Klaar als..."
        Op hobbys.html staan je kaarten naast elkaar en zijn ze even breed. Maak je het venster smaller, dan schuiven ze netjes door.

=== blok-7 | Header en menu
## Je menu met flexbox

In module 2 gebruikte je `inline-block`. Met flex gaat het makkelijker.
{: .sub}

1. **display: flex op de ul.** De ul is de container, de li's zijn de items. Ze komen vanzelf naast elkaar.
2. **gap in plaats van margin.** Geen `margin-right` meer op elke li, maar één `gap` op de ul.
3. **Haal de oude regels weg.** `display: inline-block` en `margin-right` bij `nav li` heb je niet meer nodig.

Zo was het (module 2). Deze regels mogen weg:
{: .bestandsnaam}

```css
nav li {
  display: inline-block;
  margin-right: 15px;
}
```

Zo wordt het:
{: .bestandsnaam}

```css
nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  gap: 10px;
}
```

!!! tip "margin: 0 op de ul"
    Een ul heeft uit zichzelf ruimte boven en onder. Met `margin: 0` staat je menu netjes in de balk.

## Naam links, menu rechts

Het bekendste patroon van het web: een header met flex.
{: .sub}

1. **De header is de container.** De h1 en de nav zijn de items.
2. **space-between.** Je naam gaat naar links, je menu naar rechts.
3. **align-items: center.** Naam en menu staan even hoog, in het midden van de balk.

```css
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

```demo titel="Zo ziet je header eruit"
<style>header{display:flex;justify-content:space-between;align-items:center;background:#1B1F3B;color:#fff;padding:12px 16px;border-radius:8px}h1{margin:0;font-size:20px}ul{list-style:none;padding:0;margin:0;display:flex;gap:10px}a{color:#fff;text-decoration:none;padding:4px 10px;border-radius:6px}a.actief{background:#E44D26}</style>
<header><h1>Sam Jansen</h1><nav><ul><li><a class="actief" href="#">Home</a></li><li><a href="#">Hobby's</a></li><li><a href="#">Contact</a></li></ul></nav></header>
```

!!! tip "text-align: center mag weg"
    Stond je header in het midden met `text-align: center`? Flex regelt nu waar alles staat. Geef je h1 ook `margin: 0`.

??? check "Check: header en menu"
    **1. Je li's staan met flex naast elkaar. Welke regel mag weg?**

    - A. `display: flex` bij nav ul
    - B. `display: inline-block` bij nav li
    - C. `list-style: none`
    - D. `color` bij nav a

    **2. Header met display: flex. Naam en menu staan niet even hoog. Wat helpt?**

    - A. `align-items: center;`
    - B. `justify-content: center;`
    - C. `text-align: center;`
    - D. `flex-wrap: wrap;`

    ??? antwoord "Bekijk de antwoorden"
        **1. B – display: inline-block bij nav li.** Flex zet de li's al naast elkaar. `list-style: none` heb je nog wel nodig, anders komen de bolletjes terug.

        **2. A – align-items: center;** In een rij werkt align-items in de hoogte. `justify-content: center` zou je naam en je menu allebei naar het midden schuiven.

!!! opdracht "7. Bouw je header met flex"
    Ongeveer 15 minuten · Je werkt in: `opdracht-7`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit `opdracht-6` naar `opdracht-7`.
    2. Zet je menu met flexbox naast elkaar, met een gap.
    3. Haal de oude regels bij `nav li` weg.
    4. Zet in je header je naam links en je menu rechts.
    5. Zet je naam en je menu in de hoogte netjes in het midden.
    6. Haal `text-align: center` en overbodige margins weg als dat nodig is.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        footer {
          display: flex;
          justify-content: ...;
          align-items: ...;
        }
        ```

    !!! klaar "Klaar als..."
        Op alle drie je pagina's staat je naam links en je menu rechts, op dezelfde hoogte. Bij `nav li` staat geen inline-block meer.

=== blok-8 | Op je telefoon
## Je site op een telefoon

Drie kaarten naast elkaar passen niet op een smal scherm.
{: .sub}

1. **Een smal scherm.** Een telefoon is zo'n 400px breed. Drie kaarten naast elkaar worden dan heel smal.
2. **Test met Ctrl + Shift + M.** In de DevTools kies je bovenin een telefoon, zoals iPhone SE.
3. **De viewport-regel.** In je head staat `<meta name="viewport" ...>`. Die kwam er met ! + Tab. Zonder die regel doet een telefoon alsof hij een groot scherm is.

<div class="naast" markdown>

```demo titel="Laptop: past"
<style>.k{display:flex;gap:8px}.k div{flex:1;background:#E8EAF6;padding:14px 6px;text-align:center;border-radius:6px}</style>
<div class="k"><div>kaart</div><div>kaart</div><div>kaart</div></div>
```

```demo titel="Telefoon: te smal"
<style>.t{width:150px;margin:0 auto;border:3px solid #1B1F3B;border-radius:14px;padding:8px}.k{display:flex;gap:4px}.k div{flex:1;background:#E8EAF6;padding:14px 0;text-align:center;border-radius:4px;font-size:10px;overflow:hidden}</style>
<div class="t"><div class="k"><div>kaart</div><div>kaart</div><div>kaart</div></div></div>
```

</div>

!!! tip "Eerst kijken, dan aanpassen"
    Open al je pagina's in de telefoonweergave. Schrijf op wat te smal is of uitsteekt.

## Andere CSS voor een smal scherm

Met een media query geef je regels die alleen op een smal scherm gelden.
{: .sub}

1. **@media (max-width: 600px).** Alles tussen de accolades geldt alleen als het scherm 600px of smaller is.
2. **Twee paar accolades.** Eén paar voor de media query. Daarbinnen staan je gewone regels, met hun eigen accolades.
3. **Onderaan je style.css.** Zet de media query helemaal onderaan. Dan wint hij van de regels erboven.

```css
@media (max-width: 600px) {
  .kaarten {
    flex-direction: column;
  }
}
```

<div class="naast" markdown>

```demo titel="Breder dan 600px"
<style>.k{display:flex;gap:8px}.k div{flex:1;background:#E8EAF6;padding:10px;text-align:center;border-radius:6px}</style>
<div class="k"><div>kaart</div><div>kaart</div><div>kaart</div></div>
```

```demo titel="600px of smaller"
<style>.k{display:flex;flex-direction:column;gap:6px;width:150px;margin:0 auto}.k div{background:#E8EAF6;padding:8px;text-align:center;border-radius:6px}</style>
<div class="k"><div>kaart</div><div>kaart</div><div>kaart</div></div>
```

</div>

!!! let-op "Tel je accolades"
    Mist er een `}`, dan werkt alles eronder niet meer. Sla op, dan springt Prettier je code in. Staat de laatste `}` niet helemaal links? Dan mist er ergens een `}`.

??? check "Check: op je telefoon"
    **1. Wanneer geldt de CSS in @media (max-width: 600px)?**

    - A. Altijd
    - B. Scherm 600px of smaller
    - C. Scherm breder dan 600px
    - D. Alleen bij printen

    **2. Waar zet je je media query in style.css?**

    - A. Helemaal bovenaan
    - B. In de head
    - C. Helemaal onderaan
    - D. In een apart bestand

    ??? antwoord "Bekijk de antwoorden"
        **1. B – als het scherm 600px of smaller is.** max-width betekent: tot en met deze breedte. Op een laptop geldt de regel dus niet.

        **2. C – helemaal onderaan.** Zeggen twee regels iets anders over hetzelfde element, dan wint de onderste. Staat je media query bovenaan, dan wint de gewone regel eronder.

!!! opdracht "8. Maak je site geschikt voor een telefoon"
    Ongeveer 15 minuten · Je werkt in: `opdracht-8`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit `opdracht-7` naar `opdracht-8`.
    2. Druk in de DevTools op Ctrl + Shift + M en kies bovenin een telefoon.
    3. Zet onderaan style.css een media query voor schermen tot 600px.
    4. Zet daarin je kaarten onder elkaar.
    5. Doe hetzelfde voor je header, je foto met tekst en je footer.
    6. Is je foto nu te klein? Maak hem in de media query weer breder.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        @media (max-width: 600px) {
          nav ul {
            flex-direction: ...;
          }
        }
        ```

    !!! klaar "Klaar als..."
        Op een laptop staan je kaarten naast elkaar. In de telefoonweergave staat alles onder elkaar en steekt er niets uit.

=== eindopdracht | Eindopdracht
!!! opdracht eind "Zet je site in de rij"
    Je werkt in je map `eindopdracht`. Kopieer eerst alle bestanden en mappen uit `opdracht-8` naar `eindopdracht`.
    {: .meta}

    **Op je site staat:**

    - Map `eindopdracht` met je drie pagina's, style.css en de map images
    - Een header met je naam links en je menu rechts, op dezelfde hoogte
    - Een menu met `display: flex` en `gap`, zonder inline-block
    - Kaarten naast elkaar met ruimte ertussen, op al je pagina's
    - Minstens vier hobbykaarten, even breed, die naar een nieuwe regel schuiven als het venster smaller wordt
    - Op je homepagina een foto met tekst ernaast, met de tekst in de hoogte in het midden naast de foto
    - Een footer met minstens drie onderdelen, zoals je mailadres, je stad en © met je naam, verdeeld over de breedte
    - Een media query: tot 600px staat alles onder elkaar
    {: .checklist}

    !!! tip "Al klaar?"
        Geef één kaart `flex: 2`, zodat hij twee keer zo breed wordt. Of zet op je contactpagina twee kaarten naast elkaar.

Alles wat je nodig hebt, heb je in de mini-opdrachten al een keer gemaakt. Kijk gerust terug in je eigen mappen.

## Inleveren

Zip de hele map `module4-jouwnaam`. Daarin zitten `opdracht-1` tot en met `opdracht-8` en de map `eindopdracht`. Noem de zip `module4-jouwnaam.zip`.

**Checklist: vink af voordat je inlevert**

- Map `module4-jouwnaam` met `opdracht-1` tot en met `opdracht-8`
- Map `eindopdracht` met drie html-bestanden en style.css
- Een div om je kaarten op elke pagina
- De media query helemaal onderaan style.css
- Geen gele driehoekjes meer in de DevTools
- Alle map- en bestandsnamen met kleine letters
- Alles opgeslagen met Ctrl + S
- Elke pagina getest in de telefoonweergave
{: .checklist}

!!! tip "Zo maak je een zip"
    Rechtsklik op de map `module4-jouwnaam` en kies **Comprimeren naar > ZIP-bestand**. Op oudere Windows: **Kopiëren naar > Gecomprimeerde map**.

!!! tip "Werk je thuis?"
    Je hebt VS Code en Chrome nodig. De telefoonweergave zit in Chrome zelf, je hebt geen echte telefoon nodig. Kom je er niet uit? Schrijf je vraag op en neem hem mee.

Twijfel je of iets af is? Kijk bij **Klaar als...** bij die opdracht.

=== werkt-het-niet | Werkt het niet?
Met de DevTools en het label flex vind je de fout meestal binnen een minuut.
{: .sub}

1. **Heb je alles opgeslagen?** Een witte stip op een tabblad in VS Code betekent: nog niet opgeslagen.
2. **Staat display: flex op de goede plek?** Op de container, de ouder. Niet op de items zelf.
3. **Staan je items direct in de container?** Alleen wat er direct in staat, doet mee. Kijk in Elements hoe je HTML genest is.
4. **justify-content doet niets?** Er is geen ruimte over. De items vullen de rij al.
5. **Media query werkt niet?** Staat hij onderaan? Kloppen alle accolades? Staat de viewport-regel in je head?

!!! tip "Nog steeds niet?"
    Vraag eerst een klasgenoot, daarna je docent. Laat de DevTools openstaan en klik op het label flex, dan zoeken jullie samen.

=== naslag | Naslag
## flexbox

Alles van blok 1 t/m 6 bij elkaar. Kijk hier eerst als je iets kwijt bent.
{: .sub}

Op de container
{: .bestandsnaam}

```css
.kaarten {
  display: flex;
  flex-direction: row;
  gap: 20px;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
}
```

Op de items
{: .bestandsnaam}

```css
.kaart {
  flex: 1;
  min-width: 200px;
}

.breed {
  flex: 2;
}
```

!!! onthoud "Container en items"
    De container is de doos met `display: flex`. Alleen wat er direct in staat, zijn items.

!!! tip "De waarden op een rij"
    **justify-content:** flex-start, center, flex-end, space-between.<br>
    **align-items:** stretch, flex-start, center, flex-end.

## Header, menu en telefoon

Alles van blok 7 en 8, en de DevTools.
{: .sub}

Header en menu
{: .bestandsnaam}

```css
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
nav ul {
  display: flex;
  gap: 10px;
  margin: 0;
}
```

Media query
{: .bestandsnaam}

```css
@media (max-width: 600px) {
  header,
  .kaarten {
    flex-direction: column;
  }
}
```

!!! tip "DevTools"
    F12 opent ze. Klik op het label flex voor de paarse lijnen. Het icoontje naast `display: flex` opent de flex-knoppen. Ctrl + Shift + M toont een telefoon.

!!! onthoud "Onthoud"
    Flex zet je op de ouder. De media query staat helemaal onderaan je style.css.

=== woordenlijst | Woordenlijst
De Engelse woorden van module 4, met de Nederlandse vertaling en uitleg in gewone taal. De woorden van module 1 t/m 3 staan in de woordenlijst van die modules.
{: .sub}

| Engels | Nederlands | Uitleg |
|---|---|---|
| **layout** | indeling | hoe de blokken op je pagina staan |
| **block** | blok | pakt de hele breedte, begint op een nieuwe regel |
| **inline** | in de regel | zo breed als de inhoud, staat naast andere |
| **display** | weergave | block, inline of flex |
| **flexbox** (flexible box) | flexibele doos | items in een rij of kolom zetten |
| **container** | houder | de doos met display: flex |
| **item** | onderdeel | wat direct in de container staat |
| **gap** | tussenruimte | ruimte tussen de items |
| **direction** | richting | row of column |
| **row** | rij | naast elkaar |
| **column** | kolom | onder elkaar |
| **justify** | uitvullen | verdelen in de hoofdrichting |
| **align-items** | items uitlijnen | uitlijnen in de andere richting |
| **start / end** | begin / eind | links of rechts, boven of onder |
| **stretch** | uitrekken | items even hoog maken |
| **space-between** | ruimte ertussen | eerste links, laatste rechts |
| **wrap** | laten doorlopen | naar een nieuwe regel |
| **min-width** | minimale breedte | nooit smaller dan dit |
| **media query** | schermvraag | CSS die alleen bij een bepaalde breedte geldt |
| **viewport** | zichtbaar venster | het stuk scherm waarin je pagina staat |
