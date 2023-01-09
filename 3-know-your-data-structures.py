import pandas as pd


def get_metadata():
    return pd.read_csv("data/metadata-300k.tsv", sep='\t', usecols=['strain'])


def check_for_matches(random_strings, strain_ids):
    for random_string in random_strings:
        if random_string in strain_ids:
            print("Hit the jackpot!")


if __name__ == "__main__":
    metadata = get_metadata()
    print("Metadata:")
    print(metadata)

    # Generate 10k 5-letter strings
    random_strings = pd._testing.rands_array(5, 10 ** 4)
    print("First 10 random strings:")
    print(random_strings[:10])

    strain_ids = list(metadata['strain'])

    # Check if any of the random strings are strain names
    for random_string in random_strings:
        if random_string in strain_ids:
            print("Hit the jackpot!")


# Use sets instead of lists when determining if a collection
# of items contains a specific item.
