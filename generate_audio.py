# Run: pip install gtts
# Then: python generate_audio.py
# It creates an 'audio/' folder with all MP3 files.

from gtts import gTTS
import os
import time

os.makedirs('audio', exist_ok=True)

listening_sets = [
    {   # Set 1
        "teil1": [
            "Guten Tag, hier ist die Praxis Dr. Müller. Wir bestätigen Ihren Termin morgen um 10 Uhr. Bitte bringen Sie Ihre Versicherungskarte mit. Wenn Sie nicht kommen können, rufen Sie bitte an.",
            "Achtung Reisende! Der Zug IC 123 nach Hamburg hat heute 20 Minuten Verspätung. Er fährt jetzt um 14:35 Uhr von Gleis 7 ab. Wir bitten um Entschuldigung.",
            "Hier spricht Maria. Ich bin krank und komme heute nicht zur Arbeit. Ich habe Fieber und muss zum Arzt gehen. Ich rufe morgen wieder an.",
            "Willkommen im Hotel Seeblick. Ihr Zimmer ist 304 im dritten Stock. Das Frühstück ist von 7 bis 10 Uhr im Restaurant. WLAN-Passwort: Seeblick2024.",
            "Liebe Kunden, unser Supermarkt hat ab Montag neue Öffnungszeiten. Wir sind jetzt von 8 bis 22 Uhr geöffnet. Sonntags bleiben wir geschlossen."
        ],
        "teil2": "Hallo Anna, hast du schon Pläne für die Woche? Am Montag habe ich Tanzkurs, aber der Lehrer ist krank. Dienstag gehen wir ins Kino. Mittwoch treffen wir uns mit Maria zum Essen. Donnerstag mache ich Sport. Freitag habe ich Geburtstag und wir feiern im Restaurant.",
        "teil3": [
            "Was hast du gestern Abend gegessen?",
            "Wohin fährst du in den Urlaub?",
            "Wann treffen wir uns?",
            "Was schenkst du deiner Mutter zum Geburtstag?",
            "Wie kommst du zur Arbeit?"
        ],
        "teil4": "Im Interview: Frau Schmidt, Sie sind seit 20 Jahren Lehrerin. Was gefällt Ihnen an Ihrem Beruf? Ich arbeite gerne mit Kindern. Es macht Spaß, ihnen etwas beizubringen. Aber manchmal ist es auch stressig. Die Klassen sind oft zu groß. Trotzdem bereue ich nichts."
    },
    {   # Set 2
        "teil1": [
            "Guten Tag, hier ist das Restaurant Bella Italia. Ihre Reservierung für heute Abend um 19:30 Uhr ist bestätigt. Wir haben einen Tisch für 4 Personen. Bis später!",
            "Achtung! Die Autobahn A3 ist zwischen Ausfahrt 45 und 46 wegen Bauarbeiten gesperrt. Bitte nutzen Sie die Umleitung über die B12. Die Sperrung dauert bis morgen 18 Uhr.",
            "Hallo, hier ist die Apotheke am Markt. Ihre Medikamente sind abholbereit. Wir haben heute bis 20 Uhr geöffnet. Bitte bringen Sie das Rezept mit.",
            "Liebe Gäste, der Film 'Der Berg' beginnt um 20:15 Uhr in Saal 3. Bitte kommen Sie 15 Minuten früher. Popcorn und Getränke gibt es im Foyer.",
            "Willkommen bei der Bahn. Ihr Zug nach München fährt heute von Gleis 12. Der Zug ist pünktlich. Viel Spaß in München!"
        ],
        "teil2": "Hallo Klaus, wie war deine Woche? Am Montag war ich beim Zahnarzt. Dienstag habe ich meine Schwester besucht. Mittwoch war ich shoppen. Donnerstag habe ich im Garten gearbeitet. Freitag war ich im Schwimmbad.",
        "teil3": [
            "Was machst du am Wochenende?",
            "Wo warst du gestern?",
            "Wie findest du das neue Restaurant?",
            "Wann hast du Geburtstag?",
            "Was möchtest du trinken?"
        ],
        "teil4": "Herr Weber, Sie sind Geschäftsführer einer großen Firma. Wie sieht Ihr typischer Arbeitstag aus? Ich beginne um 7 Uhr mit E-Mails. Dann habe ich Meetings. Um 13 Uhr esse ich Mittag. Nachmittags arbeite ich an Strategien. Ich ende meistens um 19 Uhr."
    },
    {   # Set 3
        "teil1": [
            "Guten Tag, hier spricht Frau Müller vom Kindergarten Sonnenschein. Ihr Kind kann ab nächstem Monat bei uns anfangen. Die Eingewöhnung ist am 3. September um 9 Uhr. Bitte bringen Sie Hausschuhe und Wechselkleidung mit.",
            "Achtung Fahrgäste! Wegen einer technischen Störung fällt die U-Bahn Linie 4 zwischen Hauptbahnhof und Rathaus aus. Bitte nutzen Sie die Buslinie 12 als Ersatz.",
            "Hallo, hier ist Peter. Ich bin im Krankenhaus. Ich hatte einen kleinen Unfall mit dem Fahrrad. Nichts Schlimmes, aber der Arzt sagt, ich muss zwei Tage hier bleiben.",
            "Willkommen in der Sprachschule EuroLingua. Ihr Kurs 'Deutsch A2' beginnt am Dienstag, den 10. Oktober, um 18 Uhr im Raum 305. Wir freuen uns auf Sie!",
            "Liebe Kunden, ab sofort haben wir in unserem Supermarkt eine neue Backabteilung. Frisches Brot und Brötchen gibt es täglich ab 6 Uhr. Sonntags ab 8 Uhr."
        ],
        "teil2": "Hallo Sarah, was machst du diese Woche? Montag gehe ich zum Friseur. Dienstag habe ich einen Termin beim Arzt. Mittwoch lerne ich für die Prüfung. Donnerstag gehe ich ins Fitnessstudio. Freitag koche ich für meine Freunde.",
        "teil3": [
            "Wie war dein Urlaub?",
            "Was machst du beruflich?",
            "Wo wohnst du jetzt?",
            "Wie oft gehst du sporteln?",
            "Was möchtest du zum Geburtstag?"
        ],
        "teil4": "Frau Hoffmann, Sie sind seit 30 Jahren Bäckerin. Warum haben Sie diesen Beruf gewählt? Ich liebe es, Brot zu backen. Der Geruch von frischem Brot ist wunderbar. Aber die Arbeit ist hart. Ich stehe jeden Tag um 3 Uhr auf. Trotzdem würde ich nie etwas anderes machen."
    },
    {   # Set 4
        "teil1": [
            "Guten Tag, hier ist die Buchhandlung Leselust. Ihr bestelltes Buch ist angekommen. Sie können es bis Samstag abholen. Wir sind montags bis samstags von 9 bis 20 Uhr geöffnet.",
            "Achtung! Wegen starken Regens ist der Wanderweg auf den Berg gesperrt. Bitte nutzen Sie nur den asphaltierten Weg. Die Sperrung gilt bis auf Weiteres.",
            "Hallo Mama, ich bin gut in Köln angekommen. Das Wetter ist schön. Morgen besuche ich den Kölner Dom und am Wochenende gehe ich zu einer Party. Ich rufe dich am Sonntag an.",
            "Willkommen im Fitness-Center Power. Ihre Mitgliedschaft beginnt ab sofort. Sie können alle Geräte und Kurse nutzen. Bitte denken Sie an ein Handtuch und saubere Sportschuhe.",
            "Liebe Gäste, das Schwimmbad hat heute wegen einer Veranstaltung ab 16 Uhr geschlossen. Morgen sind wir wieder normal von 6 bis 22 Uhr geöffnet. Wir bitten um Verständnis."
        ],
        "teil2": "Hallo Maria, was hast du letzte Woche gemacht? Montag war ich im Museum. Dienstag habe ich gekocht. Mittwoch war ich shoppen. Donnerstag habe ich einen Film gesehen. Freitag war ich im Restaurant.",
        "teil3": [
            "Wie findest du das Wetter heute?",
            "Was hast du gestern gekauft?",
            "Wohin fährst du nächstes Wochenende?",
            "Wann hast du Zeit für ein Treffen?",
            "Was isst du am liebsten?"
        ],
        "teil4": "Herr Schmidt, Sie sind Polizist seit 25 Jahren. Was ist der schwierigste Teil Ihres Berufs? Die Nachtschichten sind sehr anstrengend. Aber am schwierigsten ist es, traurige Nachrichten an Familien zu überbringen. Trotzdem bin ich stolz auf meinen Beruf. Ich helfe den Menschen."
    },
    {   # Set 5
        "teil1": [
            "Guten Tag, hier ist die Reinigung Blitzblank. Ihre Kleidung ist fertig. Sie können sie ab sofort abholen. Wir haben montags bis freitags von 8 bis 18 Uhr und samstags von 9 bis 14 Uhr geöffnet.",
            "Achtung! Die Straße 'Hauptstraße' ist wegen eines Wasserrohrbruchs gesperrt. Die Feuerwehr ist vor Ort. Bitte meiden Sie diesen Bereich. Die Sperrung dauert voraussichtlich bis 20 Uhr.",
            "Hallo, hier ist die Tierarztpraxis. Ihr Hund Max hat morgen um 10:30 Uhr einen Termin. Bitte bringen Sie seinen Impfpass mit. Wenn Sie nicht kommen können, sagen Sie bitte bis heute 18 Uhr Bescheid.",
            "Willkommen im Theater am Markt. Das Stück 'Romeo und Julia' beginnt heute um 19:30 Uhr. Die Pause ist nach dem zweiten Akt. Getränke können Sie im Foyer kaufen.",
            "Liebe Gäste, unser Restaurant hat ab nächster Woche neue Öffnungszeiten. Wir sind dienstags bis sonntags von 11:30 bis 23 Uhr geöffnet. Montags haben wir Ruhetag."
        ],
        "teil2": "Hallo Tom, was hast du diese Woche vor? Montag gehe ich zum Zahnarzt. Dienstag habe ich Fußballtraining. Mittwoch lerne ich Deutsch. Donnerstag gehe ich ins Kino. Freitag habe ich Geburtstag.",
        "teil3": [
            "Wie war dein Tag?",
            "Was machst du in deiner Freizeit?",
            "Wohin gehst du heute Abend?",
            "Wann fährt dein Zug?",
            "Was möchtest du essen?"
        ],
        "teil4": "Frau Klein, Sie sind Krankenschwester. Was motiviert Sie in Ihrem Beruf? Ich möchte den Menschen helfen. Es ist schön, wenn Patienten sich bedanken. Aber die Schichtarbeit ist schwierig. Man verpasst oft Familienfeiern. Trotzdem liebe ich meinen Beruf."
    },
    {   # Set 6
        "teil1": [
            "Guten Tag, hier ist die Autowerkstatt Müller. Ihr Auto ist fertig. Die Reparatur hat 350 Euro gekostet. Sie können das Auto heute bis 18 Uhr abholen. Bitte bringen Sie den Schlüssel mit.",
            "Achtung Reisende! Der Bus Linie 15 hat heute eine geänderte Route. Er fährt nicht durch die Innenstadt, sondern über die Ringstraße. Die Haltestelle 'Markt' fällt aus.",
            "Hallo, hier ist Frau Schmidt. Ich kann heute leider nicht zum Kurs kommen. Mein Sohn ist krank und ich muss zu Hause bleiben. Ich komme nächste Woche wieder.",
            "Willkommen im Yoga-Studio Harmonie. Ihr Kurs 'Yoga für Anfänger' ist dienstags und donnerstags um 18 Uhr. Bitte kommen Sie 10 Minuten früher und bringen Sie bequeme Kleidung mit.",
            "Liebe Kunden, wir haben ab sofort eine neue Telefonnummer: 030-12345678. Die alte Nummer ist nicht mehr gültig. Sie erreichen uns montags bis freitags von 9 bis 17 Uhr."
        ],
        "teil2": "Hallo Lisa, wie war deine Woche? Montag war ich krank und zu Hause. Dienstag habe ich gearbeitet. Mittwoch war ich beim Friseur. Donnerstag habe ich meine Eltern besucht. Freitag war ich im Restaurant.",
        "teil3": [
            "Wie findest du den Film?",
            "Was hast du am Wochenende gemacht?",
            "Wohin möchtest du reisen?",
            "Wann beginnt die Party?",
            "Was schenkst du ihr?"
        ],
        "teil4": "Herr Braun, Sie sind Taxifahrer. Was gefällt Ihnen an Ihrem Job? Ich lerne viele interessante Menschen kennen. Jeder Tag ist anders. Aber der Verkehr in der Stadt ist sehr stressig. Besonders am Freitagabend. Trotzdem würde ich nie etwas anderes machen."
    },
    {   # Set 7
        "teil1": [
            "Guten Tag, hier ist die Praxis Dr. Weber. Wir müssen Ihren Termin verschieben. Statt morgen um 10 Uhr können wir Sie am Freitag um 14 Uhr empfangen. Passt Ihnen das?",
            "Achtung! Wegen eines Unfalls auf der A7 ist der Verkehr zwischen Ausfahrt 32 und 33 stark behindert. Es gibt einen Stau von etwa 5 Kilometern. Bitte nutzen Sie alternative Routen.",
            "Hallo, hier ist die Firma Müller. Ihre Lieferung kommt heute zwischen 14 und 16 Uhr. Bitte stellen Sie sicher, dass jemand zu Hause ist. Vielen Dank!",
            "Willkommen im Museum für Moderne Kunst. Die Sonderausstellung 'Farben' ist noch bis zum 30. September zu sehen. Öffnungszeiten: dienstags bis sonntags 10 bis 18 Uhr. Montags geschlossen.",
            "Liebe Gäste, das Konzert von Max Mustermann wurde vom Samstag auf den Sonntag verlegt. Beginn ist um 20 Uhr. Bereits gekaufte Tickets bleiben gültig."
        ],
        "teil2": "Hallo Klaus, was machst du diese Woche? Montag gehe ich zum Zahnarzt. Dienstag habe ich einen wichtigen Termin. Mittwoch lerne ich für die Prüfung. Donnerstag gehe ich ins Fitnessstudio. Freitag habe ich Geburtstag.",
        "teil3": [
            "Wie geht es dir?",
            "Was machst du beruflich?",
            "Wo warst du gestern?",
            "Wann fährt der Bus?",
            "Was möchtest du trinken?"
        ],
        "teil4": "Frau Groß, Sie sind Gärtnerin. Was ist das Schönste an Ihrem Beruf? Ich arbeite draußen in der Natur. Es ist wunderbar, Blumen wachsen zu sehen. Aber die Arbeit ist physisch anstrengend. Im Winter ist es auch kalt. Trotzdem liebe ich meinen Beruf."
    },
    {   # Set 8
        "teil1": [
            "Guten Tag, hier ist die Wäscherei Sauber. Ihre Wäsche ist fertig. Sie können sie ab morgen abholen. Wir sind montags bis samstags von 8 bis 19 Uhr geöffnet. Sonntags haben wir geschlossen.",
            "Achtung! Wegen eines Stromausfalls in der Innenstadt fällt die U-Bahn Linie 2 aus. Busse fahren als Ersatz. Die Störung wird voraussichtlich in zwei Stunden behoben.",
            "Hallo, hier ist die Tierpension. Ihr Hund Bella ist gut angekommen. Sie spielt gerne mit den anderen Hunden. Sie können sie ab Samstag abholen. Vielen Dank!",
            "Willkommen im Kurszentrum. Ihr Computerkurs 'Excel für Anfänger' beginnt am Montag, den 5. November, um 17 Uhr. Der Kurs dauert 4 Wochen. Bitte bringen Sie einen Laptop mit.",
            "Liebe Kunden, wir haben ab sofort eine neue Filiale in der Bahnhofstraße 45. Dort finden Sie alle unsere Produkte und einen kostenlosen Beratungsservice. Öffnungszeiten: 9 bis 20 Uhr."
        ],
        "teil2": "Hallo Anna, was hast du letzte Woche gemacht? Montag war ich im Büro. Dienstag habe ich eine Präsentation gehalten. Mittwoch war ich beim Kunden. Donnerstag habe ich im Homeoffice gearbeitet. Freitag war ich auf einer Messe.",
        "teil3": [
            "Wie war dein Urlaub?",
            "Was machst du am Wochenende?",
            "Wo wohnst du?",
            "Wann hast du Zeit?",
            "Was möchtest du essen?"
        ],
        "teil4": "Herr Weiß, Sie sind seit 40 Jahren Musiker. Was ist das Besondere an Musik? Musik verbindet Menschen. Es ist schön, wenn das Publikum applaudiert. Aber das Üben ist manchmal einsam. Trotzdem würde ich nie aufhören."
    },
    {   # Set 9
        "teil1": [
            "Guten Tag, hier ist die Optik Sehklar. Ihre neue Brille ist fertig. Sie können sie ab sofort abholen. Wir haben montags bis freitags von 9 bis 18 Uhr und samstags von 9 bis 14 Uhr geöffnet.",
            "Achtung! Wegen starken Windes ist die Fähre nach Amrum heute gesperrt. Die nächste Fähre fährt morgen um 8 Uhr. Wir bitten um Verständnis.",
            "Hallo, hier ist die Musikschule. Ihr Sohn kann ab nächster Woche im Klavierkurs anfangen. Der Kurs ist mittwochs um 16 Uhr. Bitte bringen Sie ein Notenheft mit.",
            "Willkommen im Hotel Bergblick. Ihr Zimmer 205 ist im zweiten Stock. Das Frühstück ist von 6:30 bis 10 Uhr im Restaurant. Der Wellnessbereich ist von 7 bis 22 Uhr geöffnet.",
            "Liebe Gäste, der Workshop 'Kochen für Anfänger' wurde von Dienstag auf Mittwoch verlegt. Beginn ist um 17 Uhr. Bereits angemeldete Teilnehmer behalten ihren Platz."
        ],
        "teil2": "Hallo Maria, wie war deine Woche? Montag war ich im Schwimmbad. Dienstag habe ich gekocht. Mittwoch war ich shoppen. Donnerstag habe ich einen Film gesehen. Freitag war ich im Restaurant.",
        "teil3": [
            "Wie findest du das Buch?",
            "Was hast du gestern gemacht?",
            "Wohin fährst du in den Urlaub?",
            "Wann treffen wir uns?",
            "Was schenkst du ihm?"
        ],
        "teil4": "Frau Schwarz, Sie sind Köchin. Was ist das Wichtigste beim Kochen? Frische Zutaten sind sehr wichtig. Es macht mir Spaß, neue Rezepte auszuprobieren. Aber die Arbeit in der Küche ist heiß und anstrengend. Trotzdem liebe ich meinen Beruf."
    },
    {   # Set 10
        "teil1": [
            "Guten Tag, hier ist die Schneiderei Maßarbeit. Ihr Anzug ist fertig. Sie können ihn ab Freitag abholen. Wir haben montags bis freitags von 9 bis 18 Uhr geöffnet. Samstags nur nach Termin.",
            "Achtung! Wegen eines Baum auf der Straße ist die Hauptstraße gesperrt. Die Feuerwehr ist vor Ort. Bitte nutzen Sie die Nebenstraße. Die Sperrung dauert voraussichtlich bis 16 Uhr.",
            "Hallo, hier ist die Tanzschule Eleganz. Ihr Kurs 'Walzer für Anfänger' beginnt am Dienstag, den 12. März, um 19 Uhr. Bitte bringen Sie bequeme Schuhe mit. Wir freuen uns auf Sie!",
            "Willkommen im Café Central. Ihre Reservierung für 6 Personen am Samstag um 15 Uhr ist bestätigt. Wir haben einen Tisch im Garten für Sie. Bei Regen sitzen Sie drinnen.",
            "Liebe Kunden, wir haben ab sofort neue Öffnungszeiten. Montag bis Freitag 10 bis 20 Uhr. Samstag 10 bis 18 Uhr. Sonntag geschlossen. Abholung von Online-Bestellungen jederzeit möglich."
        ],
        "teil2": "Hallo Tom, was hast du diese Woche gemacht? Montag war ich im Museum. Dienstag habe ich gekocht. Mittwoch war ich shoppen. Donnerstag habe ich einen Film gesehen. Freitag war ich auf einer Party.",
        "teil3": [
            "Wie geht es dir?",
            "Was machst du beruflich?",
            "Wo warst du gestern?",
            "Wann fährt dein Zug?",
            "Was möchtest du essen?"
        ],
        "teil4": "Herr Grün, Sie sind Architekt. Was ist das Schönste an Ihrem Beruf? Ich kann kreative Ideen verwirklichen. Es ist schön, ein fertiges Gebäude zu sehen. Aber die Planung dauert sehr lange. Trotzdem bin ich stolz auf meine Arbeit."
    }
]

