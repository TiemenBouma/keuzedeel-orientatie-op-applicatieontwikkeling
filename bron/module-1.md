---
nr: 1
titel: HTML & CSS basis
kort: Je bouwt je eerste eigen webpagina: een profielpagina met HTML, opgemaakt met CSS.
tags: h1 | img | class | padding
---

=== start | Start
## Dit ga je maken

Aan het eind van deze module heb je je eigen profielpagina.

| Wat zie je? | Hoe doe je dat? |
|---|---|
| Een kop met je naam | HTML |
| Een lijstje met je hobby's | HTML |
| Kleuren en een nette knop | CSS |
| Netjes uitgelijnd met ruimte | CSS |

```demo titel="Zo kan je profielpagina er aan het eind uitzien"
<style>body{background:#E8EAF6}.kop{background:#2965F1;color:#fff;text-align:center;padding:14px;border-radius:8px;margin:0 0 10px}.knop{display:inline-block;background:#E44D26;color:#fff;text-decoration:none;padding:10px 22px;border-radius:8px;margin-top:6px}h2{font-size:17px;margin:12px 0 4px}</style>
<h1 class="kop">Sam Jansen</h1>
<p>Student ICT in Utrecht.</p>
<h2>Mijn hobby's</h2>
<ul><li>Gamen</li><li>Fietsen</li></ul>
<a class="knop" href="#">Mail mij</a>
```

## Zo werk je

Elk blok werkt hetzelfde: eerst de **uitleg**, dan een **check** om te kijken of je het snapt, en daarna een **mini-opdracht** die je meteen in VS Code maakt.

!!! tip "Er is geen haast"
    We doen er meerdere lessen over. Snap je iets niet? Zeg het meteen. Werk je zelfstandig? Achteraan staan de naslag en een lijstje met veelgemaakte fouten.

| Blok | Onderwerp |
|---|---|
| 1 | Aan de slag: VS Code en Live Server installeren |
| 2 | Tags: h1, h2, p |
| 3 | Het skelet: head en body |
| 4 | Koppen, lijstjes, links en plaatjes |
| 5 | CSS koppelen |
| 6 | Selectors: tagnaam en class |
| 7 | Kleur en tekst |
| 8 | Boxmodel: padding, border en margin |

### Eén map per opdracht

Elke opdracht maak je in een eigen map. Zo kun je altijd terugkijken, en zo lever je het straks in.

```text
les1-jouwnaam/
   opdracht-1/
   opdracht-2/
   ...
   opdracht-8/
   eindopdracht/
```

In elke opdrachtmap staan je bestanden, bijvoorbeeld:

```text
opdracht-4/
   index.html
   style.css
   foto.jpg
```

!!! let-op "De regel"
    Altijd kleine letters. Geen spaties in map- of bestandsnamen.

!!! tip "Tip"
    Elke opdracht: nieuwe map, nieuwe index.html. Je kunt je werk kopiëren uit de vorige map en daarin verder werken. Je oude mappen laat je gewoon staan. Kopiëren doe je met Ctrl + A, Ctrl + C en Ctrl + V.

=== blok-1 | Aan de slag
## Hoe werkt een webpagina?

Drie dingen werken samen om een webpagina op je scherm te krijgen.
{: .sub}

| Wie | Wat doet het? | Voorbeeld |
|---|---|---|
| **HTML** | De structuur: wat staat er op de pagina? | Koppen, tekst, plaatjes |
| **CSS** | De opmaak: hoe ziet het eruit? | Kleuren, ruimte, lettertype |
| **Browser** | Laat het zien: leest jouw code en tekent de pagina | Chrome |

!!! onthoud "Vergelijk het met een huis"
    HTML zijn de muren. CSS is de verf en de inrichting. Zonder CSS staat je huis er wel, maar ziet het er kaal uit.

## Stap 1: VS Code installeren

Dit is het programma waarin je je code typt.
{: .sub}

1. **Ga naar code.visualstudio.com.** Typ dit adres in Chrome. Geen www ervoor nodig.
2. **Klik op de grote blauwe knop.** Je krijgt vanzelf de versie voor Windows.
3. **Open het gedownloade bestand.** Klik onderin of rechtsboven in je browser op het bestand dat je net downloadde.
4. **Klik steeds op Volgende.** Accepteer de voorwaarden. De standaardinstellingen zijn prima.
5. **Start VS Code.** Je ziet een welkomstscherm. Dat mag je wegklikken.

!!! tip "Gratis en veilig"
    VS Code is gratis en wordt gemaakt door Microsoft. Je hoeft geen account aan te maken.

## Stap 2: Live Server erbij zetten

Hiermee zie je meteen wat je typt, zonder steeds te verversen.
{: .sub}

