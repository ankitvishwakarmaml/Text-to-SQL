import streamlit as st 
from utils.db_utlis import get_data_from_database
from utils.model_utils import get_sql_query

def main():
    st.set_page_config(page_title="Text To SQL")
    st.header("Talk to your Database!")

    user_query=st.text_input("Input:")
    submit=st.button("Enter")

    if submit:
        sql_query = get_sql_query(user_query)
        retrieved_data = get_data_from_database(sql_query)
        st.subheader(f"Retrieving results from the database for the query: [{sql_query}]")
        for row in retrieved_data:
            st.header(row)

if __name__ == '__main__':
    main()