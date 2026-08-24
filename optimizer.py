import re


PROMPT_COMPONENTS = [
    "Role",
    "Context",
    "Task",
    "Target Audience",
    "Constraints",
    "Output Format",
    "Examples"
]


def analyze_prompt(prompt):
    """
    Analyze the prompt for important Prompt Engineering components.
    """

    text = prompt.lower()

    analysis = {}

    # Role detection
    role_words = [
        "act as",
        "you are",
        "role",
        "expert",
        "professor",
        "developer",
        "teacher",
        "analyst"
    ]

    analysis["Role"] = any(word in text for word in role_words)

    # Context detection
    context_words = [
        "context",
        "background",
        "scenario",
        "for my project",
        "for my assignment",
        "for a student",
        "for a company"
    ]

    analysis["Context"] = any(word in text for word in context_words)

    # Task detection
    task_words = [
        "explain",
        "create",
        "write",
        "generate",
        "analyze",
        "compare",
        "summarize",
        "design",
        "develop",
        "list"
    ]

    analysis["Task"] = any(
        word in text for word in task_words
    )

    # Target audience detection
    audience_words = [
        "student",
        "beginner",
        "expert",
        "developer",
        "teacher",
        "researcher",
        "professional",
        "audience"
    ]

    analysis["Target Audience"] = any(
        word in text for word in audience_words
    )

    # Constraints detection
    constraint_words = [
        "under",
        "within",
        "limit",
        "simple language",
        "avoid",
        "must",
        "should",
        "exactly",
        "maximum",
        "minimum"
    ]

    analysis["Constraints"] = any(
        word in text for word in constraint_words
    )

    # Output format detection
    format_words = [
        "bullet points",
        "numbered list",
        "table",
        "paragraph",
        "headings",
        "json",
        "format",
        "steps"
    ]

    analysis["Output Format"] = any(
        word in text for word in format_words
    )

    # Examples detection
    example_words = [
        "example",
        "examples",
        "sample",
        "illustration"
    ]

    analysis["Examples"] = any(
        word in text for word in example_words
    )

    return analysis


def calculate_score(analysis):
    """
    Calculate prompt quality score.
    """

    weights = {
        "Role": 15,
        "Context": 15,
        "Task": 20,
        "Target Audience": 10,
        "Constraints": 15,
        "Output Format": 15,
        "Examples": 10
    }

    score = 0

    for component, present in analysis.items():

        if present:
            score += weights[component]

    return score


def optimize_prompt(prompt, mode="General"):

    analysis = analyze_prompt(prompt)

    # Task extraction
    task = prompt.strip()

    if not task:
        return None

    # Mode-specific settings
    if mode == "Academic":

        role = "Act as an experienced Computer Science professor."

        audience = (
            "Explain the topic to an undergraduate CSE student "
            "preparing for examinations."
        )

        constraints = (
            "Use simple academic language, include important concepts, "
            "and focus on examination-relevant information."
        )

        output_format = (
            "Use clear headings, bullet points, and concise explanations."
        )

    elif mode == "Coding":

        role = "Act as a senior software developer."

        audience = (
            "Provide the solution for a beginner-to-intermediate "
            "programming student."
        )

        constraints = (
            "Write clean, readable, and well-commented code. "
            "Mention important edge cases."
        )

        output_format = (
            "Provide the solution, code, explanation, and example output."
        )

    elif mode == "Research":

        role = "Act as an academic research assistant."

        audience = (
            "Prepare the response for a student or researcher."
        )

        constraints = (
            "Use precise terminology, clearly distinguish facts from "
            "assumptions, and organize the information logically."
        )

        output_format = (
            "Use structured headings and concise research-oriented points."
        )

    elif mode == "Resume":

        role = "Act as a professional technical recruiter."

        audience = (
            "Optimize the content for a job applicant."
        )

        constraints = (
            "Use professional language, action-oriented wording, "
            "and avoid unnecessary information."
        )

        output_format = (
            "Provide concise, professional, resume-ready content."
        )

    elif mode == "Creative Writing":

        role = "Act as a professional creative writer."

        audience = (
            "Write for a general audience."
        )

        constraints = (
            "Make the content engaging, original, and easy to understand."
        )

        output_format = (
            "Use natural paragraphs and an engaging writing style."
        )

    elif mode == "Business":

        role = "Act as a business communication specialist."

        audience = (
            "Prepare the response for a professional business audience."
        )

        constraints = (
            "Use clear, concise, and professional business language."
        )

        output_format = (
            "Use structured sections and actionable points."
        )

    else:

        role = "Act as an expert in the relevant subject."

        audience = (
            "Provide the response in a clear and beginner-friendly manner."
        )

        constraints = (
            "Avoid unnecessary complexity and focus on useful information."
        )

        output_format = (
            "Use clear headings and concise bullet points where appropriate."
        )

    optimized_prompt = f"""
{role}

Task:
{task}

{audience}

{constraints}

{output_format}

Preserve the original intention of the request while providing a clear,
specific, and well-structured response.
""".strip()

    optimized_analysis = analyze_prompt(optimized_prompt)

    original_score = calculate_score(analysis)
    optimized_score = calculate_score(optimized_analysis)

    return {
        "original_prompt": prompt,
        "optimized_prompt": optimized_prompt,
        "original_analysis": analysis,
        "optimized_analysis": optimized_analysis,
        "original_score": original_score,
        "optimized_score": optimized_score,
        "improvement": optimized_score - original_score
    }