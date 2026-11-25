---
nr: 5
titel: JavaScript: je pagina reageert
kort: Je bouwt het spel Raad het getal op een nieuwe pagina in je eigen site.
tags: let | querySelector | addEventListener | if
---

=== start | Start
## Dit ga je maken

Aan het eind van deze module staat er een nieuwe pagina spel.html op je site, met een spel dat echt werkt. De computer kiest een geheim getal van 1 tot 100. Jij raadt, en de pagina zegt of het hoger of lager is.

| Wat zie je? | Hoe doe je dat? |
|---|---|
| Een vakje en een knop | een input en addEventListener |
| Hoger of lager | if, else if en else |
| Een geheim getal en een teller | Math.random en let |
| Groen bij goed, spelregels uitklappen | classList |

```demo titel="Zo kan je spel eruitzien. Probeer het maar."
<style>
body{font-family:Arial,sans-serif;color:#1B1F3B;margin:0;padding:14px;font-size:15px;background:#fff}
.kaart{background:#E8EAF6;border-radius:10px;padding:14px 16px}
.kaart h2{margin:0 0 6px;font-size:19px}.kaart p{margin:6px 0}
button{padding:7px 14px;border:0;border-radius:6px;background:#2965F1;color:#fff;font-size:15px;cursor:pointer;font-family:Arial,sans-serif}
button.donkerknop{background:#1B1F3B}
input{width:90px;padding:6px;font-size:15px;border:1px solid #9aa0c3;border-radius:5px}
.rij{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
#melding{font-weight:bold;min-height:20px}
.goed{color:#1E8E4E}.fout{color:#E44D26}
.verborgen{display:none}
small{color:#5b6075}
.label{font-size:12px;color:#5b6075;margin:0 0 4px}
.twee{display:flex;gap:14px}.twee>div{flex:1}
</style><div class="kaart"><h2>Raad het getal</h2><p>Ik denk aan een getal van 1 tot 100.</p>
<div class="rij"><input id="gok" type="number" min="1" max="100" placeholder="1 - 100"><button id="raad">Raad!</button><button id="opnieuw" class="donkerknop">Opnieuw</button></div>
<p id="melding"></p><small>Pogingen: <span id="teller">0</span></small></div><script>
const invoer = document.querySelector("#gok");
const melding = document.querySelector("#melding");
const teller = document.querySelector("#teller");
let geheim = Math.floor(Math.random() * 100) + 1;
let pogingen = 0;
document.querySelector("#raad").addEventListener("click", function () {
  const gok = Number(invoer.value);
  pogingen = pogingen + 1;
  teller.textContent = pogingen;
  melding.classList.remove("goed");
  melding.classList.remove("fout");
  if (invoer.value === "") { melding.textContent = "Vul eerst een getal in."; }
  else if (gok > geheim) { melding.textContent = "Lager!"; melding.classList.add("fout"); }
  else if (gok < geheim) { melding.textContent = "Hoger!"; melding.classList.add("fout"); }
  else { melding.textContent = "Goed geraden!"; melding.classList.add("goed"); }
});
document.querySelector("#opnieuw").addEventListener("click", function () {
  geheim = Math.floor(Math.random() * 100) + 1;
  pogingen = 0; teller.textContent = pogingen;
  melding.textContent = ""; invoer.value = "";
  melding.classList.remove("goed"); melding.classList.remove("fout");
});
</script>
```

## Dit kun je al

Alles in deze module bouwt verder op wat je al gemaakt hebt.

- **HTML:** Drie pagina's (index, hobbys en contact) met een menu, een header, kaarten en een footer. Je weet wat een id en een class zijn.
- **CSS:** Kleuren, een lettertype, schaduw en :hover. Met display: flex en gap zet je dingen naast elkaar.
- **DevTools:** Met Elements en Styles kijk je hoe je pagina gemaakt is. Het tabblad Console heb je al een keer gezien.

!!! tip "Iets kwijt?"
    De naslag van module 1 tot en met 4 mag je er de hele tijd bij houden. Vooral de selectors heb je nodig: # voor een id en . voor een class. Die gebruik je in JavaScript ook.

## Zo werk je

In opdracht 1 maak je in Documenten de map module5-jouwnaam, met daarin de mappen opdracht-1 tot en met opdracht-8 en eindopdracht. In opdracht-1 zet je een kopie van je eindopdracht van module 4. Bij elke volgende opdracht kopieer je alle bestanden en mappen uit de vorige opdrachtmap naar de volgende. Er komen twee nieuwe bestanden bij: spel.html en script.js. In script.js schrijf je je JavaScript.

Elk blok werkt hetzelfde: eerst de **uitleg**, dan een **check** om te kijken of je het snapt, en daarna een **mini-opdracht** die je meteen in VS Code maakt.

| Blok | Onderwerp |
|---|---|
| 1 | Kennismaken: wat is JavaScript, script.js koppelen, de Console |
| 2 | Variabelen: const en let, tekst en getallen |
| 3 | Vind en verander: querySelector en textContent |
| 4 | Een knop die werkt: addEventListener |
| 5 | Classes aan en uit: classList en toggle |
| 6 | Invoer lezen: een invoerveld, value en Number() |
| 7 | Hoger of lager: if, else if en else |
| 8 | Toeval, tellen en opnieuw: Math.random en een teller |

!!! onthoud "Vergelijk het met een huis"
    HTML zijn de muren, CSS is de verf en JavaScript is de elektriciteit: daarmee gaat er iets gebeuren als je op een knop drukt.

=== blok-1 | Kennismaken
## Je nieuwe gereedschap: de Console

Hier zie je wat je JavaScript doet, en wat er misgaat.
{: .sub}

1. **Open de DevTools.** Open je pagina met Live Server en druk op F12.
2. **Klik op Console.** Bovenin staan tabbladen. Console staat naast Elements. Zie je hem niet? Klik op &gt;&gt; om meer tabbladen te zien.
3. **Lees je berichten.** Wat je met console.log opschrijft, staat hier. Rechts staat in welk bestand en op welke regel.
4. **Rood is een fout.** Een rode regel betekent: hier stopt je JavaScript. Lees wat er staat en klik rechts op script.js:2. Chrome laat dan de regel zien.
5. **Maak hem leeg.** Met het rondje met de streep erdoor, linksboven in de Console, haal je oude berichten weg.

```demo titel="Zo ziet de Console eruit: een bericht en een rode fout op regel 2"
<style>
.dt{font-family:Consolas,monospace;font-size:13px;border:1px solid #c9ccd8;border-radius:6px;overflow:hidden;background:#fff}
.dt .tabs{background:#f1f3f4;border-bottom:1px solid #c9ccd8;padding:5px 8px;font-family:Arial,sans-serif;font-size:12px;color:#5f6368}
.dt .tabs b{color:#1a73e8;border-bottom:2px solid #1a73e8;padding-bottom:3px;margin:0 8px}
.dt .r{display:flex;justify-content:space-between;gap:10px;padding:4px 10px;border-bottom:1px solid #eee}
.dt .r u{color:#5f6368;text-decoration:underline}
.dt .r.fout{background:#fdeceb;color:#c5221f;border-color:#f6c6c2}
.dt .r.in{color:#1a73e8}
</style><div class="dt"><div class="tabs">Elements <b>Console</b> Sources</div><div class="r"><span>Hallo vanuit script.js!</span><u>script.js:1</u></div><div class="r fout"><span>&#9940; Uncaught ReferenceError: consol is not defined</span><u>script.js:2</u></div></div>
```

!!! tip "Zet hem altijd open"
    Werk je met JavaScript, laat dan de Console de hele tijd openstaan. Dan zie je een fout meteen.

!!! let-op "Typfout = fout"
    consol in plaats van console is al genoeg voor een rode melding. JavaScript let op elke letter, ook op hoofdletters.

## Wat is JavaScript?

HTML en CSS maken je pagina. JavaScript laat hem reageren..
{: .sub}

1. **Vergelijk het met een huis.** HTML zijn de muren, CSS is de verf en JavaScript is de elektriciteit. Pas met elektriciteit gaat er een lamp aan als je op de knop drukt.
2. **Het werkt in de browser.** Chrome leest je JavaScript en voert het uit, regel voor regel, van boven naar beneden. Je hebt geen extra programma nodig.
3. **Een eigen bestand.** Je CSS staat in style.css. Je JavaScript zet je in een eigen bestand: script.js.

```demo titel="Dezelfde knop met HTML, met CSS en met JavaScript. Klik maar op de derde."
<style>
body{font-family:Arial,sans-serif;color:#1B1F3B;margin:0;padding:14px;font-size:15px;background:#fff}
.kaart{background:#E8EAF6;border-radius:10px;padding:14px 16px}
.kaart h2{margin:0 0 6px;font-size:19px}.kaart p{margin:6px 0}
button{padding:7px 14px;border:0;border-radius:6px;background:#2965F1;color:#fff;font-size:15px;cursor:pointer;font-family:Arial,sans-serif}
button.donkerknop{background:#1B1F3B}
input{width:90px;padding:6px;font-size:15px;border:1px solid #9aa0c3;border-radius:5px}
.rij{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
#melding{font-weight:bold;min-height:20px}
.goed{color:#1E8E4E}.fout{color:#E44D26}
.verborgen{display:none}
small{color:#5b6075}
.label{font-size:12px;color:#5b6075;margin:0 0 4px}
.twee{display:flex;gap:14px}.twee>div{flex:1}
</style><div class="twee">
<div><p class="label">Alleen HTML</p><button style="all:revert">Klik mij</button></div>
<div><p class="label">HTML + CSS</p><button>Klik mij</button></div>
<div><p class="label">HTML + CSS + JavaScript</p><button id="k">Klik mij</button><p id="m" style="font-weight:bold;margin:6px 0;min-height:20px"></p></div>
</div><script>document.querySelector("#k").addEventListener("click", function () { document.querySelector("#m").textContent = "Je hebt geklikt!"; });</script>
```

