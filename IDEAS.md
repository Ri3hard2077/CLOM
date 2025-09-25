# CLOM Ideas

## 🎨 1. Interface & Gebruikservaring

### Welkomstscherm & Introductiehandleiding
- Neonstijl startscherm met CLOM‑logo en versie‑info (**CLOM v1.0 — Nexus Edition**).
- Taalkeuze: Nederlands of Engels (later uitbreidbaar).
- Korte uitleg: *“Beheer je Cyberpunk 2077 mods met volledige controle over laadvolgorde, conflicten en updates.”*
- Verschijnt automatisch bij eerste opstart, met stapsgewijze uitleg van functies:
  - Mods scannen
  - Conflicten herkennen
  - Mod Notes gebruiken
  - Thema’s instellen
  - Nexus updatebewaking
  - Profielen opslaan/laden
  - Exporteren en back‑ups maken
- Checkbox: *“Toon deze handleiding bij volgende keer opstarten”* (opgeslagen in `clm_config.json`).
- Altijd opnieuw te openen via menu **Opties**.
- Vormgeving: Cyberpunk‑stijl venster met neonaccenten.
- Scrollbaar en interactief (klikbare tips, links naar Nexus of Discord).

### Eerste Setup Wizard
- Stap 1: Welkomscherm met logo, versie en taalkeuze.
- Stap 2: Introductiehandleiding met uitleg functies.
- Stap 3: Setup Wizard: kies modmap, thema, Nexus API, scanoptie.
- Stap 4: Eerste scan + conflictadvies.
- Stap 5: Opslaan als profiel + optionele backup.

### Thema’s & Layout
- Thema’s:
  - Cyberpunk Neon (geel/blauw/paars op zwart)
  - NetRunner (blauw/groen matrixstijl)
  - Voodoo (paars/rood tribal stijl)
  - Licht Thema (wit/grijs met blauwe accenten)
  - Donker Thema (zwart/grijs met gele accenten)
- Gebruikers kunnen thema’s live wisselen via dropdown.
- Kleuren aanpassen via RGB‑sliders.
- Lettertype en kolombreedte instellen.
- Volledige scrollondersteuning voor grote modlijsten.

### Meertalige Ondersteuning
- Standaard: Nederlands en Engels.
- Uitbreidbaar via vertaalbestanden (.json/.ini).
- Community kan vertalingen toevoegen.
- Taalkeuzemenu in de GUI.

### Interface Functies
- Sorteren op datum, naam, grootte.
- Groeperen per modfolder.
- Filteren op tags of keywords.
- Conflicten markeren in rood, opgelost‑label.
- Automatische detectie van MO2’s `modlist.txt`.
- Exportopties: `.txt` en `.csv` met metadata (inclusief mod notes en conflictstatus).

### Toegankelijkheid
- Hoog contrast thema’s.
- Grotere lettertypes.
- Optioneel: tekst‑naar‑spraak voor notificaties.

## 🗂️ 2. Modbeheer & Detectie

### Modbeheer & Detectie
- Velden: foldernaam, grootte, datum, override‑status, prioriteit.
- Mod Notes: eigen notities per mod.
- Conflicten visueel gemarkeerd.
- Updatebewaking: detectie gewijzigde bestanden, waarschuwing bij hernoemde `.archive`.
- Nexus API integratie: check nieuwe versies, changelogs, koppeling mod‑ID’s.
- Prioriteit override: drag & drop of forceer boven/onder.

### Mod Versiebeheer
- Meerdere versies per mod opslaan.
- Vergelijken, terugzetten, versienotities.
- Tabblad **Versiebeheer** met lijst, knoppen *Vergelijk*, *Activeer*, *Verwijder*.
- Slimme integratie met Kalender, Vergelijker, Handleiding.

### Mod Backup Scheduler
- Tijdgestuurd (dagelijks, wekelijks, maandelijks).
- Actiegestuurd (bij scan, wijziging, diagnose).
- Back‑ups bevatten: modmap, profielen, tags, loadorder, versies.
- Tabblad **Backup Scheduler** met statusindicator.

### Mod Conflict Resolver
- Detecteert overschrijvingen en botsingen.
- Automatische oplossingen op basis van tags, datum, versie, status.
- Tabblad **Conflict Resolver** met analyse, *Los op*, *Undo*, batch‑fix.
- Instelbaar: automatisch, met toestemming, undo altijd beschikbaar.

