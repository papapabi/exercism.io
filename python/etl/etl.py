def transform(legacy_data):
    return {letter.lower(): score for score, list in legacy_data.items()
            for letter in list}
