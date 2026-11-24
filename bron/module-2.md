---
nr: 2
titel: Van pagina naar site
kort: Je pagina wordt een echte website: drie pagina's met een menubalk die naar elkaar linken.
tags: div | nav | id | paden
---

=== start | Start
## Dit ga je maken

Aan het eind van deze module heb je een site van drie pagina's (Home, Hobby's en Contact) met een menubalk.

| Wat zie je? | Hoe doe je dat? |
|---|---|
| Een menubalk op elke pagina | HTML en CSS |
| Drie pagina's die naar elkaar linken | HTML |
| Blokken met een kop en tekst | HTML en CSS |
| Je foto netjes in een eigen map | een pad |

```demo titel="Zo kan je mini-site er aan het eind uitzien"
<style>body{background:#E8EAF6;padding:0}header{background:#1B1F3B;color:#fff;padding:12px 16px}header h1{margin:0;font-size:20px}nav{background:#1B1F3B;padding:6px 10px;border-top:1px solid #333a66}nav ul{list-style:none;padding:0;margin:0}nav li{display:inline-block}nav a{color:#fff;text-decoration:none;padding:6px 12px;font-size:14px}nav a.actief{background:#E44D26}main{padding:12px 16px}.kaart{background:#fff;padding:10px 14px;border-radius:8px;margin-bottom:10px}.kaart h2{margin:0 0 4px;font-size:16px}.kaart p{margin:0;font-size:14px}footer{background:#1B1F3B;color:#fff;padding:8px 16px;font-size:13px}</style>
<header><h1>Sam Jansen</h1></header>
<nav><ul><li><a class="actief" href="#">Home</a></li><li><a href="#">Hobby's</a></li><li><a href="#">Contact</a></li></ul></nav>
<main><div class="kaart"><h2>Mijn hobby's</h2><p>Gamen en fietsen</p></div><div class="kaart"><h2>Over mij</h2><p>Ik woon in Utrecht</p></div></main>
<footer>sam@mail.nl</footer>
```

## Dit kun je al

- **HTML:** h1, h2, p, ul met li, a met href, img met src en alt. En het skelet met head en body.
- **CSS:** style.css met `<link>` in de head. Een selector is waarmee je aanwijst wat je aanpast: `p { }` of `.kaart { }`.
- **Boxmodel:** padding binnen de rand, margin erbuiten en border ertussen.

!!! tip "Iets kwijt?"
    De naslag van module 1 mag je er de hele tijd bij houden. Blok 1 is een korte opfrisser.

## Zo werk je

Begin met een lege map `les2-jouwnaam`. Daarin maak je weer `opdracht-1` tot en met `opdracht-8` en een map `eindopdracht`. Je mappen van module 1 laat je gewoon staan. Bij elke opdracht kopieer je de vorige opdrachtmap naar een nieuwe map en werk je daarin verder.

| Blok | Onderwerp |
|---|---|
| 1 | Opfrissen en Prettier installeren |
| 2 | Groeperen met div |
| 3 | Semantische tags |
| 4 | id en ankerlinks |
| 5 | Een tweede pagina |
| 6 | Paden |
| 7 | De menubalk |
| 8 | Menu opmaken |

!!! let-op "De regel"
    Altijd kleine letters. Geen spaties in map- of bestandsnamen.

=== blok-1 | Opfrissen
## Nieuw gereedschap: Prettier

Deze extensie zet je code bij elke keer opslaan netjes recht.
{: .sub}

1. **Open VS Code.** Kijk in de balk helemaal links.
2. **Klik op het blokjes-icoon.** Dat is Extensions. Sneltoets: Ctrl + Shift + X.
3. **Zoek op: Prettier.** Kies **Prettier - Code formatter** van Prettier.
4. **Klik op Install.** Onder de naam staat esbenp.prettier-vscode. Kijk goed.
5. **Zet de instellingen erin.** Druk Ctrl + Shift + P, typ **settings json** en kies **Open User Settings (JSON)**. Zet de regels hieronder tussen de accolades { }.

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnPaste": true
}
```

!!! tip "Wat doet het?"
    Bij elke Ctrl + S zet Prettier je code netjes recht en springt hij goed in. Scheve of niet gesloten code valt meteen op. Handmatig rechtzetten: Shift + Alt + F.

!!! let-op "Staat er al iets in je settings?"
    Staan er al regels tussen de accolades { }? Zet dan een komma achter de laatste regel en plak de drie nieuwe regels eronder. Er hoort maar één paar accolades { } in het bestand.

## Waar waren we gebleven?

Elke pagina begint met hetzelfde skelet.
{: .sub}

1. **Typ ! en druk op Tab.** In een leeg bestand dat op .html eindigt. VS Code typt het skelet voor je.
2. **In de head zet je informatie.** De `<title>` voor het tabblad, en de koppeling naar je CSS. style.css staat in dezelfde map.
3. **In de body zet je de inhoud.** Alles wat de bezoeker moet zien staat tussen `<body>` en `</body>`.

```html
<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8">
  <title>Sam Jansen</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Sam Jansen</h1>
</body>
</html>
```

!!! let-op "Let op die link-regel"
    Zonder die regel in de head doet je style.css helemaal niets. Dit is fout nummer 1 van module 1.

## Tags en classes, kort herhaald

index.html
{: .bestandsnaam}

```html
<h1 class="kop">Sam</h1>
<p>Ik woon in Utrecht.</p>
<ul>
  <li>Gamen</li>
