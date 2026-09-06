import re


# ============================================================
# PROMPT OPTIMIZER
# Adaptive Rule-Based Prompt Engineering System
# ============================================================


# ============================================================
# 1. INTENT DETECTION
# ============================================================

def detect_intent(prompt):

    text = prompt.lower().strip()

    # Recommendation
    recommendation_words = [
        "recommend",
        "recommendation",
        "suggest",
        "suggestion",
        "suggest me",
        "give me options",
        "which one should i",
        "what should i choose",
        "best",
        "top"
    ]

    if any(word in text for word in recommendation_words):
        return "recommendation"

    # Coding
    coding_words = [
        "code",
        "coding",
        "program",
        "programming",
        "python",
        "java",
        "javascript",
        "c++",
        "html",
        "css",
        "react",
        "function",
        "algorithm",
        "debug",
        "fix this code",
        "write a program"
    ]

    if any(word in text for word in coding_words):
        return "coding"

    # Explanation / Education
    education_words = [
        "explain",
        "define",
        "what is",
        "what are",
        "how does",
        "how do",
        "why does",
        "why is",
        "teach me",
        "learn",
        "study",
        "exam",
        "assignment",
        "notes"
    ]

    if any(word in text for word in education_words):
        return "education"

    # Creative writing
    creative_words = [
        "story",
        "moral story",
        "short story",
        "tale",
        "poem",
        "poetry",
        "fiction",
        "dialogue",
        "script",
        "creative",
        "write a story"
    ]

    if any(word in text for word in creative_words):
        return "creative"

    # Summarization
    summary_words = [
        "summarize",
        "summary",
        "summarise",
        "shorten",
        "brief summary",
        "key points",
        "main points"
    ]

    if any(word in text for word in summary_words):
        return "summarization"

    # Translation
    translation_words = [
        "translate",
        "translation",
        "convert into",
        "translate this"
    ]

    if any(word in text for word in translation_words):
        return "translation"

    # Comparison
    comparison_words = [
        "compare",
        "comparison",
        "difference between",
        "differences between",
        "versus",
        "vs",
        "better than"
    ]

    if any(word in text for word in comparison_words):
        return "comparison"

    # Email / Professional writing
    professional_words = [
        "email",
        "mail",
        "cover letter",
        "professional message",
        "official letter",
        "request letter",
        "application letter"
    ]

    if any(word in text for word in professional_words):
        return "professional_writing"

    # Planning
    planning_words = [
        "plan",
        "planning",
        "schedule",
        "roadmap",
        "study plan",
        "learning plan",
        "prepare for",
        "preparation"
    ]

    if any(word in text for word in planning_words):
        return "planning"

    # Research
    research_words = [
        "research",
        "research paper",
        "literature survey",
        "literature review",
        "research topic",
        "research ideas",
        "academic paper"
    ]

    if any(word in text for word in research_words):
        return "research"

    # General question
    if "?" in text:
        return "question"

    return "general"


# ============================================================
# 2. DOMAIN DETECTION
# ============================================================

