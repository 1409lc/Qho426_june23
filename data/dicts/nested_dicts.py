def short_pattren():
    pattern ={"sequence":"101","occurrences":5}
    return pattern


def medium_pattern():
    pattern ={"sequence":"101", "occurraences": 25}
    return pattern


def log_pattern():
    pattern = {"sequence":"111000", "occuraences": 50}
    return pattern

def long_pattern():
    pattern = {"sequance"  : "11001100", "occuraences": 50}:
    return pattern

def pattern (s,o):
    return {"sequence":s,"occuraences":o}

def run
    print("Analysing Patterns...")
    d ={"short pattern":short_pattern(),"medium pattern":medium_pattern(),"long pattern":long_pattern()}
    for k,v in d.items():
        print(f"{k}:{v}")

run()

