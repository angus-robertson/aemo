# Introduction to energy markets and the National Electricity Market (NEM)

This repository contains all the supporting data, analysis and visualisations for the **Introduction to Energy Markets and the National Electricity Market** presentation. The materials are intended to provide a comprehensive overview of energy market fundamentals, market operations, and key insights into the Australian National Electricity Market (NEM).


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
 
### Charts

#### 1. Electricity consumption per capita vs GDP per capita (TODO)


#### 2. Map of Australia's electricity grids (TODO)
Map showing the geographic location of key electricity grids, including: NEM, SWIS, NWIS, DKIS, NWPS.

Should be accompanied by a supporting table, including:
- installed capacity (GW)
- demand (TWh/yr)
- transmission lines (km)
- distribution lines (km)
- market structure (energy/capacity market, spot/day-ahead/bilateral contract, gross/net pooled, bilateral, single buyer)
- regulatory bodies
- market operator

#### 3. Detailed map of the NEM (TODO)
Map showing the NEM regions and interconnectors.


#### 4. Bid stack for the NEM
Chart showing an actual bid stack a given 5-minute interval in the NEM. 
- x-axis: cumulative bids (MW), y-axis: offer price ($/MWh), colored by fuel type

#### 5. SRMC stack NEM generators
Chart showing the estimated SMRC stack for current generators in the NEM (perhaps could match generators the were operating in the selected 5-minute window above, but does introduction some fuel cost timeing issues). 
- x-axis: cumulative bids (MW), y-axis: SMRC ($/MWh), colored by fuel type

#### 6. Installed generation capacity
Stacked bar chart showing installed generation capacity by technology over time.
- x-axis: time (years), y-axis: installed capacity (GW), colored by fuel type

#### 7. Dispatched electricity by technology
Stacked bar chart showing dispatched electricity by technology over time.
- x-axis: time (years), y-axis: dispatched capacity (GW), colored by fuel type

#### 8. Price setting by technology
Stacked bar chart showing price setter by technology over time.
- x-axis: time (years), y-axis: percentage of time price setter, colored by fuel type

#### 8. LCOEs for different technologies


### Other charts

- weather dependency of renewables? (dispatchable vs non, limited by weather dependence). See NEM review for inspiration.
- emissions reduction targets and electricity share of emissions
- emissions intensity of generators in the NEM? 
- capacity factors / LCOEs for various technologies
- average availability of coal capacity by age of generator, % availability
- monthly average whole prices, A$/MWh
- coal capacity and scheduled retirements
- duck curve
- transmission ISP projects 