def detect_domain(prompt):

    text = prompt.lower()

    # Books / Novels
    if any(word in text for word in [
        "book",
        "books",
        "novel",
        "novels",
        "author",
        "fiction",
        "reading",
        "read"
    ]):
        return "books"

    # Movies / Entertainment
    if any(word in text for word in [
        "movie",
        "movies",
        "film",
        "films",
        "cinema",
        "series",
        "web series",
        "netflix",
        "comedy",
        "horror",
        "thriller",
        "romance"
    ]):
        return "entertainment"

    # Programming
    if any(word in text for word in [
        "python",
        "java",
        "javascript",
        "programming",
        "program",
        "code",
        "coding",
        "html",
        "css",
        "react",
        "flutter",
        "dart",
        "sql",
        "database",
        "algorithm"
    ]):
        return "technology"

    # AI / ML
    if any(word in text for word in [
        "machine learning",
        "artificial intelligence",
        "ai",
        "deep learning",
        "neural network",
        "nlp",
        "computer vision",
        "generative ai"
    ]):
        return "artificial_intelligence"

    # Education
    if any(word in text for word in [
        "exam",
        "subject",
        "assignment",
        "college",
        "university",
        "student",
        "study",
        "learning",
        "notes"
    ]):
        return "education"

    # Career
    if any(word in text for word in [
        "resume",
        "cv",
        "job",
        "career",
        "interview",
        "linkedin",
        "placement",
        "salary"
    ]):
        return "career"

    # Travel
    if any(word in text for word in [
        "travel",
        "trip",
        "tour",
        "vacation",
        "holiday",
        "hotel",
        "flight",
        "destination",
        "itinerary"
    ]):
        return "travel"

    # Food
    if any(word in text for word in [
        "food",
        "recipe",
        "cook",
        "cooking",
        "restaurant",
        "dish",
        "meal"
    ]):
        return "food"

    # Health / fitness general content
    if any(word in text for word in [
        "exercise",
        "workout",
        "fitness",
        "diet",
        "nutrition"
    ]):
        return "fitness"

    return "general"


# ============================================================
# 3. EXTRACT USER DETAILS
# ============================================================

def extract_details(prompt):

    text = prompt.lower()

    details = []

    # Time
    time_words = [
        "today",
        "tomorrow",
        "this weekend",
        "this week",
        "next week",
        "this month",
        "tonight"
    ]

    for word in time_words:
        if word in text:
            details.append(f"Time preference: {word}")

    # Audience
    audience_words = [
        "beginner",
        "beginners",
        "student",
        "students",
        "children",
        "child",
        "professional",
        "developer",
        "developers",
        "teacher",
        "expert"
    ]

    for word in audience_words:
        if word in text:
            details.append(f"Audience: {word}")

    # Quantity
    number_match = re.search(
        r"\b(\d+)\b",
        text
    )

    if number_match:
        details.append(
            f"Requested quantity: {number_match.group(1)}"
        )

    return details


# ============================================================
# 4. COMPONENT DETECTION
# ============================================================

def detect_components(prompt):

    text = prompt.lower()

    return {
        "Role": any(word in text for word in [
            "act as",
            "you are",
            "as an expert",
            "as a teacher",
            "as a developer",
            "as a writer"
        ]),

        "Context": any(word in text for word in [
            "because",
            "for my",
            "for a",
            "for an",
            "this weekend",
            "today",
            "tomorrow",
            "in my project",
            "in my assignment"
        ]),

        "Task": any(word in text for word in [
            "explain",
            "write",
            "create",
            "generate",
            "recommend",
            "suggest",
            "compare",
            "summarize",
            "translate",
            "analyze",
            "design",
            "develop",
            "find",
            "list",
            "solve"
        ]),

        "Target Audience": any(word in text for word in [
            "beginner",
            "student",
            "students",
            "children",
            "professional",
            "developer",
            "teacher",
            "expert"
        ]),

        "Constraints": any(word in text for word in [
            "only",
            "avoid",
            "must",
            "should",
            "do not",
            "don't",
            "without",
            "under",
            "less than",
            "maximum",
            "minimum",
            "concise",
            "brief",
            "simple",
            "short",
            "spoiler-free",
            "no spoilers"
        ]),

        "Output Format": any(word in text for word in [
            "bullet",
            "bullets",
            "list",
            "table",
            "steps",
            "headings",
            "format",
            "paragraph",
            "numbered"
        ]),

        "Examples": any(word in text for word in [
            "example",
            "examples",
            "such as",
            "for instance"
        ])
    }


# ============================================================
# 5. QUALITY SCORE
# ============================================================

WEIGHTS = {
    "Role": 15,
    "Context": 15,
    "Task": 20,
    "Target Audience": 10,
    "Constraints": 15,
    "Output Format": 15,
    "Examples": 10
}