</ul>
<a href="...">Mail mij</a>
```

style.css
{: .bestandsnaam}

```css
.kop {
  color: navy;
}
p {
  color: gray;
}
a { color: red; }
```

1. **De punt staat alleen in je CSS.** In je HTML schrijf je `class="kop"` zonder punt. In je CSS wordt dat `.kop { }`.
2. **Een tagnaam pakt alles.** `p { }` past elke alinea op je pagina aan. Een class gebruik je zo vaak als je wilt.

??? check "Check: opfrissen"
    **1. Welke regel koppelt je CSS aan je HTML?**

    - A. `<link rel="stylesheet" href="style.css">`
    - B. `<css src="style.css">`
    - C. `<style href="style.css">`
    - D. `<link css="style.css">`

    **2. In je HTML staat `class="kaart"`. Hoe schrijf je die selector in CSS?**

    - A. `kaart { }`
    - B. `.kaart { }`
    - C. `#kaart { }`
    - D. `class kaart { }`

    ??? antwoord "Bekijk de antwoorden"
        **1. A – `<link rel="stylesheet" href="style.css">`.** Die regel zet je in de head. rel zegt wat voor bestand het is, href zegt waar het staat.

        **2. B – `.kaart { }`.** Een class herken je in CSS aan de punt ervoor. Zonder punt zoekt de browser naar een tag die kaart heet, en die bestaat niet.

!!! opdracht "1. Zet je werkmap voor les 2 klaar"
    Ongeveer 10 minuten · Je werkt in: `opdracht-1`
    {: .meta}

    1. Maak een map `les2-jouwnaam`. Maak daarin een map `opdracht-1`.
    2. Open VS Code, kies File > Open Folder en kies `les2-jouwnaam`.
    3. Maak in `opdracht-1` een bestand index.html. Typ ! en druk op Tab.
    4. Zet je naam in de `<title>`. Maak een `<h1>` en twee alinea's.
    5. Maak style.css, koppel hem in de head en geef de body een kleur.
    6. Open met Live Server en kijk of je kleur er staat.

    ??? hint "Codehint (niet het antwoord)"
        ```html
        <link rel="stylesheet" href="style.css">
        ```
        ```css
        body {
          background-color: #E8EAF6;
        }
        ```

    !!! klaar "Klaar als..."
        Je pagina heeft een eigen achtergrondkleur en in het tabblad staat je naam. Lukt het niet uit je hoofd? De naslag van module 1 mag erbij. Probeer het daarna nog een keer zonder.

=== blok-2 | Groeperen met div
## Een doos om je onderdelen heen

Met een `<div>` zet je dingen bij elkaar die bij elkaar horen.
{: .sub}

1. **Een div is een lege doos.** Hij betekent niets en je ziet hem niet. Hij is er alleen om dingen te groeperen.
2. **Alles ertussen hoort bij elkaar.** De kop en de alinea zijn nu samen één blok op je pagina.
3. **Geef hem een class.** Anders kun je hem niet aanwijzen in je CSS. Met `.kaart { }` maak je hem opeens zichtbaar.

```html
<div class="kaart">
  <h2>Mijn hobby's</h2>
  <p>Ik game graag.</p>
</div>
<div class="kaart">
  <h2>Over mij</h2>
  <p>Ik woon in Utrecht.</p>
</div>
```

!!! tip "Waarom zou je dat doen?"
    Zodra je twee dingen samen een kleur wilt geven, of straks naast elkaar wilt zetten, heb je een doos nodig om ze in te stoppen.

## Nesten: een tag in een tag

De div gebruik je hier als doos waar andere elementen in zitten. Een tag binnen een andere tag heet **nesten**.
{: .sub}

1. **Wat je als laatste opent, sluit je als eerste.** Dus `<div><p>Hoi</p></div>` en niet `<div><p>Hoi</div></p>`.
2. **Spring in met Tab.** Alles wat binnen een tag staat, zet je één Tab naar rechts. Snel rechtzetten: Shift + Alt + F.

```demo titel="De h2 en de p staan in de code binnen de div, dus op de pagina ook"
<style>.div{border:3px solid #2965F1;padding:8px;border-radius:8px;position:relative}.l{font-family:Consolas,monospace;font-size:11px;font-weight:bold;color:#fff;padding:1px 6px;border-radius:4px;margin-right:6px}h2,p{margin:4px 0;padding:4px;border-radius:4px}h2{border:2px solid #E44D26;font-size:17px}p{border:2px solid #1E8E4E}</style>
<div class="div"><span class="l" style="background:#2965F1">div</span>
<h2><span class="l" style="background:#E44D26">h2</span>Mijn hobby's</h2>
<p><span class="l" style="background:#1E8E4E">p</span>Ik game graag.</p></div>
```

Zo maak je de doos zichtbaar. Zonder CSS zie je een div niet.

```css
.kaart {
  background-color: #E8EAF6;
  padding: 20px;
  border-radius: 8px;
}
```

```demo titel="Twee kaarten met een achtergrond, padding, ronde hoeken en ruimte ertussen"
<style>body{background:#f6f7fc}.kaart{background:#fff;padding:20px;border-radius:8px;margin-bottom:12px}h2{margin:0 0 4px;font-size:18px}p{margin:0}</style>
<div class="kaart"><h2>Mijn hobby's</h2><p>Ik game graag.</p></div><div class="kaart"><h2>Over mij</h2><p>Ik woon in Utrecht.</p></div>
```

