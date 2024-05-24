import streamlit as st

st.title('Atendimento - Informações')

busca = st.text_input(label='Buscar')

if busca:
    st.markdown(f'Sua busca foi: **{busca}**.')
