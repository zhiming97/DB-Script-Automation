import re
from datetime import datetime
import os
import streamlit as st

def DB_SCIRPT_CLEANUP(db):
    try:
        datetime_pattern = r"'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}'"
        matches = re.findall(datetime_pattern, db)
        for match in matches:
            formatted_match = datetime.strptime(match, "'%Y-%m-%d %H:%M:%S.000'").strftime('SYSDATE')
            db = db.replace(match, formatted_match)
        
        db = db.replace(';', '@')

        return db
    except Exception as e:
        return f"Error: {e}"

def main():
    st.title('DB Script Preparation Tool 🤖')

    uploaded_file = st.file_uploader('Upload Your DB Script', type=['sql'])

    if uploaded_file is not None:
        content = uploaded_file.read().decode('utf-8')
        modified_db_script = DB_SCIRPT_CLEANUP(content)
        
        st.text(modified_db_script)
        
        new_db_script = modified_db_script.encode('utf-8')
        st.download_button('Download Your New DB Script', data=new_db_script, file_name='New_DB_Script.sql', mime='text/sql')

    else:
        st.info('Use At Your Own Risk 🤡')

if __name__ == '__main__':
    main()
