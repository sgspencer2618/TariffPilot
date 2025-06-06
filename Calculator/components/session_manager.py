import streamlit as st

def initialize_session_state():
    """Initialize all session state variables"""
    if 'user_email' not in st.session_state:
        st.session_state.user_email = ""
    
    if 'order_number' not in st.session_state:
        st.session_state.order_number = ""
    
    if 'country_of_origin' not in st.session_state:
        st.session_state.country_of_origin = ""
    
    if 'hs_code_list' not in st.session_state:
        st.session_state.hs_code_list = []
    
    if 'form_counter' not in st.session_state:
        st.session_state.form_counter = 0
    
    # ADD THIS - Goods types management
    if 'custom_goods_types' not in st.session_state:
        st.session_state.custom_goods_types = [
            "Trench CA Finished Goods",
            "Warranty Replacement",
            "Warranty Repair",
            "After Sales Parts",
            "Resale"
        ]

def reset_order():
    """Reset user info and start fresh"""
    st.session_state.user_email = ""
    st.session_state.order_number = ""
    st.session_state.country_of_origin = ""
    st.session_state.hs_code_list = []
    st.session_state.form_counter = 0
    st.success("Order reset successfully!")