1. **Open VS Code.** Kijk in de balk helemaal links.
2. **Klik op het blokjes-icoon.** Dat is Extensions. Sneltoets: Ctrl + Shift + X.
3. **Zoek op: Live Server.** Typ het in het zoekvak bovenaan.
4. **Kies die van Ritwick Dey.** Er zijn er meer met dezelfde naam. Kijk goed.
5. **Klik op Install.** Klaar. Je hoeft niets in te stellen.

!!! onthoud "Zo start je Live Server"
    Rechtsklik op je bestand index.html en kies **Open with Live Server**. Je pagina opent in Chrome en ververst zichzelf zodra je opslaat met Ctrl + S.

!!! opdracht "1. Maak je werkmap en test Live Server"
    Ongeveer 5 minuten · Je werkt in: `opdracht-1`
    {: .meta}

    1. Maak een map `les1-jouwnaam`. Maak daarin een map `opdracht-1`.
    2. Open VS Code en kies File > Open Folder. Kies de map `les1-jouwnaam`.
    3. Maak in `opdracht-1` een nieuw bestand: klik op het icoontje New File.
    4. Noem het bestand index.html (kleine letters).
    5. Typ de regel uit de codehint en sla op met Ctrl + S.
    6. Rechtsklik op index.html > Open with Live Server.

    ??? hint "Codehint"
        ```html
        <h1>Hallo, ik ben ...</h1>
        ```

    !!! klaar "Klaar als..."
        Je ziet in Chrome de tekst 'Hallo, ik ben ...' staan. Verander de tekst, sla op, en kijk of de pagina meteen verandert.

=== blok-2 | Tags
## HTML werkt met tags

Een tag vertelt de browser wat iets is.
{: .sub}

```html
<h1>Sam Jansen</h1>
```

1. **Elke tag staat tussen punthaken.** `<` en `>` typ je met Shift en de toets naast de linker Shift.
2. **Openen en sluiten hoort bij elkaar.** De sluittag is hetzelfde, maar met een `/` erin: `</h1>`.
3. **Wat ertussen staat, zie je op de pagina.** De tags zelf zie je niet in de browser.

## Drie tags om mee te beginnen

| Tag | Wat is het? | Voorbeeld |
|---|---|---|
| `<h1>` | Een grote kop. Gebruik je één keer, voor je naam bovenaan. | `<h1>Sam Jansen</h1>` |
| `<p>` | Een stukje tekst, een alinea. p staat voor paragraph. | `<p>Ik woon in Utrecht.</p>` |
| `<h2>` | Een kleinere kop, voor een kopje boven een stukje tekst. | `<h2>Mijn hobby's</h2>` |

```html
<h1>Sam Jansen</h1>
<p>Ik woon in Utrecht.</p>
<h2>Mijn hobby's</h2>
```

```demo titel="Zo ziet de code hierboven eruit in Chrome"
<h1>Sam Jansen</h1>
<p>Ik woon in Utrecht.</p>
<h2>Mijn hobby's</h2>
```

Er zijn honderden tags. Deze drie en die van straks zijn genoeg voor je eerste pagina.

??? check "Check: tags"
    **1. Hoe sluit je `<h1>` af?**

    - A. `</h1>`
    - B. `<h1/>`
    - C. `/h1`
    - D. `<stop>`

    **2. Welke tag gebruik je voor een kopje onder je titel?**

    - A. `<p>`
    - B. `<h2>`
    - C. `<h6>`
    - D. `<kop>`

    ??? antwoord "Bekijk de antwoorden"
        **1. A – `</h1>`.** De sluittag is dezelfde tag als de openingstag, maar met een schuine streep erin.

        **2. B – `<h2>`.** h1 is de grootste kop en gebruik je één keer, bovenaan. Daaronder gebruik je h2. h6 bestaat wel, maar is de kleinste. `<kop>` bestaat niet.

!!! opdracht "2. Je eerste tekst op de pagina"
    Ongeveer 5 minuten · Je werkt in: `opdracht-2`
    {: .meta}

    1. Maak een map `opdracht-2` met daarin een nieuw bestand index.html.
    2. Maak een `<h1>` met je eigen naam erin.
    3. Zet daaronder een `<p>` met een zin over jezelf.
    4. Maak nog een `<p>` met je favoriete game of sport.
    5. Sla op met Ctrl + S en bekijk het met Live Server.

    ??? hint "Codehint (niet het antwoord)"
        ```html
        <h1>Jouw naam</h1>
        <p>Ik ben 17 jaar.</p>
        <p>Ik game graag.</p>
        ```

    !!! klaar "Klaar als..."
        Je ziet je naam groot en dik. Daaronder staan twee stukjes gewone tekst.

=== blok-3 | Het skelet
## Elke pagina heeft een vast skelet

Deze onderdelen staan op elke website ter wereld.
{: .sub}

```html
<!DOCTYPE html>
<html lang="nl">
  <head>
    <meta charset="UTF-8">
    <title>Mijn pagina</title>
  </head>
  <body>
    <h1>Sam Jansen</h1>
  </body>
</html>
```