??? check "Check: groeperen met div"
    **1. Waarvoor gebruik je een `<div>`?**

    - A. Om tekst dik te maken
    - B. Om elementen te groeperen
    - C. Om een link te maken
    - D. Om je CSS te koppelen

    **2. Welke code is goed genest?**

    - A. `<div><p>Hoi</div></p>`
    - B. `<div><p>Hoi</p></div>`
    - C. `<p><div>Hoi</p></div>`
    - D. `<div><p>Hoi<div></p>`

    ??? antwoord "Bekijk de antwoorden"
        **1. B – om elementen te groeperen.** Een div doet uit zichzelf niets. Hij zet dingen bij elkaar, zodat je ze samen kunt opmaken of verplaatsen.

        **2. B – `<div><p>Hoi</p></div>`.** De p is als laatste geopend, dus die sluit je als eerste. Bij de andere antwoorden lopen de tags door elkaar heen.

!!! opdracht "2. Maak je eerste kaartje"
    Ongeveer 10 minuten · Je werkt in: `opdracht-2`
    {: .meta}

    1. Kopieer de inhoud van `opdracht-1` naar een nieuwe map `opdracht-2`.
    2. Zet een `<h2>` en een alinea samen in een `<div class="kaart">`.
    3. Geef `.kaart` in style.css een achtergrondkleur.
    4. Geef `.kaart` ook `padding: 20px` en `border-radius: 8px`.
    5. Maak eronder een tweede kaart met dezelfde class.
    6. Zet er ruimte tussen met `margin-bottom: 20px`.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        .kaart {
          background-color: white;
          padding: 20px;
          border-radius: 8px;
          margin-bottom: 20px;
        }
        ```

    !!! klaar "Klaar als..."
        Je ziet twee gekleurde blokken onder elkaar staan, met ruimte tussen de rand en de tekst, en ruimte tussen de blokken.

=== blok-3 | Semantische tags
## Divs met een naam

Deze vier tags doen hetzelfde als een div, maar vertellen erbij wat het is.
{: .sub}

| Tag | Wat is het? | Wat staat erin? |
|---|---|---|
| `<header>` | De bovenkant | Meestal je naam of het logo van de site. |
| `<nav>` | Het menu | De links naar de andere pagina's van je site. |
| `<main>` | De hoofdinhoud | Waar het op deze pagina echt om gaat. Eén keer per pagina, net als h1. |
| `<footer>` | De onderkant | Contactgegevens, je mailadres, het jaartal. |

!!! tip "Waarom niet gewoon overal div?"
    Omdat jij zelf in een lange pagina zo terugziet wat waar staat. Google leest je pagina ook beter. En blinde bezoekers gebruiken een schermlezer die met deze tags meteen naar het menu of de hoofdinhoud kan springen. Dat heet **semantiek**: de tag zegt wat het is.

## Zo ziet je body er dan uit

Dezelfde inhoud als eerst, maar nu netjes verdeeld.
{: .sub}

```html
<body>
  <header>
    <h1>Sam Jansen</h1>
  </header>
  <nav>
    <a href="index.html">Home</a>
  </nav>
  <main>
    <section class="kaart">
      <h2>Mijn hobby's</h2>
    </section>
  </main>
  <footer>
    <p>sam@mail.nl</p>
  </footer>
</body>
```

```demo titel="Zo verdelen de semantische tags je pagina"
<style>div{border:2px dashed;border-radius:6px;padding:6px 10px;margin-bottom:6px;font-family:Consolas,monospace;font-size:13px}</style>
<div style="border-color:#2965F1">header</div><div style="border-color:#E44D26">nav</div>
<div style="border-color:#1E8E4E;padding-bottom:30px">main<div style="border-color:#b8bddc;margin-top:6px">section class="kaart"</div></div>
<div style="border-color:#1B1F3B">footer</div>
```

1. **Alles zit nog steeds in de body.** Je verandert niets aan je tekst. Je zet er dozen omheen.
2. **`<section>` is een stuk pagina.** Een deel met een eigen kopje. Je mag er zoveel gebruiken als je wilt.
3. **In CSS net als elke tag.** `header { }` en `footer { }` werken precies zoals `p { }` of `h1 { }`.

!!! let-op "Let op de volgorde"
    De browser tekent de tags van boven naar beneden. Zet je de footer bovenaan in je body, dan staat hij ook bovenaan op je pagina.

??? check "Check: semantische tags"
    **1. Welke tag gebruik je voor je menu?**

    - A. `<navigatie>`
    - B. `<nav>`
    - C. `<menubalk>`
    - D. `<header>`

    **2. Wat hoort er in `<main>`?**

    - A. De titel van het tabblad
    - B. De koppeling naar je CSS
    - C. De hoofdinhoud van de pagina
    - D. Alleen plaatjes

    ??? antwoord "Bekijk de antwoorden"
        **1. B – `<nav>`.** nav komt van navigatie. `<navigatie>` en `<menubalk>` bestaan niet. `<header>` is de bovenkant van je pagina, en daar staat je nav vaak wel in.

        **2. C – de hoofdinhoud van de pagina.** De titel van het tabblad en de link naar je CSS staan in de head. Die zie je niet op de pagina zelf.

!!! opdracht "3. Verdeel je pagina in blokken"
    Ongeveer 10 minuten · Je werkt in: `opdracht-3`
    {: .meta}

    1. Kopieer `opdracht-2` naar een nieuwe map `opdracht-3`.
    2. Zet je `<h1>` in een `<header>`.
    3. Zet je kaarten samen in een `<main>`.
    4. Maak onderaan een `<footer>` met je mailadres erin.
    5. Geef header en footer in style.css een achtergrondkleur en padding.
    6. Controleer of alles goed is ingesprongen: Shift + Alt + F.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        header {
          background-color: #1B1F3B;
          color: white;
          padding: 20px;
        }
        ```

    !!! klaar "Klaar als..."
        Bovenaan je pagina staat een gekleurde balk met je naam, onderaan een balk met je mailadres, en je kaarten staan ertussen.

