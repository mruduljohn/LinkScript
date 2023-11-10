import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
# Set your OpenAI API key
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)


# Function to generate content using GPT-4
def generate_content(mood, type, subject, date, description, tags):
    prompt = (
        f"I want you to draft me a {mood} LinkedIn post. It is based on "
        f"{type}. The following are the details: {type} {subject} "
        f"{date} {description}. You can include more similar tags like {tags}"
    )

    response = client.completions.create(
        model="text-davinci-003",
        #engine="text-davinci-003",  # You can experiment with different engines
        prompt=prompt,
        max_tokens=200  # Adjust based on your needs
    )
    return response.choices[0].text.strip()

# Page title
st.title("LinkedIn Post Generator - LinkScript")

# User inputs
subject = st.text_input("Subject:")
description = st.text_area("Description:")
date = st.date_input("Date:")
mood = st.selectbox("Mood of Writing:", ["Happy", "Neutral", "Professional,Cool", "Sad"])
type = st.selectbox("Type:", ["Article", "Event", "Job", "Achievement", "Other"])
#specify the typpe if other is selected
if type == "Other":
    type = st.text_input("Type:")
tags = st.text_input("Tags (comma-separated):")

# Button to generate post
if st.button("Generate Post"):
    # Use GPT-4 to generate content
    generated_content = generate_content(mood, type, subject, date, description, tags)

    # Combine inputs with generated content into a post
    post_content = f"🚀 **{subject}**\n\n{description}\n\n📅 {date}\n\n😊 Mood: {mood}\n\nType: {type}\n\nGenerated Content: {generated_content}\n\nTags: {tags}"

    # Display the generated post
    st.success("Your LinkedIn Post is ready! Copy and paste the content below:")
    st.code(generated_content)

# GitHub link
st.markdown("[GitHub Repository](https://github.com/mruduljohn/LinkScript)")

# Motivation
st.markdown("## Motivation\n\nOur motivation is to simplify the creation of engaging LinkedIn content...")

# Footer
st.markdown("Let's code, contribute, and become Legend Gladiators together! 🚀")
