import streamlit as st
import io
import json
from pathlib import Path
import docxtpl
import pandas as pd
import openai
import datetime

st.set_page_config("MatCom - Templates", page_icon="🗞️", layout="wide")


@st.cache_resource
def get_client():
    return openai.OpenAI(api_key=st.secrets["API_KEY"], base_url=st.secrets["BASE_URL"])

client = get_client()

@st.cache_data(show_spinner="Generando...")
def generate(prompt):
    result = client.chat.completions.create(messages=[dict(role="user", content=prompt)], model=st.secrets["MODEL"], response_format=dict(type="json_object")).choices[0].message.content
    return json.loads(result)

templates = {p.stem: p for p in Path("templates").glob("*.docx")}
template_path = templates[st.sidebar.selectbox("Seleccione una plantilla", list(templates))]
year = st.sidebar.number_input("Año", value=datetime.date.today().year)
data = st.sidebar.file_uploader("Suba los datos a rellenar", "csv")

if not data:
    st.stop()

data = pd.read_csv(data).fillna("")
data = st.data_editor(data, use_container_width=True)

selected = st.selectbox("Seleccione una entrada", range(len(data)), format_func=lambda r: data.iloc[r,0])
context = data.iloc[selected].to_dict()
context["Year"] = year
name = data.iloc[selected,0]

st.write(context)

prompt_path = Path("prompts") / template_path.with_suffix(".md").name

template = docxtpl.DocxTemplate(template_path)
prompt = open(prompt_path).read().format(**context)

with st.expander("Prompt"):
    st.code(prompt)

result = generate(prompt)

with st.expander("Respuesta"):
    st.write(result)

context.update(result)
template.render(context)

buffer = io.BytesIO()
template.save(buffer)

st.download_button("Descargar", buffer.getvalue(), file_name=f"{name}-{template_path.stem}.docx")
