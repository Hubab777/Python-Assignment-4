import streamlit as st

st.set_page_config(page_title="🎭 Mad Libs Stories", layout="centered")

st.title("🎭 Ultimate Mad Libs Adventure!")
st.markdown("Choose a story, fill in the blanks, and create magic! ✨")

# Story Selector
story_option = st.selectbox("🗂️ Choose Your Story:", ["🔬 Science Lab", "🕵️ Spy Mission", "🐾 Jungle Adventure"])

# ========= STORY 1: Science Lab ==========
if story_option == "🔬 Science Lab":
    st.markdown("### 🧾 Story: *The Secret Lab*")
    st.markdown(
        """
In your **_____** lab, you carefully picked up the **_____** and began to **_____**.  
A bright light flashed as the **_____** reacted — just as **_____** predicted.  
Your experiment worked! You’ve made scientific history! 🏆🔬
"""
    )

    st.sidebar.header("🧪 Fill in the Blanks (Science)")
    adjectives = ["unstable", "radioactive", "glowing"]
    verbs = ["mix", "explode", "transform"]
    nouns = ["test tube", "chemical", "laser"]
    scientists = ["Albert Einstein", "Marie Curie", "Isaac Newton"]
    elements = ["Oxygen", "Plutonium", "Carbon"]

    adj = st.sidebar.selectbox("1️⃣ Choose an Adjective", [""] + adjectives)
    noun = st.sidebar.selectbox("2️⃣ Choose a Noun", [""] + nouns)
    verb = st.sidebar.selectbox("3️⃣ Choose a Verb", [""] + verbs)
    element = st.sidebar.selectbox("4️⃣ Choose an Element", [""] + elements)
    scientist = st.sidebar.selectbox("5️⃣ Choose a Scientist", [""] + scientists)

    correct_combo = {
        "adj": "glowing",
        "verb": "mix",
        "noun": "test tube",
        "scientist": "Marie Curie",
        "element": "Carbon"
    }

    if all([adj, noun, verb, element, scientist]):
        if st.button("🔬 Start Experiment"):
            if (
                adj == correct_combo["adj"] and
                verb == correct_combo["verb"] and
                noun == correct_combo["noun"] and
                scientist == correct_combo["scientist"] and
                element == correct_combo["element"]
            ):
                st.success(
                    f"In your {adj} lab, you carefully picked up the {noun} and began to {verb}. "
                    f"A bright light flashed as the {element} reacted — just as {scientist} predicted. "
                    f"Your experiment worked! You’ve made scientific history! 🏆🔬"
                )
            else:
                st.error("🧯 Experiment Failed!")
                st.subheader("✅ Here's the Correct Version")
                st.success(
                    "In your glowing lab, you carefully picked up the test tube and began to mix. "
                    "A bright light flashed as the Carbon reacted — just as Marie Curie predicted. "
                    "Your experiment worked! You’ve made scientific history! 🏆🔬"
                )

