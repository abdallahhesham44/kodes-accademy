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
# LOGO DISPLAY FUNCTION (Using your exact logo)
# ==========================================
def display_logo(sidebar=False):
    """
    Displays the uploaded Kodex Academy logo.
    """
    # اسم ملف اللوجو الذي قمت برفعه
    logo_path = "1001738156.jpg" 
    
    if os.path.exists(logo_path):
        if sidebar:
            st.sidebar.image(logo_path, use_container_width=True)
            st.sidebar.markdown("<br>", unsafe_allow_html=True)
        else:
            st.image(logo_path, width=160)
    else:
        # تصميم احتياطي بنفس ألوان اللوجو في حال عدم العثور على الملف
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
    /* Global Background matched to Logo Dark Background */
    .stApp {
        background-color: #040814 !important;
        background: radial-gradient(circle at top right, #081229 0%, #040814 70%, #01040a 100%) !important;
    }
    
    /* Text Color Adjustments */
    .main, .stMarkdown, p, h1, h2, h3, h4, h5, h6, label, span {
        color: #f1f7ff !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Sidebar matching the logo core dark color */
    section[data-testid="stSidebar"] {
        background-color: #02050d !important;
        border-right: 1px solid #0b1528;
    }
    
    /* Tech Tag styled after the Logo circuit glow */
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
    
    /* Matching the bright gradient in the 'K' letter */
    .hero-accent {
        background: linear-gradient(135deg, #00d2ff 0%, #0072ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Dashboard Stat Cards */
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
    
    /* Premium Course Cards */
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
    
    /* Form & Container Styling */
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
    
    /* Dynamic Buttons matching the 'K' gradient glow */
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
    
    /* Inputs Dark Mode Overrides */
    div[data-baseweb="input"] input, div[data-baseweb="select"] {
        background-color: #02050d !important;
        color: #f1f7ff !important;
        border-radius: 10px !important;
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
    page = st.radio(
        "Menu Navigation",
        ["🏠 Home", "📚 Flagship Courses", "📊 Admin Dashboard", "📞 Enroll Now"],
        label_visibility="collapsed"
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
        
        # Grid Stats
        stat_col1, stat_col2, stat_col3 = st.columns(3)
        with stat_col1:
            st.markdown('<div class="stat-box"><div class="stat-number">4.9 ★</div><div class="stat-label">Student Rating</div></div>', unsafe_allow_html=True)
        with stat_col2:
            st.markdown('<div class="stat-box"><div class="stat-number">800+</div><div class="stat-label">Active Learners</div></div>', unsafe_allow_html=True)
        with stat_col3:
            st.markdown('<div class="stat-box"><div class="stat-number">25+</div><div class="stat-label">Tech Experts</div></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div style='text-align:center; padding-top:1.5rem;'>", unsafe_allow_html=True)
        display_logo(sidebar=False) # عرض اللوجو بشكل أنيق في الرئيسية
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
# COURSES PAGE
# ==========================================
elif page == "📚 Flagship Courses":
    st.markdown('<h2 class="section-header">Explore Production-Ready Programs</h2>', unsafe_allow_html=True)
    
    c_col1, c_col2, c_col3 = st.columns(3, gap="medium")
    
    courses = [
        {
            "icon": "🤖",
            "title": "Robotics Engineering",
            "features": ["Arduino & Raspberry Pi Ecosystems", "ROS2 Architecture and Control", "Computer Vision Edge Inference", "Hardware-in-the-loop (HIL) Labs"],
            "duration": "14 Weeks · Capstone Portfolio"
        },
        {
            "icon": "🧠",
            "title": "Artificial Intelligence",
            "features": ["Deep Learning & PyTorch Foundations", "Transformers & Generative Modeling", "Advanced Computer Vision (YOLO/ViT)", "LLM Fine-Tuning Architectures"],
            "duration": "16 Weeks · Production Ready"
        },
        {
            "icon": "💻",
            "title": "Full-Stack Web Architect",
            "features": ["Modern React Ecosystem & Next.js", "Asynchronous Node.js Runtimes", "Distributed NoSQL/SQL Architecture", "CI/CD Cloud Automation (Docker)"],
            "duration": "12 Weeks · Microservices Centric"
        }
    ]
    
    for idx, col in enumerate([c_col1, c_col2, c_col3]):
        with col:
            st.markdown(f"""
            <div class="course-card">
                <div>
                    <div style="font-size:2.5rem; margin-bottom:1rem;">{courses[idx]['icon']}</div>
                    <div class="course-title">{courses[idx]['title']}</div>
                    <ul class="feature-list" style="list-style:none; padding:0;">
                        {"".join([f"<li><span style='color:#00d2ff; font-weight:bold;'>✓</span> {item}</li>" for item in courses[idx]['features']])}
                    </ul>
                </div>
                <div style="margin-top: 1.5rem;">
                    <span class="course-badge">{courses[idx]['duration']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown('<h2 class="section-header">Alumni Success Stories</h2>', unsafe_allow_html=True)
    t_col1, t_col2, t_col3 = st.columns(3, gap="medium")
    
    testimonials = [
        {"text": "The Robotics architecture gave me true hands-on HIL experience. Building the computer vision tracking pipelines directly helped land my current core robotics engineering role.", "name": "Ahmed R., Robotics Infrastructure Engineer"},
        {"text": "The Deep Learning modules are unparalleled. They remove abstractions and force you to construct neural nets from the mathematical foundation up.", "name": "Sara M., Enterprise AI Architect"},
        {"text": "Rigorous, production-focused curriculum. The multi-tenant backend architecture labs pushed me to get hired before I even graduated.", "name": "Omar K., Systems Software Engineer"}
    ]
    
    for idx, col in enumerate([t_col1, t_col2, t_col3]):
        with col:
            st.markdown(f"""
            <div class="testimonial-card">
                <p style="font-style:italic; color: #cbd5e1 !important; line-height:1.6;">“{testimonials[idx]['text']}”</p>
                <p style="font-weight:700; color:#00d2ff !important; margin-top:1.2rem; font-size:0.9rem;">— {testimonials[idx]['name']}</p>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# ENROLLMENT PAGE
# ==========================================
elif page == "📞 Enroll Now":
    st.markdown('<h2 class="section-header">Accelerate Your Engineering Career</h2>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        form_col1, form_col2 = st.columns(2, gap="large")
        
        with form_col1:
            name = st.text_input("👤 Full Name *", placeholder="e.g. Alex Mercer")
            age = st.number_input("🎂 Age *", min_value=5, max_value=100, step=1, value=20)
            email = st.text_input("📧 Personal / Professional Email *", placeholder="alex@domain.com")
        
        with form_col2:
            phone = st.text_input("📞 Phone Number (with Country Code) *", placeholder="+20 123 456 7890")
            course = st.selectbox(
                "📚 Select Target Track *",
                ["Robotics Engineering", "Artificial Intelligence", "Full-Stack Web Architect"]
            )
            hear_about = st.selectbox(
                "Discovery Source",
                ["Social Networks", "Professional Recommendation", "Search Platforms", "Other"]
            )
            
        st.markdown("<br>", unsafe_allow_html=True)
        submit_btn = st.button("🚀 Process Application Execution", use_container_width=True)
        
        if submit_btn:
            errors = []
            if not name: errors.append("Name profile entry is required")
            if not email or not validate_email(email): errors.append("Valid syntax for Email is required")
            if not phone or not validate_phone(phone): errors.append("Valid parameters for phone required")
            
            if errors:
                for error in errors:
                    st.error(f"⚠️ {error}")
            else:
                save_student_data(name, age, email, phone, course)
                st.balloons()
                st.success(f"✔️ Application sequence complete! Welcome, {name}. Our team will contact you within 24 hours.")
                
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ADMIN DASHBOARD
# ==========================================
elif page == "📊 Admin Dashboard":
    st.markdown('<h2 class="section-header">Terminal Access Layer</h2>', unsafe_allow_html=True)
    
    _, center_col, _ = st.columns([1, 1.5, 1])
    with center_col:
        password = st.text_input("Provide Admin Decryption Key:", type="password")
    
    if password == "admin123":
        st.success("🔒 Access Authorization Granted.")
        
        if os.path.exists(EXCEL_FILE):
            df = pd.read_excel(EXCEL_FILE)
            
            if not df.empty:
                m_col1, m_col2, m_col3, m_col4 = st.columns(4)
                with m_col1: st.metric("Total Applications Ingested", len(df))
                with m_col2: st.metric("Active Live Tracks", 3)
                with m_col3: 
                    avg_age = df['Age'].mean() if 'Age' in df.columns else 0
                    st.metric("Mean Class Age", f"{avg_age:.1f} yrs")
                with m_col4:
                    top_c = df['Course Interest'].mode().iloc[0] if not df['Course Interest'].empty else "None"
                    st.metric("High-Demand Track", top_c)
                
                st.markdown("<br><hr>", unsafe_allow_html=True)
                
                st.markdown("### 📊 Distribution Across Modules")
                st.bar_chart(df['Course Interest'].value_counts())
                
                st.markdown("### 📋 Student Ingestion Database")
                st.dataframe(df.style.background_gradient(cmap="Blues"), use_container_width=True)
                
                csv_data = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Export Secure CSV File",
                    data=csv_data,
                    file_name=f"kodex_db_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv"
                )
            else:
                st.info("Database array is initialized but contains 0 records.")
        else:
            st.info("No active Relational Database file found.")
    elif password != "":
        st.error("🛑 Security token mismatch. Access Denied.")

# ==========================================
# FOOTER
# ==========================================
st.markdown("""
<hr>
<div class="footer">
    <p>© 2026 Kodex Academy — Where Next-Gen Architects Are Forged. All Rights Reserved.</p>
</div>
""", unsafe_allow_html=True)