!!! onthoud "Eerst bouwen, dan laten reageren"
    Je JavaScript werkt altijd samen met je HTML. In je HTML zet je de knop. In script.js zeg je wat er gebeurt als iemand erop klikt.

## script.js koppelen

Net als style.css koppel je script.js in de head.
{: .sub}

1. **Maak script.js.** Maak in dezelfde map als spel.html een nieuw bestand script.js.
2. **Koppel het in de head.** Zet in de head van spel.html een script-regel met src="script.js". Vergeet de sluittag &lt;/script&gt; niet.
3. **defer betekent: wacht even.** Met defer voert Chrome je script pas uit als de hele pagina geladen is. Anders zoekt je script naar knoppen die er nog niet zijn.

spel.html
{: .bestandsnaam}

```html
<head>
  <link rel="stylesheet" href="style.css">
  <script src="script.js" defer></script>
</head>
```

script.js
{: .bestandsnaam}

```js
console.log("Hallo vanuit script.js!");
```

```demo titel="In de Console zie je het bericht uit script.js"
<style>
.dt{font-family:Consolas,monospace;font-size:13px;border:1px solid #c9ccd8;border-radius:6px;overflow:hidden;background:#fff}
.dt .tabs{background:#f1f3f4;border-bottom:1px solid #c9ccd8;padding:5px 8px;font-family:Arial,sans-serif;font-size:12px;color:#5f6368}
.dt .tabs b{color:#1a73e8;border-bottom:2px solid #1a73e8;padding-bottom:3px;margin:0 8px}
.dt .r{display:flex;justify-content:space-between;gap:10px;padding:4px 10px;border-bottom:1px solid #eee}
.dt .r u{color:#5f6368;text-decoration:underline}
.dt .r.fout{background:#fdeceb;color:#c5221f;border-color:#f6c6c2}
.dt .r.in{color:#1a73e8}
</style><div class="dt"><div class="tabs">Elements <b>Console</b> Sources</div><div class="r"><span>Hallo vanuit script.js!</span><u>script.js:1</u></div></div>
```

!!! tip "console.log is je controle"
    Met console.log("...") schrijf je een bericht in de Console. Zo kun je altijd even controleren of je script werkt. Bezoekers van je site zien dit niet.

??? check "Check: kennismaken"
    **1. Waar zet je de regel &lt;script src="script.js" defer&gt;&lt;/script&gt;?**

    - A. `In style.css`
    - B. `In de head van spel.html`
    - C. `In script.js zelf`
    - D. `Achter de </html>`

    **2. In de Console staat een rode regel. Wat betekent dat?**

    - A. Er zit een fout in je JavaScript
    - B. `Je bericht van console.log`
    - C. Je CSS is niet goed
    - D. Je pagina is helemaal klaar

    ??? antwoord "Bekijk de antwoorden"
        **1. B – `In de head van spel.html`.** Net als de link naar style.css staat de script-regel in de head. Door defer wacht Chrome tot de hele pagina klaar is. In style.css en script.js zelf hoort geen HTML, en achter &lt;/html&gt; mag niets meer staan.

        **2. A – Er zit een fout in je JavaScript.** Rood betekent een fout: daar stopt je JavaScript. Een gewoon bericht van console.log is zwart. Fouten in je CSS zie je niet in de Console, maar bij Styles (een streep of een geel driehoekje).

!!! opdracht "1. Maak je spelpagina en koppel script.js"
    Ongeveer 15 minuten · Je werkt in: `opdracht-1`
    {: .meta}

    1. Maak in Documenten een map module5-jouwnaam. Maak daarin de mappen opdracht-1 tot en met opdracht-8 en de map eindopdracht.
    2. Kopieer alle bestanden en mappen uit de map eindopdracht van module 4 naar opdracht-1.
    3. Maak een kopie van contact.html en noem die spel.html. Haal alles uit de main weg en zet er een h2 met de tekst Raad het getal in.
    4. Zet in het menu van al je pagina's een link Spel naar spel.html. Op spel.html krijgt die link de class actief.
    5. Maak een bestand script.js naast style.css. Koppel het in de head van spel.html, met defer.
    6. Zet in script.js een console.log met een eigen bericht. Open spel.html met Live Server, druk op F12 en kijk in de Console.

    ??? hint "Codehint (niet het antwoord)"
        ```js
        <script src="..." defer></script>

        console.log("...");
        ```

    !!! klaar "Klaar als..."
        Op elke pagina staat Spel in het menu. Op spel.html staat je kop, en in de Console staat jouw bericht. Er staan geen rode fouten.

=== blok-2 | Variabelen
## Namen voor je waarden

Een variabele is een naam voor een waarde die je later weer gebruikt.
{: .sub}

1. **Een naam en een waarde.** Je geeft een waarde één keer een naam. Daarna gebruik je overal die naam. Het = teken betekent: krijgt de waarde. Het is geen vraag.
2. **const: de waarde blijft hetzelfde.** Gebruik const als de waarde niet meer verandert, zoals je naam. Probeer je het toch te veranderen, dan krijg je een rode fout.
3. **let: de waarde mag veranderen.** Gebruik let als de waarde later anders wordt, zoals een score of een aantal pogingen. Bij het veranderen schrijf je let niet nog een keer.

script.js
{: .bestandsnaam}

```js
const naam = "Sam";
let punten = 0;
console.log(naam);
console.log(punten);

punten = 10;
console.log(punten);
```

```demo titel="Eén regel in stukjes"
<style>
body{font-family:Arial,sans-serif;color:#1B1F3B;margin:0;padding:14px;font-size:15px;background:#fff}
.kaart{background:#E8EAF6;border-radius:10px;padding:14px 16px}
.kaart h2{margin:0 0 6px;font-size:19px}.kaart p{margin:6px 0}
button{padding:7px 14px;border:0;border-radius:6px;background:#2965F1;color:#fff;font-size:15px;cursor:pointer;font-family:Arial,sans-serif}
button.donkerknop{background:#1B1F3B}
input{width:90px;padding:6px;font-size:15px;border:1px solid #9aa0c3;border-radius:5px}
.rij{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
#melding{font-weight:bold;min-height:20px}
.goed{color:#1E8E4E}.fout{color:#E44D26}
.verborgen{display:none}
small{color:#5b6075}
.label{font-size:12px;color:#5b6075;margin:0 0 4px}
.twee{display:flex;gap:14px}.twee>div{flex:1}
</style><style>
.cl{display:flex;flex-wrap:wrap;gap:4px;align-items:flex-start}
.cl .st{display:flex;flex-direction:column;align-items:center;gap:6px}
.cl code{font-family:Consolas,monospace;font-size:17px;background:#1B1F3B;color:#fff;padding:6px 8px;border-radius:6px;border-bottom:4px solid}
.cl span{font-size:13px;font-weight:bold;text-align:center;max-width:130px}
</style><div class="cl"><div class="st"><code style="border-color:#E44D26">const</code><span style="color:#E44D26">soort</span></div><div class="st"><code style="border-color:#2965F1">naam</code><span style="color:#2965F1">de naam</span></div><div class="st"><code style="border-color:#5b6075">=</code><span style="color:#5b6075">krijgt</span></div><div class="st"><code style="border-color:#1E8E4E">"Sam"</code><span style="color:#1E8E4E">de waarde</span></div><div class="st"><code style="border-color:#5b6075">;</code><span style="color:#5b6075">einde</span></div></div><div style="height:12px"></div><style>
.dt{font-family:Consolas,monospace;font-size:13px;border:1px solid #c9ccd8;border-radius:6px;overflow:hidden;background:#fff}
.dt .tabs{background:#f1f3f4;border-bottom:1px solid #c9ccd8;padding:5px 8px;font-family:Arial,sans-serif;font-size:12px;color:#5f6368}
.dt .tabs b{color:#1a73e8;border-bottom:2px solid #1a73e8;padding-bottom:3px;margin:0 8px}
.dt .r{display:flex;justify-content:space-between;gap:10px;padding:4px 10px;border-bottom:1px solid #eee}
.dt .r u{color:#5f6368;text-decoration:underline}
.dt .r.fout{background:#fdeceb;color:#c5221f;border-color:#f6c6c2}
.dt .r.in{color:#1a73e8}
</style><div class="dt"><div class="tabs">Elements <b>Console</b> Sources</div><div class="r"><span>Sam</span><u>script.js:3</u></div><div class="r"><span>0</span><u>script.js:4</u></div><div class="r"><span>10</span><u>script.js:7</u></div></div>
```

!!! tip "Namen in camelCase"
    Een naam heeft geen spaties. Bestaat hij uit meer woorden, dan plak je ze aan elkaar en begint elk nieuw woord met een hoofdletter: geheimGetal, raadKnop. Dat heet camelCase, omdat de hoofdletters bulten zijn, net als bij een kameel.

## Tekst en getallen

JavaScript kent het verschil tussen tekst en een getal.
{: .sub}

1. **Tekst tussen aanhalingstekens.** Tekst zet je tussen aanhalingstekens: "Sam". Tekst heet in het Engels een string.
2. **Getallen zonder aanhalingstekens.** Met getallen kun je rekenen: + optellen, - aftrekken, \* keer en / delen.
3. **Plakken met +.** Zet je + tussen tekst, dan plakt JavaScript de stukken aan elkaar. Zo maak je een zin: "Hoi " + naam.

