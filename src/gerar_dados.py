"""Gera um conjunto inteiramente fictício de eventos de usuários."""
from pathlib import Path
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 2500
periodo = rng.choice(["manha", "tarde", "noite"], size=n)
newsletter = rng.binomial(1, 0.35, n)
streak = rng.integers(1, 6, n)
# Parâmetros hipotéticos para fins didáticos, sem relação com dados reais.
p_d1 = np.clip(0.12 + 0.025 * streak + 0.035 * (periodo == "manha"), 0, 1)
p_d30 = np.clip(0.15 + 0.04 * streak + 0.06 * newsletter, 0, 1)
df = pd.DataFrame({"user_id": np.arange(1,n+1), "periodo": periodo, "abriu_newsletter": newsletter, "streak": streak, "retorno_d1": rng.binomial(1,p_d1), "ativo_d30": rng.binomial(1,p_d30)})
p = Path(__file__).resolve().parents[1] / "data" / "usuarios_sinteticos.csv"
df.to_csv(p, index=False)
print(f"Criados {len(df)} registros sintéticos em {p}")
