# my_family = {
#     "child1": {
#         "name": "Emil",
#         "year": 2004
#     },
#     "child2": {
#         "name": "Tobias",
#         "year": 2007
#     },
#     "child3": {
#         "name": "Linus",
#         "year": 2011
#     }
# }
# print(my_family)

# for i in my_family.keys():
#     print(my_family[i]['name'])

company_data = {
    'Engineering': {
        'Employees': {
            'Alice': {
                'age': 32,
                'role': 'Software Engineer',
                'skills': ['Python', 'Django', 'SQL'],
                'projects': {
                    'ProjectA': {'status': 'Active', 'team_size': 5},
                    'ProjectB': {'status': 'Inactive', 'team_size': 3}
                }
            },
            'Bob': {
                'age': 28,
                'role': 'Junior Developer',
                'skills': ['Python', 'Flask'],
                'projects': {
                    'ProjectC': {'status': 'Active', 'team_size': 2}
                }
            }
        },
        'Head': 'Charlie'
    },
    'Sales': {
        'Employees': {
            'David': {
                'age': 45,
                'role': 'Sales Manager',
                'skills': ['Negotiation', 'CRM'],
                'clients': ['ClientX', 'ClientY']
            }
        },
        'Head': 'Eve'
    },
    'CompanyInfo': {
        'Name': 'TechCorp',
        'Location': 'San Francisco',
        'YearFounded': 2010
    }
}

for j,i in company_data.items():
    if 'Employees' in i:
        for e_name , e_detail in i['Employees'].items():
            print(e_name,end='')
            print(e_detail.get("skills",[]))