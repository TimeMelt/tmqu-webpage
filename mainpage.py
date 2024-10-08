import streamlit as st

logo = "qflux-logo.png"

st.set_page_config(
    layout="wide",
    page_title="TMQU",
    page_icon=logo
)

sidebar = st.sidebar
st.image(logo, width=75)
mainpanel = st.container()
maincol1, maincol2, maincol3 = st.columns(3)
col1, col2, col3 = st.columns(3)
bottompanel = st.container()
creditspanel = st.container()

coffee_emoji = "\U00002615"
dollar_emoji = "\U0001F4B2"
book_emoji = "\U0001F4DA"
notebook_emoji = "\U0001F4D3"
globe_emoji = "\U0001F30E"
memo_emoji = "\U0001F4DD"
caution_emoji = "\U000026A0"
light_emoji = "\U0001F4A1"

values_desc = '''
- Combining the power of quantum, cryptography, and blockchain tech!!! 
- create open and accessible quantum software
- foster an enviornment of open collaboration and development for quantum technology
'''
goals_desc = '''
- develop new cryptography standard
    - key certificates that are truly random
    - ensure that it is quantum resistant
- develop blockchain based on Qash circuits
    - develop blockchain as a service/digital ledger platform based on Qash software
- benchmark crytographic security of Qash (quantum key derivation circuits)
- adapt circuits to other types of quantum processors (trapped-ion, neutral atom, etc.)
- gain access to multiple types of physical, quantum hardware for real world testing and implementation
'''
software_products_live_desc = '''
- Qash-QKDC: pennylane hashing (superconductor, photonic)
- Qash Demo Ui: ui demo for Qash-QKDC
- QashChain: quantum powered blockchain ledger (basic implementation)
- GausQash: strawberryfields hashing circuit (xanadu/photonic)
'''
software_products_not_live_desc = '''
- Qash API:
    - generate unique keys and hashes 
    - QPU and simulator support
- QashChain Ui: demo ui for using QashChain
- QashChain features:
    - consensus algorithm
    - basic node communication protocol
    - smart contracts
'''

sidebar.header("Apps", divider='rainbow')
sidebar.page_link("https://qkdc-ui.streamlit.app/", label="Qash Demo", icon=light_emoji)
sidebar.page_link("https://github.com/TimeMelt/qashchain", label="QashChain Demo", icon=caution_emoji, disabled=True)
sidebar.header("Donate/Support", divider='rainbow')
sidebar.page_link("https://buy.stripe.com/fZe4i46ht5mEfMkeUY", label="PickYourAmount", icon=dollar_emoji)

with mainpanel:
    st.header("TimeMelt Quantum", divider='rainbow')
    col1.header("Links & Pages", divider="rainbow")
    col1.subheader("Project Pages")
    col1.page_link("https://timemelt.itch.io/qash-qkdc", label="Qash (itch.io)", icon=globe_emoji)
    col1.page_link("https://timemelt.itch.io/qashchain", label="QashChain (itch.io)", icon=globe_emoji)
    col1.page_link("https://timemelt.itch.io/GausQash", label="GausQash (itch.io)", icon=globe_emoji)

    col1.subheader("GitHub Repos")
    col1.page_link("https://github.com/TimeMelt/qash-qkdc", label="Qash Jupyter Notebook", icon=notebook_emoji)
    col1.page_link("https://github.com/TimeMelt/qash-qkdc-streamlit", label="Qash Ui Repo", icon=book_emoji)
    col1.page_link("https://github.com/TimeMelt/qashchain", label="QashChain Jupyter Notebook", icon=notebook_emoji)
    col1.page_link("https://github.com/TimeMelt/GausQash", label="GausQash Jupyter Notebook", icon=notebook_emoji)
    
    col2.header("Mission", divider="rainbow")
    col2.subheader("Core Values")
    col2.markdown(values_desc)
    col2.subheader("Goals/Endeavors")
    col2.markdown(goals_desc)

    col3.header("Software Products", divider='rainbow')
    col3.subheader("Available Now!")
    col3.markdown(software_products_live_desc)
    col3.subheader("Future Plans...")
    col3.markdown(software_products_not_live_desc)
    
    st.caption("quantum research & development")

bottompanel.header("Contact", divider='rainbow')
bottompanel.caption("fill out the google form below and someone will get back to you shortly.")
bottompanel.page_link("https://docs.google.com/forms/d/e/1FAIpQLSchyxvYEiAG1yMxmml7EyZUQgN_kD1P8ak3ndCt2qt85-2hwA/viewform?usp=sf_link", label="Contact Form", icon=memo_emoji)
bottompanel.divider()
creditspanel.caption("By TimeMelt")