script.js
{: .bestandsnaam}

```js
const naam = "Sam";
const leeftijd = 17;

console.log(leeftijd + 1);
console.log("Hoi " + naam);
console.log("5" + 5);
```

```demo titel="Wat er in de Console komt"
<style>
.dt{font-family:Consolas,monospace;font-size:13px;border:1px solid #c9ccd8;border-radius:6px;overflow:hidden;background:#fff}
.dt .tabs{background:#f1f3f4;border-bottom:1px solid #c9ccd8;padding:5px 8px;font-family:Arial,sans-serif;font-size:12px;color:#5f6368}
.dt .tabs b{color:#1a73e8;border-bottom:2px solid #1a73e8;padding-bottom:3px;margin:0 8px}
.dt .r{display:flex;justify-content:space-between;gap:10px;padding:4px 10px;border-bottom:1px solid #eee}
.dt .r u{color:#5f6368;text-decoration:underline}
.dt .r.fout{background:#fdeceb;color:#c5221f;border-color:#f6c6c2}
.dt .r.in{color:#1a73e8}
</style><div class="dt"><div class="tabs">Elements <b>Console</b> Sources</div><div class="r"><span>18</span><u>script.js:4</u></div><div class="r"><span>Hoi Sam</span><u>script.js:5</u></div><div class="r"><span>55</span><u>script.js:6</u></div></div>
```

!!! let-op ""5" + 5 is geen 10"
    Is één van de twee tekst, dan wordt het samen tekst. "5" + 5 wordt dan "55". Dit kom je in blok 6 weer tegen bij een invoerveld.

??? check "Check: variabelen"
    **1. Het aantal pogingen wordt later groter. Hoe maak je die variabele?**

    - A. `const pogingen = 0;`
    - B. `let pogingen = 0;`
    - C. `change pogingen = 0;`
    - D. `pogingen == 0;`

    **2. Wat staat er in de Console na console.log("3" + 4); ?**

    - A. 7
    - B. 34
    - C. `"3" + 4`
    - D. Een rode fout

    ??? antwoord "Bekijk de antwoorden"
        **1. B – `let pogingen = 0;`.** De waarde verandert later, dus gebruik je let. Met const krijg je een rode fout zodra je de waarde verandert. change bestaat niet, en == vergelijkt alleen, het geeft geen waarde.

        **2. B – 34.** "3" staat tussen aanhalingstekens, dus het is tekst. Tekst + getal wordt samen tekst: 34. Er komt geen 7, want er wordt niet gerekend. Een fout is het ook niet: JavaScript plakt gewoon.

!!! opdracht "2. Maak je eerste variabelen"
    Ongeveer 10 minuten · Je werkt in: `opdracht-2`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit opdracht-1 naar opdracht-2.
    2. Maak in script.js een variabele met je eigen naam. Kies zelf of je const of let gebruikt.
    3. Maak een const geheim met het getal 42. Maak ook een variabele pogingen die begint bij 0. Die moet later kunnen veranderen.
    4. Schrijf met console.log een zin in de Console, zoals Hoi Sam. Plak daarvoor tekst en je naam aan elkaar.
    5. Maak pogingen daarna 1 en schrijf pogingen opnieuw in de Console.
    6. Probeer ook geheim te veranderen naar 50. Lees de rode fout in de Console. Haal die regel daarna weer weg.

    ??? hint "Codehint (niet het antwoord)"
        ```js
        const stad = "Utrecht";
        let score = 0;
        score = 5;
        console.log("Ik woon in " + ...);
        ```

    !!! klaar "Klaar als..."
        In de Console staan je zin met je naam, en daarna de getallen 0 en 1. Je hebt de rode fout gezien en weer opgelost.

=== blok-3 | Vind en verander
## Een element vinden

Eerst zoek je op je pagina het element dat je wilt veranderen.
{: .sub}

1. **Geef het element een id.** In je HTML geef je het element een id, bijvoorbeeld &lt;p id="melding"&gt;. Een id mag maar één keer op een pagina staan.
2. **Zoek het met querySelector.** document.querySelector("#melding") zoekt op de pagina het element met die id. Je gebruikt dezelfde selector als in CSS: # voor een id.
3. **Bewaar het in een const.** Je zet het gevonden element in een const. Dan hoef je het maar één keer te zoeken en kun je de naam steeds gebruiken.

spel.html
{: .bestandsnaam}

```html
<p id="melding">Ik denk aan een getal.</p>
```

script.js
{: .bestandsnaam}

```js
const melding = document.querySelector("#melding");
console.log(melding);
```

```demo titel="De zoekregel in stukjes"
<style>
body{font-family:Arial,sans-serif;color:#1B1F3B;margin:0;padding:14px;font-size:15px;background:#fff}
.kaart{background:#E8EAF6;border-radius:10px;padding:14px 16px}
.kaart h2{margin:0 0 6px;font-size:19px}.kaart p{margin:6px 0}
button{padding:7px 14px;border:0;border-radius:6px;background:#2965F1;color:#fff;font-size:15px;cursor:pointer;font-family:Arial,sans-serif}
button.donkerknop{background:#1B1F3B}
input{width:90px;padding:6px;font-size:15px;border:1px solid #9aa0c3;border-radius:5px}
.rij{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
#melding{font-weight:bold;min-height:20px}
.goed{color:#1E8E4E}.fout{color:#E44D26}
.verborgen{display:none}
small{color:#5b6075}
.label{font-size:12px;color:#5b6075;margin:0 0 4px}
.twee{display:flex;gap:14px}.twee>div{flex:1}
</style><style>
.cl{display:flex;flex-wrap:wrap;gap:4px;align-items:flex-start}
.cl .st{display:flex;flex-direction:column;align-items:center;gap:6px}
.cl code{font-family:Consolas,monospace;font-size:17px;background:#1B1F3B;color:#fff;padding:6px 8px;border-radius:6px;border-bottom:4px solid}
.cl span{font-size:13px;font-weight:bold;text-align:center;max-width:130px}
</style><div class="cl"><div class="st"><code style="border-color:#2965F1">document</code><span style="color:#2965F1">de hele pagina</span></div><div class="st"><code style="border-color:#E44D26">.querySelector</code><span style="color:#E44D26">zoek een element</span></div><div class="st"><code style="border-color:#1E8E4E">("#melding")</code><span style="color:#1E8E4E">met deze selector</span></div></div>
```

!!! tip "Lees de regel van links naar rechts"
    In gewone taal staat er: zoek in de pagina het element met de id melding. De punt tussen document en querySelector betekent: van de pagina.

## De tekst veranderen

Met textContent zet je nieuwe tekst in een element.
{: .sub}

1. **textContent is de tekst.** melding.textContent is de tekst die in het element staat.
2. **Een nieuwe tekst met =.** Met = geef je het element een nieuwe tekst. De oude tekst verdwijnt.
3. **Je HTML-bestand verandert niet.** JavaScript verandert de pagina in Chrome. In spel.html in VS Code blijft de oude tekst staan. In Elements zie je de nieuwe tekst wel.

script.js
{: .bestandsnaam}

```js
const melding = document.querySelector("#melding");
melding.textContent = "Raad maar!";
```

```demo titel="Zonder en met deze twee regels JavaScript"
<style>
body{font-family:Arial,sans-serif;color:#1B1F3B;margin:0;padding:14px;font-size:15px;background:#fff}
.kaart{background:#E8EAF6;border-radius:10px;padding:14px 16px}
.kaart h2{margin:0 0 6px;font-size:19px}.kaart p{margin:6px 0}
button{padding:7px 14px;border:0;border-radius:6px;background:#2965F1;color:#fff;font-size:15px;cursor:pointer;font-family:Arial,sans-serif}
button.donkerknop{background:#1B1F3B}
input{width:90px;padding:6px;font-size:15px;border:1px solid #9aa0c3;border-radius:5px}
.rij{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
#melding{font-weight:bold;min-height:20px}
.goed{color:#1E8E4E}.fout{color:#E44D26}
.verborgen{display:none}
small{color:#5b6075}
.label{font-size:12px;color:#5b6075;margin:0 0 4px}
.twee{display:flex;gap:14px}.twee>div{flex:1}
</style><div class="twee"><div><p class="label">Zonder JavaScript</p><div class="kaart"><p id="a">Ik denk aan een getal.</p></div></div>
<div><p class="label">Met JavaScript</p><div class="kaart"><p><b>Raad maar!</b></p></div></div></div>
```

!!! let-op "null in de Console?"
    Staat er null of een rode fout met null erin? Dan heeft querySelector niets gevonden. Kijk of de id in je HTML precies hetzelfde is, en of je het hekje # niet bent vergeten.

??? check "Check: vind en verander"
    **1. Welke regel vindt het element &lt;p id="uitslag"&gt;?**

    - A. `document.querySelector("uitslag");`
    - B. `document.querySelector("#uitslag");`
    - C. `document.querySelector(".uitslag");`
    - D. `document.find("#uitslag");`

    **2. Wat doet melding.textContent = "Hoger!"; ?**

    - A. Het schrijft Hoger! in de Console
    - B. Het zet Hoger! in het element op de pagina
    - C. `Het past spel.html aan in VS Code`
    - D. Het maakt een nieuwe p

    ??? antwoord "Bekijk de antwoorden"
        **1. B – `document.querySelector("#uitslag");`.** Voor een id zet je een hekje, net als in CSS. Zonder hekje zoekt JavaScript naar een tag uitslag, en met een punt naar een class. find bestaat niet: dan krijg je een rode fout.

        **2. B – Het zet Hoger! in het element op de pagina.** textContent is de tekst in het element. Met = komt er Hoger! te staan, op de pagina in Chrome. Je bestand in VS Code verandert niet. In de Console schrijf je met console.log, en er komt geen nieuw element bij.

