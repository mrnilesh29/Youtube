import streamlit as st


def apply_theme():
    """
    Ye function poore app ka black-glass 3D theme laga deta hai.
    Har page ke top pe bas ye 2 lines likhni hain:

        from style import apply_theme
        apply_theme()
    """
    st.markdown("""
    <style>

    /* Poora background pure black shades ka moving gradient */
    .stApp {
        background: linear-gradient(-45deg, #000000, #0a0a0a, #121212, #050505);
        background-size: 400% 400%;
        animation: gradientMove 15s ease infinite;
    }

    @keyframes gradientMove {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Sab text white kar diya kyunki background dark hai */
    h1, h2, h3, h4, h5, h6, p, li, span, label {
        color: #f5f5f5 !important;
    }

    /* Title floating + shine effect */
    .main-title {
        text-align: center;
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(90deg, #ffffff, #9ca3af, #ffffff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: floatTitle 3s ease-in-out infinite;
        margin-bottom: 1.5rem;
    }

    @keyframes floatTitle {
        0%, 100% { transform: translateY(0px); }
        50%      { transform: translateY(-8px); }
    }

    /* =====================================================
       🪟 SIDEBAR — glass panel + halka blur
       ===================================================== */
    section[data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.15);
    }

    /* Sidebar ke andar page links (jaise Add_student, Dashboard...) */
    section[data-testid="stSidebar"] a {
        border-radius: 12px !important;
        margin: 4px 8px !important;
        transition: all 0.3s ease;
        color: #e5e7eb !important;
    }

    section[data-testid="stSidebar"] a:hover {
        background: rgba(255, 255, 255, 0.1) !important;
        transform: translateX(4px) scale(1.02);
        box-shadow: 0 4px 15px rgba(255, 255, 255, 0.15);
    }

    /* Currently selected/active page link ko highlight kiya */
    section[data-testid="stSidebar"] a[aria-current="page"] {
        background: rgba(255, 255, 255, 0.12) !important;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 0 12px rgba(255, 255, 255, 0.2);
    }

    /* =====================================================
       🪟 COMMON INPUT GLASS STYLE (text, number, select)
       ===================================================== */
    div[data-baseweb="input"], div[data-baseweb="select"] > div {
        background: rgba(255, 255, 255, 0.08) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        backdrop-filter: blur(10px);
        color: #ffffff !important;
        transition: all 0.3s ease;
    }

    div[data-baseweb="input"]:hover, div[data-baseweb="select"] > div:hover {
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        box-shadow: 0 0 12px rgba(255, 255, 255, 0.2);
    }

    input, textarea {
        color: #ffffff !important;
    }

    button[data-testid="stNumberInputStepUp"], button[data-testid="stNumberInputStepDown"] {
        background: rgba(255, 255, 255, 0.1) !important;
        color: #fff !important;
    }

    /* =====================================================
       🪟 COMMON GLASS CARD (wrap any content in this)
       ===================================================== */
    .glass-card {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 20px;
        padding: 30px 35px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
        margin: 15px 0 20px 0;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        transform-style: preserve-3d;
    }

    .glass-card:hover {
        transform: perspective(1000px) rotateX(2deg) rotateY(-2deg) translateY(-5px);
        box-shadow: 0 20px 40px rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.4);
    }

    /* =====================================================
       🪟 BUTTONS — glowing 3D press effect
       ===================================================== */
    .stButton > button {
        background: rgba(255, 255, 255, 0.1) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        border-radius: 14px !important;
        padding: 10px 0 !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: perspective(600px) rotateX(6deg) translateY(-3px) scale(1.02);
        box-shadow: 0 12px 25px rgba(255, 255, 255, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.8) !important;
        background: rgba(255, 255, 255, 0.18) !important;
    }

    .stButton > button:active {
        transform: scale(0.97);
    }

    /* =====================================================
       🪟 METRIC CARDS (Dashboard ke liye)
       ===================================================== */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.07);
        border-radius: 18px;
        padding: 20px 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        transform-style: preserve-3d;
        text-align: center;
    }

    div[data-testid="stMetric"]:hover {
        transform: perspective(1000px) rotateX(4deg) rotateY(-4deg) translateY(-8px) scale(1.03);
        box-shadow: 0 20px 40px rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.5);
    }

    div[data-testid="stMetricLabel"] {
        color: #d1d5db !important;
        font-size: 1rem !important;
    }

    div[data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 1.8rem !important;
        font-weight: 800 !important;
    }

    /* =====================================================
       🪟 TABLE / DATAFRAME + CHART glass wrap
       ===================================================== */
    div[data-testid="stDataFrame"], div[data-testid="stPlotlyChart"] {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 18px;
        padding: 12px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
        margin-top: 15px;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
    }

    div[data-testid="stDataFrame"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 36px rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.4);
    }

    /* =====================================================
       🪟 ALERT BOXES (info / success / error) glass style
       ===================================================== */
    div[data-testid="stAlertContainer"] {
        background: rgba(255, 255, 255, 0.07) !important;
        border-radius: 18px !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
        padding: 15px 20px !important;
    }

    /* =====================================================
       🪟 BALANCE BOX (CodexBank specific)
       ===================================================== */
    .balance-box {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 18px;
        text-align: center;
        margin-top: 10px;
        border: 1px solid rgba(255, 255, 255, 0.25);
        font-weight: 800;
        font-size: 1.2rem;
    }

    </style>
    """, unsafe_allow_html=True)