=== blok-4 | id en ankerlinks
## id: elke naam maar één keer per pagina

Naast de class is er nog een manier om iets aan te wijzen: het **id**.
{: .sub}

| | class | id |
|---|---|---|
| Teken in CSS | punt: `.kaart` | hekje: `#contact` |
| Hoe vaak? | Zo vaak je wilt | Elk id maar één keer per pagina |
| Gebruik je voor | Opmaak van alles wat vaker terugkomt: kaarten, knoppen, kopjes. Dat is verreweg het meest. | Precies één plek op de pagina aanwijzen. Vooral handig om ergens naartoe te springen. |

HTML
{: .bestandsnaam}

```html
<div class="kaart">...</div>
<div class="kaart">...</div>
<footer id="contact">...</footer>
```

CSS
{: .bestandsnaam}

```css
.kaart {
  padding: 20px;
}
#contact {
  background-color: navy;
}
```

## Springen naar een plek op je pagina

Een link met een hekje gaat niet naar een andere pagina, maar naar een plek op dezelfde pagina. Zo'n link heet een **ankerlink**.
{: .sub}

1. **Geef het doel een id.** Bijvoorbeeld je footer: `<footer id="contact">`. De naam verzin je zelf.
2. **Verwijs ernaar met een hekje.** In de link schrijf je `href="#contact"`. Dat hekje zegt: blijf op deze pagina.
3. **Het hekje staat niet in je HTML-id.** In de HTML: `id="contact"`. In de link en in je CSS: `#contact`. Net als bij de punt van een class.

```html
<header>
  <a href="#contact">Mail mij</a>
</header>

<footer id="contact">
  <p>sam@mail.nl</p>
</footer>
```

!!! tip "Zie je niks gebeuren?"
    Springen kan alleen als je pagina langer is dan je scherm. Zet er tijdelijk wat extra alinea's in en probeer het opnieuw.

??? check "Check: id en ankerlinks"
    **1. Hoe schrijf je in CSS een regel voor `id="contact"`?**

    - A. `.contact { }`
    - B. `#contact { }`
    - C. `contact { }`
    - D. `id=contact { }`

    **2. Wat doet `<a href="#contact">`?**

    - A. Opent een nieuwe pagina
    - B. Springt naar het element met dat id
    - C. Maakt de tekst blauw
    - D. Koppelt je CSS

    ??? antwoord "Bekijk de antwoorden"
        **1. B – `#contact { }`.** Een id herken je in CSS aan het hekje. Met een punt zoekt de browser naar een class, en die heet hier anders.

        **2. B – springt naar het element met dat id.** Een href zonder hekje gaat naar een ander bestand. Met een hekje blijf je op dezelfde pagina en scrollt de browser erheen.

!!! opdracht "4. Maak een link die naar je footer springt"
    Ongeveer 10 minuten · Je werkt in: `opdracht-4`
    {: .meta}

    1. Kopieer `opdracht-3` naar een nieuwe map `opdracht-4`.
    2. Geef je `<footer>` het id contact.
    3. Zet in je header een link: `<a href="#contact">Mail mij</a>`.
    4. Maak in style.css een regel `#contact` met een eigen achtergrondkleur.
    5. Maak je pagina langer met een paar extra alinea's.
    6. Klik op de link en kijk of de pagina naar beneden springt.

    ??? hint "Codehint (niet het antwoord)"
        ```html
        <a href="#contact">Mail mij</a>

        <footer id="contact">
          ...
        </footer>
        ```
        ```css
        #contact { padding: 30px; }
        ```

    !!! klaar "Klaar als..."
        Je klikt bovenaan op Mail mij en je komt onderaan bij je footer uit. Gebeurt er niets? Dan past je hele pagina nog op één scherm.

=== blok-5 | Een tweede pagina
## Een site is meer dan één bestand

Elke pagina van je site is een eigen .html-bestand.
{: .sub}

```text
opdracht-5/
   index.html
   hobbys.html
   contact.html
   style.css
```

1. **index.html is je startpagina.** Die naam is geen toeval: een browser opent index.html automatisch als eerste.
2. **Elke pagina een eigen naam:** hobbys.html, contact.html. Allemaal in dezelfde map als je index.html.
3. **Kleine letters, geen spaties.** Gebruik een streepje: mijn-hobbys.html. Geen accenten, geen hoofdletters en geen tekens als ' of &.

!!! tip "Waarom geen spaties?"
    Een webadres kan niet tegen spaties. `mijn hobbys.html` wordt op internet `mijn%20hobbys.html` en dat gaat vroeg of laat fout.