!!! opdracht "3. Zet tekst op je pagina met JavaScript"
    Ongeveer 10 minuten · Je werkt in: `opdracht-3`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit opdracht-2 naar opdracht-3. Haal in script.js de oefenregels van opdracht 2 weg, behalve geheim en pogingen.
    2. Zet in de main van spel.html een div met de class kaart. Zet daar je h2 in, en een p met de tekst Ik denk aan een getal van 1 tot 100.
    3. Zet daaronder in de kaart een lege p met de id melding.
    4. Zoek in script.js dat element op en bewaar het in een const.
    5. Zet met textContent een tekst in je melding, bijvoorbeeld Succes!
    6. Kijk in de DevTools bij Elements: staat de tekst in je p? Kijk daarna in VS Code in spel.html: staat hij daar ook?

    ??? hint "Codehint (niet het antwoord)"
        ```js
        const titel = document.querySelector("#titel");
        titel.textContent = "...";
        ```

    !!! klaar "Klaar als..."
        Op spel.html staat in je melding de tekst die je in script.js hebt gezet. In spel.html in VS Code is de p nog leeg. Er staan geen rode fouten in de Console.

=== blok-4 | Een knop die werkt
## Wachten op een klik

Met addEventListener doet je pagina pas iets als iemand klikt.
{: .sub}

1. **Een knop in je HTML.** Zet een button in je HTML en geef hem een id.
2. **Zoek de knop.** Zoek de knop op met querySelector en bewaar hem in een const, net als in blok 3.
3. **Luister naar de klik.** knop.addEventListener("click", function () { ... }) betekent: wacht op een klik. Wat tussen de { } staat, gebeurt pas na de klik, en bij elke klik opnieuw.

spel.html
{: .bestandsnaam}

```html
<button id="raad">Raad!</button>
<p id="melding"></p>
```

script.js
{: .bestandsnaam}

```js
const knop = document.querySelector("#raad");
const melding = document.querySelector("#melding");

knop.addEventListener("click", function () {
  melding.textContent = "Je hebt geklikt!";
});
```

```demo titel="Voor en na de klik. Probeer het maar."
<style>
body{font-family:Arial,sans-serif;color:#1B1F3B;margin:0;padding:14px;font-size:15px;background:#fff}
.kaart{background:#E8EAF6;border-radius:10px;padding:14px 16px}
.kaart h2{margin:0 0 6px;font-size:19px}.kaart p{margin:6px 0}
button{padding:7px 14px;border:0;border-radius:6px;background:#2965F1;color:#fff;font-size:15px;cursor:pointer;font-family:Arial,sans-serif}
button.donkerknop{background:#1B1F3B}
input{width:90px;padding:6px;font-size:15px;border:1px solid #9aa0c3;border-radius:5px}
.rij{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
#melding{font-weight:bold;min-height:20px}
.goed{color:#1E8E4E}.fout{color:#E44D26}
.verborgen{display:none}
small{color:#5b6075}
.label{font-size:12px;color:#5b6075;margin:0 0 4px}
.twee{display:flex;gap:14px}.twee>div{flex:1}
</style><div class="twee"><div><p class="label">Voor de klik</p><div class="kaart"><button>Raad!</button><p style="min-height:20px"></p></div></div>
<div><p class="label">Na de klik</p><div class="kaart"><button id="raad">Raad!</button><p id="melding" style="font-weight:bold;min-height:20px"></p></div></div></div>
<script>document.querySelector("#raad").addEventListener("click", function () { document.querySelector("#melding").textContent = "Je hebt geklikt!"; });</script>
```

!!! let-op "Sluit goed af met });"
    De function sluit je af met }. Daarna sluit je addEventListener af met ). De puntkomma maakt de regel af. Samen: });

## Het recept: vind, wacht, verander

Bijna alles wat je met JavaScript op een pagina doet, gaat in deze drie stappen.
{: .sub}

1. **Vind.** Zoek het element op met querySelector. Bijvoorbeeld een knop of een melding.
2. **Wacht.** Wacht met addEventListener tot er iets gebeurt, meestal een klik. Zo'n gebeurtenis heet een event.
3. **Verander.** Verander iets op de pagina: de tekst met textContent, of de opmaak met classList. Dat leer je in blok 5.

script.js
{: .bestandsnaam}

```js
// 1. vind
const knop = document.querySelector("#raad");

// 2. wacht
knop.addEventListener("click", function () {
  // 3. verander
  melding.textContent = "Je hebt geklikt!";
});
```

```demo titel="Het recept in drie stappen"
<style>
body{font-family:Arial,sans-serif;color:#1B1F3B;margin:0;padding:14px;font-size:15px;background:#fff}
.kaart{background:#E8EAF6;border-radius:10px;padding:14px 16px}
.kaart h2{margin:0 0 6px;font-size:19px}.kaart p{margin:6px 0}
button{padding:7px 14px;border:0;border-radius:6px;background:#2965F1;color:#fff;font-size:15px;cursor:pointer;font-family:Arial,sans-serif}
button.donkerknop{background:#1B1F3B}
input{width:90px;padding:6px;font-size:15px;border:1px solid #9aa0c3;border-radius:5px}
.rij{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
#melding{font-weight:bold;min-height:20px}
.goed{color:#1E8E4E}.fout{color:#E44D26}
.verborgen{display:none}
small{color:#5b6075}
.label{font-size:12px;color:#5b6075;margin:0 0 4px}
.twee{display:flex;gap:14px}.twee>div{flex:1}
</style><div style="display:flex;gap:8px"><div style="flex:1;background:#E8EAF6;border-radius:10px;padding:10px 12px"><b style="font-size:16px">1. Vind</b><div style="font-size:14px;margin-top:4px">querySelector zoekt de knop en de melding</div></div><div style="font-size:26px;color:#2965F1;align-self:center">&#10140;</div><div style="flex:1;background:#ffe0d6;border-radius:10px;padding:10px 12px"><b style="font-size:16px">2. Wacht</b><div style="font-size:14px;margin-top:4px">addEventListener wacht op een klik</div></div><div style="font-size:26px;color:#2965F1;align-self:center">&#10140;</div><div style="flex:1;background:#e9f8ee;border-radius:10px;padding:10px 12px"><b style="font-size:16px">3. Verander</b><div style="font-size:14px;margin-top:4px">textContent of classList verandert de pagina</div></div></div>
```

!!! onthoud "// is een opmerking"
    Een regel die begint met // is een opmerking. JavaScript slaat die over. Zo kun je in je eigen woorden opschrijven wat je code doet. Dat helpt je ook bij het examen.

??? check "Check: een knop die werkt"
    **1. Wanneer wordt de code tussen de { } van de function uitgevoerd?**

    - A. Als de pagina laadt
    - B. Als iemand op de knop klikt
    - C. Als je opslaat in VS Code
    - D. Nooit

    **2. Wat ontbreekt er aan het eind van deze code?**

    ```js
    knop.addEventListener("click", function () {
      melding.textContent = "Hoi";
    ```

    - A. Een punt .
    - B. `});`
    - C. `Een hekje #`
    - D. Niets, het werkt zo

    ??? antwoord "Bekijk de antwoorden"
        **1. B – Als iemand op de knop klikt.** addEventListener wacht op het event "click". Pas dan, en bij elke klik opnieuw, wordt de code tussen de { } uitgevoerd. De regels erbuiten worden wel meteen uitgevoerd als de pagina laadt.

        **2. B – `});`.** De { van de function en de ( van addEventListener zijn nog open. Je sluit af met });. Zonder dat krijg je een rode fout in de Console. Een punt of een hekje helpt hier niet.

!!! opdracht "4. Maak een knop die iets doet"
    Ongeveer 10 minuten · Je werkt in: `opdracht-4`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit opdracht-3 naar opdracht-4.
    2. Zet in je kaart op spel.html, boven je melding, een button met de tekst Raad! en de id raad.
    3. Zoek de knop op in script.js en bewaar hem in een const.
    4. Laat de knop luisteren naar een klik.
    5. Zet na de klik een tekst in je melding, zoals Je hebt geklikt! Zet ook een console.log in de function.
    6. Klik een paar keer. Kijk in de Console: achter je bericht staat een getal. Dat telt hoe vaak het bericht kwam.

    ??? hint "Codehint (niet het antwoord)"
        ```js
        const hallo = document.querySelector("#hallo");
        hallo.addEventListener("click", function () {
          ...
        });
        ```

    !!! klaar "Klaar als..."
        Als je op Raad! klikt, verschijnt je tekst onder de knop. In de Console komt bij elke klik je bericht erbij.

=== blok-5 | Classes aan en uit
## Een class toevoegen en weghalen

Met classList verander je de opmaak van een element.
{: .sub}

1. **Maak de class in CSS.** In style.css maak je een class met de opmaak die je wilt, bijvoorbeeld .goed met een groene kleur.
2. **classList.add zet hem aan.** melding.classList.add("goed") geeft het element de class goed. Dan krijgt het meteen de opmaak uit je CSS.
3. **classList.remove haalt hem weg.** melding.classList.remove("goed") haalt de class weer weg. De opmaak verdwijnt dan ook.

style.css
{: .bestandsnaam}

```css
.goed {
  color: #1E8E4E;
}
.fout {
  color: #E44D26;
}
```

script.js
{: .bestandsnaam}

