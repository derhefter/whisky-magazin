"""
Themen-Bibliothek fuer den Whisky-Reise Content-Generator.
Enthaelt hunderte von Themenvorschlaegen, die automatisch rotiert werden.
"""

WHISKY_TOPICS = [
    # --- Destillerien & Regionen ---
    {"title": "Die besten Whisky-Destillerien auf Islay", "category": "Whisky", "tags": ["Islay", "Distillery", "Single Malt", "Schottland"], "type": "guide"},
    {"title": "Speyside entdecken: Schottlands Whisky-Herz", "category": "Whisky", "tags": ["Speyside", "Distillery", "Schottland"], "type": "guide"},
    {"title": "Highland Whisky: Raue Landschaft, weicher Geschmack", "category": "Whisky", "tags": ["Highlands", "Distillery", "Single Malt"], "type": "guide"},
    {"title": "Lowland Whiskys: Leicht, elegant und unterschaetzt", "category": "Whisky", "tags": ["Lowlands", "Single Malt"], "type": "article"},
    {"title": "Campbeltown: Die vergessene Whisky-Hauptstadt", "category": "Whisky", "tags": ["Campbeltown", "Distillery"], "type": "article"},
    {"title": "Die Geschichte von Lagavulin: 200 Jahre Torfrauch", "category": "Whisky", "tags": ["Lagavulin", "Islay", "Single Malt"], "type": "article"},
    {"title": "Ardbeg: Der intensivste Whisky der Welt?", "category": "Whisky", "tags": ["Ardbeg", "Islay", "Tasting"], "type": "review"},
    {"title": "Laphroaig: Warum Whisky-Fans diesen Dram lieben oder hassen", "category": "Whisky", "tags": ["Laphroaig", "Islay", "Tasting"], "type": "review"},
    {"title": "Bowmore: Tradition trifft Innovation", "category": "Whisky", "tags": ["Bowmore", "Islay", "Distillery"], "type": "article"},
    {"title": "Talisker: Der Whisky von der Insel Skye", "category": "Whisky", "tags": ["Talisker", "Skye", "Single Malt"], "type": "review"},
    {"title": "Glenfiddich vs. Glenlivet: Der grosse Vergleich", "category": "Whisky", "tags": ["Glenfiddich", "Glenlivet", "Tasting"], "type": "review"},
    {"title": "Macallan: Ist der Hype gerechtfertigt?", "category": "Whisky", "tags": ["Macallan", "Speyside", "Single Malt"], "type": "article"},
    {"title": "Bruichladdich und Octomore: Extremer Torf, einzigartiger Charakter", "category": "Whisky", "tags": ["Bruichladdich", "Islay", "Tasting"], "type": "review"},
    {"title": "Kilchoman: Islays juengste Destillerie", "category": "Whisky", "tags": ["Kilchoman", "Islay", "Distillery"], "type": "article"},
    {"title": "Port Ellen: Die Legende lebt wieder", "category": "Whisky", "tags": ["Port Ellen", "Islay", "Distillery"], "type": "article"},
    {"title": "Japanischer Whisky: Warum die Welt auf Japan schaut", "category": "Whisky", "tags": ["Japan", "Whisky"], "type": "guide"},
    {"title": "Irish Whiskey: Der sanfte Rivale aus Irland", "category": "Whisky", "tags": ["Irish Whiskey", "Irland"], "type": "guide"},
    {"title": "Bourbon vs. Scotch: Die grossen Unterschiede erklaert", "category": "Whisky", "tags": ["Bourbon", "Scotch", "Whisky"], "type": "article"},
    {"title": "Deutscher Whisky: Eine Szene im Aufbruch", "category": "Whisky", "tags": ["Deutscher Whisky"], "type": "article"},
    {"title": "Taiwanesischer Whisky: Kavalan und Co.", "category": "Whisky", "tags": ["Taiwan", "Kavalan", "Whisky"], "type": "article"},

    # --- Tastings & Bewertungen ---
    {"title": "Whisky-Tasting fuer Einsteiger: So geht's richtig", "category": "Whisky", "tags": ["Tasting", "Einsteiger"], "type": "guide"},
    {"title": "Die 10 besten Whiskys unter 50 Euro", "category": "Whisky", "tags": ["Tasting", "Whisky"], "type": "listicle"},
    {"title": "Whisky-Adventskalender: Die besten fuer die Weihnachtszeit", "category": "Whisky", "tags": ["Whisky", "Weihnachten"], "type": "listicle"},
    {"title": "Sherry-Fass vs. Bourbon-Fass: Wie das Fass den Whisky praegt", "category": "Whisky", "tags": ["Tasting", "Whisky"], "type": "article"},
    {"title": "Torfiger Whisky: Fuer wen ist er geeignet?", "category": "Whisky", "tags": ["Tasting", "Islay", "Single Malt"], "type": "article"},
    {"title": "Single Malt vs. Blended: Was ist besser?", "category": "Whisky", "tags": ["Single Malt", "Whisky"], "type": "article"},
    {"title": "Cask Strength Whisky: Ungefiltert und unverdunnt", "category": "Whisky", "tags": ["Tasting", "Whisky"], "type": "article"},
    {"title": "Die richtige Whisky-Lagerung: So bleibt dein Dram perfekt", "category": "Whisky", "tags": ["Whisky", "Tipps"], "type": "guide"},
    {"title": "Whisky und Schokolade: Das perfekte Pairing", "category": "Lifestyle", "tags": ["Whisky", "Pairing", "Lifestyle"], "type": "article"},
    {"title": "Whisky und Kaese: Ueberraschende Kombinationen", "category": "Lifestyle", "tags": ["Whisky", "Pairing", "Lifestyle"], "type": "article"},
    {"title": "Online Whisky Tasting: Die besten Anbieter im Vergleich", "category": "Whisky", "tags": ["Tasting", "Online"], "type": "listicle"},
    {"title": "Whisky-Glaeser: Welches Glas fuer welchen Whisky?", "category": "Whisky", "tags": ["Whisky", "Zubehoer"], "type": "guide"},
    {"title": "Whisky als Geldanlage: Lohnt sich das Investment?", "category": "Whisky", "tags": ["Whisky", "Investment"], "type": "article"},

    # --- Reise: Schottland ---
    {"title": "Schottland Roadtrip: Die beste Route fuer Whisky-Fans", "category": "Reise", "tags": ["Schottland", "Roadtrip", "Whisky"], "type": "guide"},
    {"title": "Edinburgh fuer Whisky-Liebhaber: Bars, Shops und Touren", "category": "Reise", "tags": ["Edinburgh", "Schottland", "Whisky Bars"], "type": "guide"},
    {"title": "Glasgow: Mehr als nur eine Durchreise", "category": "Reise", "tags": ["Glasgow", "Schottland"], "type": "guide"},
    {"title": "Die North Coast 500: Schottlands schoenste Kuestenstrasse", "category": "Reise", "tags": ["Schottland", "Roadtrip", "NC500"], "type": "guide"},
    {"title": "Mit der Faehre nach Schottland: Alle Routen und Tipps", "category": "Reise", "tags": ["Schottland", "Faehre"], "type": "guide"},
    {"title": "Wohnmobil-Reise durch Schottland: Was du wissen musst", "category": "Reise", "tags": ["Schottland", "Wohnmobil"], "type": "guide"},
    {"title": "Islay erreichen: Faehre, Flug oder beides?", "category": "Reise", "tags": ["Islay", "Schottland", "Faehre"], "type": "guide"},
    {"title": "Die schoensten B&Bs in Schottland", "category": "Reise", "tags": ["Schottland", "B&B", "Hotels"], "type": "listicle"},
    {"title": "Highland Games: Tradition und Spektakel erleben", "category": "Reise", "tags": ["Schottland", "Highlands", "Kultur"], "type": "article"},
    {"title": "Die Isle of Skye: Naturwunder und Whisky", "category": "Reise", "tags": ["Skye", "Schottland", "Natur"], "type": "guide"},
    {"title": "Schottische Kueche: Mehr als Haggis", "category": "Reise", "tags": ["Schottland", "Essen", "Kultur"], "type": "article"},
    {"title": "Mietwagen in Schottland: Linksverkehr und andere Tipps", "category": "Reise", "tags": ["Schottland", "Mietwagen"], "type": "guide"},
    {"title": "Die Orkney-Inseln: Highland Park und mehr", "category": "Reise", "tags": ["Orkney", "Schottland", "Distillery"], "type": "guide"},
    {"title": "Fruehling in Schottland: Die beste Reisezeit?", "category": "Reise", "tags": ["Schottland", "Reisezeit"], "type": "article"},
    {"title": "Herbst in den Highlands: Farben, Ruhe und guter Whisky", "category": "Reise", "tags": ["Schottland", "Highlands", "Herbst"], "type": "article"},
    {"title": "Packliste fuer Schottland: Das brauchst du wirklich", "category": "Reise", "tags": ["Schottland", "Packliste", "Tipps"], "type": "guide"},

    # --- Reise: Irland ---
    {"title": "Dublin fuer Whiskey-Liebhaber: Die besten Pubs und Destillerien", "category": "Reise", "tags": ["Dublin", "Irland", "Irish Whiskey"], "type": "guide"},
    {"title": "Irlands Whiskey Trail: Von Dublin bis Galway", "category": "Reise", "tags": ["Irland", "Irish Whiskey", "Roadtrip"], "type": "guide"},
    {"title": "Teeling Distillery Dublin: Ein Besuch lohnt sich", "category": "Reise", "tags": ["Teeling Whiskey", "Dublin", "Irland"], "type": "article"},
    {"title": "Wild Atlantic Way: Irlands spektakulaerste Kuestenstrasse", "category": "Reise", "tags": ["Irland", "Roadtrip"], "type": "guide"},

    # --- Reise: Andere Laender ---
    {"title": "Kentucky Bourbon Trail: Ein Roadtrip durch die USA", "category": "Reise", "tags": ["USA", "Bourbon", "Roadtrip"], "type": "guide"},
    {"title": "Whisky-Reise nach Japan: Suntory, Nikka und mehr", "category": "Reise", "tags": ["Japan", "Whisky", "Reise"], "type": "guide"},
    {"title": "Whisky-Regionen der Welt: Eine Uebersicht", "category": "Reise", "tags": ["Whisky", "Reise", "Welt"], "type": "guide"},

    # --- Natur & Outdoor ---
    {"title": "Wandern in den Highlands: Die 5 schoensten Routen", "category": "Natur", "tags": ["Schottland", "Highlands", "Wandern"], "type": "listicle"},
    {"title": "Wildlife in Schottland: Hirsche, Adler und Robben", "category": "Natur", "tags": ["Schottland", "Natur", "Wildlife"], "type": "article"},
    {"title": "Die schoensten Straende Schottlands", "category": "Natur", "tags": ["Schottland", "Natur", "Straende"], "type": "listicle"},
    {"title": "Loch Ness und mehr: Schottlands geheimnisvolle Seen", "category": "Natur", "tags": ["Schottland", "Natur", "Loch Ness"], "type": "article"},
    {"title": "Highland Rinder: Wo man sie am besten sieht", "category": "Natur", "tags": ["Schottland", "Highland Rinder", "Natur"], "type": "article"},

    # --- Lifestyle ---
    {"title": "Whisky-Cocktails: Mehr als nur pur geniessen", "category": "Lifestyle", "tags": ["Whisky", "Cocktails", "Lifestyle"], "type": "article"},
    {"title": "Burns Night feiern: Tradition und Rezepte", "category": "Lifestyle", "tags": ["Burns Night", "Schottland", "Kultur"], "type": "article"},
    {"title": "Die besten Whisky-Buecher fuer Einsteiger und Kenner", "category": "Lifestyle", "tags": ["Whisky", "Buecher"], "type": "listicle"},
    {"title": "Whisky-Geschenke: Die besten Ideen fuer jeden Anlass", "category": "Lifestyle", "tags": ["Whisky", "Geschenke"], "type": "listicle"},
    {"title": "Whisky und Zigarren: Eine klassische Kombination", "category": "Lifestyle", "tags": ["Whisky", "Zigarren", "Lifestyle"], "type": "article"},
    {"title": "Die schoensten Whisky-Bars in Deutschland", "category": "Lifestyle", "tags": ["Whisky Bars", "Deutschland"], "type": "listicle"},
    {"title": "Whisky als Hobby: Was du zum Start brauchst", "category": "Lifestyle", "tags": ["Whisky", "Einsteiger"], "type": "guide"},

    # --- Urlaub ---
    {"title": "Familienurlaub in Schottland: Tipps fuer Eltern (und Whisky-Fans)", "category": "Urlaub", "tags": ["Schottland", "Familienurlaub"], "type": "guide"},
    {"title": "Reiseversicherung fuer Schottland: Was du wirklich brauchst", "category": "Urlaub", "tags": ["Reiseversicherung", "Schottland"], "type": "guide"},
    {"title": "Guenstig nach Schottland: Spartipps fuer die Whisky-Reise", "category": "Urlaub", "tags": ["Schottland", "Spartipps", "Budget"], "type": "guide"},
    {"title": "Luxusurlaub in Schottland: Schlosshotels und Fine Dining", "category": "Urlaub", "tags": ["Schottland", "Luxus", "Hotels"], "type": "guide"},
    {"title": "Schottland im Winter: Lohnt sich eine Reise?", "category": "Urlaub", "tags": ["Schottland", "Winter", "Reisezeit"], "type": "article"},
]

# Mapping von Kategorien zu WordPress-Kategorie-Namen
CATEGORY_MAP = {
    "Whisky": "Whisky",
    "Reise": "Reise",
    "Natur": "Natur",
    "Lifestyle": "Lifestyle",
    "Urlaub": "Urlaub",
    "Allgemein": "Allgemein",
}
