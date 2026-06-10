import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from fpdf import FPDF
import streamlit.components.v1 as components
import os   # ✅ ADD THIS

# ✅ FIXED MODEL LOADING
model_path = os.path.join(os.path.dirname(__file__), "food_model.pkl")
model = joblib.load(model_path)

# (optional but recommended fix for CSV too)
csv_path = os.path.join(os.path.dirname(__file__), "food_nutrition.csv")
df = pd.read_csv(csv_path)

df["food_name"] = df["food_name"].astype(str).str.lower().str.strip()

st.set_page_config(page_title="AI Food Health Analyzer", layout="wide")

st.markdown("""
<style>

/* ===================== */
/* 🌸 BACKGROUND THEME */
/* ===================== */
.stApp {
    background: linear-gradient(to right, #faebd7, #fffaf0); /* Antique White + Floral White */
    color: #000000 !important;
}

/* ===================== */
/* GLOBAL TEXT FIX */
/* ===================== */
html, body, [class*="css"] {
    color: #000000 !important;
}

/* ===================== */
/* TITLE */
/* ===================== */
.title {
    text-align: center;
    font-size: 44px;
    font-weight: bold;
    color: #2f4f4f !important; /* Dark Slate Gray */
}

/* ===================== */
/* SUBTITLE */
/* ===================== */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555 !important;
}

/* ===================== */
/* CARD DESIGN */
/* ===================== */
.card {
    background: #ffffff !important;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 8px 22px rgba(0,0,0,0.10);
    border: 1px solid #eee;
    color: #000000 !important;
}

/* FORCE CARD TEXT BLACK */
.card * {
    color: #000000 !important;
}

/* ===================== */
/* METRICS FIX */
/* ===================== */
[data-testid="stMetric"] {
    background-color: transparent !important;
}

[data-testid="stMetricLabel"] {
    color: #333 !important;
}

[data-testid="stMetricValue"] {
    color: #000000 !important;
    font-weight: bold !important;
}

/* ===================== */
/* TEXT ELEMENTS */
/* ===================== */
p, span {
    color: #000000 !important;
}

/* ===================== */
/* BUTTON STYLING */
/* ===================== */
.stButton > button {
    background-color: #ffffff !important;
    color: #000000 !important;
    border: 2px solid #2f4f4f !important;
    border-radius: 10px !important;
    padding: 0.5em 1.2em !important;
    font-weight: bold !important;
    transition: 0.3s ease-in-out;
}

/* Hover effect */
.stButton > button:hover {
    background-color: #2f4f4f !important;
    color: #ffffff !important;
    border: 2px solid #2f4f4f !important;
}

/* ===================== */
/* GRAPH BACKGROUND */
/* ===================== */
.css-1kyxreq, .css-1v0mbdj {
    background-color: white !important;
    border-radius: 12px !important;
    padding: 10px !important;
}
/* ===================== */
/* DOWNLOAD BUTTON FIX */
/* ===================== */
.stDownloadButton > button {
    background-color: #ffffff !important;
    color: #000000 !important;
    border: 2px solid #2f4f4f !important;
    border-radius: 10px !important;
    font-weight: bold !important;
    padding: 0.5em 1.2em !important;
}

/* Hover effect */
.stDownloadButton > button:hover {
    background-color: #2f4f4f !important;
    color: #ffffff !important;
    border: 2px solid #2f4f4f !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🍎 AI Food Nutrition & Health Analyzer</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Smart Nutrition Analysis & Health Recommendation System</div>", unsafe_allow_html=True)

food = st.text_input("Enter Food Name (e.g., apple, banana, burger)")

# ---------------- HEALTH SCORE ----------------
def health_score(row):
    score = 100

    if row["fat"] > 10:
        score -= 20
    if row["calories"] > 250:
        score -= 20
    if row["protein"] < 5:
        score -= 15
    if row["vitamin_c"] < 5:
        score -= 15

    return max(score, 0)

# ---------------- ADVICE ----------------
def get_advice(row):
    html = """
<div style="
background-color:#f0fff4;
padding:20px;
border-radius:12px;
border-left:6px solid #4CAF50;
margin-top:10px;
margin-bottom:15px;
">
<h2>🥗 Dietary Recommendations</h2>
"""

    tips_added = False

    if row["fat"] > 10:
        tips_added = True
        html += """
        <p>✅ Reduce fried and oily foods</p>
        <p>✅ Switch to grilled or boiled food</p>
        <p>✅ High fat intake may increase health risks</p>
        <p>✅ Maintain balanced fat consumption</p>
        """

    if row["calories"] > 250:
        tips_added = True
        html += """
        <p>✅ Control portion size</p>
        <p>✅ Avoid frequent high-calorie meals</p>
        <p>✅ Add vegetables and fruits to your diet</p>
        <p>✅ Include daily walking or exercise</p>
        """

    if row["vitamin_c"] < 5:
        tips_added = True
        html += """
        <p>✅ Add citrus fruits such as oranges and lemons</p>
        <p>✅ Boost immunity naturally</p>
        <p>✅ Eat leafy green vegetables</p>
        <p>✅ Increase vitamin-rich foods</p>
        """

    if row["protein"] < 5:
        tips_added = True
        html += """
        <p>✅ Add eggs, dal, paneer, nuts, or legumes</p>
        <p>✅ Protein supports muscle growth</p>
        <p>✅ Important for recovery and tissue repair</p>
        <p>✅ Essential for overall body strength</p>
        """

    if not tips_added:
        html += """
        <p>✅ Balanced food item</p>
        <p>✅ Suitable for regular consumption</p>
        <p>✅ Maintain a varied and nutritious diet</p>
        <p>✅ Continue healthy eating habits</p>
        """

    html += """
</div>
"""

    html += """
<div style="
background-color:#e8f4ff;
padding:20px;
border-radius:12px;
border-left:6px solid #2196F3;
margin-bottom:15px;
">
<h2>💧 Hydration Advice</h2>

<p>💧 Drink at least 2–3 liters of water daily</p>
<p>💧 Water improves digestion and metabolism</p>
<p>💧 Hydration helps maintain energy levels</p>
<p>💧 Supports healthy skin and body functions</p>
<p>💧 Increase water intake during exercise</p>

</div>
"""

    html += """
<div style="
background-color:#fff3e6;
padding:20px;
border-radius:12px;
border-left:6px solid #ff9800;
">
<h2>🧠 Lifestyle Tips</h2>

<p>🧠 Maintain 7–8 hours of quality sleep</p>
<p>🧠 Reduce stress through meditation or walking</p>
<p>🧠 Avoid excessive junk food consumption</p>
<p>🧠 Stay physically active throughout the day</p>
<p>🧠 Follow a consistent meal schedule</p>

</div>
"""

    return html
# ---------------- PDF ----------------
def create_pdf(data):
    pdf = FPDF()
    pdf.add_page()

    # LIGHT BACKGROUND FEEL (simulated)
    pdf.set_fill_color(250, 235, 215)  # antique white tone

    # TITLE
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(47, 79, 79)  # dark slate gray
    pdf.cell(200, 12, txt="AI Food Health Report", ln=True, align='C')

    pdf.ln(5)

    # RESET TEXT COLOR FOR CONTENT
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)

    for k, v in data.items():
        pdf.cell(200, 10, txt=f"{k}: {v}", ln=True)

    file = "report.pdf"
    pdf.output(file)

    return file

# ---------------- MAIN ----------------
if st.button("Analyze Food"):

    food = food.lower().strip()

    # IMPROVED MATCHING (prevents false not found)
    food_row = df[df["food_name"].str.contains(food, na=False)]

    if not food_row.empty:

        row = food_row.iloc[0]

        calories = row["calories"]
        protein = row["protein"]
        carbs = row["carbs"]
        fat = row["fat"]
        iron = row["iron"]
        vitamin_c = row["vitamin_c"]

        score = health_score(row)

        sample = [[calories, protein, carbs, fat, iron, vitamin_c]]
        result = model.predict(sample)[0]

        col1, col2 = st.columns(2)

        # ---------------- LEFT ----------------
        with col1:
            st.markdown("<div class='card'>", unsafe_allow_html=True)

            st.subheader("🍽 Nutrition Info")

            st.markdown(f"<p style='color:black;'><b>Calories:</b> {calories}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:black;'><b>Protein:</b> {protein}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:black;'><b>Carbs:</b> {carbs}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:black;'><b>Fat:</b> {fat}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:black;'><b>Iron:</b> {iron}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:black;'><b>Vitamin C:</b> {vitamin_c}</p>", unsafe_allow_html=True)

            st.subheader("🧠 Prediction")

            if result == "healthy":
                st.markdown("<p style='color:green; font-size:18px; font-weight:bold;'>🟢 Healthy Food</p>", unsafe_allow_html=True)

            elif result == "moderate":
                st.markdown("<p style='color:orange; font-size:18px; font-weight:bold;'>🟡 Moderate Food</p>", unsafe_allow_html=True)

            else:
                st.markdown("<p style='color:red; font-size:18px; font-weight:bold;'>🔴 Unhealthy Food</p>", unsafe_allow_html=True)

            st.subheader("💯 Health Score")
            st.progress(score / 100)
            st.write(f"Score: {score}/100")

            st.subheader("🥗 Diet & Exercise Advice")

            components.html(
                get_advice(row),
                height=700,
                scrolling=True
            )

            st.markdown("</div>", unsafe_allow_html=True)

        # ---------------- RIGHT ----------------
        with col2:
            st.markdown("<div class='card'>", unsafe_allow_html=True)

            st.subheader("📊 Nutrition Bar Chart")

            fig, ax = plt.subplots()

            ax.bar(
                ["Calories", "Protein", "Carbs", "Fat", "Iron", "Vitamin C"],
                [calories, protein, carbs, fat, iron, vitamin_c],
                color=["#4CAF50", "#2196F3", "#FF9800", "#E91E63", "#9C27B0", "#00BCD4"]
            )

            st.pyplot(fig)

            st.subheader("🥧 Macro Distribution")

            fig2, ax2 = plt.subplots()

            ax2.pie(
                [protein, carbs, fat],
                labels=["Protein", "Carbs", "Fat"],
                autopct="%1.1f%%",
                colors=["#4CAF50", "#2196F3", "#FF9800"]
            )

            st.pyplot(fig2)

            st.markdown("</div>", unsafe_allow_html=True)

        # ---------------- PDF ----------------
        pdf_data = {
            "Food": food,
            "Calories": calories,
            "Protein": protein,
            "Carbs": carbs,
            "Fat": fat,
            "Iron": iron,
            "Vitamin C": vitamin_c,
            "Health Score": score,
            "Prediction": result
        }

        file = create_pdf(pdf_data)

        with open(file, "rb") as f:
            st.download_button("📥 Download Report", f, file_name="food_report.pdf")

    else:
        st.error("Food not found in dataset")