```js
melding.classList.add("goed");
```

```demo titel="Dezelfde melding zonder class, met goed en met fout"
<style>
body{font-family:Arial,sans-serif;color:#1B1F3B;margin:0;padding:14px;font-size:15px;background:#fff}
.kaart{background:#E8EAF6;border-radius:10px;padding:14px 16px}
.kaart h2{margin:0 0 6px;font-size:19px}.kaart p{margin:6px 0}
button{padding:7px 14px;border:0;border-radius:6px;background:#2965F1;color:#fff;font-size:15px;cursor:pointer;font-family:Arial,sans-serif}
button.donkerknop{background:#1B1F3B}
input{width:90px;padding:6px;font-size:15px;border:1px solid #9aa0c3;border-radius:5px}
.rij{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
#melding{font-weight:bold;min-height:20px}
.goed{color:#1E8E4E}.fout{color:#E44D26}
.verborgen{display:none}
small{color:#5b6075}
.label{font-size:12px;color:#5b6075;margin:0 0 4px}
.twee{display:flex;gap:14px}.twee>div{flex:1}
</style><div class="twee"><div><p class="label">Zonder class</p><div class="kaart"><p><b>Goed geraden!</b></p></div></div>
<div><p class="label">class goed</p><div class="kaart"><p class="goed"><b>Goed geraden!</b></p></div></div>
<div><p class="label">class fout</p><div class="kaart"><p class="fout"><b>Lager!</b></p></div></div></div>
```

!!! let-op "Geen punt in classList"
    In CSS schrijf je .goed met een punt. In classList schrijf je "goed" zonder punt. JavaScript weet al dat het om een class gaat.

## Aan en uit met toggle

Eén knop die iets aanzet, en bij de volgende klik weer uit.
{: .sub}

1. **toggle wisselt.** classList.toggle("verborgen") zet de class aan als hij er niet is, en haalt hem weg als hij er wel is. Elke klik wisselt hij.
2. **Uitklappen.** Met .verborgen { display: none; } verdwijnt een element. Toggle je die class, dan klapt de tekst open en weer dicht.
3. **Donkere modus.** Toggle je een class donker op de body, dan kan je hele pagina donker worden. In CSS schrijf je dan body.donker { ... }.

style.css
{: .bestandsnaam}

```css
.verborgen {
  display: none;
}
```

script.js
{: .bestandsnaam}

```js
const regelsKnop = document.querySelector("#regels-knop");
const regels = document.querySelector("#regels");

regelsKnop.addEventListener("click", function () {
  regels.classList.toggle("verborgen");
});
```

```demo titel="Klik op Spelregels: de tekst klapt open en weer dicht"
<style>
body{font-family:Arial,sans-serif;color:#1B1F3B;margin:0;padding:14px;font-size:15px;background:#fff}
.kaart{background:#E8EAF6;border-radius:10px;padding:14px 16px}
.kaart h2{margin:0 0 6px;font-size:19px}.kaart p{margin:6px 0}
button{padding:7px 14px;border:0;border-radius:6px;background:#2965F1;color:#fff;font-size:15px;cursor:pointer;font-family:Arial,sans-serif}
button.donkerknop{background:#1B1F3B}
input{width:90px;padding:6px;font-size:15px;border:1px solid #9aa0c3;border-radius:5px}
.rij{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
#melding{font-weight:bold;min-height:20px}
.goed{color:#1E8E4E}.fout{color:#E44D26}
.verborgen{display:none}
small{color:#5b6075}
.label{font-size:12px;color:#5b6075;margin:0 0 4px}
.twee{display:flex;gap:14px}.twee>div{flex:1}
</style><div class="kaart" style="min-height:105px;box-sizing:border-box"><button id="regels-knop" class="donkerknop">Spelregels</button>
<p id="regels" class="verborgen">De computer kiest een getal van 1 tot 100. Jij raadt. Je hoort of het hoger of lager is.</p></div>
<script>document.querySelector("#regels-knop").addEventListener("click", function () { document.querySelector("#regels").classList.toggle("verborgen"); });</script>
```

!!! tip "Kijk in Elements"
    Klik op je knop en kijk in Elements naar het element. Je ziet de class erbij komen en weer verdwijnen. Zo weet je zeker dat je JavaScript werkt, ook als je CSS nog niet klopt.

??? check "Check: classes aan en uit"
    **1. Welke regel geeft de melding de class goed?**

    - A. `melding.classList.add(".goed");`
    - B. `melding.classList.add("goed");`
    - C. `melding.class = goed;`
    - D. `melding.classList.remove("goed");`

    **2. Een p heeft de class verborgen. Je voert regels.classList.toggle("verborgen"); uit. Wat gebeurt er?**

    - A. De class gaat weg en je ziet de tekst
    - B. De class komt er nog een keer bij
    - C. De p wordt uit de pagina gehaald
    - D. Je krijgt een rode fout

    ??? antwoord "Bekijk de antwoorden"
        **1. B – `melding.classList.add("goed");`.** In classList schrijf je de naam zonder punt, tussen aanhalingstekens. Met ".goed" zoekt JavaScript naar een class die .goed heet, met de punt erbij. melding.class bestaat niet, en remove haalt de class juist weg.

        **2. A – De class gaat weg en je ziet de tekst.** toggle wisselt: de class was er, dus hij gaat weg. Dan geldt display: none niet meer en zie je de tekst. Bij de volgende klik komt de class terug. Het element zelf blijft gewoon in de pagina.

!!! opdracht "5. Klap je spelregels open en dicht"
    Ongeveer 15 minuten · Je werkt in: `opdracht-5`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit opdracht-4 naar opdracht-5.
    2. Maak in style.css de classes .goed (groene tekst), .fout (een andere kleur) en .verborgen (display: none).
    3. Zet in je kaart een knop Spelregels met een eigen id. Zet daaronder een p met een eigen id, de class verborgen en de spelregels in je eigen woorden.
    4. Zoek de knop en de p op in script.js. Laat de knop bij een klik de class verborgen toggelen.
    5. Geef in de function van je knop Raad! de melding ook de class goed. Klopt de kleur?
    6. Klik op je knoppen en kijk in Elements hoe de classes erbij komen en weggaan.

    ??? hint "Codehint (niet het antwoord)"
        ```js
        foto.classList.toggle("...");

        .groot {
          width: 300px;
        }
        ```

    !!! klaar "Klaar als..."
        Met de knop Spelregels klap je de tekst open en weer dicht. Na een klik op Raad! is je melding groen.

=== blok-6 | Invoer lezen
## Een invoerveld

Met een input kan de bezoeker zelf iets intypen.
{: .sub}

1. **type="number".** Een input met type="number" is een vakje voor getallen, met pijltjes om hoger en lager te gaan.
2. **min en max.** min="1" en max="100" zijn het kleinste en het grootste getal voor de pijltjes.
3. **placeholder.** De placeholder is een grijze hulptekst in het lege vakje. Zodra je typt, verdwijnt hij.

spel.html
{: .bestandsnaam}

```html
<input id="gok" type="number" min="1" max="100" placeholder="1 - 100">
<button id="raad">Raad!</button>
```

```demo titel="Leeg vakje met placeholder, en een vakje waarin 50 is getypt"
<style>
body{font-family:Arial,sans-serif;color:#1B1F3B;margin:0;padding:14px;font-size:15px;background:#fff}
.kaart{background:#E8EAF6;border-radius:10px;padding:14px 16px}
.kaart h2{margin:0 0 6px;font-size:19px}.kaart p{margin:6px 0}
button{padding:7px 14px;border:0;border-radius:6px;background:#2965F1;color:#fff;font-size:15px;cursor:pointer;font-family:Arial,sans-serif}
button.donkerknop{background:#1B1F3B}
input{width:90px;padding:6px;font-size:15px;border:1px solid #9aa0c3;border-radius:5px}
.rij{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
#melding{font-weight:bold;min-height:20px}
.goed{color:#1E8E4E}.fout{color:#E44D26}
.verborgen{display:none}
small{color:#5b6075}
.label{font-size:12px;color:#5b6075;margin:0 0 4px}
.twee{display:flex;gap:14px}.twee>div{flex:1}
</style><div class="twee"><div><p class="label">Leeg</p><div class="rij"><input type="number" placeholder="1 - 100"><button>Raad!</button></div></div>
<div><p class="label">Ingevuld</p><div class="rij"><input type="number" value="50"><button>Raad!</button></div></div></div>
```

!!! onthoud "Een input heeft geen sluittag"
    Je schrijft alleen &lt;input ...&gt;. Er bestaat geen &lt;/input&gt;, net als bij een img.

## Lezen wat er is ingevuld

Met .value lees je wat er in het vakje staat.
{: .sub}

1. **value is wat er staat.** invoer.value is wat de bezoeker in het vakje heeft getypt.
2. **Lees het in de function.** Lees de value pas tussen de { } van je klik-functie. Doe je het erbuiten, dan lees je het vakje als de pagina laadt, en dan is het nog leeg.
3. **Maak er een getal van.** value is altijd tekst, ook bij type="number". Met Number(invoer.value) maak je er een getal van, zodat je kunt rekenen en vergelijken.

script.js
{: .bestandsnaam}

```js
const invoer = document.querySelector("#gok");

knop.addEventListener("click", function () {
  const gok = Number(invoer.value);
  melding.textContent = "Jij raadt " + gok;
});
```