## Linken en één style.css

Naar je eigen pagina linken is makkelijker dan naar internet.
{: .sub}

Linken naar je eigen pagina, en naar een andere website
{: .bestandsnaam}

```html
<a href="hobbys.html">Mijn hobby's</a>
<a href="https://nu.nl">Het nieuws</a>
```

In de head van élke pagina
{: .bestandsnaam}

```html
<head>
  <meta charset="UTF-8">
  <title>Hobby's</title>
  <link rel="stylesheet" href="style.css">
</head>
```

1. **Eigen bestand? Alleen de naam.** Staat het bestand in dezelfde map, dan is de bestandsnaam genoeg. Geen https:// en geen www ervoor.
2. **Wij werken met één style.css.** In deze cursus koppel je één CSS-bestand aan al je pagina's. Verander je een kleur, dan verandert hij meteen op alle pagina's. Het is geen wet: bij een grote site, of als één pagina een heel eigen opmaak krijgt, kun je ook meerdere CSS-bestanden maken.

??? check "Check: een tweede pagina"
    **1. Hoe link je naar hobbys.html in dezelfde map?**

    - A. `href="www.hobbys.html"`
    - B. `href="hobbys.html"`
    - C. `src="hobbys.html"`
    - D. `href="#hobbys"`

    **2. Hoeveel style.css-bestanden heb je nodig voor drie pagina's?**

    - A. Drie, één per pagina
    - B. Eén, gekoppeld in elke head
    - C. Geen enkele
    - D. Eén per map

    ??? antwoord "Bekijk de antwoorden"
        **1. B – `href="hobbys.html"`.** Voor een bestand in dezelfde map is de naam genoeg. src gebruik je bij een plaatje, niet bij een link. Met een hekje blijf je op dezelfde pagina.

        **2. B – één, gekoppeld in elke head.** Je maakt één style.css en zet in elke pagina dezelfde link-regel in de head. Zo zien al je pagina's er hetzelfde uit.

!!! opdracht "5. Maak je tweede pagina"
    Ongeveer 10 minuten · Je werkt in: `opdracht-5`
    {: .meta}

    1. Kopieer `opdracht-4` naar een nieuwe map `opdracht-5`.
    2. Maak een nieuw bestand hobbys.html. Typ ! en druk op Tab.
    3. Koppel style.css in de head van hobbys.html.
    4. Zet op hobbys.html een `<h1>` en je lijstje met drie hobby's.
    5. Zet op index.html een link naar hobbys.html.
    6. Zet op hobbys.html een link terug naar index.html.

    ??? hint "Codehint (niet het antwoord)"
        ```html
        <a href="hobbys.html">Mijn hobby's</a>

        <a href="index.html">Terug</a>
        ```

    !!! klaar "Klaar als..."
        Je klikt heen en weer tussen je twee pagina's, en ze hebben allebei dezelfde achtergrondkleur. Is de tweede pagina wit? Dan mist de link-regel in de head.

=== blok-6 | Paden
## Waar staat dat bestand?

Een **pad** is de route van je HTML-bestand naar het bestand dat je zoekt.
{: .sub}

```text
opdracht-6/
   index.html
   hobbys.html
   style.css
   images/
      foto.jpg
      logo.png
```

| Waar staat het? | Zo schrijf je het pad | Uitleg |
|---|---|---|
| In dezelfde map | `href="style.css"` | Alleen de naam, want style.css staat ernaast. |
| Een map naar beneden | `src="images/foto.jpg"` | Eerst de mapnaam, dan een schuine streep, dan het bestand. |
| Een map naar boven | `src="../logo.png"` | Twee puntjes en een streep: ga één map omhoog. Die heb je pas nodig als je bestanden in verschillende mappen staan. |

!!! let-op "Let op de richting"
    Het is een schuine streep vooruit: `/` en niet `\`. Op je toetsenbord zit die naast de rechter Shift.

## Waarom je plaatje niet laadt

Er zijn zes bekende oorzaken. Je ziet ze allemaal hetzelfde: een leeg vlak met je alt-tekst.
{: .sub}

| # | Oorzaak | Oplossing |
|---|---|---|
| 1 | Een hoofdletter te veel | `Foto.JPG` is voor de browser iets anders dan `foto.jpg`. |
| 2 | Een spatie in de naam | `mijn foto.jpg` werkt niet. Maak er `mijn-foto.jpg` van. |
| 3 | De map vergeten | `src="foto.jpg"` terwijl hij in images staat. Het moet `images/foto.jpg` zijn. |
| 4 | De streep de verkeerde kant op | `images\foto.jpg` werkt niet. Het is `images/foto.jpg`. |
| 5 | Het bestand staat er niet | Hij staat nog in je map Downloads. Sleep hem eerst naar je opdrachtmap. |
| 6 | Je ziet het .jpg niet staan | Windows verbergt dat stukje soms. Zet het aan in Verkenner bij Beeld > Bestandsnaamextensies. |

!!! tip "Laat VS Code het voor je typen"
    Typ `src="` en druk daarna op Ctrl + Spatie. VS Code laat zien welke bestanden en mappen er echt zijn. Kies je er een, dan is het pad altijd goed.

