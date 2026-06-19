import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    ads = ads.groupby('ad_id').agg(
        clicked = ('action', lambda x : (x == 'Clicked').sum()),
        viewed = ('action', lambda x : (x == 'Viewed').sum())
    ).reset_index()
    
    ads['ctr'] = (ads['clicked'] / (ads['clicked'] + ads['viewed']) * 100).round(2).fillna(0)
    return ads.sort_values(by=['ctr', 'ad_id'], ascending=[False, True])[['ad_id', 'ctr']]