```demo titel="Typ een getal en klik op Raad!"
<style>
body{font-family:Arial,sans-serif;color:#1B1F3B;margin:0;padding:14px;font-size:15px;background:#fff}
.kaart{background:#E8EAF6;border-radius:10px;padding:14px 16px}
.kaart h2{margin:0 0 6px;font-size:19px}.kaart p{margin:6px 0}
button{padding:7px 14px;border:0;border-radius:6px;background:#2965F1;color:#fff;font-size:15px;cursor:pointer;font-family:Arial,sans-serif}
button.donkerknop{background:#1B1F3B}
input{width:90px;padding:6px;font-size:15px;border:1px solid #9aa0c3;border-radius:5px}
.rij{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
#melding{font-weight:bold;min-height:20px}
.goed{color:#1E8E4E}.fout{color:#E44D26}
.verborgen{display:none}
small{color:#5b6075}
.label{font-size:12px;color:#5b6075;margin:0 0 4px}
.twee{display:flex;gap:14px}.twee>div{flex:1}
</style><div class="kaart"><div class="rij"><input id="gok" type="number" min="1" max="100" placeholder="1 - 100"><button id="raad">Raad!</button></div><p id="melding"></p></div>
<script>const invoer = document.querySelector("#gok"); document.querySelector("#raad").addEventListener("click", function () { const gok = Number(invoer.value); document.querySelector("#melding").textContent = "Jij raadt " + gok; });</script>
```

!!! let-op "Vergeet Number() niet"
    Zonder Number() is de invoer tekst. Typt iemand 50, dan wordt invoer.value + 1 niet 51 maar "501". Net als "5" + 5 in blok 2.

??? check "Check: invoer lezen"
    **1. Welke regel leest wat er in &lt;input id="gok"&gt; is getypt? (invoer is dat element)**

    - A. `invoer.textContent`
    - B. `invoer.value`
    - C. `invoer.input`
    - D. `invoer.number`

    **2. Iemand typt 8 in het vakje. Wat geeft invoer.value + 2?**

    - A. 10
    - B. 82
    - C. 8
    - D. Een rode fout

    ??? antwoord "Bekijk de antwoorden"
        **1. B – `invoer.value`.** Wat er in een invoerveld staat, is de value. textContent is de tekst tussen een openingstag en een sluittag, en die heeft een input niet. input en number bestaan niet: dan krijg je undefined.

        **2. B – 82.** value is altijd tekst. Tekst + getal wordt tekst: 82. Voor 10 moet je eerst Number(invoer.value) gebruiken. Een fout krijg je niet, JavaScript plakt gewoon.

!!! opdracht "6. Lees wat de speler typt"
    Ongeveer 15 minuten · Je werkt in: `opdracht-6`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit opdracht-5 naar opdracht-6.
    2. Zet vóór je knop Raad! een invoerveld voor getallen van 1 tot 100, met een id en een placeholder.
    3. Zet het vakje en de knop met flexbox naast elkaar, met een gap.
    4. Zoek het invoerveld op in script.js en bewaar het in een const.
    5. Lees in de function van je knop de value. Maak er een getal van en bewaar dat in een const gok.
    6. Zet in je melding een zin met het getal, zoals Jij raadt 50. Zet ook console.log(gok + 1) in de function: komt er 51?

    ??? hint "Codehint (niet het antwoord)"
        ```js
        const leeftijdVak = document.querySelector("#leeftijd");

        const leeftijd = Number(...);
        uitslag.textContent = "Jij bent " + leeftijd;
        ```

    !!! klaar "Klaar als..."
        Typ je 50 en klik je op Raad!, dan staat er Jij raadt 50 op de pagina. In de Console staat 51.

=== blok-7 | Hoger of lager
## Kiezen met if en else

Je code kiest zelf welke melding er komt.
{: .sub}

1. **if: als het klopt.** if (gok &gt; geheim) { ... } betekent: als de gok groter is dan het geheim, doe dan wat tussen de { } staat.
2. **else if: anders, als.** Klopt de eerste niet, dan kijkt JavaScript naar de volgende: else if (gok &lt; geheim) { ... }.
3. **else: in alle andere gevallen.** Klopt geen van de vergelijkingen, dan doet JavaScript wat bij else staat. Hier betekent dat: de gok is goed.

script.js
{: .bestandsnaam}

```js
const geheim = 42;

if (gok > geheim) {
  melding.textContent = "Lager!";
} else if (gok < geheim) {
  melding.textContent = "Hoger!";
} else {
  melding.textContent = "Goed geraden!";
}
```

```demo titel="Drie keer raden als het geheime getal 42 is"
<style>
body{font-family:Arial,sans-serif;color:#1B1F3B;margin:0;padding:14px;font-size:15px;background:#fff}
.kaart{background:#E8EAF6;border-radius:10px;padding:14px 16px}
.kaart h2{margin:0 0 6px;font-size:19px}.kaart p{margin:6px 0}
button{padding:7px 14px;border:0;border-radius:6px;background:#2965F1;color:#fff;font-size:15px;cursor:pointer;font-family:Arial,sans-serif}
button.donkerknop{background:#1B1F3B}
input{width:90px;padding:6px;font-size:15px;border:1px solid #9aa0c3;border-radius:5px}
.rij{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
#melding{font-weight:bold;min-height:20px}
.goed{color:#1E8E4E}.fout{color:#E44D26}
.verborgen{display:none}
small{color:#5b6075}
.label{font-size:12px;color:#5b6075;margin:0 0 4px}
.twee{display:flex;gap:14px}.twee>div{flex:1}
</style><style>.w{display:grid;grid-template-columns:auto auto auto;gap:6px 12px;align-items:center;font-size:15px}.w div{padding:6px 10px;border-radius:6px;background:#E8EAF6}.w .k{font-family:Consolas,monospace}</style>
<div class="w"><b>Gok</b><b>Vergelijking</b><b>Melding</b>
<div>50</div><div class="k">50 &gt; 42 is waar</div><div class="fout"><b>Lager!</b></div>
<div>30</div><div class="k">30 &lt; 42 is waar</div><div class="fout"><b>Hoger!</b></div>
<div>42</div><div class="k">geen van beide</div><div class="goed"><b>Goed geraden!</b></div></div>
```

!!! onthoud "Vergelijken"
    &gt; betekent groter dan, &lt; betekent kleiner dan en === betekent is gelijk aan. Een vergelijking is waar (true) of niet waar (false). Eén = is geen vergelijking: dat geeft een waarde.

## Een leeg vakje en een kleur

Klik je zonder iets in te vullen, dan zegt je spel dat ook.
{: .sub}

1. **Eerst kijken of het vakje leeg is.** invoer.value === "" is waar als er niets is ingevuld. Zet deze controle bovenaan, vóór hoger en lager.
2. **Haal eerst de oude kleur weg.** Haal met classList.remove de classes goed en fout weg. Zo begint elke klik zonder kleur.
3. **Geef daarna de goede kleur.** Zet in elk stuk van je if de class die erbij past: fout bij hoger en lager, goed bij goed geraden.

script.js
{: .bestandsnaam}

```js
melding.classList.remove("goed");
melding.classList.remove("fout");

if (invoer.value === "") {
  melding.textContent = "Vul eerst een getal in.";
} else if (gok > geheim) {
  melding.textContent = "Lager!";
  melding.classList.add("fout");
} else if (gok < geheim) {
  ...
} else {
  ...
}
```

```demo titel="De vier meldingen van je spel"
<style>
body{font-family:Arial,sans-serif;color:#1B1F3B;margin:0;padding:14px;font-size:15px;background:#fff}
.kaart{background:#E8EAF6;border-radius:10px;padding:14px 16px}
.kaart h2{margin:0 0 6px;font-size:19px}.kaart p{margin:6px 0}
button{padding:7px 14px;border:0;border-radius:6px;background:#2965F1;color:#fff;font-size:15px;cursor:pointer;font-family:Arial,sans-serif}
button.donkerknop{background:#1B1F3B}
input{width:90px;padding:6px;font-size:15px;border:1px solid #9aa0c3;border-radius:5px}
.rij{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
#melding{font-weight:bold;min-height:20px}
.goed{color:#1E8E4E}.fout{color:#E44D26}
.verborgen{display:none}
small{color:#5b6075}
.label{font-size:12px;color:#5b6075;margin:0 0 4px}
.twee{display:flex;gap:14px}.twee>div{flex:1}
</style><div class="twee"><div class="kaart"><p class="label">Leeg vakje</p><p><b>Vul eerst een getal in.</b></p></div>
<div class="kaart"><p class="label">Gok 50</p><p class="fout"><b>Lager!</b></p></div>
<div class="kaart"><p class="label">Gok 30</p><p class="fout"><b>Hoger!</b></p></div>
<div class="kaart"><p class="label">Gok 42</p><p class="goed"><b>Goed geraden!</b></p></div></div>
```

!!! tip "Test alle wegen"
    Test je spel vier keer: met een leeg vakje, te hoog, te laag en precies goed. Zo weet je zeker dat elk stuk van je if werkt. Dit lijstje kun je straks ook gebruiken voor het testlijstje van je examen.

??? check "Check: hoger of lager"
    **1. geheim is 42 en gok is 30. Welke melding komt er?**

    ```js
    if (gok > geheim) → Lager!
    else if (gok < geheim) → Hoger!
    else → Goed geraden!
    ```

    - A. Lager!
    - B. Hoger!
    - C. Goed geraden!
    - D. Geen melding

    **2. Met welke regel kijk je of gok gelijk is aan geheim?**

    - A. `if (gok = geheim)`
    - B. `if (gok === geheim)`
    - C. `if (gok is geheim)`
    - D. `if (gok => geheim)`

    ??? antwoord "Bekijk de antwoorden"
        **1. B – Hoger!.** 30 &gt; 42 is niet waar, dus Lager! komt er niet. Dan kijkt JavaScript naar 30 &lt; 42: dat is waar, dus Hoger!. Bij else komt hij niet meer, want er klopte al een vergelijking.

        **2. B – `if (gok === geheim)`.** === vergelijkt. Eén = geeft gok de waarde van geheim, en dan klopt je spel niet meer. is bestaat niet in JavaScript, en =&gt; betekent iets heel anders.