def generate_audio():
    total = 0
    for set_idx, s in enumerate(listening_sets, 1):
        # Teil 1: 5 items
        for i, text in enumerate(s["teil1"], 1):
            tts = gTTS(text=text, lang='de', slow=False)
            tts.save(f'audio/set{set_idx}_teil1_q{i}.mp3')
            total += 1
            print(f"✓ Created: audio/set{set_idx}_teil1_q{i}.mp3")
            time.sleep(0.3)

        # Teil 2: 1 audio
        tts = gTTS(text=s["teil2"], lang='de', slow=False)
        tts.save(f'audio/set{set_idx}_teil2.mp3')
        total += 1
        print(f"✓ Created: audio/set{set_idx}_teil2.mp3")
        time.sleep(0.3)

        # Teil 3: 5 items
        for i, text in enumerate(s["teil3"], 1):
            tts = gTTS(text=text, lang='de', slow=False)
            tts.save(f'audio/set{set_idx}_teil3_q{i}.mp3')
            total += 1
            print(f"✓ Created: audio/set{set_idx}_teil3_q{i}.mp3")
            time.sleep(0.3)

        # Teil 4: 1 audio
        tts = gTTS(text=s["teil4"], lang='de', slow=False)
        tts.save(f'audio/set{set_idx}_teil4.mp3')
        total += 1
        print(f"✓ Created: audio/set{set_idx}_teil4.mp3")
        time.sleep(0.3)

    print(f"\n 🎉 Done! Created {total} audio files in 'audio/' folder.")
    print("Upload the 'audio/' folder + HTML file to GitHub Pages.")

if __name__ == "__main__":
    generate_audio()