| Onderdeel | Wat doet het? |
|---|---|
| `<!DOCTYPE html>` | Zegt tegen de browser: dit is een moderne webpagina. |
| `<html>` | Hier begint je pagina. Alles zit hierin. |
| `<head>` | Informatie over de pagina. Dit ziet de bezoeker **niet**. |
| `<body>` | Alles wat de bezoeker **wel** ziet. |

!!! onthoud "Snelle manier"
    Typ in een leeg .html-bestand een uitroepteken (!) en druk op Tab. Het hele skelet verschijnt vanzelf.

## Head of body: waar hoort het?

Het verschil zie je meteen in de browser.
{: .sub}

| In de head | In de body |
|---|---|
| De titel van het tabblad. En straks ook de koppeling naar je CSS-bestand. | Al je tekst, koppen, lijstjes, links en plaatjes. |
| `<title>Sam Jansen</title>` | `<h1>Sam Jansen</h1>` |

```demo titel="De title zie je in het tabblad, de h1 op de pagina zelf"
<style>.tab{display:inline-block;background:#E8EAF6;border-radius:8px 8px 0 0;padding:6px 14px;font-size:13px}.pagina{border:1px solid #b8bddc;padding:10px 14px}small{color:#E44D26;font-size:12px}</style>
<div class="tab">Sam Jansen</div> <small>← dit is de &lt;title&gt; uit de head</small>
<div class="pagina"><h1 style="margin:0">Sam Jansen</h1><small>↑ dit is de &lt;h1&gt; uit de body</small></div>
```

??? check "Check: het skelet"
    **1. Waar zet je de tekst die de bezoeker moet zien?**

    - A. In de head
    - B. In de body
    - C. In de title
    - D. In de meta

    **2. Wat typ je voor het skelet in VS Code?**

    - A. ? en Tab
    - B. ! en Tab
    - C. # en Tab
    - D. * en Tab

    ??? antwoord "Bekijk de antwoorden"
        **1. B – in de body.** In de head staat alleen informatie over de pagina, zoals de titel van het tabblad.

        **2. B – ! en dan Tab.** Dit werkt alleen in een leeg bestand dat op .html eindigt.

!!! opdracht "3. Zet je pagina netjes in het skelet"
    Ongeveer 5 minuten · Je werkt in: `opdracht-3`
    {: .meta}

    1. Maak een map `opdracht-3` met een leeg bestand index.html.
    2. Typ een uitroepteken en druk op Tab.
    3. Zet tussen `<title>` en `</title>` jouw naam.
    4. Neem je h1 en je alinea's uit opdracht-2 over in de body.
    5. Open met Live Server en kijk naar het tabblad bovenin Chrome.

    ??? hint "Codehint (niet het antwoord)"
        ```html
        <title>Sam Jansen</title>

        <body>
          <h1>Sam</h1>
        </body>
        ```

    !!! klaar "Klaar als..."
        In het tabblad van Chrome staat jouw naam. Op de pagina zelf staat je tekst.

=== blok-4 | Koppen en lijstjes
## Koppen en lijstjes

Zo krijgt je pagina structuur.
{: .sub}

1. **Koppen: h1 tot en met h6.** h1 is de grootste, h6 de kleinste. Gebruik h1 voor de titel van je pagina en h2 voor de kopjes daaronder.
2. **Lijstje: ul met li erin.** De `<ul>` is de lijst zelf. Elke `<li>` is één regel met een bolletje ervoor.
3. **Nummers in plaats van bolletjes?** Gebruik dan `<ol>` in plaats van `<ul>`. De li's blijven precies hetzelfde.

```html
<h2>Mijn hobby's</h2>
<ul>
  <li>Gamen</li>
  <li>Fietsen</li>
  <li>Tekenen</li>
</ul>

<ol>
  <li>Eerst dit</li>
  <li>Daarna dit</li>
</ol>
```

```demo titel="ul geeft bolletjes, ol geeft nummers"
<h2 style="margin:0 0 4px">Mijn hobby's</h2>
<ul style="margin-top:0"><li>Gamen</li><li>Fietsen</li><li>Tekenen</li></ul>
<ol><li>Eerst dit</li><li>Daarna dit</li></ol>
```

!!! tip "Engelse woorden"
    ul staat voor *unordered list* (lijst zonder volgorde), ol voor *ordered list* (lijst met volgorde), li voor *list item* (regel van de lijst).

## Links en plaatjes

Deze twee tags hebben extra informatie nodig. Die extra informatie heet een **attribuut** en zet je in de openingstag.
{: .sub}

1. **Een link: `<a>`.** `href` is het adres waar de link naartoe gaat. De tekst tussen `<a>` en `</a>` is wat je aanklikt.
2. **Een plaatje: `<img>`.** `src` is de bestandsnaam van je foto. `alt` beschrijft wat erop staat. `<img>` sluit je niet: er is geen `</img>`.

```html
<a href="https://nu.nl">Naar het nieuws</a>

<img src="foto.jpg" alt="Foto van Sam">
```

