import streamlit as st
import pandas as pd
from datetime import datetime
import os
import re

# Page configuration
st.set_page_config(
    page_title="Kodesx Academy | Robotics · AI · Web Development",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main styling */
    .stApp {
        background: linear-gradient(135deg, #f5f7ff 0%, #ffffff 100%);
    }
    
    /* Hero section */
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #1E3C72, #2A5298);
        -webkit-background-clip: text;
        -webkit-text-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: #4a5568;
        margin-bottom: 2rem;
    }
    
    /* Course cards */
    .course-card {
        background: white;
        padding: 1.5rem;
        border-radius: 20px;
        border: 1px solid #eef2f8;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        transition: transform 0.3s;
        height: 100%;
    }
    
    .course-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    
    .course-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .course-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1E3C72;
        margin-bottom: 0.5rem;
    }
    
    .feature-list {
        list-style: none;
        padding-left: 0;
    }
    
    .feature-list li {
        padding: 0.3rem 0;
        color: #4a5568;
    }
    
    /* Stats styling */
    .stat-box {
        background: linear-gradient(135deg, #1E3C72, #2A5298);
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        color: white;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 800;
    }
    
    /* Testimonial cards */
    .testimonial-card {
        background: white;
        padding: 1.5rem;
        border-radius: 20px;
        border-left: 4px solid #2A5298;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #1E3C72, #2A5298);
        color: white;
        border-radius: 40px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        border: none;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(30,60,114,0.3);
    }
    
    /* Form styling */
    .form-container {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #5a6e85;
        border-top: 1px solid #e2e8f0;
        margin-top: 3rem;
    }
    
    /* Section headers */
    .section-header {
        font-size: 2.2rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        color: #0a1929;
    }
    
    hr {
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Excel file handling functions
EXCEL_FILE = "kodesx_students.xlsx"

def init_excel_file():
    """Create Excel file with headers if it doesn't exist"""
    if not os.path.exists(EXCEL_FILE):
        df = pd.DataFrame(columns=[
            "Timestamp",
            "Student Name",
            "Age",
            "Email",
            "Phone Number",
            "Course Interest",
            "Status"
        ])
        df.to_excel(EXCEL_FILE, index=False)
        return df
    return pd.read_excel(EXCEL_FILE)

def save_student_data(name, age, email, phone, course):
    """Save student data to Excel file"""
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
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone number (basic validation)"""
    # Remove spaces, dashes, and plus sign
    cleaned = re.sub(r'[\s\-+]', '', phone)
    return cleaned.isdigit() and len(cleaned) >= 8

# Navigation menu
st.sidebar.markdown("---")
st.sidebar.markdown("## 📱 Quick Links")
page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "📚 Courses", "📊 Admin Dashboard", "📞 Contact"]
)
st.sidebar.markdown("---")
st.sidebar.info(
    "**Kodesx Academy**\n\n"
    "📧 hello@kodesx.com\n\n"
    "📞 +1 (555) 123-4567"
)

# Admin login (simple for demo)
if page == "📊 Admin Dashboard":
    st.markdown("## 🔐 Admin Access")
    password = st.text_input("Enter admin password:", type="password")
    
    if password == "admin123":  # Change this to your preferred password
        st.success("✅ Access granted!")
        
        # Load and display student data
        if os.path.exists(EXCEL_FILE):
            df = pd.read_excel(EXCEL_FILE)
            
            if not df.empty:
                st.markdown("## 📊 Student Registration Data")
                st.dataframe(df, use_container_width=True)
                
                # Download button
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download as CSV",
                    data=csv,
                    file_name=f"kodesx_students_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv"
                )
                
                # Basic statistics
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Total Students", len(df))
                with col2:
                    st.metric("Courses Offered", 3)
                with col3:
                    avg_age = df['Age'].mean() if 'Age' in df.columns else 0
                    st.metric("Average Age", f"{avg_age:.1f}")
                with col4:
                    top_course = df['Course Interest'].mode().iloc[0] if not df['Course Interest'].empty else "N/A"
                    st.metric("Most Popular", top_course)
                
                # Course distribution chart
                st.markdown("### 📊 Course Distribution")
                course_counts = df['Course Interest'].value_counts()
                st.bar_chart(course_counts)
                
            else:
                st.info("No student data available yet.")
        else:
            st.info("No data file found. Submit a form first!")
    else:
        st.error("❌ Incorrect password")

# Main page content
elif page == "🏠 Home":
    # Hero section
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown('<p style="background:#eef2ff; display:inline-block; padding:6px 14px; border-radius:30px; font-size:0.85rem;">🚀 Future-tech learning hub</p>', unsafe_allow_html=True)
        st.markdown('<h1 style="font-size:3rem; font-weight:800;">Master <span style="color:#2A5298;">Robotics, AI & Web</span><br>with Kodesx Academy</h1>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:1.2rem; color:#4a5568;">Hands-on projects, expert mentors, and career-ready skills in the most in-demand tech fields.</p>', unsafe_allow_html=True)
        
        # Stats row
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.markdown('<div class="stat-box"><div class="stat-number">4.9</div><div>⭐ student rating</div></div>', unsafe_allow_html=True)
        with col_b:
            st.markdown('<div class="stat-box"><div class="stat-number">1,800+</div><div>active learners</div></div>', unsafe_allow_html=True)
        with col_c:
            st.markdown('<div class="stat-box"><div class="stat-number">25+</div><div>industry experts</div></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background:linear-gradient(145deg, #e0e7ff, #f5f7ff); border-radius:40px; padding:2rem; text-align:center;">
            <div style="font-size:5rem;">🤖🧠💻</div>
            <h3 style="color:#1E3C72;">Learn · Build · Innovate</h3>
            <p>Join 1,800+ students worldwide</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Why Kodesx section
    st.markdown('<h2 class="section-header">Why Kodesx Academy?</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 🎯 Our Mission
        We bridge the gap between theory and real-world engineering. Every course is co-created with tech industry leaders.
        
        ✅ Live interactive sessions & 1:1 mentoring  
        ✅ Real-world projects & portfolio building  
        ✅ Career support & interview prep  
        ✅ Lifetime access to course materials
        """)
    
    with col2:
        st.markdown("""
        <div style="background:#f0f4fe; padding:1.5rem; border-radius:20px;">
            <h4>📊 Our Impact</h4>
            <p>🎓 <strong>92%</strong> job placement rate</p>
            <p>🏆 <strong>50+</strong> partner companies</p>
            <p>🌍 <strong>35+</strong> countries represented</p>
            <p>⭐ <strong>4.89/5</strong> average rating</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "📚 Courses":
    st.markdown('<h2 class="section-header">📘 Our Flagship Programs</h2>', unsafe_allow_html=True)
    
    # Course cards using columns
    col1, col2, col3 = st.columns(3)
    
    courses = [
        {
            "icon": "🤖",
            "title": "Robotics",
            "features": [
                "Arduino & Raspberry Pi",
                "ROS (Robot Operating System)",
                "Computer Vision for robots",
                "Build 5+ real robots"
            ],
            "duration": "14 weeks · project-based"
        },
        {
            "icon": "🧠",
            "title": "Artificial Intelligence",
            "features": [
                "Python & TensorFlow/PyTorch",
                "Neural Networks & NLP",
                "Computer Vision & LLMs",
                "8 portfolio projects"
            ],
            "duration": "16 weeks · mentor-led"
        },
        {
            "icon": "💻",
            "title": "Web Development",
            "features": [
                "HTML/CSS/JavaScript",
                "React & Node.js",
                "Databases & API design",
                "6 live projects"
            ],
            "duration": "12 weeks · career focus"
        }
    ]
    
    for idx, course in enumerate(courses):
        with [col1, col2, col3][idx]:
            st.markdown(f"""
            <div class="course-card">
                <div class="course-icon">{course['icon']}</div>
                <div class="course-title">{course['title']}</div>
                <ul class="feature-list">
                    {"".join([f"<li>✅ {f}</li>" for f in course['features']])}
                </ul>
                <p style="margin-top:1rem;"><span style="background:#eef2ff; padding:0.3rem 0.8rem; border-radius:20px;">{course['duration']}</span></p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Testimonials
    st.markdown('<h2 class="section-header">✨ What Our Students Say</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    testimonials = [
        {"text": "The Robotics course at Kodesx gave me hands-on experience I couldn't get anywhere else. I built a line-following robot and a robotic arm. Now I'm working as a robotics engineer!", "name": "Ahmed R., Robotics Engineer"},
        {"text": "The AI program is exceptional. The instructors break down complex ML concepts into digestible lessons. The projects helped me land a data scientist role within 3 months.", "name": "Sara M., AI Specialist"},
        {"text": "From zero to full-stack developer in 12 weeks. The web dev course is intense but worth it. The career support team helped me prepare for interviews.", "name": "Omar K., Full-Stack Dev"}
    ]
    
    for idx, testimonial in enumerate(testimonials):
        with [col1, col2, col3][idx]:
            st.markdown(f"""
            <div class="testimonial-card">
                <p style="font-style:italic;">“{testimonial['text']}”</p>
                <p style="font-weight:700; color:#1E3C72; margin-top:0.5rem;">— {testimonial['name']}</p>
            </div>
            """, unsafe_allow_html=True)

elif page == "📞 Contact":
    st.markdown('<h2 class="section-header">📝 Enroll at Kodesx Academy</h2>', unsafe_allow_html=True)
    
    st.info("🎓 Fill out the form below to get course information and a free consultation!")
    
    with st.container():
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("👤 Full Name *", placeholder="Enter your full name")
            age = st.number_input("🎂 Age *", min_value=5, max_value=100, step=1, placeholder="Enter your age")
            email = st.text_input("📧 Email Address *", placeholder="your@email.com")
        
        with col2:
            phone = st.text_input("📞 Phone Number *", placeholder="+1 234 567 8900")
            course = st.selectbox(
                "📚 Select Course *",
                ["Robotics", "Artificial Intelligence", "Web Development"]
            )
            hear_about = st.selectbox(
                "How did you hear about us?",
                ["Social Media", "Friend/Family", "Google Search", "Advertisement", "Other"]
            )
        
        st.markdown("---")
        
        if st.button("🚀 Submit Application", use_container_width=True):
            # Validation
            errors = []
            
            if not name:
                errors.append("Name is required")
            if not age or age < 5:
                errors.append("Please enter a valid age (5-100)")
            if not email or not validate_email(email):
                errors.append("Please enter a valid email address")
            if not phone or not validate_phone(phone):
                errors.append("Please enter a valid phone number (at least 8 digits)")
            
            if errors:
                for error in errors:
                    st.error(f"❌ {error}")
            else:
                # Save to Excel
                save_student_data(name, age, email, phone, course)
                
                # Success message
                st.success(f"""
                ✅ **Registration successful!**
                
                Thank you {name}! We've received your application for {course}.
                
                🎉 **What's next?**
                - Our team will contact you within 24 hours
                - You'll receive course details and pricing
                - A free consultation call will be scheduled
                
                Check your email at {email} for confirmation.
                """)
                
                st.balloons()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Contact info sidebar
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**📧 Email**\nhello@kodesx.com")
    with col2:
        st.markdown("**📞 Phone**\n+1 (555) 123-4567")
    with col3:
        st.markdown("**🌐 Location**\nOnline · Worldwide")

# Footer
st.markdown("---")
st.markdown('<div class="footer"><p>© 2025 Kodesx Academy — Where innovators are made. All rights reserved.</p><p style="margin-top:8px;">📧 hello@kodesx.com &nbsp;|&nbsp; 📞 +1 (555) 123-4567</p></div>', unsafe_allow_html=True)
