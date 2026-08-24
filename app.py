import streamlit as st

from optimizer import optimize_prompt


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Prompt Optimizer",
    page_icon="✨",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #888888;
        margin-bottom: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown(
    '<div class="main-title">✨ AI Prompt Optimizer</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Transform vague prompts into clear, structured and effective prompts
    using Prompt Engineering techniques.
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# OPTIMIZATION MODE
# --------------------------------------------------

st.subheader("🎯 Optimization Mode")

mode = st.selectbox(
    "Choose the type of prompt:",
    [
        "General",
        "Academic",
        "Coding",
        "Research",
        "Resume",
        "Creative Writing",
        "Business"
    ]
)


# --------------------------------------------------
# EXAMPLE PROMPTS
# --------------------------------------------------

st.subheader("🧪 Example Prompts")

examples = {
    "Education": "Explain machine learning",
    "Coding": "Create a Python calculator",
    "Resume": "Improve my resume summary",
    "Research": "Explain artificial intelligence research",
    "Business": "Write a professional email",
    "General": "Tell me about cloud computing"
}

example_name = st.selectbox(
    "Choose an example:",
    list(examples.keys())
)

if st.button("Use Example"):

    st.session_state.prompt = examples[example_name]


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

st.subheader("📝 Enter Your Prompt")

if "prompt" not in st.session_state:
    st.session_state.prompt = ""

user_prompt = st.text_area(
    "Original Prompt",
    value=st.session_state.prompt,
    height=150,
    placeholder="Example: Explain machine learning"
)


# --------------------------------------------------
# OPTIMIZE
# --------------------------------------------------

if st.button(
    "🚀 Optimize Prompt",
    type="primary"
):

    if not user_prompt.strip():

        st.warning(
            "Please enter a prompt before optimizing."
        )

    else:

        result = optimize_prompt(
            user_prompt,
            mode
        )

        st.success(
            "Prompt optimized successfully!"
        )

        # --------------------------------------------------
        # ORIGINAL PROMPT
        # --------------------------------------------------

        st.subheader("📌 Original Prompt")

        st.info(
            result["original_prompt"]
        )

        # --------------------------------------------------
        # OPTIMIZED PROMPT
        # --------------------------------------------------

        st.subheader("✨ Optimized Prompt")

        st.success(
            result["optimized_prompt"]
        )

        st.code(
            result["optimized_prompt"],
            language="text"
        )

        # --------------------------------------------------
        # QUALITY SCORE
        # --------------------------------------------------

        st.subheader("📊 Prompt Quality")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Original Score",
                f'{result["original_score"]}/100'
            )

        with col2:

            st.metric(
                "Optimized Score",
                f'{result["optimized_score"]}/100'
            )

        with col3:

            st.metric(
                "Improvement",
                f'+{result["improvement"]} points'
            )

        # --------------------------------------------------
        # COMPONENT ANALYSIS
        # --------------------------------------------------

        st.subheader(
            "🔍 Prompt Component Analysis"
        )

        components = [
            "Role",
            "Context",
            "Task",
            "Target Audience",
            "Constraints",
            "Output Format",
            "Examples"
        ]

        for component in components:

            original = result[
                "original_analysis"
            ][component]

            optimized = result[
                "optimized_analysis"
            ][component]

            original_status = (
                "✅ Present"
                if original
                else "❌ Missing"
            )

            optimized_status = (
                "✅ Present"
                if optimized
                else "❌ Missing"
            )

            st.write(
                f"**{component}**  |  "
                f"Original: {original_status}  |  "
                f"Optimized: {optimized_status}"
            )

        # --------------------------------------------------
        # IMPROVEMENT SUMMARY
        # --------------------------------------------------

        st.subheader(
            "💡 Improvement Summary"
        )

        missing = [
            component
            for component, present
            in result["original_analysis"].items()
            if not present
        ]

        if missing:

            st.write(
                "The optimizer added or strengthened the following "
                "components:"
            )

            for component in missing:

                st.write(
                    f"• {component}"
                )

        else:

            st.success(
                "The original prompt was already well structured."
            )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "AI Prompt Optimizer | Prompt Engineering Minor Project"
)