### Mod Archief
- Mods tijdelijk uitschakelen zonder verwijderen.
- Tabblad **Mod Archief** met naam, laatste gebruik, tags, notities.
- Knoppen: *Verplaats naar archief*, *Herstel uit archief*.
- Exportoptie: lijst van gearchiveerde mods.

### Snelle Scan Functie
- Vergelijkt alleen nieuwe/gewijzigde bestanden.
- Profiel‑specifiek scanstatus.
- Interface: knop *Snelle Scan* naast *Volledige Scan*.

### Mod Notities
- Vrije tekstnotities per mod.
- Verschijnen in Kalender en Statistieken.
- Exportoptie: notities opnemen in `.csv`.

### Mod Groepsbeheer
- Groepen maken (bv. *Visual Pack*, *Stealth Mods*).
- Groepsacties: activeren/deactiveren, archiveren, dupliceren.
- Integratie met Kalender, Statistieken, Diagnose.

### Mod Vergelijker
- Vergelijk twee mods/versies op naam, datum, grootte, tags, notes, conflicten, loadorder.
- Tabblad **Vergelijker** met kleurmarkering (🟢 gelijk, 🟡 verschil, 🔴 conflict).
- Knop: *Gebruik deze versie*.
- Exportoptie: rapport.

### Mod Kalender
- Maandweergave met gebeurtenissen per dag.
- Kleuren: 🟢 toegevoegd, 🔵 gewijzigd, 🟠 conflict, 🔴 verwijderd, 🟣 hersteld.
- Exportoptie: `.csv` of `.ics`.

### Mod Tags & Favorieten
- Eigen labels (Visuals, Gameplay, NPC, Patch).
- Iconen per tag.
- Filteren en groeperen.
- Favorieten: ster‑icoon, filter *Toon alleen favorieten*.
- Waardering: 1–5 sterren.
- Integratie met Diagnose en Aanbevelingen.

### Mod Statistieken
- Overzicht: aantal mods, per tag, gemiddelde sterren, conflicten opgelost, archiefstatus.
- Grafieken: staaf, lijn, cirkel.
- Exportoptie: `.csv` of afbeelding.

## 👤 3. Profielen & Configuratie

### Profielbeheer
- Opslaan en laden van verschillende modsets.
- Profielwissel met één klik.
- Automatisch herladen van instellingen en filters.
- Elk profiel bevat:
  - Geselecteerde mods
  - Load order
  - Mod Notes
  - Thema‑instellingen
  - Taalvoorkeur

### Profielnotities
- Vrije tekstnotitie per profiel, bv. *“Visual overhaul met RTX mods”*.
- Veld **Profielnotitie** zichtbaar in Profielbeheer.
- Opties: notitie bewerken, verwijderen of exporteren.
- Slimme integratie: notities worden opgeslagen in profielbestand, verschijnen in Mod Kalender en Statistieken.
- Setup Wizard biedt stap om notitie toe te voegen bij profielcreatie.
- Bij duplicatie via Profiel Duplicator wordt de notitie meegekopieerd.

### Profiel Duplicator
- Maak een volledige kopie van een profiel.
- Kopieert: modlijst, load order, tags/sterren, back‑upinstellingen, notificatievoorkeuren, archiefstatus.
- Na duplicatie direct hernoemen.
- Handig vóór risicovolle wijzigingen (bijv. diagnoseherstel of load order herschikking).

### Launch Presets
- Vooraf ingestelde configuraties (bv. *RTX run*, *Benchmark mode*).
- Tabblad **Launch Presets**.
- Opties: dupliceren, hernoemen, exporteren.
- Integratie met Setup Wizard, Conflict Resolver, Backup Scheduler.

### Setup Wizard
- **Snelle Wizard:** taal, modmap, thema, scanoptie.
- **Volledige Wizard:** alle instellingen inclusief Nexus API, notificaties, synchronisatie.
- Slimme detectie: stelt filters voor op basis van modmap.
- Wizard opnieuw starten via menu.

### Freeze/Lock Profielen
- Profiel in read‑only modus zetten.
- Geen wijzigingen mogelijk tot je het profiel “ontgrendelt”.
- Handig voor stabiele builds en playthroughs.

## ⚔️ 4. Diagnostiek & Herstel

