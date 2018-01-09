# CSV_to_Json


The problem:
An excel file containing game level "enemy waves' was converted to CSV (enemy arrays data.csv)

The file needs to be converted to 5 arrays in a 'json-like' format to be used in a game engine. The format is slightly different to son as it contains extra double quotes.

The csv file format:
Column 1 has a level (1-10)
Column 2 has a wav number within the level (1-10)
Column 3 has an enemy type (10 in total)

Column 4 has a probability of a given enemy appearing in that level/wave.
Column 5 has a time in seconds between enemies appearing on the screen in a given level/wave.

The enemies can come from 4 different directions on the ground and 1 direction in the air. Each direction has a probability/time combinations.
Columns (6,7), (8,9), (10,11), (12,13) are the same as columns (4,5) but for other directions.

The data needs to be converted to 5 arrays. Each array starts with:
	"{""c2array"":true,""size"":[10,10,11],""data"":
Followed by the data from the columns and ends with a }"

The csv_to_json.py was my first attempt and it worked purely on strings.
csv_to_json_new.py is my new attempt and hopefully more Pythonic.
