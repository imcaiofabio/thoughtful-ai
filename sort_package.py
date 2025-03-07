from pandas import read_csv

def sort(width, height, length, mass):
    if not all(isinstance(x, (int, float)) and x >= 0 for x in [width, height, length, mass]):
        raise ValueError("All dimensions and mass must be non-negative numbers.")
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150

    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


def ingest_data(file_path="/Users/caio/code/thoughtful-ai/packages.csv"):
    df = read_csv(file_path, on_bad_lines='skip')
    df_list = df.values.tolist()

    sorted_packages = []
    for d in df_list:
        w, h, l, m = d
        try:
            r = sort(float(w), float(h), float(l), float(m))
            d.append(r)
            sorted_packages.append(d)
        except Exception:
            pass
    return sorted_packages