!!! opdracht "7. Zeg of het hoger of lager is"
    Ongeveer 15 minuten · Je werkt in: `opdracht-7`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit opdracht-6 naar opdracht-7. Haal je console.log(gok + 1) weg.
    2. Je hebt al een geheim van 42 uit opdracht 2. Vergelijk in de function je gok met het geheim.
    3. Zet de melding Lager!, Hoger! of Goed geraden! op de pagina, met if, else if en else.
    4. Zet bovenaan je if een controle voor een leeg vakje, met een eigen melding.
    5. Haal aan het begin van de function de classes goed en fout weg. Geef daarna in elk stuk van je if de goede class.
    6. Test vier keer: leeg, 10, 90 en 42. Klopt elke melding en elke kleur?

    ??? hint "Codehint (niet het antwoord)"
        ```js
        if (leeftijd > 17) {
          uitslag.textContent = "...";
        } else {
          uitslag.textContent = "...";
        }
        ```

    !!! klaar "Klaar als..."
        Bij een leeg vakje, bij 10, bij 90 en bij 42 krijg je steeds de goede melding. Goed geraden is groen, hoger en lager hebben een andere kleur.

=== blok-8 | Toeval, tellen en opnieuw
## Een geheim getal kiezen

De computer kiest het getal, zodat jij het ook niet weet.
{: .sub}

1. **Math.random().** Math.random() geeft een willekeurig kommagetal van 0 tot 1, zoals 0.7312.
2. **Keer 100 en naar beneden.** \* 100 maakt er een getal van 0 tot 100 van, zoals 73.12. Math.floor haalt alles na de komma weg: 73.
3. **Plus 1.** Math.floor kan ook 0 geven, en nooit 100. Met + 1 krijg je een getal van 1 tot en met 100.

script.js
{: .bestandsnaam}

```js
let geheim = Math.floor(Math.random() * 100) + 1;
console.log(geheim);
```

```demo titel="Stap voor stap van Math.random() naar een getal van 1 tot 100"
<style>
body{font-family:Arial,sans-serif;color:#1B1F3B;margin:0;padding:14px;font-size:15px;background:#fff}
.kaart{background:#E8EAF6;border-radius:10px;padding:14px 16px}
.kaart h2{margin:0 0 6px;font-size:19px}.kaart p{margin:6px 0}
button{padding:7px 14px;border:0;border-radius:6px;background:#2965F1;color:#fff;font-size:15px;cursor:pointer;font-family:Arial,sans-serif}
button.donkerknop{background:#1B1F3B}
input{width:90px;padding:6px;font-size:15px;border:1px solid #9aa0c3;border-radius:5px}
.rij{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
#melding{font-weight:bold;min-height:20px}
.goed{color:#1E8E4E}.fout{color:#E44D26}
.verborgen{display:none}
small{color:#5b6075}
.label{font-size:12px;color:#5b6075;margin:0 0 4px}
.twee{display:flex;gap:14px}.twee>div{flex:1}
</style><div style="display:flex;gap:6px"><div style="flex:1;background:#E8EAF6;border-radius:10px;padding:10px 12px"><b style="font-size:16px">Math.random()</b><div style="font-size:14px;margin-top:4px"><code>0.7312</code></div></div><div style="font-size:26px;color:#2965F1;align-self:center">&#10140;</div><div style="flex:1;background:#E8EAF6;border-radius:10px;padding:10px 12px"><b style="font-size:16px">* 100</b><div style="font-size:14px;margin-top:4px"><code>73.12</code></div></div><div style="font-size:26px;color:#2965F1;align-self:center">&#10140;</div><div style="flex:1;background:#E8EAF6;border-radius:10px;padding:10px 12px"><b style="font-size:16px">Math.floor</b><div style="font-size:14px;margin-top:4px"><code>73</code></div></div><div style="font-size:26px;color:#2965F1;align-self:center">&#10140;</div><div style="flex:1;background:#e9f8ee;border-radius:10px;padding:10px 12px"><b style="font-size:16px">+ 1</b><div style="font-size:14px;margin-top:4px"><code>74</code></div></div></div>
```

!!! tip "Spieken mag tijdens het testen"
    Met console.log(geheim) zie je in de Console welk getal de computer heeft gekozen. Zo kun je testen of goed geraden werkt. Haal die regel weg als je spel af is.

## Tellen en opnieuw beginnen

Een teller laat zien hoe vaak je hebt geraden.
{: .sub}

1. **De teller begint bij 0.** Zet let pogingen = 0; bovenaan je script, buiten de function. Het is let, want de waarde verandert.
2. **Bij elke klik eentje erbij.** pogingen = pogingen + 1; betekent: pogingen wordt wat hij was, plus 1. Zet het getal daarna met textContent op de pagina.
3. **Een knop Opnieuw.** Een tweede knop zet alles terug: een nieuw geheim getal, de teller op 0, de melding leeg en het vakje leeg met invoer.value = "".

script.js
{: .bestandsnaam}

```js
let pogingen = 0;

knop.addEventListener("click", function () {
  pogingen = pogingen + 1;
  teller.textContent = pogingen;
  // ... je if van blok 7
});

opnieuwKnop.addEventListener("click", function () {
  geheim = Math.floor(Math.random() * 100) + 1;
  pogingen = 0;
  teller.textContent = pogingen;
  melding.textContent = "";
  invoer.value = "";
});
```

```demo titel="Je hele spel. Probeer het maar."
<style>
body{font-family:Arial,sans-serif;color:#1B1F3B;margin:0;padding:14px;font-size:15px;background:#fff}
.kaart{background:#E8EAF6;border-radius:10px;padding:14px 16px}
.kaart h2{margin:0 0 6px;font-size:19px}.kaart p{margin:6px 0}
button{padding:7px 14px;border:0;border-radius:6px;background:#2965F1;color:#fff;font-size:15px;cursor:pointer;font-family:Arial,sans-serif}
button.donkerknop{background:#1B1F3B}
input{width:90px;padding:6px;font-size:15px;border:1px solid #9aa0c3;border-radius:5px}
.rij{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
#melding{font-weight:bold;min-height:20px}
.goed{color:#1E8E4E}.fout{color:#E44D26}
.verborgen{display:none}
small{color:#5b6075}
.label{font-size:12px;color:#5b6075;margin:0 0 4px}
.twee{display:flex;gap:14px}.twee>div{flex:1}
</style><div class="kaart"><h2>Raad het getal</h2><p>Ik denk aan een getal van 1 tot 100.</p>
<div class="rij"><input id="gok" type="number" min="1" max="100" placeholder="1 - 100"><button id="raad">Raad!</button><button id="opnieuw" class="donkerknop">Opnieuw</button></div>
<p id="melding"></p><small>Pogingen: <span id="teller">0</span></small></div><script>
const invoer = document.querySelector("#gok");
const melding = document.querySelector("#melding");
const teller = document.querySelector("#teller");
let geheim = Math.floor(Math.random() * 100) + 1;
let pogingen = 0;
document.querySelector("#raad").addEventListener("click", function () {
  const gok = Number(invoer.value);
  pogingen = pogingen + 1;
  teller.textContent = pogingen;
  melding.classList.remove("goed");
  melding.classList.remove("fout");
  if (invoer.value === "") { melding.textContent = "Vul eerst een getal in."; }
  else if (gok > geheim) { melding.textContent = "Lager!"; melding.classList.add("fout"); }
  else if (gok < geheim) { melding.textContent = "Hoger!"; melding.classList.add("fout"); }
  else { melding.textContent = "Goed geraden!"; melding.classList.add("goed"); }
});
document.querySelector("#opnieuw").addEventListener("click", function () {
  geheim = Math.floor(Math.random() * 100) + 1;
  pogingen = 0; teller.textContent = pogingen;
  melding.textContent = ""; invoer.value = "";
  melding.classList.remove("goed"); melding.classList.remove("fout");
});
</script>
```

!!! let-op "let pogingen buiten de function"
    Staat let pogingen = 0; binnen de function, dan begint de teller bij elke klik weer bij 0. Daarom staat hij erbuiten, bovenaan je script.

??? check "Check: toeval, tellen en opnieuw"
    **1. Welke getallen kan Math.floor(Math.random() \* 10) + 1 geven?**

    - A. 0 tot en met 10
    - B. 1 tot en met 10
    - C. 1 tot en met 11
    - D. Altijd 10

    **2. Waarom staat let pogingen = 0; buiten de function?**

    - A. Anders begint de teller bij elke klik weer bij 0
    - B. Dan staat het netter
    - C. Binnen een function mag geen let
    - D. `Anders werkt Math.random niet`

    ??? antwoord "Bekijk de antwoorden"
        **1. B – 1 tot en met 10.** Math.random() \* 10 geeft 0 tot 10, maar nooit precies 10. Math.floor maakt daar 0 tot en met 9 van. Met + 1 wordt het 1 tot en met 10.

        **2. A – Anders begint de teller bij elke klik weer bij 0.** Alles tussen de { } wordt bij elke klik opnieuw uitgevoerd. Staat let pogingen = 0; daar, dan begint de teller steeds opnieuw. let mag wel in een function, en met Math.random heeft het niets te maken.