```demo titel="Een link, en een foto die niet gevonden wordt: dan zie je de alt-tekst"
<a href="#">Naar het nieuws</a><br><br>
<img src="bestaat-niet.jpg" alt="Foto van Sam" style="border:1px dashed #b8bddc;padding:20px">
```

!!! let-op "Let op: dezelfde map"
    Je foto moet in dezelfde map staan als je index.html. Staat hij ergens anders, dan blijft de plek op je pagina leeg.

!!! tip "Waarom alt-tekst?"
    Blinde bezoekers laten de tekst voorlezen door hun computer. En als je foto kapot is, zie je de alt-tekst staan.

??? check "Check: koppen, lijstjes, links"
    **1. Welke tag maakt een lijstje met bolletjes?**

    - A. `<ol>`
    - B. `<li>`
    - C. `<ul>`
    - D. `<list>`

    **2. Wat hoort er bij `<img>` om het plaatje te vinden?**

    - A. href
    - B. src
    - C. link
    - D. file

    ??? antwoord "Bekijk de antwoorden"
        **1. C – `<ul>`.** `<ul>` is de lijst met bolletjes. De `<li>` daarbinnen zijn de losse regels. `<ol>` geeft nummers.

        **2. B – src.** src betekent source, oftewel bron. href gebruik je bij een link, niet bij een plaatje.

!!! opdracht "4. Vul je pagina aan"
    Ongeveer 10 minuten · Je werkt in: `opdracht-4`
    {: .meta}

    1. Maak map `opdracht-4` met een nieuw index.html: ! en dan Tab.
    2. Neem je h1 en je alinea's uit opdracht-3 over in de body.
    3. Zet een `<h2>` met Mijn hobby's en daaronder een lijstje met drie hobby's.
    4. Zet er een link in naar een site die je vaak gebruikt.
    5. Zet een foto in `opdracht-4` en toon hem met `<img>` en een alt-tekst.

    ??? hint "Codehint (niet het antwoord)"
        ```html
        <h2>Mijn hobby's</h2>
        <ul>
          <li>...</li>
        </ul>
        ```

    !!! klaar "Klaar als..."
        Je pagina heeft nu een kop, tekst, een lijstje, een werkende link en een plaatje.

=== blok-5 | CSS koppelen
## Wat is CSS eigenlijk?

HTML zegt **wat** er staat. CSS zegt **hoe** het eruitziet.
{: .sub}

<div class="naast" markdown>

```demo titel="Zonder CSS"
<h1>Sam Jansen</h1><p>Student ICT in Utrecht.</p><a href="#">Contact</a>
```

```demo titel="Met CSS (dezelfde HTML)"
<style>body{background:#E8EAF6;font-family:Arial}h1{background:#2965F1;color:#fff;text-align:center;padding:10px;border-radius:8px}a{background:#E44D26;color:#fff;padding:6px 16px;border-radius:8px;text-decoration:none}</style>
<h1>Sam Jansen</h1><p>Student ICT in Utrecht.</p><a href="#">Contact</a>
```

</div>

1. **De HTML is precies hetzelfde.** Links en rechts staat dezelfde code. Alleen de opmaak is toegevoegd.
2. **CSS betekent Cascading Style Sheets.** Style sheet betekent letterlijk: opmaakblad.
3. **Zonder CSS kiest de browser zelf.** Dan wordt alles zwart, met een standaard lettertype.

## Zo maak en koppel je je CSS

Je CSS komt in een apart bestand naast je HTML.
{: .sub}

1. **Maak het bestand.** style.css hoort in dezelfde opdrachtmap als je index.html.
2. **Koppel het aan je HTML.** De link-regel zet je in de `<head>` van index.html.
3. **Schrijf je regels.** Zo ziet een CSS-regel eruit: `h1 { color: blue; }`

style.css
{: .bestandsnaam}

```css
/* style.css */
body {
  background-color: lightblue;
}
```

index.html, in de head
{: .bestandsnaam}

```html
<link rel="stylesheet" href="style.css">
```

| Onderdeel | In het voorbeeld | Betekenis |
|---|---|---|
| selector | `h1` | Wat pas je aan? |
| eigenschap | `color` | Wat verander je? |
| waarde | `blue` | Waarin verander je het? |

!!! onthoud "De vorm van elke regel"
    Tussen eigenschap en waarde staat een dubbele punt. De puntkomma sluit de regel af.

??? check "Check: CSS koppelen"
    **1. In welk deel van je HTML zet je de `<link>`?**

    - A. In de body
    - B. In de head
    - C. Onderaan
    - D. In de css

    **2. Welke CSS-regel is goed geschreven?**

    - A. `color = blue;`
    - B. `color: blue;`
    - C. `color blue`
    - D. `{color blue}`

    ??? antwoord "Bekijk de antwoorden"
        **1. B – in de head.** De browser leest eerst de head. Zo weet hij meteen welke opmaak hij moet gebruiken.

        **2. B – `color: blue;`** Een dubbele punt tussen eigenschap en waarde, en een puntkomma erachter.

