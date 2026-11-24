---
nr: 3
titel: Meer CSS
kort: Je mini-site gaat eruitzien als een echte website: lettertypes, kleuren, achtergronden en beweging.
tags: Google Fonts | gradient | box-shadow | :hover
---

=== start | Start
## Dit ga je maken

Aan het eind van deze module ziet je mini-site eruit als een echte website.

| Wat zie je? | Hoe doe je dat? |
|---|---|
| Een eigen lettertype van Google | een link en `font-family` |
| Een foto achter je naam | `background-image` |
| Kaarten die zweven | `box-shadow` en `:hover` |
| Alles netjes in het midden | `max-width` en `margin` |

```demo titel="Zo kan je site eruitzien. Ga met je muis over een kaart."
<style>body{background:#E8EAF6;padding:0;font-family:Verdana,sans-serif}header{background:linear-gradient(rgba(0,0,0,.5),rgba(0,0,0,.5)),linear-gradient(135deg,#5b7bd5,#e48a5a);color:#fff;padding:28px 16px;text-align:center}h1{margin:0;font-family:Georgia,serif;text-shadow:1px 1px 3px #000}header p{margin:4px 0 0;font-size:14px}nav{background:linear-gradient(to right,#2965F1,#1B1F3B);padding:6px 10px}nav a{color:#fff;text-decoration:none;padding:6px 12px;font-size:14px}nav a.actief{background:#E44D26}main{max-width:420px;margin:0 auto;padding:12px}.kaart{background:#fff;padding:12px 14px;border-radius:8px;margin-bottom:10px;box-shadow:0 4px 12px rgba(0,0,0,.15);transition:all .3s}.kaart:hover{transform:translateY(-4px);box-shadow:0 8px 20px rgba(0,0,0,.25)}.kaart h2{margin:0 0 2px;font-size:16px}.kaart p{margin:0;font-size:13px}</style>
<header><h1>Sam Jansen</h1><p>Student ICT in Utrecht</p></header>
<nav><a class="actief" href="#">Home</a><a href="#">Hobby's</a><a href="#">Contact</a></nav>
<main><div class="kaart"><h2>Mijn hobby's</h2><p>Gamen en fietsen</p></div><div class="kaart"><h2>Over mij</h2><p>Ik woon in Utrecht</p></div></main>
```

## Dit kun je al

- **HTML:** header, nav, main, footer en section. Een div als doos, en nesten met inspringen.
- **CSS:** een tag, een `.class` en een `#id`. Een spatie betekent binnen: `nav a` pakt alleen je menulinks.
- **Site:** drie pagina's met één style.css, een menubalk en paden naar je map images.

!!! tip "Iets kwijt?"
    De naslag van module 1 en 2 mag je er de hele tijd bij houden. Blok 1 herhaalt kort wat je in module 1 en 2 hebt geleerd, en je leert één nieuw stuk gereedschap: de DevTools.

## Zo werk je

In opdracht 1 maak je in Documenten de map `module3-jouwnaam`, met daarin de mappen `opdracht-1` tot en met `opdracht-8` en `eindopdracht`. In `opdracht-1` zet je een kopie van je eindopdracht van module 2. Bij elke volgende opdracht kopieer je alle bestanden en mappen uit de vorige opdrachtmap naar de volgende. In deze module verandert vooral je style.css.

| Blok | Onderwerp |
|---|---|
| 1 | Opfrissen en de DevTools |
| 2 | Lettertypes |
| 3 | Google Fonts |
| 4 | Kleuren |
| 5 | Achtergrondfoto |
| 6 | Verloop en schaduw |
| 7 | Breedte en centreren |
| 8 | Hover en overgang |

=== blok-1 | Opfrissen
## Je nieuwe gereedschap: de DevTools

In Chrome zit een venster waarmee je in de CSS van elke pagina kunt kijken.
{: .sub}

1. **Open je pagina.** Met Live Server. Chrome opent vanzelf.
2. **Druk op F12.** Of rechtsklik op je pagina en kies Inspecteren.
3. **Tabblad Elements.** Links zie je je HTML, rechts je CSS.
4. **Klik op het pijltje.** Sneltoets: Ctrl + Shift + C. Klik daarna op iets op je pagina.
5. **Kijk rechts bij Styles.** Daar staat de CSS van het element dat je aanklikte.

Zo ziet het stukje Styles eruit:

```css
element.style {
}
.kaart {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
}
```

!!! tip "Wat heb je eraan?"
    Je ziet precies welke CSS de browser gebruikt, en uit welke regel die komt.

!!! let-op "Gebeurt er niets bij F12?"
    Op veel laptops moet je Fn ingedrukt houden: Fn + F12.

## Waar waren we gebleven?

Je mini-site van module 2 is het startpunt.
{: .sub}

1. **Drie pagina's, één style.css.** index.html, hobbys.html en contact.html gebruiken allemaal dezelfde opmaak.
2. **Een nav op elke pagina.** Een ul met links, naast elkaar gezet met `display: inline-block`.
3. **Tag, punt of hekje.** `nav` is een tag, `.kaart` een class en `#contact` een id. Een spatie betekent binnen.

```css
nav a {
  color: white;
  text-decoration: none;
}
.kaart {
  background-color: white;
  padding: 20px;
}
#contact {
  padding: 30px;
}
```

## Wat vertellen de DevTools je?

Vier dingen die je in deze module steeds tegenkomt.
{: .sub}

