# 10.24._karatavas
#Petra Pildava 12.B
#02.10.24. - ...

" " "
Spēles apraksts
" " "

Mērķis: Izveidot strādājošu 'Karātavu' spēli. 
Papildus mērķis: Ja izdodas uzprogrammēt strādājošu spēli uztaisīt logu kurā spēle tiek raidīta. (Spēle tiek spēlēta nevis "run python file", bet atsevišķā logā.)

Spēles gaita: Programma sasveicinās ar spēlētāju un aicina izvēlēties tēmu no kuras tā randomā izvēlēsies vienu vārdu, tad aicinās spēlētāju minēt burtus. Ja burts ir vārdā ieliek to uz svītras, ja nav pareizs noliek to malā, lai spēlētājs var redzēt kādi burti jau ir minēti.

Uzvaras nosacījumi: Spēlētājs uzvar ja vārds tiek uzminēts pirms cilvēciņš ir pakārts.

Zaudēšanas nosacījumi: Spēlētājs zaudē, ja vārds nav uzminēts un cilvēciņs ir pakārts.


" " "
Komponentes
" " " 

Vārdu saraksts, izvēle: Programma randomā izvēlēsies vienu tēmu, kura tiks pateikta spēlētājam, no kuras izvēlēsies vienu vārdu.
Tēmas nosaukums,vārdi -  'Programmēšanas valodas': python, ruby, JavaScript, PHP, pascal.
                          'Galda spēles': Cirks, Riču Raču, Domino, Bingo, Kuģu kaujas, Šahs, Dambrete
                          'Valstis': Latvija, Vācija, Japāna, Amerika, Itālija, Zviedrija, Turcija
                          'Latvijas prezidenti': Egils Levits, Andris Bērziņš, Vaira Vīķe-Freiberga, Guntis Ulmanis, Jānis Čakste

Informācijas ievade:

Spēles attēlojums (stāvoklis):
karātavu attēlojums: 
hangman = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
      +---+
      |   |
      o   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  | 
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  |
     / \  |
          |
    =========
    """
]

Spēles darbības (plūsma): Programma sasveicinās ar spēlētāju un aicina izvēlēties tēmu no kuras tā randomā izvēlēsies vienu vārdu, tad aicinās spēlētāju minēt burtus. Ja burts ir vārdā ieliek to uz svītras, ja nav pareizs noliek to malā, lai spēlētājs var redzēt kādi burti jau ir minēti un tā kamēr vārds ir uzminēts vai cilvēciņš pakārts. Kad spēle beigusies programma paziņo rezultātus, ja spēlētājs uzvarējis pasaka 'Tu esi uzvarējis! :)', bet ja zaudējis tad pasaka 'Tu esi zaudējis :('.

Spēles beigas: Ja spēlētājs ir uzvarējis programma pasaka 'Tu esi uzvarējis', bet ja zaudējis tad pasaka 'Tu esi zaudējis'.