??? check "Check: paden"
    **1. Je foto staat in de map images. Wat zet je in src?**

    - A. `foto.jpg`
    - B. `images/foto.jpg`
    - C. `images\foto.jpg`
    - D. `../images/foto.jpg`

    **2. Wat betekent `../` aan het begin van een pad?**

    - A. Ga één map omlaag
    - B. Ga naar de hoofdmap
    - C. Ga naar internet
    - D. Ga één map omhoog

    ??? antwoord "Bekijk de antwoorden"
        **1. B – `images/foto.jpg`.** Eerst de mapnaam, dan een schuine streep vooruit, dan het bestand. De backslash werkt niet op het web. `../` zou je juist uit de map halen.

        **2. D – ga één map omhoog.** Twee puntjes betekenen: één map terug. Dat heb je nodig als je HTML-bestand in een andere map staat dan het bestand dat je zoekt.

!!! opdracht "6. Zet je foto in een eigen map"
    Ongeveer 10 minuten · Je werkt in: `opdracht-6`
    {: .meta}

    1. Kopieer `opdracht-5` naar een nieuwe map `opdracht-6`.
    2. Maak in `opdracht-6` een map images.
    3. Zet een foto in die map. Kleine letters, geen spaties in de naam.
    4. Toon de foto op index.html met `<img>` en een alt-tekst.
    5. Zie je alleen je alt-tekst? Loop het lijstje 'Waarom je plaatje niet laadt' hierboven af.
    6. Geef de foto in style.css een border-radius van 8px.

    ??? hint "Codehint (niet het antwoord)"
        ```html
        <img src="images/foto.jpg" alt="Foto van Sam">
        ```
        ```css
        img {
          border-radius: 8px;
        }
        ```

    !!! klaar "Klaar als..."
        Je foto staat op de pagina, terwijl het bestand netjes in de map images zit en niet los in je opdrachtmap.

=== blok-7 | De menubalk
## Een menu is een lijstje met links

Drie tags die je allemaal al kent, in elkaar gezet.
{: .sub}

1. **`<nav>` zegt: dit is het menu.** De doos eromheen. Hierin zet je je hele menu.
2. **`<ul>` is het lijstje.** Precies hetzelfde lijstje als bij je hobby's. Straks halen we de bolletjes weg.
3. **In elke `<li>` een `<a>`.** Elke regel van het lijstje is een link naar een andere pagina van je site.

```html
<nav>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="hobbys.html">Hobby's</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>
</nav>
```

```demo titel="Zonder CSS ziet je menu eruit als een gewoon lijstje met bolletjes. Dat is goed."
<nav><ul><li><a href="#">Home</a></li><li><a href="#">Hobby's</a></li><li><a href="#">Contact</a></li></ul></nav>
```

!!! onthoud "Op elke pagina precies hetzelfde"
    Anders raakt je bezoeker de weg kwijt. Kopieer je nav dus letterlijk naar je andere pagina's.

## Laat zien waar je bent

Eén extra class maakt duidelijk welke pagina open is. Het enige verschil tussen de pagina's is waar `class="actief"` staat. De rest is letterlijk gelijk.
{: .sub}

index.html
{: .bestandsnaam}

```html
<nav>
  <ul>
    <li><a href="index.html" class="actief">Home</a></li>
    <li><a href="hobbys.html">Hobby's</a></li>
  </ul>
</nav>
```

hobbys.html
{: .bestandsnaam}

```html
<nav>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="hobbys.html" class="actief">Hobby's</a></li>
  </ul>
</nav>
```

!!! tip "Werkvolgorde"
    Kopieer eerst je nav naar alle pagina's. Pas daarna verplaats je op elke pagina de class. Zo vergeet je niets.

??? check "Check: de menubalk"
    **1. Wat zet je binnen een `<li>` van je menu?**

    - A. Een `<ul>`
    - B. Een `<a>`
    - C. Een `<nav>`
    - D. Een `<div>`

    **2. Waarom geef je één link de class actief?**

    - A. Anders werkt de link niet
    - B. Om te laten zien op welke pagina je bent
    - C. Om de link te openen
    - D. Dat moet van HTML

    ??? antwoord "Bekijk de antwoorden"
        **1. B – een `<a>`.** De li is de regel van het lijstje, en de link staat daarin. De nav en de ul zitten er juist omheen.

        **2. B – om te laten zien op welke pagina je bent.** De link werkt ook zonder die class prima. Hij is er alleen zodat jij hem in je CSS een andere kleur kunt geven.

!!! opdracht "7. Bouw je menu op alle pagina's"
    Ongeveer 15 minuten · Je werkt in: `opdracht-7`
    {: .meta}

    1. Kopieer `opdracht-6` naar een nieuwe map `opdracht-7`.
    2. Maak een derde pagina contact.html en koppel style.css.
    3. Bouw op index.html een `<nav>` met een ul en drie li's met links.
    4. Kopieer die hele nav naar hobbys.html en contact.html.
    5. Geef op elke pagina de juiste link de class actief.
    6. Test: klik vanaf elke pagina naar elke andere pagina.

    ??? hint "Codehint (niet het antwoord)"
        ```html
        <nav>
          <ul>
            <li><a href="index.html" class="actief">Home</a></li>
          </ul>
        </nav>
        ```

    !!! klaar "Klaar als..."
        Je kunt vanaf elke pagina naar elke andere pagina klikken en je komt nooit vast te zitten. Het menu ziet er nog uit als een lijstje met bolletjes, dat is goed.

=== blok-8 | Menu opmaken
## Van lijstje naar balk

