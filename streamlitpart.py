import streamlit as st
import json
import random


st.title("AR5 vs AR6")
subj = st.selectbox("Select a subject", ["Food Production", "Freshwater Detail", "Freshwater Executive Summary", "Precipitation"])
item = st.selectbox("Select an option", ["Individual Summaries", "Comparative Summaries", "Questions", "Original Text"])

subjtofold = {"Food Production": "foodproduction", "Freshwater Detail": "freshwater detail",
              "Freshwater Executive Summary": "freshwaterexec", "Precipitation":"precipitation"}

if item == "Individual Summaries":
    with open(f"{subjtofold[subj]}/sum5.txt", 'r') as f:
        sum5 = f.read()
    with open(f"{subjtofold[subj]}/sum6.txt", 'r') as f:
        sum6 = f.read()
    ex = st.expander("AR5")
    ex.write(sum5)
    ex = st.expander("AR6")
    ex.write(sum6)
if item == "Comparative Summaries":
    with open(f"{subjtofold[subj]}/sumboth.json", 'r') as f:
        sumboth = json.load(f)
    for doc in sumboth['documents']:
        ex = st.expander("Prompt")
        ex.write(doc['prompt'])
        ex = st.expander("Text")
        ex.write(doc['text'])
if item == "Questions":
    for ar in ["AR5QandA", "AR6QandA"]:
        st.header(ar[:3])
        with open(f"{subjtofold[subj]}/{ar}.json", 'r') as f:
            text = json.load(f)
        for prompt in text['Prompts']:
            st.subheader(prompt['type'])
            ex = st.expander("Prompt")
            ex.write(prompt['description'])
            for i, q in enumerate(prompt['questions']):
                if prompt['type'] == "Short Answer":
                    st.write(q['question'])
                    ex = st.expander("Answer")
                    ex.write(q['answer'])
                if prompt['type'] == "Multiple Choice":
                    st.write(q['question'])
                    for opt in q['options']:
                        st.write(opt)
                    answers = ['Choose Answer'] + q['options']
                    print(answers)
                    ans = st.selectbox("Select an Answer", answers, key=q['question'])
                    if ans == q['answer']:
                        st.write(":green[Correct!]")
                    elif ans == 'Choose Answer':
                        st.write("")
                    else:
                        st.write(":red[Not quite, try again!]")
if item == "Original Text":
    with open(f"{subjtofold[subj]}/ar5complete.txt", 'r') as f:
        foodprodar5 = f.read()
    with open(f"{subjtofold[subj]}/ar6complete.txt", 'r') as f:
        foodprodar6 = f.read()
    ex = st.expander("AR5")
    ex.write(foodprodar5)
    ex = st.expander("AR6")
    ex.write(foodprodar6)

