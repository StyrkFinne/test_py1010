# -*- coding: utf-8 -*-
"""
Total kostnader - og kostnads differanse - for ELbil og Bensinbil pr år

Kodet onsdag Sep 16 2026

@author: Styrk Finne

"""

Km_pr_aar             = 10000  # kjørt km/år
Ant_dag_aar           = 365    # antall dager i året

Forsikring_ELbil      = 5000   # forsikring ELbil pr år
Forsikring_Bensinbil  = 7500   # forsikring Bensinbil pr år

Trafikk_forsikring    = 8.38   # Trafikkforsikrings avgift kr/dag

Strom_ELbil           = 0.2    # Strømforbruk kwh/km
Strom_pris            = 2.00   # Strømpris kr/kwh

Bensin                = 1.00   # Bensin kost kr/km

Bom_ELbil             = 0.1    # Bomavgift ELbil kr/km
Bom_Bensinbil         = 0.3    # Bomavgift bensinbil kr/km

# Total kostnad ELbil
Kostnad_ELbil         = Forsikring_ELbil + (Trafikk_forsikring * Ant_dag_aar) + (Strom_ELbil * Strom_pris * Km_pr_aar ) + (Bom_ELbil * Km_pr_aar )

# Total kostnad bensinbil
Kostnad_bensinbil     = Forsikring_Bensinbil + (Trafikk_forsikring * Ant_dag_aar) + (Bensin * Km_pr_aar) + (Bom_Bensinbil * Km_pr_aar )

# Differanse kostnad EL- og Bensin bil
Diff = Kostnad_bensinbil - Kostnad_ELbil 

# Print Beregnings resultat
print ("Kostnad EL bil     ", Kostnad_ELbil)
print ("Kostnad bensinbil  ", Kostnad_bensinbil)
print ("Kostnad differanse ", Diff)