### Diagnosemodus
- Controleert dependencies, dubbele versies, foutieve namen, mapstructuur, loadorder inconsistenties.
- Resultaten: alles in orde / waarschuwingen / kritieke fouten.
- Exportoptie: `.txt` of `.csv`.

### Slimme Aanbevelingen
- Suggesties voor modcombinaties, performance tweaks, compatibiliteit.
- Trending mods via Nexus.
- Tabblad **Aanbevelingen** met filters en klikbare links.

### Conflictbeheer + Slimme Hulp
- Details per conflict: welke mods, datum, grootte.
- Suggesties: nieuwste versie, dependency niet overschrijven, volg loadorder auteur.
- Helpknop met uitleg en links.

### Veilige Modus
- Start CLOM in read‑only sessie.
- Alleen bekijken, geen wijzigingen.
- Automatisch activeren bij fouten of corrupte mappen.

### Fixatiemodus
- Automatische oplossingen voor problemen.
- Opties: *Los automatisch op*, *Undo*, batch‑fix.
- Integratie met Versiebeheer en Backup Scheduler.

## 📤 5. Export & Community

### Export Wizard
- Stap 1: selecteer profiel of modlijst.
- Stap 2: kies exportformaat (.txt, .csv, .json).
- Stap 3: bevestig en exporteer.
- Optie: export direct delen of uploaden.
- Export bevat metadata: mod notes, tags, conflicten, loadorder.

### Community‑Ready App
- Standalone distributie (Windows .exe).
- Lichtgewicht, offline bruikbaar.
- Deelbaar via Nexus, Discord, Reddit.
- Voorbereid op community‑feedback en bugreports.

### Feedback & Bugreporting
- Knop **Feedback geven** in de interface.
- Formulier voor suggesties, bugs, feature requests.
- Optie om logbestanden mee te sturen.
- Feedback wordt opgeslagen in lokaal bestand of direct doorgestuurd.

### Nexus API Integratie
- Persoonlijke API‑sleutel invoeren.
- Check updates, changelogs, directe links naar Nexus.
- Sleutel lokaal versleuteld opgeslagen.
- Automatische melding bij nieuwe versies van geïnstalleerde mods.

### MO2 Integratie
- CLOM kan communiceren met Mod Organizer 2 via:
  - **Bestandsstructuur:** uitlezen van `modlist.txt` en `loadorder.txt`.
  - **Indirecte synchronisatie:** CLOM exporteert een aangepaste loadorderlijst die in MO2 kan worden geïmporteerd.
  - **Directe synchronisatie:** CLOM leest/schrijft direct naar MO2’s bestanden en kan commando’s sturen om mods te activeren/deactiveren.
- Functies: mods aan/uit zetten, loadorder live aanpassen, archiveren, conflicten oplossen.
- Interface: optie *“Koppel met MO2”* met statusindicator *Verbonden / Niet verbonden*.

### MO2 Export Wizard
- Begeleidt gebruikers stap‑voor‑stap bij het exporteren van een CLOM‑profiel naar MO2‑formaat.
- Exporteert: modlijst, loadorder, tags/sterren, profielnotities, archiefstatus (optioneel).
- Interface: tabblad **MO2 Export Wizard**.
- Stappen:
  - Kies profiel
  - Kies exporttype (.txt, .json, .ini)
  - Genereer bestand
- Optie: export direct openen in MO2 (indien gekoppeld).

## 📊 6. Logging & Backups

### Logboekfunctie
- Houdt alle acties bij: scans, conflictoplossingen, profielwissels, exports.
- Logbestand in leesbaar formaat (`.txt` of `.log`).
- Filteropties: per datum, per profiel, per mod.
- Optie om log te exporteren of te delen bij bugreports.

### Automatische Backups
- Back‑ups van modmap, profielen, configuratiebestanden.
- Instelbare frequentie: dagelijks, wekelijks, maandelijks.
- Back‑ups worden opgeslagen in een aparte map of cloudlocatie.
- Statusindicator in de interface: laatste backup, volgende geplande backup.

### Herstelopties
- Herstel naar laatste werkende configuratie.
- Herstel naar fabrieksinstellingen (reset naar standaard).
- Optie om specifieke backup te selecteren en terug te zetten.
- Logt elke herstelactie in het logboek.

### Synchronisatie (lokaal/cloud)
- Synchronisatie van profielen en instellingen tussen apparaten.
- Ondersteuning voor lokale opslag, OneDrive of andere cloudservices.
- Optie om automatische sync in/uit te schakelen.
- Conflictdetectie bij verschillende versies van hetzelfde profiel.

