import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("courses.csv")

# Streamlit App
st.set_page_config(page_title="Courses Recommender", layout="centered")

st.title("📚 Courses Recommendation System")
st.markdown("Find the best online courses based on your interest!")

# Input from user
user_input = st.text_input("Enter your area of interest (e.g., data science, web development):")

# Recommend courses
if user_input:
    recommendations = df[df['category'].str.contains(user_input, case=False, na=False)]
    
    if not recommendations.empty:
        st.success(f"Top {len(recommendations)} course(s) found:")
        for i, row in recommendations.iterrows():
            st.markdown(f"**🔹 {row['course_name']}**  \n📌 *Platform:* {row['platform']}  \n🔗 [Go to Course]({row['url']})\n")
    else:
        st.warning("No matching courses found. Try another keyword.")
      