!!! opdracht "5. Je eerste kleur op de pagina"
    Ongeveer 5 minuten · Je werkt in: `opdracht-5`
    {: .meta}

    1. Maak map `opdracht-5` met een nieuw index.html en neem je pagina over.
    2. Maak in `opdracht-5` een tweede bestand: style.css.
    3. Zet de link-regel in de head van index.html.
    4. Geef de body een achtergrondkleur en je h1 een andere kleur.
    5. Sla beide bestanden op met Ctrl + S.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        body {
          background-color: lightblue;
        }
        h1 {
          color: darkblue;
        }
        ```

    !!! klaar "Klaar als..."
        Je pagina heeft een gekleurde achtergrond en je naam heeft een andere kleur dan de rest.

=== blok-6 | Selectors
## Wie krijgt de opmaak?

Met een selector wijs je aan wat je wilt aanpassen. Je kent er nu twee.
{: .sub}

| Soort | Zo schrijf je het | Wat pakt het? |
|---|---|---|
| Tagnaam | `p { }` (geen teken ervoor) | Alle `<p>` op je hele pagina. |
| Class | `.knop { }` (punt ervoor) | Alles met `class="knop"`. Zo vaak als je wilt. |

!!! let-op "Let op: de punt staat alleen in je CSS"
    In je HTML schrijf je `class="knop"`, zonder punt. In je CSS wordt dat `.knop { }`.

## Allebei in één voorbeeld

Links de HTML, rechts de CSS die erbij hoort.
{: .sub}

index.html
{: .bestandsnaam}

```html
<h1 class="kop">Sam</h1>
<p>Ik woon in Utrecht.</p>
<p>Ik game graag.</p>
<a href="#" class="knop">Mail</a>
```

style.css
{: .bestandsnaam}

```css
.kop { color: navy; }
p { color: gray; }
.knop { color: red; }
```

```demo titel="Beide alinea's worden grijs, want p pakt ze allebei. De h1 en de link hebben elk hun eigen class."
<style>.kop{color:navy}p{color:gray}.knop{color:red}</style>
<h1 class="kop">Sam</h1><p>Ik woon in Utrecht.</p><p>Ik game graag.</p><a href="#" class="knop">Mail</a>
```

!!! tip "Er komt er later nog één bij"
    Naast de tagnaam en de class bestaat er ook nog een id. Die leer je in module 2. Met deze twee kun je nu alles.

??? check "Check: selectors"
    **1. Je hebt `class="knop"`. Hoe schrijf je dat in je CSS?**

    - A. `#knop`
    - B. `.knop`
    - C. `knop`
    - D. `*knop`

    **2. Waar schrijf je de punt van .knop?**

    - A. In je HTML
    - B. In je CSS
    - C. In allebei
    - D. Nergens

    ??? antwoord "Bekijk de antwoorden"
        **1. B – `.knop`.** Een class herken je in CSS aan de punt ervoor. Zonder punt zoekt de browser naar een tag.

        **2. B – in je CSS.** In je HTML staat `class="knop"` zonder punt. In je CSS schrijf je `.knop { }`. Die punt zegt tegen de browser: zoek naar een class.

!!! opdracht "6. Wijs je eigen elementen aan"
    Ongeveer 5 minuten · Je werkt in: `opdracht-6`
    {: .meta}

    1. Maak map `opdracht-6` met index.html en style.css. Neem je pagina over.
    2. Geef je link in index.html de class knop.
    3. Geef je h1 de class kop.
    4. Maak in style.css een regel voor `.knop` met een kleur.
    5. Maak een regel voor `.kop` met een andere kleur.

    ??? hint "Codehint (niet het antwoord)"
        ```html
        <a class="knop">
        <h1 class="kop">
        ```
        ```css
        .knop { color: red; }
        .kop { color: navy; }
        ```

    !!! klaar "Klaar als..."
        Je link en je kop hebben allebei hun eigen kleur, terwijl je alinea's onveranderd blijven.

=== blok-7 | Kleur en tekst
## Eigenschappen: kleur

Twee eigenschappen die je constant gebruikt.
{: .sub}

| Eigenschap | Wat doet het? | Voorbeeld |
|---|---|---|
| `color` | De kleur van de tekst zelf. | `h1 { color: white; }` |
| `background-color` | De kleur van het vlak erachter. | `h1 { background-color: navy; }` |

Een kleur opgeven kan op twee manieren:

1. **Met een naam:** red, blue, white, navy, lightblue, gray. Handig, maar er is maar een beperkt aantal namen.
2. **Met een hexcode:** een hekje met zes tekens, bijvoorbeeld `#2965F1`. Hiermee kun je elke kleur maken die bestaat. In VS Code zie je een gekleurd vierkantje naast de code. Klik erop voor de kleurenkiezer.

