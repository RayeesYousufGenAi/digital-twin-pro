import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_style_analysis(text_samples):
    """Analyzes text samples to extract personality, tone, and linguistic quirks."""
    llm = ChatOpenAI(model="gpt-4o")
    
    prompt = ChatPromptTemplate.from_template("""
    You are an expert linguistic profiler. Analyze the following text samples from a user:
    ---
    {samples}
    ---
    Identify the following:
    1. Tone (Professional, Casual, Grumpy, Enthusiastic, etc.)
    2. Common Phrases or Word Choices.
    3. Sentence Structure (Short, complex, use of emojis, etc.)
    
    Respond with a 2-paragraph "Digital Style Profile" that can be used to instruct an AI to mimic this user.
    """)
    
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"samples": text_samples})

def generate_proxy_response(user_goal, style_profile, context=""):
    """Generates a response to a given situation using the user's digital style."""
    llm = ChatOpenAI(model="gpt-4o")
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are the 'Digital Twin' of a user. You must respond to the following situation EXACTLY as the user would, following this style profile:\n\n{style_profile}"),
        ("user", "Situation/Input: {user_goal}\nContext: {context}")
    ])
    
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"user_goal": user_goal, "style_profile": style_profile, "context": context})
