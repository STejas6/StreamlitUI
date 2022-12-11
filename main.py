import streamlit as st
import streamlit_option_menu as som
page_title = 'Create DB Objects'

st.set_page_config(page_title=page_title)
st.title(page_title)

with st.sidebar:
    nav_bar = som.option_menu(menu_title='Main Menu',
                              options=['Submit Request', 'Check Requests'],
                              default_index=0,
                              menu_icon='menu-app-fill')

if nav_bar == 'Submit Request':
    object_list = ['Database', 'Schema', 'Warehouse', 'Role', 'User', 'Table']

    tabs = st.tabs(object_list)

    tab_DB = tabs[0]

    with tab_DB:
        create_type = st.radio(label='Select type of DB to be created',
                               options=['Standard', 'Shared', 'Secondary Database'],
                               horizontal=True,
                               help='''
        Standard Database\n
            CREATE [ OR REPLACE ] [ TRANSIENT ] DATABASE [ IF NOT EXISTS ] <name>
            [ CLONE <source_db>
            [ { AT | BEFORE } ( { TIMESTAMP => <timestamp> | OFFSET => <time_difference> | STATEMENT => <id> } ) ] ]
            [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
            [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
            [ DEFAULT_DDL_COLLATION = '<collation_specification>' ]
            [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
            [ COMMENT = '<string_literal>' ]
                        
        Shared Database (from a Share)\n
            CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    
        Secondary Database (Database Replication)\n
            CREATE DATABASE <name>
            AS REPLICA OF <account_identifier>.<primary_db_name>
            [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
    ''')
        if create_type == 'Standard':
            DB_name = st.text_input('Enter the DB name to be created: ')
            if DB_name != '':
                st.markdown(f"DB created with name - {DB_name}")

        elif create_type == 'Shared':
            DB_name = st.text_input('Enter the DB name to be created: ')
            Provider_account = st.text_input('Enter the Provider account name: ')
            Share_name = st.text_input('Enter the Share name: ')
        elif create_type == 'Secondary Database':
            DB_name = st.text_input('Enter the DB name to be created: ')
            Account_identifier = st.text_input('Enter the Account identifier name: ')
            primary_DB_name = st.text_input('Enter the Primary DB Name: ')

            if "disabled" not in st.session_state:
                st.session_state.disabled = False

            retention_check = st.checkbox('Enter the Data Retention time in days:', key='disabled',
                                          help='Optional Argument')
            retention_time_in_days = st.number_input('Enter the Data Retention time in days: ',
                                                     min_value=0, max_value=90, step=1,
                                                     disabled= not st.session_state.disabled,
                                                     label_visibility='collapsed')
        "---"
    tab_Schema = tabs[1]
    with tab_Schema:
        Schema_name = st.text_input('Enter schema name: ')
        if Schema_name != '':
            st.markdown(f"Table created with name - {Schema_name}")
        "---"