Met drie regels CSS wordt je lijstje met bolletjes een balk.
{: .sub}

1. **`list-style: none`** haalt de bolletjes voor je li's weg.
2. **`padding: 0`** zet de inspringing uit. De browser springt een lijstje standaard in.
3. **`display: inline-block`** zet de li's naast elkaar in plaats van onder elkaar.

```css
nav ul {
  list-style: none;
  padding: 0;
}

nav li {
  display: inline-block;
  margin-right: 15px;
}
```

!!! let-op "Let op die spatie"
    `nav ul` betekent: elke ul die binnen een nav staat. Zo raak je je lijstje met hobby's niet aan. Schrijf je alleen `ul`, dan pak je álle lijstjes.

## Kleur, hover en de actieve pagina

Nu maak je van de links echte knoppen in de balk.
{: .sub}

1. **`text-decoration: none`** haalt de streep onder je links weg, net als bij de knop van module 1.
2. **padding op de link zelf.** Daardoor wordt het klikvlak groter en lijkt het een knop.
3. **`:hover` en `.actief`.** hover is hoe het eruitziet als je muis erover gaat. actief is de pagina waar je nu bent.

```css
nav a {
  color: white;
  text-decoration: none;
  padding: 10px 15px;
}

nav a:hover {
  background-color: #2965F1;
}

.actief {
  background-color: #E44D26;
}
```

```demo titel="Probeer het: beweeg je muis over Hobby's of Contact"
<style>nav{background:#1B1F3B;padding:10px}nav ul{list-style:none;padding:0;margin:0}nav li{display:inline-block;margin-right:15px}nav a{color:#fff;text-decoration:none;padding:10px 15px}nav a:hover{background-color:#2965F1}.actief{background-color:#E44D26}</style>
<nav><ul><li><a class="actief" href="#">Home</a></li><li><a href="#">Hobby's</a></li><li><a href="#">Contact</a></li></ul></nav>
```

!!! tip "Probeer het meteen uit"
    Beweeg met je muis over je menu zonder te klikken. Verandert de kleur? Dan werkt je hover.

??? check "Check: menu opmaken"
    **1. Waarmee haal je de bolletjes uit je menu?**

    - A. `text-decoration: none`
    - B. `list-style: none`
    - C. `display: none`
    - D. `padding: 0`

    **2. Wat betekent de spatie in `nav a { }`?**

    - A. nav én alle links
    - B. Alle links binnen een nav
    - C. Een link met class nav
    - D. Niets, dat is een typefout

    ??? antwoord "Bekijk de antwoorden"
        **1. B – `list-style: none`.** text-decoration haalt de streep onder een link weg. `display: none` laat het hele menu verdwijnen. `padding: 0` haalt alleen de inspringing weg.

        **2. B – alle links binnen een nav.** Een spatie tussen twee selectors betekent binnen. `nav a` pakt dus wel je menulinks, maar niet de links in je footer.

!!! opdracht "8. Maak van je lijstje een menubalk"
    Ongeveer 15 minuten · Je werkt in: `opdracht-8`
    {: .meta}

    1. Kopieer `opdracht-7` naar een nieuwe map `opdracht-8`.
    2. Geef nav een achtergrondkleur en `padding: 10px`.
    3. Haal met list-style en padding de bolletjes en de inspringing weg.
    4. Zet de li's naast elkaar met `display: inline-block`.
    5. Haal de streep onder de links weg en geef ze een kleur.
    6. Maak een regel `nav a:hover` en een regel `.actief` met een eigen kleur.

    ??? hint "Codehint (niet het antwoord)"
        ```css
        nav ul {
          list-style: none;
          padding: 0;
        }
        nav li {
          display: inline-block;
        }
        ```

    !!! klaar "Klaar als..."
        Bovenaan elke pagina staat een gekleurde balk met je drie links naast elkaar. Je ziet aan de kleur welke pagina open is, en de links reageren als je er met je muis overheen gaat.

=== eindopdracht | Eindopdracht
!!! opdracht eind "Maak je eigen mini-site"
    Je werkt in een nieuwe map `eindopdracht`, met drie pagina's en één style.css.
    {: .meta}

    **Op je site staat:**

    - Map `eindopdracht` met index.html, hobbys.html, contact.html en style.css
    - Een map images met minstens één foto erin
    - Op elke pagina dezelfde nav met drie links naast elkaar
    - De class actief op de link van de pagina waar je bent
    - header, main en footer op elke pagina
    - Minstens twee kaarten met een div of een section
    - Een foto met alt-tekst uit de map images
    - Een link met een hekje die naar je footer met een id springt
    {: .checklist}

    !!! tip "Al klaar?"
        Geef je kaarten een schaduw met `box-shadow: 0 2px 8px gray;`. Of zet je footer-tekst in het midden met `text-align: center;`.

Alles wat je nodig hebt, heb je in de mini-opdrachten al een keer gemaakt. Kijk gerust terug in je eigen mappen.

## Inleveren

Zip de hele map `les2-jouwnaam`. Daarin zitten `opdracht-1` tot en met `opdracht-8` en de map `eindopdracht`. Noem de zip `les2-jouwnaam.zip`.

**Checklist: vink af voordat je inlevert**

