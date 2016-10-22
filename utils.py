def get_progress_emoji(ratio):
    emoji = {
        'cov_level_1': ':new_moon:',
        'cov_level_2': ':waning_crescent_moon:',
        'cov_level_3': ':last_quarter_moon:',
        'cov_level_4': ':waning_gibbous_moon:',
        'cov_level_5': ':full_moon:'
    }

    # Coverage level range
    # 0 - 10 -- 30 ---- 70 -- 90 - 100
    if ratio > 90:
        return emoji['cov_level_5']
    elif ratio > 70:
        return emoji['cov_level_4']
    elif ratio > 30:
        return emoji['cov_level_3']
    elif ratio > 10:
        return emoji['cov_level_2']
    else:
        return emoji['cov_level_1']
