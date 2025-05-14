#from sqlalchemy import create_engine
#import streamlit as st
#@st.cache_resource
#def get_engine():
    #return create_engine(
  #      "mysql+pymysql://admin:Luongloc1210@database-demo.cp2oiuwu4ba1.ap-southeast-2.rds.amazonaws.com:3306/warehouse"
 #   )
from sqlalchemy import create_engine
import streamlit as st

@st.cache_resource
def get_engine():
    db_user = st.secrets["DB_USER"]
    db_password = st.secrets["DB_PASSWORD"]
    db_host = st.secrets["DB_HOST"]
    db_port = st.secrets["DB_PORT"]
    db_name = st.secrets["DB_NAME"]

    return create_engine(
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )

