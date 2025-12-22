
from pathlib import Path
import numpy as np
import pandas as pd

# Output a dataframe with for each current generator in the NEM, including its capacity, fuel type and smrc
# In excel, we want to create a chart of cumulative capacity (x-axis) and smrc (y-axis), color filled by fuel_type
# we want to compare this chart against the actual bids from generators 


# MMSDSM - DUID detail summary
# df_DUDETAILSUMMARY

# MMSDSM - DUID details
# df_DUDETAIL

# MMSDSM - emission factors
# df_CO2EII 

def main():

    # 1. load data
    DATA_DIR = Path.cwd() / 'data'

    df_DUDETAILSUMMARY = pd.read_csv(
        DATA_DIR / 'AEMO' / 'MMSDM' / 'PUBLIC_ARCHIVE#DUDETAILSUMMARY#FILE01#202511010000.CSV',
        skiprows=1, skipfooter=1, engine="python"
    ).iloc[:, 4:].pipe(parse_DUDETAILSUMMARY)

    df_DUDETAIL = pd.read_csv(
        DATA_DIR / 'AEMO' / 'MMSDM' / 'PUBLIC_ARCHIVE#DUDETAIL#FILE01#202511010000.CSV',
        skiprows=1, skipfooter=1, engine="python"
    ).iloc[:, 4:].pipe(parse_DUDETAIL)

    df_STATION = pd.read_csv(
        DATA_DIR / 'AEMO' / 'MMSDM' / 'PUBLIC_ARCHIVE#STATION#FILE01#202511010000.CSV',
        skiprows=1, skipfooter=1, engine="python"
    ).iloc[:, 4:].pipe(parse_STATION)

    df_CO2EII = pd.read_csv(
        DATA_DIR / 'AEMO' / 'MMSDM' / 'CO2EII_AVAILABLE_GENERATORS_2025_50_20251219110419.CSV',
        skiprows=1, skipfooter=1, engine="python"
    ).iloc[:, 4:].pipe(parse_CO2EII)

    df_VOM = pd.read_excel(
            DATA_DIR / 'AEMO' / 'IASR' / "2025-inputs-and-assumptions-workbook.xlsm", 
            sheet_name='Variable OPEX', 
            skiprows=5
        ).iloc[1:-4].loc[:, ['IASR ID', 'Power Station / Technology', 'Technology', 'Variable OPEX\n($/MWh sent out)1']].rename(
            columns= { 'IASR ID': 'IASR_ID', 'Power Station / Technology': 'name', 'Technology': 'technology', 'Variable OPEX\n($/MWh sent out)1': 'VOM ($/MWh)' }
        )

    # 2. join MMSDSM data (DUDETAILSUMMARY, DUDETAIL and CO2EII)

    # join DUDETAILSUMMARY, DUDETAIL and CO2EII
    df_g = df_DUDETAILSUMMARY.join(df_DUDETAIL, how = 'left')
    df_g['CO2E_EMISSIONS_FACTOR'] = df_CO2EII.groupby('DUID')['CO2E_EMISSIONS_FACTOR'].mean()
    df_g = df_g.join(df_CO2EII[['CO2E_ENERGY_SOURCE']], how='left')

    # merge in STATIONNAME
    df_g = pd.merge(df_g, df_STATION[['STATIONNAME']], left_on='STATIONID', right_index=True)

    # AEMO use some DUIDs to represent dummy generators (DG_) and reserve traders (RT_)
    # we also want to filter any out dispatchable loads so the dataset is just GENERATORS
    mask = ~(df_g.index.str.startswith('DG_') | df_g.index.str.startswith('RT_') | (df_g['DISPATCHTYPE'] != 'GENERATOR'))
    df_g = df_g[mask].copy()

    # df_g.sort_index().reset_index().loc[:, ["DUID",
    #     "REGIONID",
    #     "CONNECTIONPOINTID",
    #     "STATIONID",
    #     "STATIONNAME",]].to_csv('gens.csv', index=False)

    # missing_ids = (
    #     # df_VOM.loc[~df_VOM["IASR_ID"].isin(df_g.index), "IASR_ID"].unique()
    #     df_g.index[~df_g.index.isin(df_VOM["IASR_ID"])].sort_values()
    # )

    # for i in missing_ids:
    #  print(i)

    

    

    # df_HEATRATE = pd.read_excel("2025-inputs-and-assumptions-workbook.xlsx", sheet_name='Heat rates', )

    # # df_FUELCOST = 

   
    # df = df_DUDETAILSUMMARY.join(df_DUDETAIL, how="left").join(df_CO2EII, how = 'left')

    # # 4. join IASR 2025 data via cross-reference keys

    # # 5. corrections (SWAN_E?)

    #     # remove dummary generators (DUIDs prefixed with DG_) and reserve traders (DUIDs prefixed with RT_)
        

    # 6. compute fuel types and smrc
    df_g = assign_fuel_type(df_g)
    # df_g = assign_srmc(df_g)

    # save output data
    df_g.sort_index().reset_index().to_csv('gens.csv', index=False)
    
    # produce table for plot
        # cumulative capacity (MW) | smrc for each fuel_type... 
        #                       0  | 10 [these two rows are one `duid`]
        #                       30 | 10

# In excel, we want to create a chart of cumulative capacity (x-axis) and smrc (y-axis), color filled by fuel_type


