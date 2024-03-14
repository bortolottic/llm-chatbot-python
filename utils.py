import streamlit as st

# tag::write_message[]
def write_message(role, content, save = True):
    """
    This is a helper function that saves a message to the
     session state and then writes a message to the UI
    """
    # Append to session state
    if save:
        st.session_state.messages.append({"role": role, "content": content})

    # Write to UI
    with st.chat_message(role):
        st.markdown(content)
# end::write_message[]

# tag::load_variables[]
def load_variables():
    with open('/mnt/dados/projetos/variables.data', 'r') as file:
        code_lines = file.readlines()
    for cl in code_lines:
        exec(cl)
    return locals()
# end::load_variables[]