## 📈 7. Performance & Optimalisatie

### Mod Performance Profiler
- Meet per mod:
  - FPS‑impact (gemiddeld en piek)
  - RAM/VRAM‑gebruik
  - AssetImpact (aantal bestanden, textures, meshes, AI‑scripts)
  - Trigger‑frequentie van scripts of routines
- Interface:
  - Tabblad **Performance Profiler**
  - Impactscore (1–5) met kleurcodering (🟢 laag, 🟡 gemiddeld, 🔴 hoog)
  - Suggesties: *“Gebruik lichtere variant”*, *“Alleen in RTX preset”*
  - Sorteren op impact, tags of groepen
- Slimme integratie:
  - Waarschuwingen bij zware combinaties in Launch Presets
  - Monitoring van totale impact per profiel
  - Logs in Kalender (performance per sessie)
  - Notificatie bij detectie van zware nieuwe mod
  - Performance meewegen in Conflict Resolver
- Handleiding:
  - Uitleg interpretatie scores
  - Tips om impact te verlagen
  - Advies voor low‑end vs high‑end systemen

### Optimalisatie‑adviezen
- Automatische aanbevelingen op basis van profiler‑data.
- Voorbeelden:
  - *“Vervang mod X door lichtere variant Y”*
  - *“Schakel mod Z alleen in bij RTX preset”*
  - *“Overweeg texture‑compressie voor mod A”*
- Adviezen worden weergegeven in een apart paneel en gelogd in het logboek.

## ⚙️ 8. Instellingen & Ondersteuning

### Geavanceerde Instellingen
- Filters, Nexus API‑sleutel, back‑upfrequentie, debug‑opties.
- Alleen zichtbaar in **Advanced Mode**.
- Optie om experimentele functies aan/uit te zetten.
- Waarschuwing bij gebruik van risicovolle instellingen.

### Configuratiebestand
- Export/import van instellingen naar `.clmconfig`.
- Handig voor delen, back‑ups en herstel.
- Bestand bevat: thema, taal, profielen, Nexus API, notificatievoorkeuren.
- Optie om configuratie te versleutelen.

### Reset naar standaardinstellingen
- Herstel naar fabrieksinstellingen.
- Optie: herstel naar laatste werkende configuratie.
- Logt elke reset in sessielogboek.
- Bevestigingsdialoog om per ongeluk resetten te voorkomen.

### Productdetails
- Versie‑informatie, licentie, credits.
- Links naar GitHub, Nexus, changelog.
- Tabblad **Over CLOM** in de interface.
- Optie om changelog direct in de app te bekijken.

## 🌍 9. Inspiratie & Toekomst

### Inspiratie uit andere software
- **Teksteditors**: undo/redo, zoek & vervang, thema’s, plug‑ins.
- **G’MIC (image filters)**: modulaire filters, uitbreidbare pipeline.
- **Minecraft toolkits**: profielen, presets, community‑packs.
- **Health trackers**: statistieken, grafieken, trends.
- **Modem configuratie**: setup wizards, herstelopties, advanced settings.
- **Mod export/documentatie tools**: export wizard, validatie, freeze‑systemen.

### Roadmap
- **MVP (v0.1 – v0.2)**:
  - Moddetectie en loadorder
  - Profielen opslaan/laden
  - Basis conflict‑detectie
  - Export naar `.txt` en `.csv`
- **v0.3 – v0.4**:
  - Profielnotities en duplicator
  - Backup scheduler
  - Conflict resolver
  - Setup Wizard
  - Nexus API integratie
- **v0.5**:
  - Performance Profiler
  - Slimme aanbevelingen
  - Launch Presets
  - Community‑ready distributie
- **v1.0**:
  - Volledige MO2 integratie
  - Cloud synchronisatie
  - Uitgebreide statistieken en grafieken
  - Toegankelijkheidsopties
  - Community plug‑in systeem

### Nice‑to‑have ideeën
- Tekst‑naar‑spraak voor notificaties.
- Automatische vertaling van modbeschrijvingen.
- Integratie met Discord (statusupdates, meldingen).
- Export naar webdashboard.
- Community‑gedeelde profielen en presets.
- AI‑gestuurde aanbevelingen op basis van Nexus‑trends.
