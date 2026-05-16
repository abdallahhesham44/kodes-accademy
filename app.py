import streamlit as st
import pandas as pd
from datetime import datetime
import os
import re

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Kodex Academy | Future-Tech Learning Hub",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# LOGO DISPLAY FUNCTION
# ==========================================
def display_logo(sidebar=False):
    logo_path = "1001738156.jpg" 
    if os.path.exists(logo_path):
        if sidebar:
            st.sidebar.image(logo_path, use_container_width=True)
            st.sidebar.markdown("<br>", unsafe_allow_html=True)
        else:
            st.image(logo_path, width=160)
    else:
        logo_html = f"""
        <div style="padding: 10px 0; margin-bottom: 15px;">
            <span style="font-size: 1.8rem; font-weight: 800; background: linear-gradient(135deg, #00d2ff, #0072ff);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;">&lt; K &gt;</span>
            <span style="font-size: 1.1rem; font-weight: 400; color: #00d2ff; block: block; letter-spacing: 1px;">KODEX ACADEMY</span>
        </div>
        """
        if sidebar:
            st.sidebar.markdown(logo_html, unsafe_allow_html=True)
        else:
            st.markdown(logo_html, unsafe_allow_html=True)

# ==========================================
# MATCHED COLORS THEME (CYAN & TECH BLUE)
# ==========================================
st.markdown("""
<style>
    .stApp {
        background-color: #040814 !important;
        background: radial-gradient(circle at top right, #081229 0%, #040814 70%, #01040a 100%) !important;
    }
    .main, .stMarkdown, p, h1, h2, h3, h4, h5, h6, label, span {
        color: #f1f7ff !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    section[data-testid="stSidebar"] {
        background-color: #02050d !important;
        border-right: 1px solid #0b1528;
    }
    .hero-tag {
        background: rgba(0, 210, 255, 0.08); 
        color: #00d2ff !important; 
        display: inline-block; 
        padding: 6px 16px; 
        border-radius: 30px; 
        font-size: 0.85rem;
        font-weight: 600;
        letter-spacing: 1px;
        border: 1px solid rgba(0, 210, 255, 0.25);
        margin-bottom: 1.2rem;
    }
    .hero-title {
        font-size: 3.6rem !important;
        font-weight: 800 !important;
        line-height: 1.2;
        background: linear-gradient(135deg, #ffffff 40%, #a2c4e8 80%, #00d2ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1.5rem;
    }
    .hero-accent {
        background: linear-gradient(135deg, #00d2ff 0%, #0072ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .stat-box {
        background: rgba(11, 21, 40, 0.5);
        border: 1px solid #0b1528;
        padding: 1.5rem 1rem;
        border-radius: 16px;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stat-box:hover {
        border-color: #00d2ff;
        background: rgba(11, 21, 40, 0.8);
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0, 210, 255, 0.1);
    }
    .stat-number {
        font-size: 2.3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #00d2ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .stat-label {
        color: #708aa6 !important;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .course-card {
        background: rgba(7, 13, 26, 0.7);
        padding: 2.2rem;
        border-radius: 24px;
        border: 1px solid #0b1528;
        box-shadow: 0 15px 35px rgba(0,0,0,0.6);
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .course-card:hover {
        transform: translateY(-8px);
        border-color: #00d2ff;
        box-shadow: 0 20px 40px rgba(0, 210, 255, 0.12);
    }
    .course-title {
        font-size: 1.55rem !important;
        font-weight: 700 !important;
        color: #ffffff !important;
        margin-bottom: 1.2rem;
    }
    .feature-list li {
        color: #8fa0b5 !important;
        margin-bottom: 0.7rem;
        font-size: 0.95rem;
    }
    .course-badge {
        background: #0b1528 !important;
        color: #00d2ff !important;
        padding: 5px 14px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 600;
        border: 1px solid #142542;
        display: inline-block;
    }
    .form-container {
        background: rgba(7, 13, 26, 0.9);
        padding: 2.5rem;
        border-radius: 24px;
        border: 1px solid #0b1528;
        box-shadow: 0 25px 50px rgba(0,0,0,0.5);
    }
    .testimonial-card {
        background: rgba(11, 21, 40, 0.3);
        padding: 2rem;
        border-radius: 20px;
        border-left: 3px solid #00d2ff;
        border-top: 1px solid #0b1528;
        border-bottom: 1px solid #0b1528;
        border-right: 1px solid #0b1528;
        height: 100%;
    }
    .section-header {
        font-size: 2.4rem !important;
        font-weight: 800 !important;
        text-align: center;
        margin: 4rem 0 2.5rem 0;
        background: linear-gradient(135deg, #ffffff 0%, #8fa0b5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .stButton > button {
        background: linear-gradient(135deg, #00d2ff 0%, #0072ff 100%) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        padding: 0.7rem 2.5rem !important;
        font-weight: 600 !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0, 210, 255, 0.25) !important;
        transition: all 0.2s ease !important;
        width: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(0, 210, 255, 0.45) !important;
    }
    div[data-baseweb="input"] input, div[data-baseweb="select"] {
        background-color: #02050d !important;
        color: #f1f7ff !important;
        border-radius: 10px !important;
    }
    /* Dynamic styling targeting Streamlit native tabs */
    button[data-baseweb="tab"] {
        color: #8fa0b5 !important;
        font-size: 1.1rem !important;
    }
    button[aria-selected="true"] {
        color: #00d2ff !important;
        border-bottom-color: #00d2ff !important;
    }
    hr {
        border-color: #0b1528 !important;
        margin: 3rem 0;
    }
    .footer {
        text-align: center;
        padding: 2.5rem 0;
        color: #4b5e73 !important;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# EXCEL HANDLING FUNCTIONS
# ==========================================
EXCEL_FILE = "kodesx_students.xlsx"

def init_excel_file():
    if not os.path.exists(EXCEL_FILE):
        df = pd.DataFrame(columns=[
            "Timestamp", "Student Name", "Age", "Email", "Phone Number", "Course Interest", "Status"
        ])
        df.to_excel(EXCEL_FILE, index=False)
        return df
    return pd.read_excel(EXCEL_FILE)

def save_student_data(name, age, email, phone, course):
    df = init_excel_file()
    new_data = pd.DataFrame([{
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Student Name": name,
        "Age": age,
        "Email": email,
        "Phone Number": phone,
        "Course Interest": course,
        "Status": "New Lead"
    }])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_excel(EXCEL_FILE, index=False)
    return df

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    cleaned = re.sub(r'[\s\-+]', '', phone)
    return cleaned.isdigit() and len(cleaned) >= 8

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    display_logo(sidebar=True)
    page = st.sidebar.radio(
        "Menu Navigation",
        ["🏠 Home", "📚 Flagship Courses", "📊 Admin Dashboard", "📞 Enroll Now"]
    )
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: rgba(11, 21, 40, 0.4); padding: 1.2rem; border-radius: 16px; border: 1px solid #0b1528;">
        <p style="font-weight: 700; margin-bottom: 8px; color: #00d2ff !important; font-size:0.9rem;">🎯 Contact Support</p>
        <p style="font-size: 0.85rem; margin: 4px 0; color:#8fa0b5 !important;">📧 kodex.accademy@gmail.com</p>
        <p style="font-size: 0.85rem; margin: 4px 0; color:#8fa0b5 !important;">📞 + (20) 01551351712</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# HOME PAGE
# ==========================================
if page == "🏠 Home":
    col1, col2 = st.columns([2.3, 1.7], gap="large")
    
    with col1:
        st.markdown('<span class="hero-tag">🚀 FUTURE-TECH LEARNING HUB</span>', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">Master <span class="hero-accent">Robotics, AI & Web Dev</span> with Kodex Academy</h1>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:1.15rem; color:#8fa0b5 !important; line-height: 1.6; margin-bottom: 2.5rem;">Build production-grade engineering skills through live immersive masterclasses guided directly by technology pioneers.</p>', unsafe_allow_html=True)
        
        stat_col1, stat_col2, stat_col3 = st.columns(3)
        with stat_col1:
            st.markdown('<div class="stat-box"><div class="stat-number">4.9 ★</div><div class="stat-label">Student Rating</div></div>', unsafe_allow_html=True)
        with stat_col2:
            st.markdown('<div class="stat-box"><div class="stat-number">800+</div><div class="stat-label">Active Learners</div></div>', unsafe_allow_html=True)
        with stat_col3:
            st.markdown('<div class="stat-box"><div class="stat-number">25+</div><div class="stat-label">Tech Experts</div></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div style='text-align:center; padding-top:1.5rem;'>", unsafe_allow_html=True)
        display_logo(sidebar=False) 
        st.markdown("""
        <div style="background: linear-gradient(145deg, #070d1a, #0b1528); border-radius:24px; padding:2rem; text-align:center; border: 1px solid #142542; box-shadow: 0 20px 40px rgba(0,0,0,0.5); margin-top: 1.5rem;">
            <h3 style="font-weight: 800; font-size: 1.5rem; margin-bottom: 0.5rem; color:#ffffff !important;">Learn · Build · Innovate</h3>
            <p style="color: #8fa0b5 !important; font-size:0.95rem;">Become part of an elite network of modern developers.</p>
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-header">Why Engineers Choose Kodex</h2>', unsafe_allow_html=True)
    
    box_col1, box_col2 = st.columns(2, gap="large")
    with box_col1:
        st.markdown("""
        <div style="background: rgba(7,13,26,0.5); padding: 2rem; border-radius: 20px; border: 1px solid #0b1528; height:100%;">
            <h4 style="color: #00d2ff !important; font-size: 1.3rem; font-weight: 700; margin-bottom:1rem;">🎯 Our Shared Mission</h4>
            <p style="color: #8fa0b5 !important; line-height: 1.6;">We break down complex engineering frameworks into progressive, project-centric milestones. Every program syllabus is refined directly alongside industry tech leads.</p>
            <ul style="color: #cbd5e1 !important; margin-top: 1rem; padding-left: 20px; line-height: 2;">
                <li>Production-grade deployment environments</li>
                <li>Comprehensive architectural code reviews</li>
                <li>Dedicated industrial portfolio building</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with box_col2:
        st.markdown("""
        <div style="background: rgba(7,13,26,0.5); padding: 2rem; border-radius: 20px; border: 1px solid #0b1528; height: 100%;">
            <h4 style="color: #0072ff !important; font-size: 1.3rem; font-weight: 700; margin-bottom:1rem;">📊 Placement Metrics</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-top: 1.5rem;">
                <div>
                    <h5 style="font-size: 1.8rem; font-weight: 800; color: #ffffff !important; margin: 0;">92%</h5>
                    <p style="color: #4b5e73 !important; font-size: 0.85rem; margin:0;">PLACEMENT RATE</p>
                </div>
                <div>
                    <h5 style="font-size: 1.8rem; font-weight: 800; color: #ffffff !important; margin: 0;">50+</h5>
                    <p style="color: #4b5e73 !important; font-size: 0.85rem; margin:0;">ENTERPRISE PARTNERS</p>
                </div>
                <div>
                    <h5 style="font-size: 1.8rem; font-weight: 800; color: #ffffff !important; margin: 0;">35+</h5>
                    <p style="color: #4b5e73 !important; font-size: 0.85rem; margin:0;">GLOBAL NATIONS</p>
                </div>
                <div>
                    <h5 style="font-size: 1.8rem; font-weight: 800; color: #ffffff !important; margin: 0;">100%</h5>
                    <p style="color: #4b5e73 !important; font-size: 0.85rem; margin:0;">PRACTICAL IMPLEMENTATION</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# COURSES PAGE (WITH NEW DYNAMIC TABS & VIDEO LAB)
# ==========================================
elif page == "📚 Flagship Courses":
    st.markdown('<h2 class="section-header">Explore Production-Ready Programs</h2>', unsafe_allow_html=True)
    
    # NEW FEATURE: Dynamic Interactive Tabs Layout
    tab_overview, tab_robotics, tab_ai, tab_web, tab_videos = st.tabs([
        "🌐 Program Overview", 
        "🤖 Robotics Track", 
        "🧠 Artificial Intelligence", 
        "💻 Web Architecture", 
        "📺 Free Intro Lectures & Videos"
    ])
    
    with tab_overview:
        st.markdown("<br>", unsafe_allow_html=True)
        c_col1, c_col2, c_col3 = st.columns(3, gap="medium")
        
        courses_data = [
            {
                "icon": "🤖", "title": "Robotics Engineering",
                "features": ["Arduino & Raspberry Pi Ecosystems", "ROS2 Architecture and Control", "Computer Vision Edge Inference", "Hardware-in-the-loop (HIL) Labs"],
                "duration": "14 Weeks · Capstone Portfolio"
            },
            {
                "icon": "🧠", "title": "Artificial Intelligence",
                "features": ["Deep Learning & PyTorch Foundations", "Transformers & Generative Modeling", "Advanced Computer Vision (YOLO/ViT)", "LLM Fine-Tuning Architectures"],
                "duration": "16 Weeks · Production Ready"
            },
            {
                "icon": "💻", "title": "Full-Stack Web Architect",
                "features": ["Modern React Ecosystem & Next.js", "Asynchronous Node.js Runtimes", "Distributed NoSQL/SQL Architecture", "CI/CD Cloud Automation (Docker)"],
                "duration": "12 Weeks · Microservices Centric"
            }
        ]
        
        for idx, col in enumerate([c_col1, c_col2, c_col3]):
            with col:
                st.markdown(f"""
                <div class="course-card">
                    <div>
                        <div style="font-size:2.5rem; margin-bottom:1rem;">{courses_data[idx]['icon']}</div>
                        <div class="course-title">{courses_data[idx]['title']}</div>
                        <ul class="feature-list" style="list-style:none; padding:0;">
                            {"".join([f"<li><span style='color:#00d2ff; font-weight:bold;'>✓</span> {item}</li>" for item in courses_data[idx]['features']])}
                        </ul>
                    </div>
                    <div style="margin-top: 1.5rem;">
                        <span class="course-badge">{courses_data[idx]['duration']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    with tab_robotics:
        st.markdown("### 🤖 Advanced Robotics Syllabus")
        col_left, col_right = st.columns(2)
        with col_left:
            st.write("Our syllabus goes from physical circuitry setups up to state-of-the-art robotic localization processing mapping setups.")
            st.markdown("""
            - *Phase 1:* Low-level Microcontrollers & PWM Execution Signals.
            - *Phase 2:* Kinematic Algorithms & Dynamic Joint Linkages.
            - *Phase 3:* Embedded Nodes orchestration via ROS2 Middleware layers.
            """)
        with col_right:
            st.info("🛠️ *Prerequisites:* Basic knowledge of C++ or Python. All hardware experimental development board simulators are provided.")

    with tab_ai:
        st.markdown("### 🧠 Deep Learning & AI Architecture")
        col_left, col_right = st.columns(2)
        with col_left:
            st.write("Construct functional neural layers directly without abstract wrapper constraints.")
            st.markdown("""
            - *Phase 1:* Loss Functions optimization via Custom Backpropagation loops.
            - *Phase 2:* Sequence Processing Transformers & Self-Attention Matrices.
            - *Phase 3:* MLOps deployment paradigms over distributed cluster groups.
            """)
        with col_right:
            st.info("⚡ *Prerequisites:* Linear Algebra foundations and fundamental Python programming patterns.")

    with tab_web:
        st.markdown("### 💻 Distributed Web Systems Architecture")
        col_left, col_right = st.columns(2)
        with col_left:
            st.write("Learn how to engineer web application fabrics intended to serve millions of concurrent network actions seamlessly.")
            st.markdown("""
            - *Phase 1:* Component lifecycle execution patterns under Next.js SSR configurations.
            - *Phase 2:* Horizontal data scalability patterns using Redis / PostgreSQL.
            - *Phase 3:* High availability isolation utilizing Docker containers & Reverse Proxies.
            """)
        with col_right:
            st.info("🚀 *Prerequisites:* Core JavaScript runtime concepts. No prior cloud infrastructure familiarity needed.")

    with tab_videos:
        st.markdown("### 📺 Kodex Streaming Tech Lab")
        st.write("Stream our foundational introductory syntax and conceptual masterclasses below:")
        
        v_col1, v_col2 = st.columns(2)
        with v_col1:
            st.markdown("##### 🟦 Robotics & ROS2 Architectural Setup")
            # You can replace this demo URL
