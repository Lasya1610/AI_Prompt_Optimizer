import streamlit as st
import textwrap

from optimizer import optimize_prompt


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="PromptIQ - Prompt Optimizer",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CSS
# IMPORTANT: CSS ONLY - NO PAGE CONTENT HTML
# ============================================================

css = """
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #070b16 0%,
        #0b1220 50%,
        #07151d 100%
    );
    color: #f8fafc;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ---------- SIDEBAR ---------- */

section[data-testid="stSidebar"] {
    background: #090e1a;
    border-right: 1px solid #1e293b;
}

section[data-testid="stSidebar"] * {
    color: #e2e8f0;
}


/* ---------- HEADINGS ---------- */

h1, h2, h3 {
    color: #f8fafc !important;
}

p {
    color: #cbd5e1;
}


/* ---------- TEXT AREA ---------- */

textarea {
    background-color: #111827 !important;
    color: #f8fafc !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
    font-size: 16px !important;
}

textarea:focus {
    border: 1px solid #818cf8 !important;
}


/* ---------- BUTTONS ---------- */

.stButton > button {
    width: 100%;
    min-height: 42px;
    border-radius: 10px;
    border: 1px solid #334155;
    background: #111827;
    color: #e2e8f0;
    font-weight: 600;
}

.stButton > button:hover {
    border-color: #818cf8;
    color: white;
}


/* ---------- METRICS ---------- */

div[data-testid="stMetric"] {
    background: #111827;
    border: 1px solid #1e293b;
    padding: 15px;
    border-radius: 12px;
}

div[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
}

div[data-testid="stMetricValue"] {
    color: #f8fafc !important;
}


/* ---------- CODE BOX ---------- */

.stCodeBlock {
    border-radius: 12px;
}


/* ---------- EXPANDER ---------- */

details {
    background: #0f172a !important;
    border: 1px solid #1e293b !important;
    border-radius: 12px !important;
}


/* ---------- DIVIDER ---------- */

hr {
    border-color: #1e293b;
}


/* ---------- INFO / WARNING ---------- */

div[data-testid="stAlert"] {
    border-radius: 10px;
}


/* ---------- SELECT BOX ---------- */

div[data-baseweb="select"] > div {
    background-color: #111827 !important;
    border-color: #334155 !important;
}

</style>
"""

