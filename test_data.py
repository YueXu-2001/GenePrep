import os
import pandas as pd

def test_geo_data_exists():
    files = os.listdir("tests/data/GEO")
    assert len(files) > 0, "No files found in GEO folder"
    df = pd.read_csv(f"tests/data/GEO/{files[0]}")
    assert not df.empty, "GEO dataset is empty"

def test_tcga_data_exists():
    files = os.listdir("tests/data/TCGA")
    assert len(files) > 0, "No files found in TCGA folder"
    df = pd.read_csv(f"tests/data/TCGA/{files[0]}")
    assert not df.empty, "TCGA dataset is empty"
