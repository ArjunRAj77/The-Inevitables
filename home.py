import streamlit as st
import json
import pandas as pd
import random

# Function to generate random background color for rows
def get_random_color():
    color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color

# Team Introduction Page
def show_team_intro():
    st.subheader("Hi there 👋 We're 'The Inevitables'")
    st.image("https://a-static.besthdwallpaper.com/penguins-of-madagascar-plucky-penguins-wallpaper-4320x1440-14052_107.jpg")
    st.markdown("**Kowalski, status report:**")
    st.markdown("## What are we? 🧙")
    st.write("A group of techies who loves to solve complex problems by participating in various hackthons and trying to bring ideas to life.\nWe constantly look for new challenges and topics rather than fixating on the tech stack we know. And of course, the ultimate aim is to give something back to society.")
    st.write("- ⚡ Fun fact: we ❤️ hackathons")

# Team Members Page
def show_team_members():
    st.header("👥 Meet Our Team Members")
    st.write("Learn more about the individuals who make up our awesome team.")
    # Replace with actual team member data
    team_members = [
        {"name": "Arjun Raj", "role": "Team Leader", "bio": "Experienced coder and leader."},
        {"name": "Akhil M Anil", "role": "DevOps Engineer", "bio": "UI/UX enthusiast and CSS magician."},
        {"name": "Akshaymon K V", "role": "Full Stack Developer", "bio": "Database guru and API ninja."},
        {"name": "Akshay V Anil", "role": "Full Stack Developer", "bio": "Data-driven problem solver."},
    ]
    for member in team_members:
        st.subheader(member["name"])
        st.write(f"Role: {member['role']}")
        st.write(member["bio"])
        st.write("-----")

# Achievements Page
def show_achievements():
    st.header("🏆 Our Achievements")
    st.write("We've participated in these hackathons and accomplished the following:")
    # Replace with actual achievements data
    with open('hackathon_data.json', 'r') as f:
        data = json.load(f)
        achievements = [entry["hackathon_name"] for entry in data]
    st.write(achievements)

# Articles and Blog Posts Page
def show_articles():
    st.header("📚 Articles and Blog Posts")
    st.write("Read what others have written about our team's accomplishments and projects.")
    # Add your articles/blog posts here
    st.write("No articles or blog posts yet.")

def main():
    st.title("Team Inevitables")

    # Sidebar navigation
    selected_page = st.sidebar.selectbox("Navigate", ["Team Intro", "Team Members", "Achievements", "Articles"])

    if selected_page == "Team Intro":
        show_team_intro()

    elif selected_page == "Team Members":
        show_team_members()

    elif selected_page == "Achievements":
        show_achievements()

    elif selected_page == "Articles":
        show_articles()

if __name__ == "__main__":
    main()
