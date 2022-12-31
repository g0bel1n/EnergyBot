# from Talky import TalkyChatbot
import streamlit as st

st.set_page_config(page_title="Energy Bot", page_icon=":robot:")

import sys
import os

path2add = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# print(path2add)
if path2add not in sys.path :sys.path.append(path2add)

from talky import TalkyChatbot


from streamlit_chat import message
from numpy.random import default_rng, randint


list_avatars = ["avataaars", "micah", "human",
                     "miniavs", "open-peeps", "pixel-art"]

st.session_state["last_input"] = (
    None if "last_input" not in st.session_state else st.session_state["last_input"]
)

st.session_state["bot"] = (
    TalkyChatbot() if "bot" not in st.session_state else st.session_state["bot"]
)


class chatMessage:
    def __init__(self, value, id, is_user) -> None:
        self.value = value
        self.id = id
        self.is_user = is_user

    @classmethod
    def from_list(cls, lst, id_list, is_user):
        return list(map(lambda el: cls(*el, is_user), zip(lst, id_list)))


class chatMessageFactory:
    def __init__(self) -> None:
        self.id = 0

    def __call__(self, value, is_user):
        if type(value) == list:
            id_list = list(range(self.id + 1, self.id + len(value) + 1))
            self.id += len(value)
            return chatMessage.from_list(value, id_list, is_user)

        self.id += 1
        return chatMessage(value, self.id, is_user)



st.session_state["chatFactory"] = (
    chatMessageFactory()
    if "chatFactory" not in st.session_state
    else st.session_state["chatFactory"]
)


def main(rand_index):

    st.header("Energy Bot")

    if "generated" not in st.session_state:
        st.session_state["generated"] = []

    if "past" not in st.session_state:
        st.session_state["past"] = []

    if "chat" not in st.session_state:
        greetings = st.session_state["bot"].greetings()[0]
        st.session_state["chat"] = [st.session_state.chatFactory(greetings, False)]

    def query(payload):
        response = st.session_state["bot"].process_answer(payload)
        return response

    def clear_text():
        st.session_state["last_input"] = st.session_state["input"]
        st.session_state["input"] = ""

    st.text_input(
        "You: ",
        "",
        help="Use numeric for numbers"
        if st.session_state["last_input"]
        else "Say hello to the bot",
        key="input",
        on_change=clear_text,
    )

    if st.session_state.bot.is_finished and "prediction" not in st.session_state:
        st.session_state["prediction"] = st.session_state.bot.get_prediction()
        st.session_state.chat.append(
            st.session_state.chatFactory(st.session_state["prediction"], False)
        )
        print(st.session_state.bot.get_recommendation())
        st.session_state["chat"] += st.session_state.chatFactory(
            st.session_state.bot.get_recommendation(), False
        )

    ### Send the query to the API
    if st.session_state["last_input"]:

        output = query(st.session_state["last_input"])
        st.session_state.chat.append(
            st.session_state.chatFactory(st.session_state["last_input"], True)
        )
        st.session_state.chat += st.session_state.chatFactory(output, False)
        st.session_state["last_input"] = None
    
    avatar_dict = {True: list_avatars[rand_index], False: "bottts/red"}

    if st.session_state.chat:
        for msg in st.session_state.chat[::-1]:
            message(
                msg.value,
                is_user=msg.is_user,
                key=msg.id,
                avatar_style=avatar_dict[msg.is_user])


if __name__ == "__main__":
    
    rand_index = randint(len(list_avatars), size=1)[0]

    main(rand_index)