st.markdown(
    textwrap.dedent(css),
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "prompt" not in st.session_state:
    st.session_state.prompt = ""

if "result" not in st.session_state:
    st.session_state.result = None


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("✨ PromptIQ")

    st.caption("Smart Prompt Engineering")

    st.divider()

    st.subheader("🎯 Optimization Mode")

    mode = st.selectbox(
        "Choose a mode",
        [
            "General",
            "Academic",
            "Coding",
            "Research",
            "Resume",
            "Business",
            "Creative Writing"
        ]
    )

    st.divider()

    st.subheader("🧠 How It Works")

    st.write("**1. Analyze**")
    st.caption("Understand the user's request.")

    st.write("**2. Detect**")
    st.caption("Identify intent and domain.")

    st.write("**3. Optimize**")
    st.caption("Add useful prompt components.")

    st.write("**4. Evaluate**")
    st.caption("Calculate prompt quality.")

    st.divider()

    st.info(
        "PromptIQ works locally using Python-based "
        "prompt engineering rules. No API key and "
        "no Ollama are required."
    )


# ============================================================
# HERO
# ============================================================

st.title("✨ PromptIQ")

st.header("Turn Simple Prompts Into Powerful Prompts.")

st.write(
    "PromptIQ analyzes your request, identifies missing "
    "prompt components, and transforms it into a clear, "
    "specific and well-structured prompt using Prompt "
    "Engineering principles."
)

st.divider()


# ============================================================
# FEATURES
# ============================================================

st.subheader("🚀 What PromptIQ Can Do")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### 🧠")
    st.markdown("**Smart Analysis**")
    st.caption(
        "Detect intent, domain and prompt components."
    )

with col2:
    st.markdown("### ⚡")
    st.markdown("**Instant Optimization**")
    st.caption(
        "Create structured prompts instantly."
    )

with col3:
    st.markdown("### 📊")
    st.markdown("**Quality Scoring**")
    st.caption(
        "Measure prompt quality before and after."
    )

with col4:
    st.markdown("### 🎯")
    st.markdown("**Multiple Modes**")
    st.caption(
        "Academic, Coding, Research and more."
    )


st.divider()


# ============================================================
# PROMPT INPUT
# ============================================================

st.subheader("🚀 Optimize Your Prompt")

st.write(
    "Enter any prompt below. PromptIQ automatically adapts "
    "the optimization according to the type of request."
)

prompt = st.text_area(
    "Your prompt",
    value=st.session_state.prompt,
    placeholder=(
        "Example: recommend me a novel that is "
        "interesting to read..."
    ),
    height=170,
    label_visibility="collapsed"
)


# ============================================================
# EXAMPLES
# ============================================================

st.markdown("**💡 Try an example:**")

example1, example2, example3, example4, example5 = st.columns(5)

with example1:

    if st.button(
        "Explain Machine Learning",
        use_container_width=True
    ):
        st.session_state.prompt = (
            "Explain machine learning"
        )
        st.rerun()


with example2:

    if st.button(
        "Recommend a Novel",
        use_container_width=True
    ):
        st.session_state.prompt = (
            "Recommend me a novel that is interesting to read"
        )
        st.rerun()


with example3:

    if st.button(
        "Write Python Code",
        use_container_width=True
    ):
        st.session_state.prompt = (
            "Write Python code to find prime numbers"
        )
        st.rerun()


with example4:

    if st.button(
        "Tell a Moral Story",
        use_container_width=True
    ):
        st.session_state.prompt = (
            "Tell me a moral story"
        )
        st.rerun()


with example5:

    if st.button(
        "Compare Python and Java",
        use_container_width=True
    ):
        st.session_state.prompt = (
            "Compare Python and Java"
        )
        st.rerun()


st.write("")


# ============================================================
# OPTIMIZE BUTTON
# ============================================================

_, button_column, _ = st.columns([1, 2, 1])

with button_column:

    optimize_clicked = st.button(
        "🚀 Optimize My Prompt",
        type="primary",
        use_container_width=True
    )


# ============================================================
# RUN OPTIMIZER
# ============================================================

if optimize_clicked:

    if not prompt.strip():

        st.warning(
            "⚠️ Please enter a prompt first."
        )

    else:

        try:

            with st.spinner(
                "Analyzing and optimizing your prompt..."
            ):

                result = optimize_prompt(
                    prompt.strip(),
                    mode
                )

                st.session_state.result = result

        except Exception as error:

            st.error(
                "❌ An error occurred while optimizing the prompt."
            )

            st.exception(error)


# ============================================================
# RESULTS
# ============================================================

result = st.session_state.result


if result is not None:

    st.divider()

    st.header("✨ Optimization Results")

    st.write(
        "Here is the analysis and improved version of your prompt."
    )


    # ========================================================
    # METRICS
    # ========================================================

    intent = result.get(
        "intent",
        "general"
    )

    domain = result.get(
        "domain",
        "general"
    )

    original_score = result.get(
        "original_score",
        0
    )

    optimized_score = result.get(
        "optimized_score",
        0
    )

    improvement = result.get(
        "improvement",
        0
    )


    metric1, metric2, metric3, metric4 = st.columns(4)

    with metric1:
        st.metric(
            "🎯 Intent",
            str(intent).title()
        )

    with metric2:
        st.metric(
            "🌐 Domain",
            str(domain).title()
        )

    with metric3:
        st.metric(
            "📉 Original Score",
            f"{original_score}/100"
        )

    with metric4:
        st.metric(
            "📈 Optimized Score",
            f"{optimized_score}/100",
            delta=f"+{improvement}"
        )


    st.write("")


    # ========================================================
    # BEFORE / AFTER
    # ========================================================

    before, after = st.columns(2)


    with before:

        st.subheader("📝 Original Prompt")

        st.caption(
            "Your prompt before optimization"
        )

        st.code(
            result.get(
                "original_prompt",
                prompt
            ),
            language="text"
        )


    with after:

        st.subheader("✨ Optimized Prompt")

        st.caption(
            "Your improved prompt"
        )

        st.code(
            result.get(
                "optimized_prompt",
                ""
            ),
            language="text"
        )


    # ========================================================
    # QUALITY
    # ========================================================

    st.divider()

    st.subheader("📊 Prompt Quality")

    st.write(
        "Comparison of prompt quality before and after optimization."
    )


    quality1, quality2 = st.columns(2)


    with quality1:

        st.markdown(
            f"**Original Prompt — {original_score}/100**"
        )

        st.progress(
            max(
                0,
                min(
                    int(original_score),
                    100
                )
            )
            / 100
        )


    with quality2:

        st.markdown(
            f"**Optimized Prompt — {optimized_score}/100**"
        )

        st.progress(
            max(
                0,
                min(
                    int(optimized_score),
                    100
                )
            )
            / 100
        )


    # ========================================================
    # DETECTED DETAILS
    # ========================================================

    details = result.get(
        "details",
        {}
    )

    if details:

        st.divider()

        st.subheader("🔍 Detected Details")

        if isinstance(details, dict):

            detail_columns = st.columns(3)

            detail_items = []

            for key, value in details.items():

                if value:

                    if isinstance(value, list):

                        value = ", ".join(
                            str(item)
                            for item in value
                        )

                    detail_items.append(
                        (
                            str(key).replace(
                                "_",
                                " "
                            ).title(),
                            str(value)
                        )
                    )

            if detail_items:

                for index, (key, value) in enumerate(
                    detail_items
                ):

                    with detail_columns[
                        index % 3
                    ]:

                        st.markdown(
                            f"**{key}**"
                        )

                        st.info(value)


    # ========================================================
    # COMPONENT ANALYSIS
    # ========================================================

    st.divider()

    st.subheader("🧩 Prompt Component Analysis")

    st.write(
        "PromptIQ checks seven important prompt engineering components."
    )


    original_analysis = result.get(
        "original_analysis",
        {}
    )

    optimized_analysis = result.get(
        "optimized_analysis",
        {}
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


    analysis1, analysis2 = st.columns(2)


    with analysis1:

        st.markdown("### 📝 Original")

        for component in components:

            present = original_analysis.get(
                component,
                False
            )

            if present:

                st.success(
                    f"✓ {component} — Present"
                )

            else:

                st.error(
                    f"✗ {component} — Missing"
                )


    with analysis2:

        st.markdown("### ✨ Optimized")

        for component in components:

            present = optimized_analysis.get(
                component,
                False
            )

            if present:

                st.success(
                    f"✓ {component} — Present"
                )

            else:

                st.error(
                    f"✗ {component} — Missing"
                )


    # ========================================================
    # WHAT CHANGED
    # ========================================================

    st.divider()

    st.subheader("🔄 What Changed?")

    changes = []

    for component in components:

        before_value = original_analysis.get(
            component,
            False
        )

        after_value = optimized_analysis.get(
            component,
            False
        )

        if not before_value and after_value:

            changes.append(component)


    if changes:

        for change in changes:

            st.info(
                f"➕ Added **{change}** to improve the prompt."
            )

    else:

        st.info(
            "The prompt was refined according to its detected "
            "intent and domain."
        )


    # ========================================================
    # SYSTEM UNDERSTANDING
    # ========================================================

    st.divider()

    st.subheader("🧠 System Understanding")

    understand1, understand2, understand3 = st.columns(3)


    with understand1:

        st.markdown("**Detected Intent**")

        st.info(
            str(intent).title()
        )


    with understand2:

        st.markdown("**Detected Domain**")

        st.info(
            str(domain).title()
        )


    with understand3:

        st.markdown("**Selected Mode**")

        st.info(
            mode
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "✨ PromptIQ • AI Prompt Optimizer"
)

st.caption(
    "Built using Python + Streamlit • "
    "Prompt Engineering Minor Project"
)