def calculate_score(components):

    score = 0

    for component, weight in WEIGHTS.items():

        if components.get(component, False):
            score += weight

    return min(score, 100)


# ============================================================
# 6. RECOMMENDATION OPTIMIZER
# ============================================================

def optimize_recommendation(prompt, domain, details):

    # BOOK / NOVEL
    if domain == "books":

        extra_context = ""

        if details:
            extra_context = "\nUser details:\n- " + \
                "\n- ".join(details)

        return f"""Act as a knowledgeable book recommendation expert.

Task:
{prompt}

Understand the user's request and recommend books or novels that closely match what the user is looking for.{extra_context}

For each recommendation, provide:
1. Title
2. Author
3. Genre
4. Short spoiler-free description
5. Why it may be interesting for the user

Requirements:
- Focus specifically on books or novels.
- Match the requested mood, genre, or purpose when provided.
- Do not recommend unrelated types of content.
- Keep the recommendations concise and useful.
- Do not reveal major plot spoilers.
- Preserve the user's original intention.

Output Format:
Use a numbered list with clear information for each recommendation."""

    # MOVIE
    if domain == "entertainment":

        return f"""Act as a knowledgeable movie and entertainment recommendation expert.

Task:
{prompt}

Recommend options that closely match the user's request.

For each recommendation, provide:
1. Movie or series title
2. Genre
3. Short spoiler-free description
4. Why it matches the request

Requirements:
- Stay focused on the requested entertainment type.
- Match the requested genre or mood.
- Avoid unrelated recommendations.
- Avoid spoilers.
- Keep the response concise.

Output Format:
Use a numbered list.

Preserve the original intention of the user's request."""

    # GENERAL RECOMMENDATION
    return f"""Act as a knowledgeable recommendation expert in the subject relevant to the request.

Task:
{prompt}

Understand what the user is asking for and provide several relevant options.

Requirements:
- Recommend only items relevant to the user's request.
- Consider any preferences, time limits, audience, or purpose mentioned.
- Briefly explain why each option is suitable.
- Avoid unrelated recommendations.
- Do not invent unnecessary requirements.
- Preserve the original intention.

Output Format:
Use a numbered list with a short explanation for each option."""


# ============================================================
# 7. CODING OPTIMIZER
# ============================================================

def optimize_coding(prompt):

    return f"""Act as an experienced software developer.

Task:
{prompt}

Provide a practical solution that directly addresses the programming task.

Requirements:
- Understand the requested programming language or technology.
- Explain the approach clearly.
- Provide clean and readable code when code is requested.
- Include useful comments.
- Mention important assumptions or edge cases.
- Avoid unrelated technologies or unnecessary complexity.
- Preserve the original requirements.

Output Format:
1. Approach
2. Code
3. Explanation
4. Example Input/Output
5. Important Notes"""


# ============================================================
# 8. EDUCATIONAL OPTIMIZER
# ============================================================

def optimize_education(prompt):

    return f"""Act as an experienced Computer Science educator.

Task:
{prompt}

Explain or answer the requested topic according to the user's question.

Requirements:
- Directly answer the requested question.
- Start with a clear definition or introduction when appropriate.
- Explain important concepts in simple language.
- Use examples where they improve understanding.
- Include important points relevant to learning or examinations when appropriate.
- Do not add unrelated topics.
- Adjust the depth of explanation to the question.

Output Format:
Use suitable headings, short paragraphs, bullet points, or examples as appropriate.

Preserve the original intention of the user's request."""


# ============================================================
# 9. CREATIVE WRITING OPTIMIZER
# ============================================================

def optimize_creative(prompt):

    if "moral" in prompt.lower():

        return f"""Act as a creative story writer.

Task:
{prompt}

Create an original and engaging moral story based on the user's request.

Requirements:
- Include a clear beginning, middle, and ending.
- Use simple and engaging language.
- Include suitable characters and a meaningful situation.
- Build the story around a clear positive moral.
- Keep the story interesting and easy to follow.
- Do not introduce unrelated themes.

Output Format:
1. Story Title
2. Story
3. Moral

Preserve the original intention of the user's request."""

    return f"""Act as a professional creative writer.

Task:
{prompt}

Create original and engaging content based specifically on the user's request.

Requirements:
- Preserve the requested theme and purpose.
- Use natural and engaging language.
- Be creative without changing the user's intention.
- Avoid unrelated information.

Output Format:
Use a suitable title and well-structured content."""


