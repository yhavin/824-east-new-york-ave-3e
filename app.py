import streamlit as st
from streamlit_carousel import carousel
from streamlit_js_eval import streamlit_js_eval



# =======================
# Constants
# =======================
screen_width = streamlit_js_eval(js_expressions='screen.width', key='SCR')
if screen_width and screen_width < 768:
    is_mobile = True
else:
    is_mobile = False

images = [
    {
        "text": "Kitchen",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5852.jpeg"
    },
    {
        "text": "Kitchen",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5854.jpeg"
    },
    {
        "text": "Kitchen",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5868.jpeg"
    },
    {
        "text": "Dining",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5851.jpeg"
    },
    {
        "text": "Dining",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5869.jpeg"
    },
    {
        "text": "Living",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5859.jpeg"
    },
    {
        "text": "Living",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5858.jpeg"
    },
    {
        "text": "Living",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5861.jpeg"
    },
    {
        "text": "Bedroom",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5871.jpeg"
    },
    {
        "text": "Bedroom",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5872.jpeg"
    },
    {
        "text": "Bedroom",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5874.jpeg"
    },
    {
        "text": "Bedroom",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5877.jpeg"
    },
    {
        "text": "Bedroom",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5880.jpeg"
    },
    {
        "text": "Bathroom",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5866.jpeg"
    },
    {
        "text": "Bathroom",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5867.jpeg"
    },
    {
        "text": "Laundry",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5862.jpeg"
    },
    {
        "text": "Porch",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5883.jpeg"
    },
    {
        "text": "Porch",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5884.jpeg"
    },
    {
        "text": "Gym",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5846.jpeg"
    },
    {
        "text": "Lobby",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5845.jpeg"
    },
    {
        "text": "Roof",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_3712.jpeg"
    },
    {
        "text": "Roof",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_3713.jpeg"
    },
    {
        "text": "Roof",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_3714.jpeg"
    },
    {
        "text": "Roof",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5844.jpeg"
    },
    {
        "text": "Bedroom",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5840.jpeg"
    },
    {
        "text": "Living",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5841.jpeg"
    },
    {
        "text": "Bathroom",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/IMG_5842.jpeg"
    },
    {
        "text": "Map",
        "img": "https://raw.githubusercontent.com/yhavin/824-east-new-york-ave-3e/main/assets/map.png"
    },

]

images = [{**image, "title": i + 1} for i, image in enumerate(images)]


# =======================
# User interface
# =======================
st.set_page_config(
    page_title="824 East New York Ave 3E",
    layout="wide",
    menu_items={
        "Get help": None,
        "Report a bug": None,
        "About": "824 East New York Ave 3E"
    }
)

hero_section = st.container()
hero_title, hero_carousel = hero_section.columns([4, 5])

with hero_title:
    st.header(":blue[824 East New York Ave 3E]", divider="blue")

    st.badge("$2,588 rent")
    st.caption("Available March 1, 2026")
    st.badge("600 sqft | 4 rooms | 1 bed | 1 bath")

    button1, button2 = st.columns([3, 2], width=300)
    button1.link_button(
        label="📱 WhatsApp Yakir",
        type="primary",
        url="https://wa.link/wvd9dq"
    )
    button2.link_button(
        label="💬 Text Yakir",
        type="secondary",
        url="sms:+19179150430?body=Hi Yakir, I'm inquiring about 824 East New Ave 3E. My name is"
    )

    st.video(
        data="https://www.youtube.com/watch?v=EVBsLhNP8EU"
    )

    st.caption("More information below images.")

with hero_carousel:
    if is_mobile:
        height = 500
    else:
        height = 700
        
    carousel(
        items=images,
        slide=False,
        wrap=True,
        pause="hover",
        container_height=height,
        width=1
    )

if is_mobile:
    button1, button2 = st.columns([3, 2], width=300)
    button1.link_button(
        label="📱 WhatsApp Yakir",
        type="primary",
        url="https://wa.link/wvd9dq"
    )
    button2.link_button(
        label="💬 Text Yakir",
        type="secondary",
        url="sms:+19179150430?body=Hi Yakir, I'm inquiring about 824 East New Ave 3E. My name is"
    )

st.divider()

st.header(
    body="About",
    text_alignment="center"
)
st.markdown(
    body="""
    Welcome to 824 East New York Ave 3E.
    
    Modern, spacious, bright 1 bedroom apartment in Crown Heights with elevators, gym, furnished roof, and parking available.

    Location: East New York Ave b/w Troy Ave and Schenectady Ave.

    **Available March 1, 2026.**

    *The bedroom fits one full bed comfortably (pictured) and one queen more tightly.*
    """
)

st.subheader(
    body="Features",
    text_alignment="center"
)
st.markdown(
    body="""
    - Washer/dryer in-unit
    - Two huge elevators
    - Split system A/C in every room
    - Dishwasher
    - Porch
    - Separate living and dining areas
    - Spacious storage and bedroom closets
    - Gas stove (gas utilities included)
    - Virtual doorman
    - South facing windows give great sunlight
    - Furnished roof
    - State of the art gym
    - Trash chute on each floor
    - Secure package room
    - Parking available (extra fee)
    - Next door to supermarket for easy grocery shopping
    - Pictured furniture not included
    """
)

st.subheader(
    body="Fees",
    text_alignment="center"
)
st.markdown(
    body="""
    - Rent: $2,588
    - Security: equal to first month's rent
    - Electric utilities: tenant responsibility
    - Gas utilities: included
    - Broker fee: None
    """
)

button1, button2 = st.columns([3, 2], width=300)
button1.link_button(
    label="📱 WhatsApp Yakir",
    type="primary",
    url="https://wa.link/wvd9dq"
)
button2.link_button(
    label="💬 Text Yakir",
    type="secondary",
    url="sms:+19179150430?body=Hi Yakir, I'm inquiring about 824 East New Ave 3E. My name is"
)

st.divider()

st.caption("Disclaimer: I (Yakir Havin) am not a real estate broker nor do I represent this building.")
st.caption("I have lived in this apartment for the past year and have been extremely happy here.")
st.caption("I am moving out to a larger apartment and am looking for a tenant to start a new lease.")