# ========= STORY 2: Spy Mission ==========
elif story_option == "🕵️ Spy Mission":
    st.markdown("### 🧾 Story: *Operation Code Shadow*")
    st.markdown(
        """
Agent **_____** received a secret message while hiding behind the **_____**.  
The mission was **_____**, and the password was "**_____**".  
Just like in the movies, only **_____** could pull it off. 🕶️💣
"""
    )

    st.sidebar.header("🕵️ Fill in the Blanks (Spy Mission)")
    agent_names = ["Shadow", "X-47", "Raven"]
    hiding_spots = ["dumpster", "statue", "vending machine"]
    missions = ["classified", "dangerous", "undercover"]
    passwords = ["blackbird", "omega", "phoenix"]
    legends = ["James Bond", "Ethan Hunt", "Natasha Romanoff"]

    agent = st.sidebar.selectbox("1️⃣ Agent Codename", [""] + agent_names)
    spot = st.sidebar.selectbox("2️⃣ Hiding Spot", [""] + hiding_spots)
    mission_type = st.sidebar.selectbox("3️⃣ Mission Type", [""] + missions)
    password = st.sidebar.selectbox("4️⃣ Secret Password", [""] + passwords)
    hero = st.sidebar.selectbox("5️⃣ Legendary Spy", [""] + legends)

    correct_spy_combo = {
        "agent": "Raven",
        "spot": "statue",
        "mission_type": "classified",
        "password": "phoenix",
        "hero": "James Bond"
    }

    if all([agent, spot, mission_type, password, hero]):
        if st.button("🕵️ Begin Operation"):
            if (
                agent == correct_spy_combo["agent"] and
                spot == correct_spy_combo["spot"] and
                mission_type == correct_spy_combo["mission_type"] and
                password == correct_spy_combo["password"] and
                hero == correct_spy_combo["hero"]
            ):
                st.success(
                    f"Agent {agent} received a secret message while hiding behind the {spot}. "
                    f"The mission was {mission_type}, and the password was \"{password}\". "
                    f"Just like in the movies, only {hero} could pull it off. 🕶️💣"
                )
            else:
                st.error("🚨 Mission Failed!")
                st.subheader("✅ Here's the Correct Version")
                st.success(
                    "Agent Raven received a secret message while hiding behind the statue. "
                    "The mission was classified, and the password was \"phoenix\". "
                    "Just like in the movies, only James Bond could pull it off. 🕶️💣"
                )

# ========= STORY 3: Jungle Adventure ==========
elif story_option == "🐾 Jungle Adventure":
    st.markdown("### 🧾 Story: *The Jungle Surprise*")
    st.markdown(
        """
Deep in the **_____** jungle, a **_____** explorer found a **_____** animal.  
It made a loud **_____** before jumping into the **_____**!  
It was a day the jungle would never forget. 🌴🐒
"""
    )

    st.sidebar.header("🐾 Fill in the Blanks (Jungle Adventure)")
    jungles = ["rainy", "dense", "tropical"]
    explorers = ["brave", "curious", "lost"]
    animals = ["spotted", "striped", "giant"]
    sounds = ["roar", "screech", "growl"]
    places = ["river", "cave", "waterfall"]

    jungle = st.sidebar.selectbox("1️⃣ Jungle Type", [""] + jungles)
    explorer = st.sidebar.selectbox("2️⃣ Explorer Type", [""] + explorers)
    animal = st.sidebar.selectbox("3️⃣ Animal Type", [""] + animals)
    sound = st.sidebar.selectbox("4️⃣ Animal Sound", [""] + sounds)
    location = st.sidebar.selectbox("5️⃣ Place in Jungle", [""] + places)

    correct_jungle_combo = {
        "jungle": "tropical",
        "explorer": "curious",
        "animal": "striped",
        "sound": "roar",
        "location": "waterfall"
    }

    if all([jungle, explorer, animal, sound, location]):
        if st.button("🐒 Begin Jungle Adventure"):
            if (
                jungle == correct_jungle_combo["jungle"] and
                explorer == correct_jungle_combo["explorer"] and
                animal == correct_jungle_combo["animal"] and
                sound == correct_jungle_combo["sound"] and
                location == correct_jungle_combo["location"]
            ):
                st.success(
                    f"Deep in the {jungle} jungle, a {explorer} explorer found a {animal} animal. "
                    f"It made a loud {sound} before jumping into the {location}! "
                    f"It was a day the jungle would never forget. 🌴🐒"
                )
            else:
                st.error("😵‍💫 Lost in the Jungle!")
                st.subheader("✅ Here's the Correct Version")
                st.success(
                    "Deep in the tropical jungle, a curious explorer found a striped animal. "
                    "It made a loud roar before jumping into the waterfall! "
                    "It was a day the jungle would never forget. 🌴🐒"
                )
                
# Separator before footer
st.markdown("---")
st.markdown("🧠 Ready for another round? Choose a different story from the top and fill in the blanks!")

# Footer
st.markdown("Made with ❤️ by Hubab — Explore Stories, One Blank at a Time! ✍️🌟")



