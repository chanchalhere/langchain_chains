from langchain_core.prompts import PromptTemplate
template=PromptTemplate(
    input_variables=['paper_input','style_input','length_input'],
    template="""You are an expert AI researcher and technical writer with strong experience in Large Language Models (LLMs), NLP, and ML systems.

TASK:
Generate a **clear, technically accurate, and research-oriented overview** for a technical LLM research paper strictly following the instructions below.

PAPER CONTEXT (provided by user):
- Paper title:{paper_input}
- Length:{length_input}
- Style:{style_input}
- Research problem / motivation:
- Target audience (e.g., ML researchers, practitioners, beginners):
- Level of technical depth (introductory / intermediate / advanced):
- Domain or subfield (e.g., LLM architectures, fine-tuning, evaluation, safety, alignment, retrieval, efficiency):
- Assumed background knowledge of reader:
- Any constraints (length, style, terminology preferences):

CONTENT REQUIREMENTS:
1. Start with **precise problem framing** — explain *what problem exists and why it matters* in the current LLM landscape.
2. Briefly summarize **existing approaches or baselines**, clearly stating their limitations.
3. Explain the **core idea or contribution** of the paper in a high-level but technically correct manner.
4. Highlight **why this work is novel or significant** compared to prior research.
5. Clearly state the **scope and assumptions** of the work.
6. Mention **key components, techniques, or methodologies** involved (no equations unless necessary).
7. Conclude with **expected impact, applications, or implications** for research or industry.

STYLE & TONE:
- Use formal, academic, research-paper style.
- No marketing language, no hype.
- No unnecessary storytelling or analogies.
- Use precise technical terms; avoid vague phrases like “powerful” or “state-of-the-art” unless justified.
- Maintain logical flow and coherence.

QUALITY CONSTRAINTS:
- Be factually grounded and internally consistent.
- Do not invent datasets, benchmarks, or results unless explicitly provided.
- Avoid speculation unless explicitly marked as such.
- Ensure clarity over verbosity.

OUTPUT FORMAT:
- 2–4 well-structured paragraphs
- Clear technical language
- No bullet points unless explicitly requested

""",
validate_template=True)
template.save('template.json')