import streamlit as st
import os
import time
from time import sleep
from pathlib import Path
from streamlit.components.v1 import html
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.schema import SystemMessage
from openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import functions as ft
import constants as ct


# 各種設定
load_dotenv()

# Streamlit UI（最低限の表示）
st.title("英会話AIアプリ")
st.write("ようこそ！この画面が見えればCloud側の描画はOKです。以降のロジックもこの下に記述してください。")