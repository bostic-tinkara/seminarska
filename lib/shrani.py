# shrani podatke v datoteko CSV

import os
import csv

def shrani_csv(podatki):
    """
    Podatke iz seznama slovarjev shrani v datoteko CSV.
    """
    with open(os.path.join("podatki", "podatki.csv"), "w", encoding="utf8") as dat:
        pisatelj = csv.writer(dat)

        pisatelj.writerow(
            [
                "id",
                "znamenitost",
                "kategorija",
                "drzave",
                "kontinenti",
                "leto vpisa",
                "povrsina [ha]",
                "kriteriji",
            ]
        )

        for znamenitost in podatki:
            pisatelj.writerow(
                [
                    znamenitost["id"],
                    znamenitost["znamenitost"],
                    znamenitost["kategorija"],
                    znamenitost["drzave"],
                    znamenitost["kontinenti"],
                    znamenitost["leto vpisa"],
                    znamenitost["povrsina"],
                    znamenitost["kriteriji"],
                ]
            )
