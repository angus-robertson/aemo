def main():
    print("Hello from generator!")


if __name__ == "__main__":
    main()


import pandas as pd

def parse_DUDETAILSUMMARY(df):
    """Extract DUID information from DUDETAILSUMMARY"""

    # convert to datetime objects
    df['START_DATE'] = pd.to_datetime(df['START_DATE'])
    df['END_DATE'] = pd.to_datetime(df['START_DATE'])

    # sort by end date and drop duplicates (e.g. retain most recent record) 
    df = df.sort_values('END_DATE', ascending = False).drop_duplicates(subset=['DUID'])

    # discard DUIDs that are no longer within the dataset
    mask = df['END_DATE'] >= '2025-11-01 00:00:00'

    # columns to keep
    cols = ['CONNECTIONPOINTID', 'REGIONID', 'STATIONID', 'PARTICIPANTID', 'TRANSMISSIONLOSSFACTOR',
            'DISTRIBUTIONLOSSFACTOR', 'SCHEDULE_TYPE', 'MIN_RAMP_RATE_UP', 'MIN_RAMP_RATE_DOWN',
            'MAX_RAMP_RATE_UP', 'MAX_RAMP_RATE_DOWN']
 
    return df.loc[mask].set_index('DIUD').loc[:, cols]

