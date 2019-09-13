TVOC_ppb = 700 #TVOC_ppb variable is assigned a Value
if TVOC_ppb > 2200 and TVOC_ppb < 5500:
    print("{Level 5 - Unhealthy}", "{Hygineic Rating - Situation not Acceptable}", "{Recommendation - Use Only if un avoidable / Intense ventillation necessary}", "{Exposure Limit - Hours}")
elif TVOC_ppb > 660 and TVOC_ppb < 2200:
    print("{Level 4 - Poor}", "{Hygineic Rating - Major Objections}", "{Recommendation - Intensified ventillation / airing necessary Search for sources}", "{Exposure Limit - < 1 month}")
elif TVOC_ppb > 220 and TVOC_ppb < 660:
    print("{Level 3 - Moderate}", "{Hygineic Rating - Some Objections}", "{Recommendation - Intensified ventillation / airing recommended Search for sources}", "{Exposure Limit - < 12 months}")
elif TVOC_ppb > 65 and TVOC_ppb < 220:
    print("{Level 2 - Good}", "{Hygineic Rating - No relevant Objections}", "{Recommendation - Ventillation / airing recommended}", "{Exposure Limit - no limit}")
elif TVOC_ppb > 0 and TVOC_ppb < 65:
    print("{Level 1 - Excellent}", "{Hygineic Rating - No Objections}", "{Recommendation - Target Value}", "{Exposure Limit - no limit}")
