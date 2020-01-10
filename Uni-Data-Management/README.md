# University data managment (For Google Code-In)

The program reads the data from the `.ods` files in [/data](./data) using `pyexcel_ods` and calculates the weighted overall percentage of the students and ranks them.

This is done by first reading the academic files ([Data1.ods](./data/Data1.ods), [Data2.ods](./data/Data2.ods), [Data3.ods](./data/Data3.ods), [Data4.ods](./data/Data4.ods)) and calculating the weighted average percentage for each student across all subjects and all terms. A dictionary (`total_scores`) is created in the form: `name: list of total scores for each subject`. The total scores across all terms for Algebra and Physics are multiplied by 2 as required. Then, a new dictionary (`avg_scores`) is created in the form: `name: weighted average score`, storing each student's academic scores.

Then the [IELTS.ods](./IELTS.ods) file is read and each student's average score is stored in a dictionary as a percentage. The same is then performed for [Interview.ods](./Interview.ods).

The three dictionaries, storing the average percentage for each student for academics, IELTS and interview scores are then combined to get the final percentage. The three different factors are weighted: academics by 40%, IELTS scores by 30% and interview scores by 30%. `decimal.Decimal` is used for storing the final values to avoid rounding errors (due to how floats are stored).

This final dictionary is then ordered by the percentage using a `collections.OrderedDict` and this data is then stored in [ranking.txt](./ranking.txt).
