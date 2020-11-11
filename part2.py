import csv

# Employees is a list of objects.
# The keys in these objects will be the header fields of your spreadsheet.
employees = [
    {
        'first_name': 'Bill',
        'last_name': 'Lumbergh',
        'job_title': 'Vice President',
        'hire_date': 1985,
        'performance_review': 'excellent'
    },
    {
        'first_name': 'Michael',
        'last_name': 'Bolton',
        'job_title': 'Programmer',
        'hire_date': 1995,
        'performance_review': 'poor'
    },
    {
        'first_name': 'Peter',
        'last_name': 'Gibbons',
        'job_title': 'Programmer',
        'hire_date': 1989,
        'performance_review': 'poor'
    },
    {
        'first_name': 'Samir',
        'last_name': 'Nagheenanajar',
        'job_title': 'Programmer',
        'hire_date': 1974,
        'performance_review': 'fair'
    },
    {
        'first_name': 'Milton',
        'last_name': 'Waddams',
        'job_title': 'Collator',
        'hire_date': 1974,
        'performance_review': 'does he even work here?'
    },
    {
        'first_name': 'Bob',
        'last_name': 'Porter',
        'job_title': 'Consultant',
        'hire_date': 1999,
        'performance_review': 'excellent'
    },
    {
        'first_name': 'Bob',
        'last_name': 'Slydell',
        'job_title': 'Consultant',
        'hire_date': 1999,
        'performance_review': 'excellent'
    }
]

with open('tps_report.csv', 'w', newline='') as csvfile:

    fieldnames = ['first_name', 'last_name', 'job_title', 'hire_date', 'performance_review', 'review_finished']

    writer = csv.DictWriter(csvfile, fieldnames)

    writer.writeheader()

    for a_dict in employees:
        if (a_dict['first_name']== 'Bill' and a_dict['last_name'] == 'Lumbergh'):
         writer.writerow({ 'first_name': a_dict['first_name'], 'last_name': a_dict['last_name'], 'job_title': a_dict['job_title'], 'hire_date': a_dict['hire_date'], 'performance_review': 'poor', 'review_finished': 'yes' })
        elif(a_dict['job_title'] == 'Consultant'):
         writer.writerow({ 'first_name': a_dict['first_name'], 'last_name': a_dict['last_name'], 'job_title': a_dict['job_title'], 'hire_date': a_dict['hire_date'], 'performance_review': 'poor', 'review_finished': 'yes' })
        else:
         writer.writerow({ 'first_name': a_dict['first_name'], 'last_name': a_dict['last_name'], 'job_title': a_dict['job_title'], 'hire_date': a_dict['hire_date'], 'performance_review': 'excellent', 'review_finished': 'yes' })