# ============================================================
# 10. SUMMARIZATION OPTIMIZER
# ============================================================

def optimize_summarization(prompt):

    return f"""Act as an expert summarization assistant.

Task:
{prompt}

Create a concise summary that preserves the most important information.

Requirements:
- Preserve the original meaning.
- Include the key ideas and important facts.
- Remove unnecessary repetition.
- Do not introduce information that is not present in the source.
- Keep the summary clear and easy to understand.

Output Format:
Provide a concise summary followed by key points when useful."""


# ============================================================
# 11. TRANSLATION OPTIMIZER
# ============================================================

def optimize_translation(prompt):

    return f"""Act as a professional translator.

Task:
{prompt}

Translate the requested content accurately while preserving its original meaning.

Requirements:
- Preserve the meaning and context.
- Maintain the appropriate tone.
- Do not add or remove important information.
- Keep names, technical terms, and important expressions accurate.

Output Format:
1. Translation
2. Important translation notes, only when necessary."""


# ============================================================
# 12. COMPARISON OPTIMIZER
# ============================================================

def optimize_comparison(prompt):

    return f"""Act as an expert comparison analyst.

Task:
{prompt}

Compare the requested subjects using relevant and meaningful criteria.

Requirements:
- Identify the main differences and similarities.
- Focus only on criteria relevant to the user's question.
- Explain the practical significance of the differences.
- Avoid unrelated information.
- Give a clear conclusion when appropriate.

Output Format:
Use a comparison table followed by a concise conclusion."""


# ============================================================
# 13. PROFESSIONAL WRITING OPTIMIZER
# ============================================================

def optimize_professional(prompt):

    return f"""Act as a professional communication specialist.

Task:
{prompt}

Create a professional response that directly serves the user's purpose.

Requirements:
- Use clear and polite language.
- Maintain an appropriate professional tone.
- Clearly communicate the user's main purpose.
- Avoid unnecessary information.
- Preserve important details from the original request.

Output Format:
Use a professional structure with clear paragraphs."""


# ============================================================
# 14. PLANNING OPTIMIZER
# ============================================================

def optimize_planning(prompt):

    return f"""Act as an experienced planning and productivity advisor.

Task:
{prompt}

Create a practical plan that directly addresses the user's goal.

Requirements:
- Break the goal into manageable steps.
- Prioritize important activities.
- Include realistic actions and time considerations when provided.
- Keep the plan practical and easy to follow.
- Do not introduce unrelated goals.

Output Format:
Use numbered steps or a structured schedule."""


# ============================================================
# 15. RESEARCH OPTIMIZER
# ============================================================

def optimize_research(prompt):

    return f"""Act as an academic research assistant.

Task:
{prompt}

Provide a structured response focused specifically on the requested research topic.

Requirements:
- Use clear academic language.
- Organize the information logically.
- Focus on relevant concepts and research directions.
- Clearly distinguish facts, suggestions, and assumptions.
- Avoid unrelated information.

Output Format:
Use clear academic headings and structured sections.

Preserve the original intention of the request."""


# ============================================================
# 16. QUESTION OPTIMIZER
# ============================================================

def optimize_question(prompt):

    return f"""Act as an expert in the subject relevant to the user's question.

Question:
{prompt}

Answer the question directly and accurately.

Requirements:
- First identify exactly what the user is asking.
- Give a direct answer before providing additional explanation.
- Explain important details only when they help answer the question.
- Use examples when useful.
- Avoid unrelated information.
- If the question is ambiguous, clearly state the assumption being made.

Output Format:
Use the most appropriate format for the question, such as a short explanation, bullet points, table, or example.

Preserve the original meaning of the question."""


