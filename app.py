import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI Proctoring NLP Module",
    layout="wide"
)

# =====================================
# TITLE
# =====================================

st.title("🎤 AI Proctoring NLP Module")

st.write(
    "Transcript-based AI Assistance Detection System"
)

# =====================================
# RECORDING SECTION
# =====================================

col1, col2 = st.columns(2)

with col1:
    start_button = st.button("▶️ Start Recording")

with col2:
    stop_button = st.button("⏹️ Stop Recording")

# =====================================
# TRANSCRIPT SECTION
# =====================================

st.subheader("📝 Transcript")

transcript_placeholder = st.empty()

transcript_placeholder.text(
    "Transcript will appear here..."
)

# =====================================
# METRICS SECTION
# =====================================

st.subheader("📊 Metrics")

metric_col1, metric_col2, metric_col3 = st.columns(3)

with metric_col1:
    st.metric(
        label="Perplexity",
        value="--"
    )

with metric_col2:
    st.metric(
        label="Vocabulary Richness",
        value="--"
    )

with metric_col3:
    st.metric(
        label="Sentence Consistency",
        value="--"
    )

metric_col4, metric_col5 = st.columns(2)

with metric_col4:
    st.metric(
        label="Repetition Score",
        value="--"
    )

with metric_col5:
    st.metric(
        label="Formality Score",
        value="--"
    )

# =====================================
# FINAL SCORE SECTION
# =====================================

st.subheader("🚨 Final Score")

st.metric(
    label="AI Assistance Likelihood",
    value="--"
)

st.info(
    "Waiting for audio input..."
)