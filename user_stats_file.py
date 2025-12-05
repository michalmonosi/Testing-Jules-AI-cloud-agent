import csv
import statistics

def calculate_statistics(file_path):
    salaries = []
    with open(file_path, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            try:
                salaries.append(float(row['salary']))
            except (ValueError, KeyError):
                pass

    if salaries:
        mean_salary = statistics.mean(salaries)
        median_salary = statistics.median(salaries)
        stdev_salary = statistics.stdev(salaries)

        print(f"Salary Statistics:\n")
        print(f"  Mean: ${mean_salary:,.2f}")
        print(f"  Median: ${median_salary:,.2f}")
        print(f"  Standard Deviation: ${stdev_salary:,.2f}")
    else:
        print("No salary data found.")

if __name__ == "__main__":
    calculate_statistics('users_sql.csv')
