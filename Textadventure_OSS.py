class Szene:
    def __init__(self, name, text, optionen = None):
        self.name = name
        self.text = text
        self.optionen = optionen





start = Szene("Start", "Du wächst in einer Hütte auf, wie du hierher gekommen bist weißt du nicht mehr, du erinnerst dich nur noch daran, dass du gestern Abend noch mit Freunden unterwegs warst. Also öffnest du die Tür der Hütte und siehst 2 mögliche Wege: Einmal ein Boot, welches am Strand gleich neben einem See liegt, der direkt neben deiner Hütte ist. Am anderen Ufer glaubst du ein Zelt zu erkennen. Du siehst auch einen Weg, der in einen Wald hineinführt, du siehst jedoch keine Hinweise wohin er führen könnte", {"1": {"beschreibung": "Das Boot zum anderen Ufer", "ziel": "see"},"2": {"beschreibung": "Den Weg in den Wald hinein", "ziel": "kreuzung"}})

see = Szene("See", "Du nimmst also die Ruder in die Hand und beginnst loszufahren. Nach dem du schon circa 1/3 des Weges hinter dir hast zieht plötzlich ein Gewitter auf", {"1": {"beschreibung": "Du drehst um und nimmst doch den Weg in den Wald", "ziel": "kreuzung"}, "2": {"beschreibung": "Du fährst trotzdem weiter in Richtung des Zeltes", "ziel": "ertrinken"}})

kreuzung = Szene("Kreuzung", "Nach einiger Zeit kommst du zu einer Wegkreuzung, beide Wege sind mit einem Schild beschriftet. Der eine führt zu einer kleinen Stadt, welche aber noch 20km weg ist. Der andere zu einem Gasthaus, welches nur 5km entfernt ist", {"1": {"beschreibung": "Du nimmst den längeren Weg in die Stadt", "ziel": "stadt"}, "2": {"beschreibung": "Du nimmst den kürzeren Weg ins Gasthaus", "ziel": "gasthaus"}})

ertrinken = Szene("Ertrinken", "Du fährst weiter und das Gewitter wird leider im stärker, als du es fast ans andere Ufer geschafft hast kippt dein Boot und du bist mitten im Wasser. Du schaffst es nicht dich irgendwo festzuhalten und ertrinkst schlussendlich im tiefen Gewässer")

stadt = Szene("Stadt", "Du bist jetzt schon lange Richtung Stadt unterwegs, als plötzlich Räuber aus dem Gebüsch springen. Sie bedrohen dich und nehmen alle deine Sachen. Das war es jetzt wohl für dich")

gasthaus = Szene("Gasthaus", "Nach gar nicht alzu langer Zeit erreichst du das Gasthaus. Dort wirst du von deinen Freunden überrascht die gerade zu Mittagessen. Gratuliere du hast deine Freunde wieder gefunden! Spiel geschafft")

szenen = {
    "start": start,
    "see": see,
    "kreuzung": kreuzung,
    "ertrinken": ertrinken,
    "stadt": stadt,
    "gasthaus": gasthaus
}


aktuelle_szene = szenen["start"]

while aktuelle_szene.optionen is not None:
    print(aktuelle_szene.text)
    for nummer, option in aktuelle_szene.optionen.items():
        print(f"{nummer}: {option['beschreibung']}")
    wahl = input()
    while wahl not in aktuelle_szene.optionen:
        wahl = input("Keine mögliche Option. Probiere nochmals: ")
    
    aktuelle_szene = szenen[aktuelle_szene.optionen[wahl]["ziel"]]
    





print(aktuelle_szene.text)
