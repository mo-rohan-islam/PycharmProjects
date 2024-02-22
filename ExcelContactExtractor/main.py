from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/extract-contacts', methods=['POST'])
def extract_contacts():
    # Get input files and output file from request
    input_files = request.json.get('input_files')
    output_file = request.json.get('output_file')

    output_columns = [
        'Name', 'Given Name', 'Additional Name', 'Family Name', 'Yomi Name', 'Given Name Yomi', 'Additional Name Yomi',
        'Family Name Yomi', 'Name Prefix', 'Name Suffix', 'Initials', 'Nickname', 'Short Name', 'Maiden Name',
        'Birthday', 'Gender', 'Location', 'Billing Information', 'Directory Server', 'Mileage', 'Occupation',
        'Hobby', 'Sensitivity', 'Priority', 'Subject', 'Notes', 'Language', 'Photo', '* myContacts',
        'E-mail 1 - Type', 'E-mail 1 - Value', 'E-mail 2 - Type', 'E-mail 2 - Value',
        'Phone 1 - Type', 'Phone 1 - Value', 'Phone 2 - Type', 'Phone 2 - Value',
        'Phone 3 - Type', 'Phone 3 - Value', 'Phone 4 - Type', 'Phone 4 - Value',
        'Address 1 - Type', 'Address 1 - Formatted', 'Address 1 - Street', 'Address 1 - City', 'Address 1 - PO Box',
        'Address 1 - Region', 'Address 1 - Postal Code', 'Address 1 - Country', 'Address 1 - Extended Address',
        'Organization 1 - Type', 'Organization 1 - Name', 'Organization 1 - Yomi Name', 'Organization 1 - Title',
        'Organization 1 - Department', 'Organization 1 - Symbol', 'Organization 1 - Location',
        'Organization 1 - Job Description', 'Relation 1 - Type', 'Relation 1 - Value', 'Website 1 - Type',
        'Website 1 - Value'
    ]

    all_data = []
    for file in input_files:
        data = pd.read_excel(file, skiprows=1)
        if 'PH' in data.columns and 'NAME' in data.columns:
            data = data[data['NAME'].notnull()]
            data['PH'] = data['PH'].apply(lambda x: x.replace('/', ' ::: ') if isinstance(x, str) and '/' in x else x)
        all_data.append(data)

    combined_data = pd.concat(all_data, ignore_index=True)
    result = pd.DataFrame(columns=output_columns)
    result['Name'] = combined_data['NAME']
    result['Phone 1 - Type'] = 'Mobile'
    result['Phone 1 - Value'] = combined_data['PH']

    result.to_csv(output_file, index=False)

    return jsonify({'message': 'Contacts extracted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
