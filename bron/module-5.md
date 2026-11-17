---
nr: 5
titel: JavaScript: je pagina reageert
kort: Je bouwt het spel Raad het getal op een nieuwe pagina in je eigen site.
tags: let | if | addEventListener | Math.random
status: binnenkort
---

=== start | Start
!!! let-op "Deze module komt binnenkort"
    De uitleg en de opdrachten van module 5 staan hier binnenkort. Hieronder zie je alvast wat je gaat leren.

## Dit ga je maken

Je bouwt het spel **Raad het getal** op een nieuwe pagina `spel.html` in je eigen site. De computer kiest een geheim getal van 1 tot 100. Jij raadt, en de pagina zegt of het hoger of lager is.

```demo titel="Zo kan je spel eruitzien. Probeer het maar."
<style>.kaart{background:#E8EAF6;border-radius:10px;padding:16px;max-width:360px}h2{margin:0 0 8px}input{width:80px;padding:6px;font-size:15px}button{padding:7px 14px;border:0;border-radius:6px;background:#2965F1;color:#fff;cursor:pointer}#melding{font-weight:bold;margin:10px 0 4px}.goed{color:#1E8E4E}.fout{color:#E44D26}small{color:#5b6075}</style>
<div class="kaart"><h2>Raad het getal</h2><p>Ik denk aan een getal van 1 tot 100.</p>
<input id="gok" type="number" min="1" max="100" placeholder="1-100"> <button id="raad">Raad!</button> <button id="opnieuw" style="background:#1B1F3B">Opnieuw</button>
<p id="melding"></p><small>Pogingen: <span id="teller">0</span></small></div>
<script>
let geheim = Math.floor(Math.random() * 100) + 1;
let pogingen = 0;
const melding = document.querySelector("#melding");
document.querySelector("#raad").addEventListener("click", function () {
  const gok = Number(document.querySelector("#gok").value);
  pogingen = pogingen + 1;
  document.querySelector("#teller").textContent = pogingen;
  melding.classList.remove("goed", "fout");
  if (gok > geheim) { melding.textContent = "Lager!"; melding.classList.add("fout"); }
  else if (gok < geheim) { melding.textContent = "Hoger!"; melding.classList.add("fout"); }
  else { melding.textContent = "Goed geraden!"; melding.classList.add("goed"); }
});
document.querySelector("#opnieuw").addEventListener("click", function () {
  geheim = Math.floor(Math.random() * 100) + 1; pogingen = 0;
  document.querySelector("#teller").textContent = 0; melding.textContent = ""; document.querySelector("#gok").value = "";
});
</script>
```

## Wat je leert

| Blok | Onderwerp |
|---|---|
| 1 | Kennismaken: wat is JavaScript, spel.html maken, script.js koppelen, console.log en de Console |
| 2 | Variabelen: namen voor je waarden, `const` en `let`, tekst en getallen |
| 3 | Pagina aanpassen: `document.querySelector` en `textContent` |
| 4 | Een knop die werkt: `addEventListener` |
| 5 | Invoer lezen: een invoerveld, `.value` en `Number()` |
| 6 | Hoger of lager: `if`, `else if` en `else` |
| 7 | Toeval en tellen: `Math.random` en een teller |
| 8 | Kleur en opnieuw: `classList` en een knop Opnieuw |

!!! onthoud "Vergelijk het met een huis"
    HTML zijn de muren, CSS is de verf en JavaScript is de elektriciteit: daarmee gaat er iets gebeuren als je op een knop drukt.

=== woordenlijst | Woordenlijst
De Engelse woorden van module 5, met de Nederlandse vertaling en uitleg in gewone taal.
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
| **camelCase** | kameelletters | woorden aan elkaar met een hoofdletter: raadKnop |
| **document** | document | de hele pagina, zoals JavaScript hem ziet |
| **querySelector** | zoeken met een selector | vindt een element met #id of .class |
| **textContent** | tekstinhoud | de tekst in een element |
| **button** | knop | element waar je op klikt |
| **event** | gebeurtenis | iets wat gebeurt, zoals een klik |
| **click** | klik | het event als iemand op iets klikt |
| **addEventListener** | luisteraar toevoegen | wacht op een event en doet dan iets |
| **function** | functie | lijstje opdrachten dat later gebeurt |
| **input** | invoer | vakje om in te typen |
| **value** | waarde | wat er in het vakje staat |
| **placeholder** | plaatshouder | grijze hulptekst in een leeg vakje |
| **if / else** | als / anders | kiest wat er gebeurt |
| **true / false** | waar / niet waar | het antwoord op een vraag |
| **random** | willekeurig | Math.random kiest een getal |
| **floor** | vloer, naar beneden | Math.floor haalt alles na de komma weg |
| **classList** | lijst met classes | add en remove zetten een class aan of uit |
| **null** | niets | querySelector heeft niets gevonden |
| **undefined** | niet bepaald | variabele zonder waarde |
