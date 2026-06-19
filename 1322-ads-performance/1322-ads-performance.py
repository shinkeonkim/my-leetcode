import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    ads = ads.groupby('ad_id')

    ads = ads.agg(
        clicked = ('action', lambda x : (x == 'Clicked').sum()),
        viewed = ('action', lambda x : (x == 'Viewed').sum())
    ).reset_index()
    
    ads['ctr'] = round(ads['clicked'] / (ads['clicked'] + ads['viewed']) * 100, 2)

    ads['ctr'] = ads['ctr'].fillna(0)
    ads = ads.sort_values(by=['ctr', 'ad_id'], ascending=[False, True])

    return ads[['ad_id', 'ctr']]