```demo titel="Kleuren met een naam en met een hexcode. Onder: witte tekst op een navy achtergrond."
<style>.r{display:flex;gap:8px;margin-bottom:10px}.r div{color:#fff;padding:8px 12px;border-radius:6px;font-family:Consolas,monospace;font-size:13px}</style>
<div class="r"><div style="background:red">red</div><div style="background:navy">navy</div><div style="background:#2965F1">#2965F1</div><div style="background:#1E8E4E">#1E8E4E</div></div>
<h1 style="color:white;background-color:navy;margin:0;padding:8px 12px">Sam Jansen</h1>
```

## Eigenschappen: tekst

Hiermee bepaal je hoe je tekst eruitziet.
{: .sub}

| Eigenschap | Wat doet het? | Voorbeeld |
|---|---|---|
| `font-size` | Hoe groot de letters zijn. | `font-size: 20px;` |
| `font-family` | Welk lettertype je gebruikt. | `font-family: Arial;` |
| `text-align` | Links, midden of rechts. | `text-align: center;` |
| `text-decoration` | Hiermee haal je de streep onder een link weg. | `text-decoration: none;` |

```demo titel="Wat de vier tekst-eigenschappen doen"
<p style="font-size:22px;margin:4px 0">font-size: 22px</p>
<p style="font-family:Georgia;margin:4px 0">font-family: Georgia</p>
<p style="text-align:center;margin:4px 0;background:#f6f7fc">text-align: center</p>
<a href="#" style="text-decoration:none">text-decoration: none (geen streep)</a>
```

!!! tip "Wat is px?"
    px staat voor pixels: de puntjes waaruit je scherm bestaat. `font-size: 20px` betekent dus letters van twintig puntjes hoog.

??? check "Check: eigenschappen"
    **1. Waarmee geef je iets een achtergrondkleur?**

    - A. color
    - B. background-color
    - C. bgcolor
    - D. fill

    **2. Waarmee haal je de streep onder een link weg?**

    - A. font-size
    - B. text-align
    - C. text-decoration
    - D. color

    ??? antwoord "Bekijk de antwoorden"
        **1. B – background-color.** color is de kleur van de tekst zelf. background-color is de kleur van het vlak erachter.

        **2. C – text-decoration.** Met `text-decoration: none` verdwijnt de streep. Dat is de eerste stap om van een link een knop te maken.

