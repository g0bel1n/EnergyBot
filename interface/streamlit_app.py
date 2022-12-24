import streamlit as st
from streamlit_chat import message
import requests

from pages import meteo

global adress

adress = None



def main():
    st.set_page_config(page_title="Energy Bot", page_icon=":robot:")

    API_URL = "http://localhost:5005/model/parse"
    #headers = {"Authorization": st.secrets['api_key']}


    st.header("Energy Bot")

    if "generated" not in st.session_state:
        st.session_state["generated"] = []

    if "past" not in st.session_state:
        st.session_state["past"] = []

    def query(payload):
        response = requests.post(API_URL, json=payload)# headers=headers, )
        return response.json()

    ### Get the user input
    def get_text():
        input_text = st.text_input("You: ", "hey", key="input")
        return input_text

    user_input = get_text()

    ### Send the query to the API
    if user_input:
        output = query(
            {
                "response_selector": 
                {
                    "all_retrieval_intents": [],
                    "default": 
                    {
                        "response": 
                        {
                            "responses": null,
                            "confidence": 0.0,
                            "intent_response_key": null,
                            "utter_action": "utter_None"
                        }
                    }
                }
            })
            #{
            #    "inputs": {
            #        "past_user_inputs": st.session_state.past,
            #        "generated_responses": st.session_state.generated,
            #        "text": user_input,
            #    },
            #    "parameters": {"repetition_penalty": 1.33},
            #}
        
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