def parse_CO2EII(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates(subset=['DUID']).set_index('DUID')

def parse_DUDETAILSUMMARY(df: pd.DataFrame) -> pd.DataFrame:
    # AEMO use '2999/12/31 00:00:00' as the 'future sentinel' for END_DATE, which we can just filter for (e.g. all current DUIDs)
    mask = df['END_DATE'] == "2999/12/31 00:00:00"   
    
    # filter records that are after Jun 2017 (when there is MMSDM date) and subset columns
    cols = ['CONNECTIONPOINTID', 'REGIONID', 'STATIONID', 'PARTICIPANTID', 'TRANSMISSIONLOSSFACTOR',
            'DISTRIBUTIONLOSSFACTOR', 'SCHEDULE_TYPE', 'MIN_RAMP_RATE_UP', 'MIN_RAMP_RATE_DOWN',
            'MAX_RAMP_RATE_UP', 'MAX_RAMP_RATE_DOWN']

    return df.loc[mask].set_index('DUID').loc[:, cols]

def parse_DUDETAIL(df: pd.DataFrame) -> pd.DataFrame:
    # convert to datetime objects
    df['LASTCHANGED'] = pd.to_datetime(df['LASTCHANGED'])

    # sort by LASTCHANGED and drop duplicates (e.g. retain most recent record for each DUID)
    df = df.sort_values('LASTCHANGED', ascending=False).drop_duplicates(subset=['DUID'])

    # subset columns
    cols = ['VOLTLEVEL', 'REGISTEREDCAPACITY', 'AGCCAPABILITY', 'DISPATCHTYPE', 'MAXCAPACITY', 'STARTTYPE',
            'NORMALLYONFLAG', 'PHYSICALDETAILSFLAG', 'SPINNINGRESERVEFLAG', 'INTERMITTENTFLAG', 'SEMISCHEDULE_FLAG', 
            'MAXRATEOFCHANGEUP', 'MAXRATEOFCHANGEDOWN']
    
    return df.set_index('DUID').loc[:, cols]

def parse_STATION(df: pd.DataFrame) -> pd.DataFrame:
    # convert to datetime objects
    df['LASTCHANGED'] = pd.to_datetime(df['LASTCHANGED'])

    # sort by LASTCHANGED and drop duplicates (e.g. retain most recent record for each DUID)
    df = df.sort_values('LASTCHANGED', ascending=False).drop_duplicates(subset=['STATIONID'])
    
     # subset columns
    cols = ['STATIONNAME', 'ADDRESS1', 'ADDRESS2', 'ADDRESS3', 'ADDRESS4', 'CITY', 'STATE', 'POSTCODE']
    
    return df.set_index('STATIONID').loc[:, cols]

def assign_fuel_type(df: pd.DataFrame) -> pd.DataFrame:
    """Assigns a fuel category to each generator"""

    FUEL_TYPE_COLUMN = "FUEL_TYPE"

    # create fuel type field and default to nan   
    df[FUEL_TYPE_COLUMN] = None

    # set renewable types
    mask_renewables = df['CO2E_ENERGY_SOURCE'].isin(['Hydro', 'Solar', 'Wind'])
    df.loc[mask_renewables, FUEL_TYPE_COLUMN] = df.loc[mask_renewables, 'CO2E_ENERGY_SOURCE']

    # fossil fuel types
    mask_fossil = df['CO2E_ENERGY_SOURCE'].isin(['Diesel oil', 'Brown coal', 'Black coal', 'Kerosene - non aviation', 'Natural Gas (Pipeline)', 'Coal mine waste gas', 'Coal seam methane'])
    df.loc[mask_fossil, FUEL_TYPE_COLUMN] = 'Fossil'

    # biofuel types
    mask_biofuel = df['CO2E_ENERGY_SOURCE'].isin(['Landfill biogas methane', 'Bagasse', 'Biomass and industrial materials', 'Other Biofuels'])
    df.loc[mask_biofuel, FUEL_TYPE_COLUMN] = 'Biofuel'
    
    return df


def assign_srmc(df: pd.DataFrame) -> pd.DataFrame: 
    """Assigns a SRMC to each generator"""
    
    # SMRC [$/MWh] = VOM [$/MWh] + (Fuel cost [$/GJ] x Heat rate [GJ/MWh])
    # 

    FUEL_TYPE_COLUMN = "FUEL_TYPE"

    # Fossil units
    mask_fossil = df[FUEL_TYPE_COLUMN].isin(['Fossil'])
    df.loc[mask_fossil, 'SRMC'] = df.loc[mask_fossil, 'NTNDP_VOM ($/MWh)'] + (df.loc[mask_fossil, 'NTNDP_Heat Rate (GJ/MWh)'] * df.loc[mask_fossil, 'Fuel_Cost_2016-17'])

    # Renewable units
    mask_renewable = df[FUEL_TYPE_COLUMN].isin(['Solar', 'Hydro', 'Wind'])
    df.loc[mask_renewable, 'SRMC'] = df.loc[mask_renewable, 'NTNDP_VOM ($/MWh)']

    # If a wind generator but has no SRMC assigned
    mask_wind = (df[FUEL_TYPE_COLUMN] == 'Wind') & (pd.isnull(df['SRMC']))
    df.loc[mask_wind, 'SRMC'] = 0

    # If a hydro generator but has no SRMC assigned
    mask_hydro = (df[FUEL_TYPE_COLUMN] == 'Hydro') & (pd.isnull(df['SRMC']))
    df.loc[mask_hydro, 'SRMC'] = 7

    return df


if __name__ == "__main__":
    main()