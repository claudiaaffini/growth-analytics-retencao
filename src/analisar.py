"""Métricas ilustrativas; não inferir causalidade a partir delas."""
from pathlib import Path
import pandas as pd

p = Path(__file__).resolve().parents[1] / "data" / "usuarios_sinteticos.csv"
df = pd.read_csv(p)
print("Usuários:", df.user_id.nunique())
print("Retenção D+1 (simulada):", f"{df.retorno_d1.mean():.1%}")
print("Atividade D30 (simulada):", f"{df.ativo_d30.mean():.1%}")
print("\nD30 por abertura de newsletter (associação simulada):")
print(df.groupby("abriu_newsletter").ativo_d30.agg(["mean", "count"]))


print("\nAtividade D30 por período do dia:")
print(df.groupby("periodo").ativo_d30.agg(["mean", "count"]))
print("\nRetenção D+1 por streak:")
print(df.groupby("streak").retorno_d1.agg(["mean", "count"]))