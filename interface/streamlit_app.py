import streamlit as st
import os

from pages import meteo


import streamlit as st
from streamlit_chat import message

global adress

adress = None


def main():
    st.set_page_config(page_title="Energy Bot", page_icon=":robot:")

    st.header("Energy Bot")

    if "generated" not in st.session_state:
        st.session_state["generated"] = []

    if "past" not in st.session_state:
        st.session_state["past"] = []

    def query(payload):
        # Send the query to the API
        # To complete
        pass

    ### Get the user input
    def get_text():
        input_text = st.text_input("You: ", "Hello, how are you?", key="input")
        return input_text

    user_input = get_text()

    ### Send the query to the API
    if user_input:
        output = query(
            {
                "inputs": {
                    "past_user_inputs": st.session_state.past,
                    "generated_responses": st.session_state.generated,
                    "text": user_input,
                },
                "parameters": {"repetition_penalty": 1.33},
            }
        )

        st.session_state.past.append(user_input)
        st.session_state.generated.append(output["generated_text"])

    ### Display the chat
    if st.session_state["generated"]:

        for i in range(len(st.session_state["generated"]) - 1, -1, -1):
            message(st.session_state["generated"][i], key=str(i))
            message(st.session_state["past"][i], is_user=True, key=f"{str(i)}_user")

    ##### Get adress when asked from the customer


if __name__ == "__main__":

    main()

    # selected_page = st.sidebar.selectbox("Select a page", ("main", "meteo"))
    # if selected_page == "meteo":
    #     meteo.main(adress)
    # else:
    #     main()
