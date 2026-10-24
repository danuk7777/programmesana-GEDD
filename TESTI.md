
# Algoritma testi

## Programmas apraksts

Fails: `04_summa_lidz_n.py`

Programma aprēķina visu veselo skaitļu summu no 1 līdz n.
Lietotājs ievada pozitīvu veselu skaitli n.
Cikls `for` pieskaita katru skaitli mainīgajam `summa`.
Ja ievade nav vesels skaitlis vai n nav pozitīvs, programma parāda kļūdas paziņojumu.

## Izpildes izsekošana

Piemērs: n = 5

| Solis | skaitlis | summa pirms | Darbība | summa pēc |
|---|---:|---:|---|---:|
| Sākums | — | — | summa = 0 | 0 |
| 1 | 1 | 0 | 0 + 1 | 1 |
| 2 | 2 | 1 | 1 + 2 | 3 |
| 3 | 3 | 3 | 3 + 3 | 6 |
| 4 | 4 | 6 | 6 + 4 | 10 |
| 5 | 5 | 10 | 10 + 5 | 15 |

Sagaidāmais rezultāts: 15.

## Testu piemēri

| Testa veids | Ievade | Sagaidāmais rezultāts | Faktiskais rezultāts | Tests izturēts? |
|---|---|---|---|---|
| Tipisks | 5 | 15 | 15 | Jā |
| Robežgadījums | 1 | 1 | 1 | Jā |
| Nederīga vērtība | abc | Kļūdas paziņojums | Jāievada vesels skaitlis | Jā |
| Robežgadījums | 0 | Kļūdas paziņojums | Skaitlim jābūt lielākam par 0 | Jā |
| Negatīva vērtība | -3 | Kļūdas paziņojums | Skaitlim jābūt lielākam par 0 | Jā |

## Kļūda vai uzlabojums

Programma pārbauda, vai n ir pozitīvs, pirms sāk summēšanu.
Tādējādi netiek aprēķināta summa nederīgai ievadei.
Papildu pārbaude: tukša ievade arī jāapstrādā ar ValueError.