| Wat zie je? | Wat betekent het? |
|---|---|
| **Streep erdoor** | Een andere regel wint. Er is nog een CSS-regel voor dezelfde eigenschap. De browser gebruikt die andere regel en slaat deze over. |
| **Geel driehoekje** | Een typefout. Deze eigenschap of waarde bestaat niet, bijvoorbeeld `colr` in plaats van `color`. |
| **Vinkje** | Hiermee zet je een regel tijdelijk uit en weer aan. Haal het vinkje voor een regel weg en kijk wat er verandert. Zet het daarna weer aan. |
| **Console: 404** | De browser kan een bestand (bijvoorbeeld een foto) niet vinden. Het staat niet op de plek die in je code staat. De Console is een tabblad bovenin de DevTools. |

!!! let-op "Let op: niets wordt opgeslagen"
    Wat je in de DevTools verandert, is weg zodra je de pagina ververst. Werkt het? Typ het dan over in je style.css en sla op met Ctrl + S.

??? check "Check: opfrissen en DevTools"
    **1. Hoe open je de DevTools in Chrome?**

    - A. F5
    - B. Ctrl + P
    - C. Ctrl + S
    - D. F12

    **2. In Styles staat een regel met een streep erdoor. Wat betekent dat?**

    - A. Er zit een typefout in
    - B. Een andere regel wint
    - C. De regel is opgeslagen
    - D. Het bestand is kwijt

    ??? antwoord "Bekijk de antwoorden"
        **1. D – F12.** Je kunt ook rechtsklikken op je pagina en Inspecteren kiezen. F5 ververst alleen de pagina.

        **2. B – een andere regel wint.** De browser gebruikt voor die eigenschap een andere regel. Een typefout herken je juist aan het gele driehoekje.

