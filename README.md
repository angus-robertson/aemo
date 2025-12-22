# Introduction to energy markets and the National Electricity Market (NEM)

This repository contains all the supporting data, analysis and visualisations for the **"Introduction to Energy Markets and the National Electricity Market"** presentation. The materials are intended to provide a comprehensive overview of energy market fundamentals, market operations, and key insights into the Australian National Electricity Market (NEM).


## Getting started

1. Clone the repository 
```bash
git clone https://github.com/angus-robertson/aemo.git && cd aemo
```

2. Setup the environment with UV
- install [uv](https://github.com/astral-sh/uv) (if not already installed)
- install dependencies 
```bash
uv sync
```

3. Run scripts
```bash
uv run src/6_smrc_stack/main.py
```

## Contents

1. Map of key electricity grids in Australia + key stats

NEM, SWIS, NWIS, DKIS, NWPS

- installed capacity (GW)
- demand (TWh/yr)
- transmission lines (km)
- distribution lines (km)
- market structure (energy/capacity market, spot/day-ahead/bilateral contract, gross/net pooled, bilateral, single buyer)
- regulatory bodies
- market operator


2. Map of the NEM + 5 regions
purpose: key overview and history of the NEM

3. Governance of the NEM
- diagram showing governance relationships and key legislation

4. Market participants of the NEM
purpose: market-based vs monopology 
- diagram of value chain (e.g. generators, transmission, distribution, retail, consumers)

5. Bid stack for the NEM 

6. SRMC stack for the NEM

5. LCOE date for different technologies

