# Growth Analytics — Retenção e Engajamento

Projeto autoral de portfólio, inspirado em desafios comuns de análise de produto. **Não contém dados, código ou documentação de processos seletivos ou empresas.**


## Contexto do projeto

Este projeto simula a análise de engajamento de usuários de um jogo digital fictício de palavras, baseado em desafios diários.

A proposta é investigar padrões de comportamento que possam contribuir para a formulação de hipóteses de produto e estratégias de Growth Analytics.

A base contém 2.500 registros sintéticos gerados em Python. Nenhum dado representa usuários reais ou resultados de empresas.

## Objetivo

Investigar a associação entre características de uso e indicadores simulados de retorno e atividade dos usuários, considerando:

- Abertura de newsletter;
- Período do dia;
- Sequência de dias consecutivos de atividade (*streak*);
- Retorno no dia seguinte (D+1);
- Atividade no marco de 30 dias (D30).

Os resultados são exploratórios e não permitem estabelecer relações de causalidade.


## Metodologia

A análise utiliza uma base de 2.500 registros sintéticos, gerada por meio de um script Python.

Cada registro representa um usuário fictício, com as seguintes variáveis:

| Variável | Descrição |
|---|---|
| `user_id` | Identificador único do usuário |
| `periodo` | Período do dia: manhã, tarde ou noite |
| `abriu_newsletter` | Indicador de abertura da newsletter (0 = não; 1 = sim) |
| `streak` | Número simulado de dias consecutivos de atividade |
| `retorno_d1` | Indicador simulado de retorno no dia seguinte (0 = não; 1 = sim) |
| `ativo_d30` | Indicador simulado de atividade no marco de 30 dias (0 = não; 1 = sim) |

### Cálculo dos indicadores

As taxas são calculadas por meio da média de variáveis binárias (0 e 1), utilizando a biblioteca pandas.

As comparações entre segmentos são realizadas com `groupby()`, seguido de agregações para obter a média (`mean`) e a quantidade de registros (`count`).

### Limitações

- Os dados são inteiramente sintéticos.
- Os indicadores D+1 e D30 são simulados, não calculados a partir de eventos reais.
- A base não contém datas de cadastro ou histórico de eventos para construir coortes reais de retenção.
- As associações observadas não demonstram relações de causa e efeito.


## Resultados da análise exploratória

A análise foi realizada sobre 2.500 registros sintéticos.

### Indicadores gerais

| Indicador | Resultado |
|---|---:|
| Usuários únicos | 2.500 |
| Retorno D+1 (simulado) | 19,1% |
| Atividade D30 (simulada) | 28,7% |

### Abertura da newsletter

| Grupo | Usuários | Atividade D30 |
|---|---:|---:|
| Não abriu a newsletter | 1.632 | 26,7% |
| Abriu a newsletter | 868 | 32,4% |

Os usuários que abriram a newsletter apresentaram atividade D30 aproximadamente 5,7 pontos percentuais superior à dos usuários que não abriram.

Essa diferença representa uma associação observada na base sintética e não comprova que a abertura da newsletter aumente a atividade.

### Período do dia

| Período | Usuários | Atividade D30 |
|---|---:|---:|
| Manhã | 847 | 31,4% |
| Noite | 826 | 28,3% |
| Tarde | 827 | 26,2% |

O período da manhã apresentou a maior taxa simulada de atividade D30, com diferença de aproximadamente 5,2 pontos percentuais em relação à tarde.

### Sequência de atividade (streak)

| Streak | Usuários | Retorno D+1 |
|---|---:|---:|
| 1 dia | 485 | 12,4% |
| 2 dias | 501 | 17,6% |
| 3 dias | 541 | 18,5% |
| 4 dias | 506 | 22,3% |
| 5 dias | 467 | 24,8% |

Os usuários com streak de cinco dias apresentaram taxa simulada de retorno D+1 aproximadamente duas vezes maior que os usuários com streak de um dia.

Esse resultado não demonstra que aumentar o streak cause maior retenção.

### Principais hipóteses para investigação

1. A abertura da newsletter pode estar associada a diferentes níveis de engajamento prévio.
2. O período do dia pode ajudar a identificar padrões de comportamento dos usuários.
3. Incentivos à formação de hábitos podem ser investigados como possíveis estratégias de retorno.

Essas hipóteses precisam de validação adicional antes de orientar decisões de produto.

## Estrutura
- `src/gerar_dados.py`: gera dados **100% sintéticos**
- `src/analisar.py`: calcula métricas e associações ilustrativas
- `data/`: arquivos gerados localmente, ignorados pelo Git

## Executar
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/gerar_dados.py
python src/analisar.py
```

## Próximos passos
1. Definir formalmente as métricas e coortes de retenção.
2. Adicionar análise SQL e testes estatísticos com checagem de pressupostos.
3. Criar visualizações e dashboard com dados sintéticos.
4. Propor desenho experimental A/B (hipótese, unidade de randomização, métrica primária e duração).

> Nota: associações observacionais não demonstram causalidade. Os dados simulados não representam resultados reais de nenhuma empresa.
