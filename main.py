import os.path
from os import walk

import pandas as pd

df = pd.DataFrame(columns=['Title', 'First Name', 'Middle Name', 'Last Name', 'Suffix', 'Company',
                           'Department', 'Job Title', 'Business Street', 'Business Street 2',
                           'Business Street 3', 'Business City', 'Business State',
                           'Business Postal Code', 'Business Country/Region', 'Home Street',
                           'Home Street 2', 'Home Street 3', 'Home City', 'Home State',
                           'Home Postal Code', 'Home Country/Region', 'Other Street',
                           'Other Street 2', 'Other Street 3', 'Other City', 'Other State',
                           'Other Postal Code', 'Other Country/Region', "Assistant's Phone",
                           'Business Fax', 'Business Phone', 'Business Phone 2', 'Callback',
                           'Car Phone', 'Company Main Phone', 'Home Fax', 'Home Phone',
                           'Home Phone 2', 'ISDN', 'Mobile Phone', 'Other Fax', 'Other Phone',
                           'Pager', 'Primary Phone', 'Radio Phone', 'TTY/TDD Phone', 'Telex',
                           'Account', 'Anniversary', "Assistant's Name", 'Billing Information',
                           'Birthday', 'Business Address PO Box', 'Categories', 'Children',
                           'Directory Server', 'E-mail Address', 'E-mail Type',
                           'E-mail Display Name', 'E-mail 2 Address', 'E-mail 2 Type',
                           'E-mail 2 Display Name', 'E-mail 3 Address', 'E-mail 3 Type',
                           'E-mail 3 Display Name', 'Gender', 'Government ID Number', 'Hobby',
                           'Home Address PO Box', 'Initials', 'Internet Free Busy', 'Keywords',
                           'Language', 'Location', "Manager's Name", 'Mileage', 'Notes',
                           'Office Location', 'Organizational ID Number', 'Other Address PO Box',
                           'Priority', 'Private', 'Profession', 'Referred By', 'Sensitivity',
                           'Spouse', 'User 1', 'User 2', 'User 3', 'User 4', 'Web Page'])


def start():
    print("Input start year (ex. 2015): ")
    start_year = int(input())
    print("Input end year (ex. 2018): ")
    end_year = int(input())

    consultations_list = []
    for year in range(start_year, end_year + 1):

        if os.path.isdir("./Test Files/" + str(year)):
            _, _, filenames = next(walk("./Test Files/" + str(year)))
            consultations_list.extend(filenames)
        else:
            print("Directory does not exist: " + str(year))

    # print(consultations_list)  # entire list for debug
    run_df_population(consultations_list)
    create_contact_csv()


def get_filename_data(pdf_name):
    """
    Called like 'get_filename_data(filenames[1])'

    :param pdf_name:
    :return:
    """
    consult_date = pdf_name[:11]

    people = pdf_name[13:].split('&')
    contacts_list = []

    for person in people:
        names = person.split(',')
        # print(consult_date, people)
        last_name = names[0]
        first_middle = names[1].split()
        first_name = first_middle[0]
        middle_name = first_middle[1:]

        middle_names = " "
        middle_names = middle_names.join(middle_name)

        # print(last_name, first_name, middle_names)
        contacts_list.append({'First Name': first_name, 'Middle Name': middle_names, 'Last Name': last_name,
                              'Consult Date': consult_date})

    return contacts_list


def add_contact(pdf_name):
    person_dict = get_filename_data(pdf_name)

    for person in person_dict:
        contact_dict = {'First Name': person['First Name'],
                        'Middle Name': person['Middle Name'],
                        'Last Name': person['Last Name'],
                        'Notes': 'Consult Only - ' + person['Consult Date']
                        }

        df.loc[len(df.index)] = contact_dict

    # display(df)


def run_df_population(filenames):
    for consultation_filename in filenames:
        # print(consultation_filename)
        add_contact(consultation_filename)

    print(df.shape)


def create_contact_csv():
    df.to_csv('generated_contacts.csv', index=False)


if __name__ == '__main__':
    start()