# WHISKY MAGAZIN - Komplettanleitung

## Was ist das?

Ein automatisches System, das KI-generierte Blog-Artikel zu den Themen
Whisky und Reisen erstellt und daraus eine komplette, fertige Website baut.

Kein WordPress noetig. Kein Server-Wissen noetig. Einfach ausfuehren.

**Was die Website enthaelt:**
- Professionell gestaltete Startseite mit Artikeluebersicht
- SEO-optimierte Einzelartikel (1.200-2.500 Woerter)
- Automatisch eingebaute Affiliate-Links (Amazon, Tradedoubler)
- Kategorie-Seiten (Whisky, Reise, Lifestyle, Natur, Urlaub)
- Sitemap fuer Google-Indexierung
- 73 vorbereitete Themen fuer ca. 6 Monate Content

---

## Taeglich nutzen

### Neuen Artikel erstellen + Website aktualisieren
```
starten.bat -> Option [5] oder [2]
```

### Nur Website anschauen
```
starten.bat -> Option [6]
```
Oeffnet die Website im Browser unter http://localhost:8090

### Kommandozeile (fuer Fortgeschrittene)
```
cd whisky-magazin
venv\Scripts\activate
python main.py --auto -n 3    # 3 Artikel generieren + Website bauen
python main.py --generate -n 5 # 5 Artikel generieren (ohne Website-Build)
python main.py --build         # Website neu bauen (aus vorhandenen Artikeln)
python main.py --stats         # Statistiken anzeigen
python main.py --serve         # Lokalen Webserver starten
```

---

## Website online stellen (Hosting)

Die generierte Website liegt im Ordner `site/`. Das sind reine HTML-Dateien,
die du ueberall hosten kannst. Hier die besten Optionen:

### Option 1: Netlify (EMPFOHLEN - kostenlos)

Netlify ist der einfachste Weg, statische Websites zu hosten. Komplett kostenlos.

1. Gehe zu https://www.netlify.com und erstelle ein Konto
2. Im Dashboard: Klicke auf "Add new site" -> "Deploy manually"
3. Ziehe den **gesamten `site/`-Ordner** per Drag & Drop in das Upload-Feld
4. Fertig! Du bekommst eine URL wie `dein-name.netlify.app`
5. Optional: Eigene Domain verbinden unter "Domain settings"

**Nach jedem neuen Artikel:**
Einfach den `site/`-Ordner erneut hochziehen (ersetzt die alte Version).

### Option 2: GitHub Pages (kostenlos)

1. Erstelle ein GitHub-Konto: https://github.com
2. Erstelle ein neues Repository (z.B. "whisky-magazin")
3. Lade den Inhalt des `site/`-Ordners hoch
4. Gehe zu Settings -> Pages -> Source: "Deploy from a branch" -> main
5. Website ist unter `deinname.github.io/whisky-magazin` erreichbar

### Option 3: Eigener Webspace / FTP

Falls du bereits Webspace hast (z.B. bei deinem Domain-Anbieter):

1. Oeffne ein FTP-Programm (z.B. FileZilla)
2. Verbinde dich mit deinem Webspace
3. Lade den Inhalt des `site/`-Ordners in das gewuenschte Verzeichnis
4. Fertig!

Wenn du den `site/`-Ordner z.B. nach `/whisky-magazin/` hochlaedst,
ist die Seite unter `www.whisky.reise/whisky-magazin/` erreichbar
(falls du Zugang zum selben Hosting hast).

### Option 4: Cloudflare Pages (kostenlos)

1. Gehe zu https://pages.cloudflare.com
2. "Create a project" -> "Direct Upload"
3. `site/`-Ordner hochladen
4. Eigene Domain verbinden

---

## Eigene Domain verbinden

Wenn du eine eigene Domain willst (z.B. whisky-magazin.de):

1. Kaufe eine Domain (z.B. bei namecheap.com, ca. 10 EUR/Jahr)
2. In den DNS-Einstellungen: Verweise sie auf deinen Hosting-Anbieter
3. Bei Netlify/Cloudflare geht das besonders einfach ueber deren Dashboard

---

## Einstellungen anpassen (config.json)