# ============================================================
# 17. GENERAL OPTIMIZER
# ============================================================

def optimize_general(prompt):

    return f"""Act as an expert assistant in the subject relevant to the user's request.

Task:
{prompt}

Understand the user's specific request before responding.

Requirements:
- Directly address the requested task.
- Preserve all important details from the original prompt.
- Add context only when it improves the response.
- Do not introduce unrelated subjects.
- Do not assume unnecessary requirements.
- Use a response format suitable for the requested task.
- Preserve the original intention.

Provide a clear, specific, and useful response."""


# ============================================================
# 18. MAIN OPTIMIZER
# ============================================================

def optimize_prompt(prompt, mode="General"):

    original_prompt = prompt.strip()

    # Detect intent
    intent = detect_intent(
        original_prompt
    )

    # Detect domain
    domain = detect_domain(
        original_prompt
    )

    # Extract details
    details = extract_details(
        original_prompt
    )

    # Analyze original prompt
    original_analysis = detect_components(
        original_prompt
    )

    # Original quality
    original_score = calculate_score(
        original_analysis
    )

    # --------------------------------------------------------
    # Select optimization strategy
    # --------------------------------------------------------

    if intent == "recommendation":

        optimized_prompt = optimize_recommendation(
            original_prompt,
            domain,
            details
        )

    elif intent == "coding":

        optimized_prompt = optimize_coding(
            original_prompt
        )

    elif intent == "education":

        optimized_prompt = optimize_education(
            original_prompt
        )

    elif intent == "creative":

        optimized_prompt = optimize_creative(
            original_prompt
        )

    elif intent == "summarization":

        optimized_prompt = optimize_summarization(
            original_prompt
        )

    elif intent == "translation":

        optimized_prompt = optimize_translation(
            original_prompt
        )

    elif intent == "comparison":

        optimized_prompt = optimize_comparison(
            original_prompt
        )

    elif intent == "professional_writing":

        optimized_prompt = optimize_professional(
            original_prompt
        )

    elif intent == "planning":

        optimized_prompt = optimize_planning(
            original_prompt
        )

    elif intent == "research":

        optimized_prompt = optimize_research(
            original_prompt
        )

    elif intent == "question":

        optimized_prompt = optimize_question(
            original_prompt
        )

    else:

        optimized_prompt = optimize_general(
            original_prompt
        )

    # --------------------------------------------------------
    # Mode override
    # --------------------------------------------------------

    if mode == "Coding":

        optimized_prompt = optimize_coding(
            original_prompt
        )

    elif mode == "Research":

        optimized_prompt = optimize_research(
            original_prompt
        )

    elif mode == "Academic":

        optimized_prompt = optimize_education(
            original_prompt
        )

    elif mode == "Resume":

        optimized_prompt = optimize_professional(
            original_prompt
        )

    elif mode == "Business":

        optimized_prompt = optimize_professional(
            original_prompt
        )

    elif mode == "Creative Writing":

        optimized_prompt = optimize_creative(
            original_prompt
        )

    # --------------------------------------------------------
    # Analyze optimized prompt
    # --------------------------------------------------------

    optimized_analysis = detect_components(
        optimized_prompt
    )

    optimized_score = calculate_score(
        optimized_analysis
    )

    optimized_score = min(
        optimized_score,
        100
    )

    improvement = (
        optimized_score -
        original_score
    )

    # --------------------------------------------------------
    # Return result
    # --------------------------------------------------------

    return {

        "original_prompt":
            original_prompt,

        "optimized_prompt":
            optimized_prompt,

        "original_analysis":
            original_analysis,

        "optimized_analysis":
            optimized_analysis,

        "original_score":
            original_score,

        "optimized_score":
            optimized_score,

        "improvement":
            improvement,

        "intent":
            intent,

        "domain":
            domain,

        "details":
            details
    }