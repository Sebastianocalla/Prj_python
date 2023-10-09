# importo le librerie utili
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importo il csv arrivi_agriturismo
df_arr_agri = pd.read_csv('/content/drive/MyDrive/Ai Machine Learning/Colab Notebooks/Dataset/Arrivi-negli-agriturismi-in-Italia-per-regione.csv',encoding ='latin')

# importo il csv presenze_agriturismo
df_prs_agri = pd.read_csv('/content/drive/MyDrive/Ai Machine Learning/Colab Notebooks/Dataset/Presenze-negli-agriturismi-in-Italia-per-regione.csv',encoding ='latin')

# importo il csv arrivi_esercizi_alb
df_arr_eser = pd.read_csv('/content/drive/MyDrive/Ai Machine Learning/Colab Notebooks/Dataset/Arrivi-negli-esercizi-alberghieri-in-Italia-per-regione.csv',encoding ='latin')

# importo il csv presenze_esercizi_alb
df_prs_eser = pd.read_csv('/content/drive/MyDrive/Ai Machine Learning/Colab Notebooks/Dataset/Presenze-negli-esercizi-alberghieri-in-Italia-per-regione.csv',encoding ='latin')

# importo il csv arrivi_campeggio
df_arr_camp = pd.read_csv('/content/drive/MyDrive/Ai Machine Learning/Colab Notebooks/Dataset/Arrivi-nei-campeggi-e-villaggi-turistici-in-italia-per-regione.csv',encoding ='latin')

# importo il csv presenze_campeggio
df_prs_camp = pd.read_csv('/content/drive/MyDrive/Ai Machine Learning/Colab Notebooks/Dataset/Presenze-nei-campeggi-e-villaggi-turistici-in-italia-per-regione.csv',encoding ='latin')


# creazione tabelle
