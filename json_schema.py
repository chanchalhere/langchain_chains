from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import json
load_dotenv()
# Define your Pydantic model
json_schema={
  "key_themes": [
    "<theme_1>",
    "<theme_2>",
    "<theme_3>"
  ],
  "summary": "<short overall summary of the review in 2–3 sentences>",
  "sentiment": "<pos | neg | neutral>",
  "pros": [
    "<pro_1>",
    "<pro_2>",
    "<pro_3>"
  ],
  "cons": [
    "<con_1>",
    "<con_2>",
    "<con_3>"
  ],
  "target_audience": "<who this product is suitable for>",
  "not_recommended_for": "<who should avoid this product>",
  "overall_verdict": "<one-line blunt conclusion>"
}


# Initialize Gemini
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# Get structured output directly
structured_llm = llm.with_structured_output(json_schema)

# Use it
result = structured_llm.invoke("""
Vivo T2 Pro 5G is… fine. Not amazing, not trash. Its one of those phones that tries to look more premium than it actually is, and honestly, it kinda succeeds at that. The phone feels slim, light, and good in hand. If you give it to someone without telling the price, theyll probably think its more expensive than it is.

The display is one of its stronger points. AMOLED + 90Hz means scrolling feels smooth and the colors look nice. Watching Netflix, YouTube, reels—no complaints there. This is the kind of screen you notice every day, and Vivo did a good job here.

Performance-wise, its decent but dont hype it in your head. Daily stuff like WhatsApp, Instagram, Chrome, and even light gaming works smoothly. But if youre thinking of heavy gaming for long hours or max graphics, youll hit limits. Its not a power monster, its a “get the job done” phone.

Battery life is solid. One full day is easy unless youre glued to gaming or videos. Charging is okay—fast enough to not annoy you, but nothing crazy like those 80W phones.

Now the camera… this is where expectations need to be controlled. Daylight photos are good enough for social media, no drama. But low light? Yeah, it struggles. Photos get soft, details drop, and night shots wont impress anyone. If camera is your top priority, this phone isnt trying very hard there.

Software is typical Vivo. Some useful features, some unnecessary apps youll probably uninstall on day one. Updates are fine but dont expect Pixel-level care.

""")


print(result)