!!! opdracht "7. Geef je pagina een eigen uitstraling"
    Ongeveer 5 minuten · Je werkt in: `opdracht-7`
    {: .meta}

    1. Maak map `opdracht-7` en neem je twee bestanden over.
    2. Geef de body een font-family, bijvoorbeeld Arial.
    3. Geef `.kop` een achtergrondkleur, witte tekst en tekst in het midden.
    4. Geef `.knop` een achtergrondkleur met een hexcode.
    5. Haal met text-decoration de streep onder je link weg.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        .kop {
          background-color: #2965F1;
          color: white;
          text-align: center;
        }
        ```

    !!! klaar "Klaar als..."
        Je pagina heeft een eigen lettertype, een gekleurde balk bovenaan en je link ziet er niet meer uit als gewone linktekst.

=== blok-8 | Boxmodel
## Ruimte maken: het boxmodel

Elk element is een rechthoek met drie lagen ruimte eromheen.
{: .sub}

| Laag | Wat is het? |
|---|---|
| `padding` | Ruimte **binnen** de rand. Je knop wordt er dikker van. |
| `border` | De rand zelf: dikte, soort en kleur. |
| `margin` | Ruimte **buiten** de rand, tussen dit element en de buren. |

```demo titel="Van binnen naar buiten: tekst (blauw), padding (groen), border (zwart), margin (oranje). Dezelfde kleuren zie je in Chrome bij F12 > Computed."
<style>.m{background:#f9cc9d;padding:16px;display:inline-block}.b{border:4px solid #1B1F3B}.p{background:#c3d08b;padding:16px}.t{background:#8cb6c0;padding:6px 14px}</style>
<div class="m"><div class="b"><div class="p"><div class="t">jouw tekst</div></div></div></div>
```

!!! onthoud "Ezelsbruggetje"
    Padding is de vulling in je jas. Margin is de afstand tot degene die naast je staat.

## Hoeveel waarden schrijf je op?

Bij padding en margin mag je één, twee of vier getallen geven.
{: .sub}

| Zo schrijf je het | Wat gebeurt er? |
|---|---|
| `padding: 20px;` | Eén getal: alle vier de kanten krijgen 20 pixels ruimte. |
| `padding: 12px 24px;` | Twee getallen: het eerste is boven én onder, het tweede links én rechts. |
| `padding: 10px 20px 30px 40px;` | Vier getallen: met de klok mee. Boven, rechts, onder, links. |

```demo titel="Dezelfde knop met drie verschillende paddings"
<style>a{display:inline-block;background:#2965F1;color:#fff;text-decoration:none;border-radius:8px;margin-right:10px}</style>
<a style="padding:20px">padding: 20px</a><a style="padding:12px 24px">padding: 12px 24px</a><a style="padding:10px 20px 30px 40px">10px 20px 30px 40px</a>
```

`margin` werkt precies hetzelfde: ook daar schrijf je één, twee of vier getallen.

### De rand en ronde hoeken

```css
border: 2px solid black;
border-radius: 8px;
```

Met `border` maak je de rand zelf: dikte, soort (`solid` is een doorgetrokken lijn) en kleur. Met `border-radius` krijg je ronde hoeken.

??? check "Check: het boxmodel"
    **1. Welke ruimte zit binnen de rand?**

    - A. margin
    - B. padding
    - C. border
    - D. radius

    **2. Bij `padding: 10px 30px;` wat doet die 30px?**

    - A. boven en onder
    - B. links en rechts
    - C. alleen links
    - D. de rand

    ??? antwoord "Bekijk de antwoorden"
        **1. B – padding.** Padding zit tussen de rand en je tekst. De ruimte buiten de rand heet margin.

        **2. B – links en rechts.** Bij twee getallen is het eerste boven en onder, het tweede links en rechts.

!!! opdracht "8. Maak je knop af en kijk in de browser"
    Ongeveer 15 minuten · Je werkt in: `opdracht-8`
    {: .meta}

    1. Maak map `opdracht-8` met je index.html en style.css uit opdracht-7.
    2. Geef `.knop` een padding van 12px 24px.
    3. Geef `.knop` een border-radius van 8px en een margin van 20px.
    4. Druk in Chrome op F12. Er opent een venster met code. (Gebeurt er niets? Probeer Fn + F12.)
    5. Klik linksboven in dat venster op het pijltje-icoon en klik daarna op je knop.
    6. Klik in dat venster op het tabblad Computed.

    ??? hint "Codehint"
        ```css
        .knop {
          padding: 12px 24px;
          border-radius: 8px;
          margin: 20px;
        }
        ```

    !!! klaar "Klaar als..."
        Bovenaan bij Computed zie je een gekleurde tekening van je knop: oranje is de margin, groen de padding. Klik in de tekening op een getal en verander het.

=== eindopdracht | Eindopdracht
!!! opdracht eind "Maak je profielpagina af"
    Je werkt in een nieuwe map `eindopdracht`, met index.html en style.css.
    {: .meta}

    **Op je pagina staat:**

    - Map `eindopdracht` met index.html, style.css en je foto
    - Een compleet skelet met head en body
    - Een `<h1>` met je naam en een eigen class
    - Twee alinea's over jezelf
    - Een lijstje met drie hobby's
    - Een foto met alt-tekst
    - Een link als knop met een class
    - Alles afgemaakt met mooie randen en kleuren
    {: .checklist}

    !!! tip "Al klaar?"
        Maak je foto rond met `border-radius: 50%` en geef je pagina een tweede kleur.

Alles wat je nodig hebt, heb je in de mini-opdrachten al een keer gemaakt. Kijk gerust terug in je eigen mappen.

## Inleveren

Zip de hele map `les1-jouwnaam`, met `opdracht-1` tot en met `opdracht-8` en de map `eindopdracht` erin. Noem de zip `les1-jouwnaam.zip`.

**Checklist: vink af voordat je inlevert**

- Map `les1-jouwnaam` met `opdracht-1` tot en met `opdracht-8`
- Map `eindopdracht` met index.html en style.css
- Je foto staat in dezelfde map als je HTML
- Alle namen met kleine letters: index.html, style.css
- Alles opgeslagen met Ctrl + S
- De pagina opent goed met Live Server
{: .checklist}

!!! tip "Zo maak je een zip"
    Rechtsklik op de map `les1-jouwnaam` en kies **Comprimeren naar > ZIP-bestand**. Op oudere Windows: **Kopiëren naar > Gecomprimeerde map**.

!!! tip "Werk je thuis?"
    Je hebt alleen VS Code en Chrome nodig. Kom je er niet uit, schrijf je vraag op en neem hem mee naar de les.

Twijfel je of iets af is? Kijk bij **Klaar als...** bij die opdracht.

=== werkt-het-niet | Werkt het niet?
Bijna altijd is het een van deze vijf.
{: .sub}

1. **Heb je opgeslagen?** Ctrl + S. Zonder opslaan verandert er niets in de browser.
2. **Klopt de bestandsnaam?** style.css met kleine letters. Style.CSS is iets anders. En geen spaties.
3. **Staan de bestanden in dezelfde map?** index.html, style.css en je foto horen in dezelfde opdrachtmap.
4. **Is de sluittag er?** Kijk of elke `<tag>` ook een `</tag>` heeft.
5. **Puntkomma vergeten in je CSS?** Elke regel eindigt op een puntkomma.

!!! tip "Nog steeds niet?"
    Vraag eerst je buurman, daarna je docent. Werk je zelfstandig? Kijk bij de naslag.

=== naslag | Naslag
## HTML

Alles van module 1 op een rij. Kijk hier eerst als je iets kwijt bent.
{: .sub}

De tags die je nu kent
{: .bestandsnaam}

```html
<h1>Grote kop</h1>
<h2>Kopje daaronder</h2>
<p>Een alinea tekst</p>
<ul>
  <li>Regel met bolletje</li>
</ul>
<a href="https://nu.nl">Kliktekst</a>
<img src="foto.jpg" alt="Foto van Sam">
```

Een complete pagina
{: .bestandsnaam}

```html
<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8">
  <title>Mijn pagina</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Sam Jansen</h1>
</body>
</html>
```

!!! onthoud "Onthoud"
    Openen en sluiten hoort bij elkaar: `<p> ... </p>`. Alleen `<img>` sluit je niet. Typ het skelet met ! en dan Tab.

## CSS

Eigenschappen die je kent
{: .bestandsnaam}

```css
color: navy;
background-color: #2965F1;
font-family: Arial;
font-size: 20px;
text-align: center;
text-decoration: none;
padding: 12px 24px;
margin: 20px;
border: 2px solid black;
border-radius: 8px;
```

Een complete style.css
{: .bestandsnaam}

```css
body {
  background-color: lightblue;
  font-family: Arial;
}
.kop {
  color: white;
  text-align: center;
}
.knop {
  padding: 12px 24px;
  border-radius: 8px;
}
```

!!! onthoud "De vorm van elke regel"
    `selector { eigenschap: waarde; }` Een dubbele punt tussen eigenschap en waarde, en een puntkomma erachter.

!!! tip "Koppelen aan je HTML"
    Zet `<link rel="stylesheet" href="style.css">` in de head, en houd beide bestanden in dezelfde map.

=== woordenlijst | Woordenlijst
De Engelse woorden van module 1, met de Nederlandse vertaling en uitleg in gewone taal.
{: .sub}

| Engels | Nederlands | Uitleg |
|---|---|---|
| **HTML** (HyperText Markup Language) | opmaaktaal voor webpagina's | zegt wát er op de pagina staat |
| **CSS** (Cascading Style Sheets) | opmaakbladen | zegt hoe de pagina eruitziet |
| **browser** | webbrowser | programma dat je pagina tekent, zoals Chrome |
| **extension** | uitbreiding | extra onderdeel voor VS Code, zoals Live Server |
| **folder** | map | plek waar je bestanden bewaart |
| **file** | bestand | bijvoorbeeld index.html |
| **save** | opslaan | Ctrl + S |
| **tag** | label | stukje HTML tussen < en > |
| **element** | element | openingstag + inhoud + sluittag |
| **attribute** | attribuut | extra informatie in een tag, zoals href |
| **head** | hoofd | informatie over de pagina, zie je niet |
| **body** | lichaam | alles wat de bezoeker wel ziet |
| **title** | titel | tekst in het tabblad |
| **heading** (h1–h6) | kop | titel of kopje |
| **paragraph** (p) | alinea | stukje tekst |
| **unordered list** (ul) | ongenummerde lijst | lijst met bolletjes |
| **ordered list** (ol) | genummerde lijst | lijst met nummers |
| **list item** (li) | lijstregel | één regel in een lijst |
| **anchor** (a) | anker | de tag voor een link |
| **link** | koppeling | klikbare verwijzing |
| **href** (hypertext reference) | adres | waar een link naartoe gaat |
| **image** (img) | afbeelding | plaatje op je pagina |
| **src** (source) | bron | bestandsnaam van het plaatje |
| **alt** (alternative text) | vervangende tekst | beschrijving van het plaatje |
| **style sheet** | opmaakblad | je CSS-bestand |
| **selector** | aanwijzer | wat je aanpast: p of .knop |
| **property** | eigenschap | wat je verandert: color |
| **value** | waarde | waarin je het verandert: blue |
| **class** | klasse, label | naam die je zo vaak mag gebruiken |
| **color** | kleur | kleur van de tekst |
| **background** | achtergrond | vlak achter iets |
| **font** | lettertype | hoe de letters eruitzien |
| **size** | grootte | bijvoorbeeld font-size |
| **align** | uitlijnen | links, midden of rechts |
| **decoration** | versiering | zoals de streep onder een link |
| **none** | geen | zet iets uit |
| **pixel** (px) | beeldpunt | puntje op je scherm |
| **hex code** | hexcode | kleur als #2965F1 |
| **padding** | opvulling | ruimte binnen de rand |
| **border** | rand | lijn om een element |
| **margin** | marge | ruimte buiten de rand |
| **radius** | straal | hoe rond de hoeken zijn |
| **solid** | doorgetrokken | een dichte lijn |
| **box model** | boxmodel | padding, border en margin samen |