!!! opdracht "1. Zet je werkmap klaar en kijk rond"
    Ongeveer 10 minuten · Je werkt in: `opdracht-1`
    {: .meta}

    1. Maak in Documenten een map `module3-jouwnaam`. Maak daarin de mappen `opdracht-1` tot en met `opdracht-8` en de map `eindopdracht`.
    2. Kopieer alle bestanden en mappen uit de map `eindopdracht` van module 2 naar `opdracht-1`.
    3. Open `module3-jouwnaam` in VS Code en start Live Server op index.html.
    4. Druk op F12, klik op het pijltje en klik daarna op een kaart.
    5. Verander bij Styles de achtergrondkleur van `.kaart`.
    6. Typ die nieuwe kleur over in style.css en sla op met Ctrl + S.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        .kaart {
          background-color: #FFF3E0;
        }
        ```

    !!! klaar "Klaar als..."
        Je kaarten hebben een nieuwe kleur, en die kleur blijft staan als je de pagina ververst met F5.

=== blok-2 | Lettertypes
## Een lettertype kiezen

Met `font-family` bepaal je welk lettertype de browser gebruikt.
{: .sub}

```demo titel="Vier lettertypes die op elke Windows-laptop staan"
<style>.r{display:flex;gap:10px;flex-wrap:wrap}.r div{flex:1;min-width:130px;background:#f6f7fc;border-radius:8px;padding:10px}.n{font-size:20px;margin-bottom:4px}small{color:#5b6075;font-family:Arial;font-size:12px}</style>
<div class="r">
<div><div class="n" style="font-family:Arial">Sam Jansen</div><small><b>Arial</b> · zonder schreef. Strak en rustig.</small></div>
<div><div class="n" style="font-family:Verdana">Sam Jansen</div><small><b>Verdana</b> · extra breed. Makkelijk te lezen.</small></div>
<div><div class="n" style="font-family:Georgia">Sam Jansen</div><small><b>Georgia</b> · met schreef. Voelt als een boek.</small></div>
<div><div class="n" style="font-family:'Courier New'">Sam Jansen</div><small><b>Courier New</b> · allemaal even breed, zoals code.</small></div>
</div>
```

!!! onthoud "Zet er altijd een reserve achter"
    `font-family: Verdana, sans-serif;` De komma betekent: lukt het eerste lettertype niet, gebruik dan het volgende. Heeft een computer Verdana niet, dan pakt de browser een ander lettertype zonder schreef (zonder de kleine voetjes onderaan de letters).

## Dikte, schuin en regelafstand

Drie eigenschappen die je tekst beter leesbaar maken.
{: .sub}

1. **font-weight.** Hoe dik de letters zijn. `bold` is dik, `normal` is gewoon.
2. **font-style.** `italic` maakt je tekst schuin. `normal` zet het weer recht.
3. **line-height.** De ruimte tussen de regels. Hier schrijf je een getal zonder px. `1.5` betekent: elke regel is anderhalf keer zo hoog als de letters.

```css
body {
  font-family: Verdana, sans-serif;
  line-height: 1.5;
}
h2 {
  font-weight: bold;
}
footer p {
  font-style: italic;
}
```

<div class="naast" markdown>

```demo titel="line-height: 1"
<p style="line-height:1;margin:0">Ik ben Sam. Ik woon in Utrecht en fiets elke dag naar school. In het weekend game ik met vrienden.</p>
```

```demo titel="line-height: 1.5"
<p style="line-height:1.5;margin:0">Ik ben Sam. Ik woon in Utrecht en fiets elke dag naar school. In het weekend game ik met vrienden.</p>
```

</div>

!!! tip "Probeer het in de DevTools"
    Klik op een alinea en verander line-height van 1 naar 2. Zie je de regels uit elkaar schuiven?

??? check "Check: lettertypes"
    **1. Wat betekent de komma in `font-family: Verdana, sans-serif;`?**

    - A. Verdana, en anders sans-serif
    - B. Gebruik ze allebei tegelijk
    - C. Verdana wordt schuin
    - D. Het is een typefout

    **2. Welke eigenschap zet meer ruimte tussen de regels?**

    - A. font-size
    - B. font-weight
    - C. line-height
    - D. padding

    ??? antwoord "Bekijk de antwoorden"
        **1. A – Verdana, en anders sans-serif.** De browser probeert eerst het eerste lettertype. Heeft de computer dat niet, dan pakt hij het volgende uit het rijtje.

        **2. C – line-height.** font-size maakt de letters zelf groter. padding maakt ruimte binnen de rand van een element, niet tussen de regels.

!!! opdracht "2. Geef je site een eigen lettertype"
    Ongeveer 10 minuten · Je werkt in: `opdracht-2`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit `opdracht-1` naar `opdracht-2`.
    2. Geef body een font-family en een reserve font-family.
    3. Kies een ander lettertype voor je h1.
    4. Geef body een line-height van 1.5.
    5. Maak de tekst in je footer schuin met font-style.
    6. Druk op F12 en klik met het pijltje op een alinea. Kijk rechts bij het tabblad Computed. Helemaal onderaan, bij **Rendered Fonts**, staat welk lettertype de browser echt gebruikt.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        body {
          font-family: Verdana, sans-serif;
          line-height: 1.5;
        }
        h1 {
          font-family: Georgia, serif;
        }
        ```

    !!! klaar "Klaar als..."
        Je kop heeft een ander lettertype dan je gewone tekst, je regels staan wat verder uit elkaar en je footer is schuin gedrukt.

=== blok-3 | Google Fonts
## Lettertypes van internet

Op Google Fonts kies je uit honderden gratis lettertypes.
{: .sub}

1. **Ga naar fonts.google.com.** Typ het adres in Chrome.
2. **Klik op een lettertype.** Bijvoorbeeld Poppins of Roboto.
3. **Klik op Get font.** De knop staat rechtsboven.
4. **Klik op Get embed code.** Je ziet nu stukjes code.
5. **Kopieer de link-regels.** Onder het kopje Web staan drie regels. Kopieer ze alle drie.

Dat plak je in de head:

```html
<head>
  <title>Sam Jansen</title>
  <link rel="preconnect" ...>
  <link rel="preconnect" ...>
  <link href="https://fonts..." rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
```

!!! tip "Waarom boven style.css?"
    Dan kent de browser het lettertype al als hij je CSS gaat lezen.

!!! onthoud "Kies er hooguit twee"
    Eén voor koppen, één voor tekst. Meer maakt je site onrustig en traag.

## Het lettertype gebruiken

Na het koppelen gebruik je de naam gewoon in je CSS.
{: .sub}

1. **Google geeft je een voorbeeld.** Onder de link-regels staat een stukje CSS met font-family. Dat mag je overnemen.
2. **Spatie in de naam? Aanhalingstekens.** `"Open Sans"` schrijf je tussen aanhalingstekens. Een naam van één woord mag zonder.
3. **Op elke pagina koppelen.** De link-regels van Google horen in de head van al je drie pagina's.

```css
body {
  font-family: "Open Sans", sans-serif;
}
h1 {
  font-family: Poppins, sans-serif;
}
```

!!! let-op "Verandert er niets?"
    Kijk of de naam precies zo gespeld is als op Google Fonts, met precies dezelfde hoofdletters. Zonder internet laadt het lettertype niet.

??? check "Check: Google Fonts"
    **1. Waar plak je de link-regels van Google Fonts?**

    - A. In style.css
    - B. In de body
    - C. In de head
    - D. In de footer

    **2. Welke regel is het best geschreven?**

    - A. `font-family: "Open Sans", sans-serif;`
    - B. `font-family: Open Sans;`
    - C. `font: "Open Sans";`
    - D. `font-family = "Open Sans";`

    ??? antwoord "Bekijk de antwoorden"
        **1. C – in de head.** Net als de koppeling naar je style.css. Zet ze daarboven, en doe het op elke pagina.

        **2. A – `font-family: "Open Sans", sans-serif;`** Aanhalingstekens om een naam met een spatie, en een reserve erachter voor als het lettertype niet laadt. Bij B mist de reserve, C en D zijn geen goede CSS.

!!! opdracht "3. Haal een lettertype van Google"
    Ongeveer 15 minuten · Je werkt in: `opdracht-3`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit `opdracht-2` naar `opdracht-3`.
    2. Kies op fonts.google.com een lettertype voor je koppen.
    3. Kopieer de link-regels via Get font en Get embed code.
    4. Plak ze in de head van alle drie je pagina's, boven style.css.
    5. Gebruik het lettertype in style.css voor h1 en h2.
    6. Controleer met F12 bij Computed, helemaal onderaan bij **Rendered Fonts**, of het echt gebruikt wordt.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        h1 {
          font-family: Poppins, sans-serif;
        }
        h2 {
          font-family: Poppins, sans-serif;
        }
        ```

    !!! klaar "Klaar als..."
        Je koppen staan in het lettertype van Google, op alle drie je pagina's. Bij Computed in de DevTools zie je de naam van dat lettertype staan.

=== blok-4 | Kleuren
## Kleuren die bij elkaar passen

Een palet is een vast rijtje kleuren voor je hele site. Kies het voordat je begint, en gebruik daarna alleen die kleuren.
{: .sub}

1. **Kies drie of vier kleuren.** Een donkere, een lichte en één opvallende. Meer heb je niet nodig.
2. **Gebruik een palet-site.** Op coolors.co druk je op de spatiebalk voor een nieuw palet. Met het slotje houd je een kleur vast.
3. **Verdeel ze 60 · 30 · 10.** 60% licht voor de achtergrond, 30% donker voor tekst en balken, 10% opvallend voor knoppen.

```demo titel="Voorbeeld van een palet"
<style>.r{display:flex;gap:8px}.r div{flex:1;border-radius:8px;padding:30px 8px 8px;font-size:12px;border:1px solid #b8bddc}b{display:block;font-size:13px}</style>
<div class="r">
<div style="background:#E8EAF6"><b>Licht</b>#E8EAF6<br>achtergrond</div>
<div style="background:#FFFFFF"><b>Wit</b>#FFFFFF<br>kaarten</div>
<div style="background:#1B1F3B;color:#fff"><b>Donker</b>#1B1F3B<br>tekst en balken</div>
<div style="background:#E44D26;color:#fff"><b>Opvallend</b>#E44D26<br>knoppen en actief</div>
</div>
```

!!! tip "Twijfel je?"
    Kijk hoe een site die je vaak gebruikt het doet. Ook daar zie je meestal maar een paar kleuren terugkomen.

## Leesbaar en doorzichtig

Een mooie kleur is pas goed als je de tekst ook kunt lezen.
{: .sub}

```demo titel="Contrast: tekst tegen achtergrond"
<style>.r{display:flex;gap:8px}.r div{flex:1;padding:10px;border-radius:6px;font-weight:bold;text-align:center;border:1px solid #ddd}</style>
<div class="r"><div style="background:#fff;color:#1B1F3B">Goed</div><div style="background:#fff;color:#ddd">Slecht</div><div style="background:#fff;color:#f5e663">Slecht</div><div style="background:#1B1F3B;color:#fff">Goed</div></div>
```

Klik in de DevTools bij Styles op het gekleurde vierkantje naast de tekstkleur (`color`). In het venster dat opent staat Contrast ratio. Staat daar een vinkje, dan is je tekst goed te lezen.

**rgba: een kleur die doorzichtig is**

```css
.kaart {
  background-color: rgba(255, 255, 255, 0.8);
}
```

1. **255, 255, 255** is rood, groen, blauw: elk van 0 tot 255. Dit is wit.
2. **0.8** is hoe dekkend de kleur is. 0 = helemaal doorzichtig (je ziet niets), 1 = helemaal niet doorzichtig.

!!! tip "Waar heb je dit in blok 5 en 6 voor nodig?"
    In blok 5 zet je een foto achter je header. Met rgba leg je er een kaart of een donker laagje overheen, waar de foto nog een beetje doorheen schijnt.

??? check "Check: kleuren"
    **1. Wat doet de 0.5 in `rgba(0, 0, 0, 0.5)`?**

    - A. Maakt de kleur 5x meer doorzichtig
    - B. Maakt de tekst half zo groot
    - C. Maakt de kleur rood
    - D. Maakt de kleur half doorzichtig

    **2. Wat is het best te lezen?**

    - A. Lichtgrijze tekst op wit
    - B. Gele tekst op wit
    - C. Donkerblauwe tekst op wit
    - D. Rode tekst op groen

    ??? antwoord "Bekijk de antwoorden"
        **1. D – de kleur wordt half doorzichtig.** De eerste drie getallen zijn rood, groen en blauw. Het vierde getal is hoe doorzichtig: 0.5 is half.

        **2. C – donkerblauwe tekst op wit.** Donker op licht geeft veel contrast. Lichtgrijs en geel op wit zijn slecht te lezen. Rood en groen kunnen sommige mensen niet goed uit elkaar houden.

!!! opdracht "4. Kies je eigen palet"
    Ongeveer 15 minuten · Je werkt in: `opdracht-4`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit `opdracht-3` naar `opdracht-4`.
    2. Maak op coolors.co een palet en kies drie of vier kleuren.
    3. Schrijf de hexcodes bovenaan in style.css tussen `/*` en `*/`. Zo'n stukje heet een opmerking: de browser slaat het over.
    4. Pas de kleuren van body, header, nav en footer aan je palet aan.
    5. Geef `.actief` en de hover van je menu je opvallende kleur.
    6. Controleer met de DevTools het contrast van je tekst.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        /* mijn palet
           #E8EAF6 licht
           #1B1F3B donker
           #E44D26 opvallend */

        body {
          background-color: #E8EAF6;
        }
        ```

    !!! klaar "Klaar als..."
        Je hele site gebruikt alleen de kleuren uit je palet, en in de DevTools staat een vinkje bij het contrast van je tekst.

=== blok-5 | Achtergrondfoto
## Een foto als achtergrond

Met `background-image` zet je een plaatje achter je tekst.
{: .sub}

1. **background-image: url().** Tussen de haakjes staat het pad naar je foto, tussen aanhalingstekens.
2. **Het pad begint bij style.css.** De browser zoekt vanaf je CSS-bestand. style.css staat naast images, dus: `images/header.jpg`.
3. **Je tekst staat erbovenop.** De foto ligt achter alles wat in het element staat. Je h1 staat er gewoon overheen.

```text
opdracht-5/
   index.html
   style.css
   images/
      header.jpg
```

```css
header {
  background-image: url("images/header.jpg");
}
```

!!! tip "Waarom geen &lt;img&gt;?"
    Een `<img>` is inhoud: een foto die bij je verhaal hoort. Een achtergrond is versiering. Daar zet je tekst overheen, en hij staat in je CSS.

## De foto netjes laten passen

Zonder extra regels herhaalt de foto zich als tegels, of zie je maar een stukje.
{: .sub}

| Regel | Wat doet het? |
|---|---|
| `background-size: cover` | Vult het hele vlak. Geen lege plekken. Past de foto niet precies, dan wordt er een stukje van de rand afgesneden. |
| `background-position: center` | Het midden van de foto blijft altijd zichtbaar. Wordt er iets afgesneden, dan gebeurt dat aan de randen. |
| `background-repeat: no-repeat` | Zonder deze regel herhaalt de browser een foto die kleiner is dan het vlak, als tegels naast en onder elkaar. |
| `background-color` | Kleur als reserve. Laadt de foto niet, dan zie je deze kleur. Kies er een die past. |

```css
header {
  background-image: url("images/header.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-color: #1B1F3B;
}
```

!!! tip "Is je tekst slecht te lezen?"
    Kies een rustige foto en maak je tekst wit. In blok 6 leer je een donker laagje over de foto te leggen.

??? check "Check: achtergrondfoto"
    **1. style.css en de map images staan naast elkaar. Wat is goed?**

    - A. `url("header.jpg")`
    - B. `url("images/header.jpg")`
    - C. `url("../header.jpg")`
    - D. `src("images/header.jpg")`

    **2. Waarmee vult de foto het hele vlak, zonder lege plekken?**

    - A. `background-size: cover;`
    - B. `background-repeat: repeat;`
    - C. `background-color: cover;`
    - D. `width: 100%;`

    ??? antwoord "Bekijk de antwoorden"
        **1. B – `url("images/header.jpg")`.** Het pad begint bij style.css. Vanaf daar ga je de map images in. src gebruik je bij `<img>`, niet in je CSS.

        **2. A – `background-size: cover;`** cover maakt de foto zo groot dat het hele vlak bedekt is. repeat zet hem juist als tegels naast elkaar, en cover is geen kleur.

!!! opdracht "5. Zet een foto achter je header"
    Ongeveer 15 minuten · Je werkt in: `opdracht-5`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit `opdracht-4` naar `opdracht-5`.
    2. Zet een brede foto in images, bijvoorbeeld van unsplash.com. Noem hem header.jpg.
    3. Geef je header een background-image met het pad naar die foto.
    4. Voeg `background-size: cover` en `background-position: center` toe.
    5. Geef je header `padding: 60px 20px`, zodat de foto ruimte krijgt.
    6. Zie je geen foto? Kijk met F12 in de Console naar een rode 404.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        header {
          background-image: url("images/header.jpg");
          background-size: cover;
          background-position: center;
          padding: 60px 20px;
        }
        ```

    !!! klaar "Klaar als..."
        Achter je naam bovenaan staat een foto die het hele vlak vult, op alle drie je pagina's.

=== blok-6 | Verloop en schaduw
## Een kleurverloop

Met `linear-gradient` loopt de ene kleur langzaam over in de andere.
{: .sub}

1. **Een verloop is een plaatje.** Daarom schrijf je het bij `background-image`, niet bij `background-color`.
2. **Eerst de richting, dan de kleuren.** `to right` loopt van links naar rechts. Zonder richting gaat het van boven naar beneden.
3. **Ook voor een donker laagje.** Een verloop kan ook bovenop je foto liggen. Hoe dat werkt, zie je hieronder.

```css
nav {
  background-image: linear-gradient(to right, #2965F1, #1B1F3B);
}
```

```demo titel="linear-gradient(to right, #2965F1, #1B1F3B)"
<div style="height:50px;border-radius:8px;background-image:linear-gradient(to right,#2965F1,#1B1F3B)"></div>
```

## Een donker laagje over je foto

Je foto wordt donkerder, zodat witte tekst er goed op te lezen is.
{: .sub}

1. **Wat is het?** Een doorzichtige zwarte laag over je foto. Net een zonnebril: je ziet de foto nog, maar donkerder.
2. **Waarom een verloop?** `background-color` ligt altijd ónder je foto. Een verloop is een plaatje, en dat mag erbovenop.
3. **Twee keer dezelfde kleur.** Zwart naar hetzelfde zwart: geen verloop, maar één egale laag. 0.5 is half doorzichtig.

```css
header {
  background-image:
    linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("images/header.jpg");
  background-size: cover;
}
```

<div class="naast" markdown>

```demo titel="Zonder laagje"
<div style="padding:26px;color:#fff;text-align:center;font-size:20px;font-weight:bold;background:linear-gradient(135deg,#bcd3f5,#f5d7a8)">Sam Jansen</div>
```

```demo titel="Met donker laagje"
<div style="padding:26px;color:#fff;text-align:center;font-size:20px;font-weight:bold;background:linear-gradient(rgba(0,0,0,.5),rgba(0,0,0,.5)),linear-gradient(135deg,#bcd3f5,#f5d7a8)">Sam Jansen</div>
```

</div>

!!! let-op "Eén background-image, met een komma"
    Zet het laagje vóór je `url()`, in dezelfde regel. Wat je als eerste noemt, ligt bovenop. Typ je een tweede background-image eronder, dan wint die en is je foto weg.

## Schaduw geven

Een schaduw laat je kaart een beetje boven de pagina zweven.
{: .sub}

```css
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
/*          opzij omlaag vaagheid  kleur      */
```

<div class="naast" markdown>

```demo titel="Zonder schaduw"
<style>body{background:#E8EAF6}</style><div style="background:#fff;padding:16px;border-radius:8px">Plakt plat op de pagina</div>
```

```demo titel="Met schaduw"
<style>body{background:#E8EAF6}</style><div style="background:#fff;padding:16px;border-radius:8px;box-shadow:0 4px 12px rgba(0,0,0,.15)">Lijkt los van de pagina</div>
```

</div>

Houd het rustig: een lichte, vage schaduw ziet er netter uit dan een harde zwarte rand.

!!! tip "text-shadow werkt net zo"
    Alleen om de letters, niet om een blok. Handig voor witte tekst op een foto. De vier waarden betekenen hetzelfde als bij box-shadow: opzij, omlaag, hoe vaag en de kleur. `h1 { text-shadow: 1px 1px 3px black; }`

??? check "Check: verloop en schaduw"
    **1. Bij welke eigenschap schrijf je linear-gradient?**

    - A. color
    - B. background-image
    - C. background-color
    - D. border

    **2. Wat doet de 12px in `box-shadow: 0 4px 12px gray;`?**

    - A. Schaduw 12px naar rechts
    - B. Schaduw 12px omlaag
    - C. Hoe dik de rand is
    - D. Hoe vaag de schaduw is

    ??? antwoord "Bekijk de antwoorden"
        **1. B – background-image.** Voor de browser is een verloop een plaatje. Daarom hoort het bij background-image, net als een foto.

        **2. D – hoe vaag de schaduw is.** Het eerste getal is opzij, het tweede omlaag en het derde hoe vaag. Hoe groter dat getal, hoe zachter de schaduw.

!!! opdracht "6. Verloop en schaduw"
    Ongeveer 15 minuten · Je werkt in: `opdracht-6`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit `opdracht-5` naar `opdracht-6`.
    2. Geef je nav een verloop met twee kleuren uit je palet.
    3. Leg een donker laagje over de foto in je header. Hoe? Zie 'Een donker laagje over je foto' hierboven.
    4. Geef je h1 witte tekst en een text-shadow.
    5. Geef `.kaart` een box-shadow.
    6. Verander in de DevTools de getallen van je schaduw tot je hem mooi vindt.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        nav {
          background-image: linear-gradient(to right, #2965F1, #1B1F3B);
        }
        .kaart {
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }
        ```

    !!! klaar "Klaar als..."
        Je menubalk loopt van de ene kleur in de andere, je naam is goed te lezen op de foto, en je kaarten zweven een beetje.

=== blok-7 | Breedte en centreren
## Hoe breed is een blok?

Uit zichzelf is een blok net zo breed als het scherm.
{: .sub}

1. **width.** Een vaste breedte, zoals `width: 300px`. Op een klein scherm past dat soms niet. In deze module gebruik je width niet.
2. **max-width.** Nooit breder dan dit, bijvoorbeeld `max-width: 800px`. Op een klein scherm wordt hij smaller. In deze module gebruik je alleen max-width.
3. **Procenten.** `width: 50%` is de helft van het blok waar hij in staat.

```demo titel="Boven: zo breed als het scherm. Onder: max-width, de rest blijft leeg."
<style>div{background:#E8EAF6;border-radius:6px;padding:8px;margin-bottom:8px;font-size:13px}</style>
<div>Zonder max-width: zo breed als het scherm</div>
<div style="max-width:60%">Met max-width: stopt bij een vaste breedte</div>
```

!!! tip "Lange regels lezen lastig"
    Bij heel lange regels raak je de draad kwijt. Daarom maken sites hun tekst meestal niet breder dan zo'n 800px.

## Een blok in het midden zetten

Met `margin: 0 auto` verdeelt de browser de lege ruimte eerlijk.
{: .sub}

1. **margin: 0 auto.** 0 is boven en onder. auto is links en rechts: de browser verdeelt de lege ruimte gelijk.
2. **Werkt alleen met een breedte.** Zonder max-width is het blok al zo breed als het scherm. Dan valt er niets te verdelen.
3. **Plaatjes die meekrimpen.** img met `max-width: 100%` wordt nooit breder dan het blok waar hij in staat.

```css
main {
  max-width: 800px;
  margin: 0 auto;
}

img {
  max-width: 100%;
}
```

```demo titel="main met max-width en margin: 0 auto"
<style>body{background:#f6f7fc}main{max-width:60%;margin:0 auto;background:#E8EAF6;border-radius:6px;padding:12px;text-align:center}</style>
<main>main staat in het midden</main>
```

!!! onthoud "Niet hetzelfde als text-align"
    `text-align: center` zet de tekst in het midden. `margin: 0 auto` zet het hele blok in het midden.

??? check "Check: breedte en centreren"
    **1. Welke regel zet een blok met max-width in het midden?**

    - A. `margin: 0 auto;`
    - B. `text-align: center;`
    - C. `padding: auto;`
    - D. `align: middle;`

    **2. Wat doet max-width: 800px op een telefoon van 400px breed?**

    - A. Het blok steekt uit het scherm
    - B. De letters worden kleiner
    - C. Het blok verdwijnt
    - D. Het blok wordt smaller

    ??? antwoord "Bekijk de antwoorden"
        **1. A – `margin: 0 auto;`** auto verdeelt de lege ruimte links en rechts gelijk. text-align: center zet alleen de tekst in het midden, niet het blok.

        **2. D – het blok wordt smaller.** max-width is een grens, geen vaste maat. Is het scherm smaller, dan wordt het blok gewoon mee smaller. Met `width: 800px` zou het wel uitsteken.

!!! opdracht "7. Zet je inhoud in het midden"
    Ongeveer 10 minuten · Je werkt in: `opdracht-7`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit `opdracht-6` naar `opdracht-7`.
    2. Geef main een max-width van 800px.
    3. Zet main in het midden met `margin: 0 auto`.
    4. Geef img een max-width van 100%.
    5. Maak je Chrome-venster smaller en kijk wat er gebeurt.
    6. Druk in de DevTools op Ctrl + Shift + M en kies bovenin een telefoon.

    ??? hint "Codehint"
        ```css
        main {
          max-width: 800px;
          margin: 0 auto;
        }

        img {
          max-width: 100%;
        }
        ```

    !!! klaar "Klaar als..."
        Op een breed scherm staan je kaarten netjes in het midden. Op een telefoon steekt er niets uit, ook je foto niet.

=== blok-8 | Hover en overgang
## Reageren op je muis

`:hover` kende je al van je menu. Het werkt op elk element.
{: .sub}

1. **:hover op een kaart.** `.kaart:hover` geldt alleen zolang je muis op de kaart staat.
2. **Geen spatie voor de dubbele punt.** `.kaart:hover` werkt. `.kaart :hover` niet, want een spatie betekent binnen.
3. **transform.** `translateY(-4px)` schuift iets 4 pixels omhoog. `scale(1.05)` maakt het een beetje groter.

```css
.kaart:hover {
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
  transform: translateY(-4px);
}
```

!!! tip "Testen met :hov"
    In de DevTools staat bij Styles een knopje `:hov`. Vink daar hover aan. Dan blijft het element in de hover-stand staan, ook als je je muis weghaalt.

## Rustig veranderen met transition

Zonder transition springt een kleur in één keer om. Met transition glijdt hij.
{: .sub}

1. **Zet transition in de gewone regel.** Dus in `.kaart`, niet in `.kaart:hover`. Dan gaat het heen én terug soepel.
2. **Eerst schrijf je wát er verandert, dan hoe lang het duurt.** `transition: background-color 0.3s;` 0.3s is drie tiende van een seconde.
3. **all voor alles tegelijk.** `transition: all 0.3s;` Handig als er meerdere dingen veranderen.

```css
nav a {
  transition: background-color 0.3s;
}

.kaart {
  transition: all 0.3s;
}
```

<div class="naast" markdown>

```demo titel="Zonder transition: ga met je muis erover"
<style>body{background:#E8EAF6}.kaart{background:#fff;padding:16px;border-radius:8px;box-shadow:0 4px 12px rgba(0,0,0,.15);margin-top:6px}.kaart:hover{transform:translateY(-4px);box-shadow:0 8px 20px rgba(0,0,0,.25)}</style>
<div class="kaart">Springt in één keer</div>
```

```demo titel="Met transition: all 0.3s"
<style>body{background:#E8EAF6}.kaart{background:#fff;padding:16px;border-radius:8px;box-shadow:0 4px 12px rgba(0,0,0,.15);margin-top:6px;transition:all .3s}.kaart:hover{transform:translateY(-4px);box-shadow:0 8px 20px rgba(0,0,0,.25)}</style>
<div class="kaart">Glijdt rustig omhoog</div>
```

</div>

!!! tip "Houd het kort"
    Tussen 0.2s en 0.5s voelt goed. Duurt het langer, dan zit je bezoeker te wachten.

??? check "Check: hover en overgang"
    **1. Waar zet je transition neer?**

    - A. Alleen bij :hover
    - B. In je HTML
    - C. Bij de gewone regel, zoals .kaart
    - D. In de head

    **2. Welke selector is goed geschreven?**

    - A. `.kaart :hover`
    - B. `.kaart:hover`
    - C. `.kaart.hover`
    - D. `kaart:hover`

    ??? antwoord "Bekijk de antwoorden"
        **1. C – bij de gewone regel, zoals .kaart.** Dan werkt de overgang als je muis erop gaat én als je muis weggaat. Staat hij alleen bij :hover, dan springt het terug.

        **2. B – `.kaart:hover`.** Geen spatie, en een dubbele punt. Met een spatie zoekt de browser binnen de kaart. Met een punt zoekt hij een class hover, en zonder punt een tag kaart.

!!! opdracht "8. Laat je site reageren"
    Ongeveer 15 minuten · Je werkt in: `opdracht-8`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit `opdracht-7` naar `opdracht-8`.
    2. Maak een regel `.kaart:hover` met een grotere schaduw.
    3. Laat de kaart bij hover 4px omhoog schuiven met transform.
    4. Geef `.kaart` een `transition: all 0.3s`.
    5. Geef ook `nav a` een transition op background-color.
    6. Test je hover met het knopje `:hov` in de DevTools.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        .kaart {
          transition: all 0.3s;
        }
        .kaart:hover {
          transform: translateY(-4px);
          box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
        }
        ```

    !!! klaar "Klaar als..."
        Gaat je muis over een kaart, dan komt die soepel een stukje omhoog. De knoppen in je menu veranderen rustig van kleur.

=== eindopdracht | Eindopdracht
!!! opdracht eind "Maak je site echt mooi"
    Je werkt in je map `eindopdracht`. Kopieer eerst alle bestanden en mappen uit `opdracht-8` naar `eindopdracht`.
    {: .meta}

    **Op je site staat:**

    - Map `eindopdracht` met je drie pagina's, style.css en de map images
    - Je palet als opmerking bovenin style.css, en je site gebruikt alleen die kleuren
    - Een Google Font, gekoppeld in de head van elke pagina
    - Een font-family met reserve en een line-height voor je tekst
    - Een foto achter je header, met cover en een donker laagje
    - Een verloop op je nav of je footer
    - Kaarten met een schaduw die bij hover soepel omhoog komen
    - main met een max-width, netjes in het midden
    {: .checklist}

    !!! tip "Al klaar?"
        Laat je menuknoppen groter worden met `transform: scale(1.1)`, of geef je foto bij hover ronde hoeken met border-radius.

Alles wat je nodig hebt, heb je in de mini-opdrachten al een keer gemaakt. Kijk gerust terug in je eigen mappen.

## Inleveren

Zip de hele map `module3-jouwnaam`. Daarin zitten `opdracht-1` tot en met `opdracht-8` en de map `eindopdracht`. Noem de zip `module3-jouwnaam.zip`.

**Checklist: vink af voordat je inlevert**

- Map `module3-jouwnaam` met `opdracht-1` tot en met `opdracht-8`
- Map `eindopdracht` met drie html-bestanden en style.css
- De Google Fonts-regels in de head van elke pagina
- Je foto's in de map images
- Geen gele driehoekjes meer in de DevTools
- Alle map- en bestandsnamen met kleine letters
- Alles opgeslagen met Ctrl + S
- Elke pagina opent goed met Live Server
{: .checklist}

!!! tip "Zo maak je een zip"
    Rechtsklik op de map `module3-jouwnaam` en kies **Comprimeren naar > ZIP-bestand**. Op oudere Windows: **Kopiëren naar > Gecomprimeerde map**.

!!! tip "Werk je thuis?"
    Je hebt VS Code, Chrome en internet nodig. Zonder internet laadt je Google Font niet. Kom je er niet uit? Schrijf je vraag op en neem hem mee.

Twijfel je of iets af is? Kijk bij **Klaar als...** bij die opdracht.

=== werkt-het-niet | Werkt het niet?
Met de DevTools vind je de fout meestal binnen een minuut.
{: .sub}

1. **Heb je alles opgeslagen?** Een witte stip op een tabblad in VS Code betekent: nog niet opgeslagen.
2. **Streep erdoor in de DevTools?** Een andere regel wint. Kijk welke regel wel geldt, zonder streep.
3. **Geel driehoekje?** Typefout in de eigenschap of waarde. Controleer letter voor letter.
4. **Google Font doet niets?** Staan de link-regels in de head van déze pagina? Klopt de naam precies?
5. **Achtergrondfoto zie je niet?** Kijk in de Console naar een rode 404. Het pad begint bij style.css.
6. **margin: 0 auto werkt niet?** Heeft het blok een max-width? Zonder breedte valt er niets te verdelen.

!!! tip "Nog steeds niet?"
    Vraag eerst een klasgenoot, daarna je docent. Laat de DevTools openstaan, dan zoeken jullie samen.

=== naslag | Naslag
## Letters, kleur en achtergrond

Alles van blok 1 t/m 5 bij elkaar. Kijk hier eerst als je iets kwijt bent.
{: .sub}

Lettertypes en kleur
{: .bestandsnaam}

```css
font-family: Verdana, sans-serif;
font-family: "Open Sans", sans-serif;
font-weight: bold;
font-style: italic;
line-height: 1.5;

color: #1B1F3B;
background-color: rgba(0, 0, 0, 0.5);
```

Achtergrondfoto
{: .bestandsnaam}

```css
header {
  background-image: url("images/header.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-color: #1B1F3B;
}
```

!!! tip "Google Fonts in het kort"
    fonts.google.com, Get font, Get embed code. Plak de link-regels in de head, boven style.css, op elke pagina.

!!! onthoud "Paden in CSS"
    Een pad in `url()` begint bij style.css, niet bij je HTML-bestand. Rode 404 in de Console? Dan klopt het pad niet.

## Schaduw, breedte en hover

Alles van blok 6 t/m 8, en de sneltoetsen van de DevTools.
{: .sub}

Verloop, schaduw en breedte
{: .bestandsnaam}

```css
background-image: linear-gradient(to right, #2965F1, #1B1F3B);
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
text-shadow: 1px 1px 3px black;

main {
  max-width: 800px;
  margin: 0 auto;
}
img { max-width: 100%; }
```

Hover en overgang
{: .bestandsnaam}

```css
.kaart {
  transition: all 0.3s;
}
.kaart:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
}
```

!!! tip "DevTools"
    F12 opent ze. Ctrl + Shift + C wijst iets aan. Ctrl + Shift + M toont een telefoon. Streep erdoor: andere regel wint. Geel driehoekje: typefout.

!!! onthoud "Onthoud"
    Wat je in de DevTools verandert, is weg na verversen. Typ het over in style.css en sla op met Ctrl + S.

=== woordenlijst | Woordenlijst
De Engelse woorden van module 3, met de Nederlandse vertaling en uitleg in gewone taal. De woorden van module 1 en 2 staan in de woordenlijst van die modules.
{: .sub}

| Engels | Nederlands | Uitleg |
|---|---|---|
| **DevTools** (developer tools) | ontwikkelaarsgereedschap | venster in Chrome, F12 |
| **inspect** | inspecteren | bekijken hoe een pagina gemaakt is |
| **styles** | stijlen | de CSS van een element |
| **computed** | berekend | wat de browser uiteindelijk gebruikt |
| **console** | console | venster met meldingen en fouten |
| **404 not found** | niet gevonden | bestand staat niet waar jij zegt |
| **font-family** | lettertypefamilie | welk lettertype je gebruikt |
| **fallback** | reserve | lettertype als het eerste ontbreekt |
| **serif / sans-serif** | met schreef / zonder schreef | met of zonder voetjes aan de letters |
| **weight** | dikte | font-weight: bold |
| **italic** | cursief, schuin | font-style: italic |
| **line-height** | regelhoogte | ruimte tussen de regels |
| **embed** | insluiten | code om iets van een andere site te gebruiken |
| **palette** | palet | de vaste kleuren van je site |
| **contrast ratio** | contrastverhouding | hoe goed tekst te lezen is op de achtergrond |
| **rgba** (red, green, blue, alpha) | rood, groen, blauw, doorzichtigheid | kleur die doorzichtig kan zijn |
| **background-image** | achtergrondafbeelding | plaatje achter een element |
| **url** (uniform resource locator) | webadres, pad | waar het plaatje staat |
| **cover** | bedekken | foto vult het hele vlak |
| **position** | positie | welk deel van de foto zichtbaar blijft |
| **repeat** | herhalen | foto als tegels naast elkaar |
| **gradient** | verloop | de ene kleur loopt in de andere |
| **linear** | in een rechte lijn | verloop in één richting |
| **blur** | vervaging | hoe vaag een schaduw is |
| **width** | breedte | hoe breed een blok is |
| **max-width** | maximale breedte | nooit breder dan dit |
| **auto** | automatisch | de browser verdeelt de ruimte |
| **center** | midden | in het midden |
| **transform** | vervormen | verschuiven of vergroten |
| **translate** | verschuiven | translateY(-4px) schuift omhoog |
| **scale** | schalen | groter of kleiner maken |
| **transition** | overgang | rustig veranderen in plaats van springen |