!!! opdracht "8. Maak je spel compleet"
    Ongeveer 15 minuten · Je werkt in: `opdracht-8`
    {: .meta}

    1. Kopieer alle bestanden en mappen uit opdracht-7 naar opdracht-8.
    2. Laat de computer een geheim getal van 1 tot 100 kiezen. Gebruik let, want bij Opnieuw verandert het. Zet het met console.log in de Console.
    3. Zet in je kaart een regel Pogingen: met daarachter een span met een id en het getal 0.
    4. Tel in je klik-functie de pogingen en zet het aantal op de pagina.
    5. Maak een knop Opnieuw die alles terugzet: een nieuw getal, de teller, de melding, de kleur en het vakje.
    6. Speel je spel een paar keer. Werkt alles? Haal dan console.log(geheim) weg.

    ??? hint "Codehint (niet het antwoord)"
        ```js
        let score = 0;

        score = score + ...;
        scoreVak.textContent = ...;
        ```

    !!! klaar "Klaar als..."
        De computer kiest steeds een ander getal. De teller loopt op bij elke gok. Na Opnieuw staat alles weer zoals aan het begin.

=== eindopdracht | Eindopdracht
!!! opdracht eind "Bouw je spel Raad het getal"
    Je werkt in je map eindopdracht. Kopieer eerst alle bestanden en mappen uit opdracht-8 naar eindopdracht.
    {: .meta}

    **Op je site staat:**

    - Spel staat in het menu van al je pagina's, en is actief op spel.html
    - Je spel staat in een kaart, met het vakje en de knoppen met flexbox naast elkaar
    - Een vakje voor een getal van 1 tot 100 en een knop Raad!
    - Een geheim getal dat de computer zelf kiest
    - Een melding op de pagina: hoger, lager of goed geraden, en een melding bij een leeg vakje
    - Een teller met het aantal pogingen
    - Groen bij goed geraden, en een andere kleur bij hoger en lager
    - Een knop Opnieuw die alles terugzet
    - Een knop die met toggle iets open- en dichtklapt, zoals je spelregels
    - Geen rode fouten in de Console, en geen console.log(geheim) meer
    {: .checklist}

    !!! tip "Al klaar?"
        Geef de speler maximaal 10 pogingen. Bij de tiende foute gok staat er: Helaas, het getal was ... Of maak een knop die met toggle een donkere modus aan- en uitzet op spel.html.

Alles wat je nodig hebt, heb je in de mini-opdrachten al een keer gemaakt. Kijk gerust terug in je eigen mappen.

## Inleveren

Zip de hele map module5-jouwnaam. Daarin zitten opdracht-1 tot en met opdracht-8 en de map eindopdracht. Noem de zip module5-jouwnaam.zip.

**Checklist: vink af voordat je inlevert**

- Map module5-jouwnaam met opdracht-1 tot en met opdracht-8
- Map eindopdracht met vier html-bestanden, style.css en script.js
- De script-regel met defer in de head van spel.html
- Geen rode fouten in de Console
- Je spel getest: leeg, te hoog, te laag en goed
- Alle map- en bestandsnamen met kleine letters
- Alles opgeslagen met Ctrl + S
- Elke pagina heeft Spel in het menu
{: .checklist}

!!! tip "Zo maak je een zip"
    Rechtsklik op de map module5-jouwnaam en kies Comprimeren naar &gt; ZIP-bestand. Op oudere Windows: Kopiëren naar &gt; Gecomprimeerde map.

!!! tip "Werk je thuis?"
    Je hebt VS Code en Chrome nodig. Kom je er niet uit? Schrijf je vraag op, met de rode fout uit de Console, en neem hem mee.

Twijfel je of iets af is? Kijk bij Klaar als... bij die opdracht.

=== werkt-het-niet | Werkt het niet?
Open de Console. Daar staat meestal precies wat er misgaat.
{: .sub}

1. **Heb je alles opgeslagen?** Een witte stip op een tabblad in VS Code betekent: nog niet opgeslagen. Sla op met Ctrl + S.
2. **Er gebeurt helemaal niets?** Kijk of de script-regel in de head van spel.html staat, met defer en de goede bestandsnaam. Zet een console.log bovenaan je script: zie je hem in de Console?
3. **Rode fout met null?** querySelector heeft niets gevonden. Klopt de id in je HTML precies? Staat het hekje # ervoor?
4. **is not defined?** Je gebruikt een naam die niet bestaat. Vaak is het een typfout of een hoofdletter: Melding is iets anders dan melding.
5. **Unexpected end of input?** Er mist een } of een ). Kijk of elke function eindigt met });. Prettier zet alles netjes ingesprongen, dan zie je het sneller.
6. **Hoger en lager kloppen niet?** Ben je Number() vergeten? Of staan &gt; en &lt; verkeerd om? Zet console.log(gok, geheim) in je function en kijk wat er echt in staat.

!!! tip "Nog steeds niet?"
    Vraag eerst een klasgenoot, daarna je docent. Laat de Console openstaan, dan zoeken jullie samen.

=== naslag | Naslag
## JavaScript: de basis

Alles van blok 1 t/m 5 bij elkaar. Kijk hier eerst als je iets kwijt bent.
{: .sub}

Koppelen (in de head)
{: .bestandsnaam}

```html
<script src="script.js" defer></script>
```

Variabelen
{: .bestandsnaam}

```js
const naam = "Sam";   // blijft hetzelfde
let pogingen = 0;     // mag veranderen
pogingen = pogingen + 1;
console.log("Hoi " + naam);
```

Vind, wacht, verander
{: .bestandsnaam}

```js
const knop = document.querySelector("#raad");
const melding = document.querySelector("#melding");

knop.addEventListener("click", function () {
  melding.textContent = "Hoi!";
  melding.classList.add("goed");
  melding.classList.remove("fout");
  regels.classList.toggle("verborgen");
});
```

!!! onthoud "Het recept"
    Vind het element met querySelector. Wacht op een klik met addEventListener. Verander de tekst met textContent of de opmaak met classList.

!!! tip "Selectors"
    # voor een id, . voor een class, net als in CSS. In classList schrijf je de naam zonder punt.

## Het spel

Alles van blok 6 t/m 8, en de Console.
{: .sub}

Invoer lezen
{: .bestandsnaam}

```js
const gok = Number(invoer.value);
invoer.value = "";   // vakje leegmaken
```

Kiezen
{: .bestandsnaam}

```js
if (invoer.value === "") {
  melding.textContent = "Vul eerst een getal in.";
} else if (gok > geheim) {
  melding.textContent = "Lager!";
} else if (gok < geheim) {
  melding.textContent = "Hoger!";
} else {
  melding.textContent = "Goed geraden!";
}
```

Toeval
{: .bestandsnaam}

```js
let geheim = Math.floor(Math.random() * 100) + 1;
```

!!! tip "Vergelijken"
    &gt; groter dan, &lt; kleiner dan, === is gelijk aan. Eén = geeft een waarde.

!!! onthoud "Console"
    F12 en dan het tabblad Console. Rood is een fout: klik rechts op script.js met het regelnummer.

=== woordenlijst | Woordenlijst
De Engelse woorden van module 5, met de Nederlandse vertaling en uitleg in gewone taal. De woorden van module 1 t/m 4 staan in de woordenlijst van die modules.
{: .sub}

| Engels | Nederlands | Uitleg |
|---|---|---|
| **JavaScript** | JavaScript | de taal die je pagina laat reageren |
| **script** | script, programmaatje | bestand met JavaScript-code |
| **defer** | uitstellen | script pas uitvoeren als de pagina klaar is |
| **console** | console | venster in de DevTools voor berichten en fouten |
| **log** | opschrijven | console.log schrijft iets in de Console |
| **error** | fout | rode melding in de Console |
| **variable** | variabele | naam voor een waarde die je later weer gebruikt |
| **let** | laat | variabele waarvan de waarde mag veranderen |
| **const** (constant) | vast | variabele waarvan de waarde hetzelfde blijft |
| **string** | tekst | tekst tussen aanhalingstekens |
| **number** | getal | getal waarmee je kunt rekenen |
| **camelCase** | kameelletters | woorden aan elkaar, elk nieuw woord met een hoofdletter: raadKnop |
| **document** | document | de hele pagina, zoals JavaScript hem ziet |
| **querySelector** | zoeken met een selector | vindt een element met #id of .class |
| **textContent** | tekstinhoud | de tekst in een element |
| **button** | knop | element waar je op klikt |
| **event** | gebeurtenis | iets wat gebeurt, zoals een klik |
| **click** | klik | het event als iemand op iets klikt |
| **addEventListener** | luisteraar toevoegen | wacht op een event en doet dan iets |
| **function** | functie | groep opdrachten die pas wordt uitgevoerd als hij wordt aangeroepen, bijvoorbeeld na een klik |
| **classList** | lijst met classes | met add, remove en toggle zet je een class aan of uit |
| **toggle** | wisselen | zet een class aan als hij uit staat, en uit als hij aan staat |
| **input** | invoer | vakje om in te typen |
| **value** | waarde | wat er in het vakje staat |
| **placeholder** | plaatshouder | grijze hulptekst in een leeg vakje |
| **if / else** | als / anders | kiest wat er gebeurt |
| **true / false** | waar / niet waar | de uitkomst van een vergelijking, zoals gok &gt; geheim |
| **random** | willekeurig | Math.random kiest een getal |
| **floor** | vloer, naar beneden | Math.floor haalt alles na de komma weg |
| **null** | niets | querySelector heeft niets gevonden |
| **undefined** | niet bepaald | iets zonder waarde, of iets wat niet bestaat |
