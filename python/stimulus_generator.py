from PIL import Image # Importiert die Image-Klasse aus der Pillow-Bibliothek, um Bilddateien öffnen und verarbeiten zu können

# Dateipfade
bild_pfad = 'armstrong.bmp'# Legt den Dateipfad des einzulesenden BMP-Bildes fest
ausgabe_pfad = 'armstrong_bin.txt' # Legt den Dateipfad der Ausgabedatei fest, in der die Binärdaten gespeichert werden

print("Lade Bild...") # Gibt eine Statusmeldung aus, dass das Bild geladen wird
img = Image.open(bild_pfad).convert('RGB') # Öffnet das Bild und wandelt es in das RGB-Format mit roten, grünen und blauen Farbwerten um
breite, hoehe = img.size # Liest die Größe des Bildes aus und speichert die Breite und Höhe in Pixeln

print("Konvertiere in Binärdaten...") # Gibt eine Statusmeldung aus, dass die Umwandlung in Binärdaten beginnt

with open(ausgabe_pfad, 'w') as f: # Öffnet die Ausgabedatei im Schreibmodus, damit die Binärdaten hineingeschrieben werden können
    for y in range(hoehe): # Durchläuft alle Bildzeilen von oben nach unten
        for x in range(breite): # Durchläuft alle Pixel einer Bildzeile von links nach rechts
            r, g, b = img.getpixel((x, y)) # Liest die RGB-Farbwerte des aktuellen Pixels an der Position x und y aus
            
            # RGB Werte in 8-Bit Binär umwandeln
            r_bin = format(r, '08b')
            g_bin = format(g, '08b')
            b_bin = format(b, '08b')
            
            # 24-Bit zusammenfügen und schreiben
            f.write(r_bin + g_bin + b_bin + '\n')

print(f"Fertig! Gespeichert als {ausgabe_pfad}") # Gibt eine Abschlussmeldung aus und zeigt den Speicherort der Ausgabedatei an
