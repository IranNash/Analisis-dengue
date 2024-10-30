from Analisis_descriptivo import dimen
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/IranNash/Analisis-dengue/refs/heads/main/dengue_abierto.csv')

def test_dimen():
    assert dimen(df) == 2