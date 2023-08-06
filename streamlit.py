import re
from datetime import datetime
import os
import streamlit as st

def replace_datetime_with_sysdate(content):
    try:
        # Regular expression to find datetime format strings like '2023-08-08 13:00:21'
        datetime_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

        # Find all occurrences of the datetime pattern in the text
        matches = re.findall(datetime_pattern, content)

        # Replace each occurrence with 'SYSDATE'
        for match in matches:
            formatted_match = datetime.strptime(match, '%Y-%m-%d %H:%M:%S').strftime('SYSDATE')
            content = content.replace(match, formatted_match)

        return content
    except Exception as e:
        return f"Error: {e}"

def main():
    st.title('Upload and Convert Datetime to SYSDATE')

    uploaded_file = st.file_uploader('Upload a dbscript file', type=['sql'])

    if uploaded_file is not None:
        content = uploaded_file.read().decode('utf-8')

        # Replace datetime with SYSDATE
        modified_content = replace_datetime_with_sysdate(content)

       # Display the modified content
        st.text(modified_content)

        # Download link for the modified file
        modified_bytes = modified_content.encode('utf-8')
        st.download_button('Download Modified File', data=modified_bytes, file_name='modified_script.sql', mime='text/sql')

    else:
        st.info('Please upload a dbscript file.')

if __name__ == '__main__':
    main()