| Einstellung | Beschreibung | Standard |
|---|---|---|
| `site.name` | Name der Website | "Whisky Magazin" |
| `site.tagline` | Untertitel | "Dein Guide..." |
| `site.author` | Autorname | "Ellas" |
| `site.base_url` | URL der Website (leer = relativ) | "" |
| `openai.model` | KI-Modell | "gpt-4o" |
| `openai.temperature` | Kreativitaet (0.0-1.0) | 0.7 |
| `min_word_count` | Mindest-Woerter pro Artikel | 1200 |
| `max_word_count` | Max-Woerter pro Artikel | 2500 |

### base_url einstellen (wichtig fuer Online-Hosting!)

Wenn die Website online steht, trage die URL ein:
```json
"base_url": "https://dein-name.netlify.app"
```
Oder bei Unterverzeichnis:
```json
"base_url": "https://www.whisky.reise/whisky-magazin"
```
Danach Website neu bauen mit `python main.py --build`.

---

## Kosten-Uebersicht

| Posten | Kosten |
|---|---|
| OpenAI API (12 Artikel/Monat) | ca. 1-2 EUR/Monat |
| Hosting (Netlify/GitHub Pages) | kostenlos |
| Eigene Domain (optional) | ca. 10 EUR/Jahr |
| **Gesamt** | **ca. 1-2 EUR/Monat** |

## Erwartete Einnahmen

| Zeitraum | Artikel | Geschaetzte Einnahmen |
|---|---|---|
| Monat 1-3 | 36 | 50-150 EUR/Monat |
| Monat 4-6 | 72 | 150-400 EUR/Monat |
| Monat 7-12 | 150+ | 300-1.000 EUR/Monat |

Einnahmequellen:
- **Amazon Affiliate** (Whisky-Verkaeufe): 3-7% Provision
- **Tradedoubler** (Reisebuchungen): 2-5% Provision
- **Reiseversicherungen**: Einmalprovisionen
- **Google AdSense** (optional spaeter): 2-5 EUR pro 1.000 Besucher

---

## Dateien im Projekt

```
whisky-magazin/
  setup.bat              <- Installation (einmal ausfuehren)
  starten.bat            <- Programm starten
  main.py                <- Hauptprogramm
  content_generator.py   <- KI-Artikelgenerierung
  site_builder.py        <- Website-Generator
  topic_library.py       <- 73 Themenvorschlaege
  config.example.json    <- Vorlage
  config.json            <- Deine Konfiguration
  requirements.txt       <- Python-Pakete
  articles/              <- Generierte Artikel (JSON)
  site/                  <- Fertige Website (HTML)
    index.html           <- Startseite
    artikel/             <- Einzelne Artikelseiten
    kategorie/           <- Kategorieseiten
    sitemap.xml          <- Fuer Google
  used_topics.json       <- Verwendete Themen
  magazin.log            <- Protokoll
```

---

## FAQ / Haeufige Fragen

**Wie fuege ich neue Themen hinzu?**
Oeffne `topic_library.py` und fuege neue Eintraege zur Liste `WHISKY_TOPICS` hinzu.
Format: `{"title": "...", "category": "Whisky", "tags": ["..."], "type": "article"}`

**Kann ich das Design aendern?**
Ja! Das gesamte CSS ist in `site_builder.py` in der Funktion `_base_template()`.
Aendere die Farben unter `:root` oder das Layout im CSS.

**Was passiert wenn alle 73 Themen aufgebraucht sind?**
Das System startet automatisch von vorne oder du kannst `used_topics.json`
loeschen um alle Themen wieder freizugeben.

**Kann ich Artikel manuell bearbeiten?**
Ja! Oeffne die JSON-Datei im `articles/`-Ordner, bearbeite den HTML-Inhalt
im Feld `html_content`, und baue die Website neu mit `python main.py --build`.

**OpenAI "insufficient_quota" Fehler?**
Guthaben aufladen: https://platform.openai.com/settings/organization/billing

**Muss mein PC die ganze Zeit an sein?**
Nein. Du fuehrst das Programm manuell aus, wann immer du neue Artikel willst.
Z.B. einmal pro Woche `starten.bat` -> Option [5] fuer 3 neue Artikel.