- Map `les2-jouwnaam` met `opdracht-1` tot en met `opdracht-8`
- Map `eindopdracht` met drie html-bestanden
- Eén style.css, gekoppeld in de head van elke pagina
- Map images met je foto erin
- Op elke pagina precies dezelfde nav
- Alle map- en bestandsnamen met kleine letters
- Alles opgeslagen met Ctrl + S
- Elke pagina opent goed met Live Server
{: .checklist}

!!! tip "Zo maak je een zip"
    Rechtsklik op de map `les2-jouwnaam` en kies **Comprimeren naar > ZIP-bestand**. Op oudere Windows: **Kopiëren naar > Gecomprimeerde map**.

!!! tip "Werk je thuis?"
    Je hebt alleen VS Code en Chrome nodig. Kom je er niet uit, schrijf je vraag op en neem hem mee naar de les.

Twijfel je of iets af is? Kijk bij **Klaar als...** bij die opdracht.

=== werkt-het-niet | Werkt het niet?
Met meerdere bestanden gaat het vaker mis op dezelfde zes plekken.
{: .sub}

1. **Heb je alles opgeslagen?** Ctrl + S werkt maar in één tabblad tegelijk.
2. **Klopt de bestandsnaam precies?** hobbys.html is iets anders dan Hobbys.html.
3. **Staat style.css in elke head?** Een witte pagina betekent bijna altijd: link-regel vergeten.
4. **Klopt het pad naar je foto?** `images/foto.jpg`, met een schuine streep vooruit.
5. **Is elke tag gesloten en genest?** Kijk of elke `<tag>` ook een `</tag>` heeft. Shift + Alt + F helpt.
6. **Puntkomma's in je CSS?** Vergeet je er één, dan doet ook de regel eronder vaak niets.

!!! tip "Nog steeds niet?"
    Rechtsklik in Chrome en kies Inspecteren. Vraag daarna je buurman, en dan je docent.

=== naslag | Naslag
## HTML

Alles van module 2 op een rij. Kijk hier eerst als je iets kwijt bent.
{: .sub}

De tags die erbij zijn gekomen
{: .bestandsnaam}

```html
<div class="kaart">...</div>
<header>...</header>
<nav>...</nav>
<main>...</main>
<section>...</section>
<footer id="contact">...</footer>

<a href="hobbys.html">Hobby's</a>
<a href="#contact">Mail mij</a>
<img src="images/foto.jpg" alt="Foto">
```

Een complete menubalk
{: .bestandsnaam}

```html
<nav>
  <ul>
    <li><a href="index.html" class="actief">Home</a></li>
    <li><a href="hobbys.html">Hobby's</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>
</nav>
```

!!! onthoud "Onthoud"
    Een class mag zo vaak je wilt. Elk id mag maar één keer per pagina, maar je mag wel meerdere verschillende id's gebruiken. In je HTML staat er geen punt en geen hekje bij, in je CSS wel.

## CSS

Nieuw in module 2
{: .bestandsnaam}

```css
#contact { }
nav ul { }
nav a:hover { }

list-style: none;
padding: 0;
display: inline-block;
margin-right: 15px;
box-shadow: 0 2px 8px gray;
```

Een complete menubalk in CSS
{: .bestandsnaam}

```css
nav {
  background-color: #1B1F3B;
  padding: 10px;
}
nav ul {
  list-style: none;
  padding: 0;
}
nav li { display: inline-block; }
nav a {
  color: white;
  text-decoration: none;
  padding: 10px 15px;
}
.actief { background-color: #E44D26; }
```

!!! onthoud "Punt, hekje of niets"
    `.kaart` is een class, `#contact` is een id, en `nav` is gewoon een tagnaam. Een spatie ertussen betekent binnen.

!!! tip "Koppelen blijft hetzelfde"
    `<link rel="stylesheet" href="style.css">` in de head van élke pagina, en style.css in dezelfde map.

=== woordenlijst | Woordenlijst
De Engelse woorden van module 2, met de Nederlandse vertaling en uitleg in gewone taal. De woorden van module 1 staan in de woordenlijst van module 1.
{: .sub}

| Engels | Nederlands | Uitleg |
|---|---|---|
| **div** (division) | vak, deel | doos zonder betekenis om te groeperen |
| **nesting / nested** | nesten / genest | een tag in een andere tag |
| **indent** | inspringen | code naar rechts zetten met Tab |
| **format** | opmaken | code netjes rechtzetten (Prettier) |
| **semantic** | betekenisvol | de tag zegt wat het is |
| **header** | kopgedeelte | bovenkant van je pagina |
| **nav** (navigation) | navigatie | het menu |
| **main** | hoofdinhoud | waar het op de pagina om gaat |
| **section** | deel, sectie | stuk pagina met een eigen kopje |
| **footer** | voettekst | onderkant van je pagina |
| **id** (identifier) | kenmerk | naam die maar één keer per pagina mag |
| **anchor link** | ankerlink | link met een hekje, blijft op de pagina |
| **path** | pad | route naar een bestand |
| **subfolder** | submap | map in een map, zoals images |
| **index** | inhoudsopgave | index.html is de startpagina |
| **menu bar** | menubalk | balk met links naar je pagina's |
| **list-style** | lijststijl | wel of geen bolletjes |
| **inline-block** | op één regel, als blok | zet elementen naast elkaar |
| **hover** | zweven | hoe iets eruitziet onder je muis |
| **active** | actief | de pagina waar je nu bent |
| **shadow** | schaduw | box-shadow onder een element |
