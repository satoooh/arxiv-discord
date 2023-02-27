import os

from dotenv import load_dotenv
load_dotenv()

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")


arxiv_subject = "cat:cs.* OR cat:eess.* OR cat:econ.* OR cat:stat.*"

arxiv_keywords = [
    # 技術トピック
    "artificial intelligence",
    "AI",
    "deep learning",
    "machine learning",
    "reinforcement learning",
    "in-context learning",
    "self-supervised learning",
    "transformer",

    # スポーツ技術
    "sport",
    "pose estimation",
    "object detection",
    "action recognition",
    "gesture recognition",
    "activity recognition",
    "highlight detection",
    "temporal action localization",
    "body orientation",
    "performance analysis",
    "human movement",
    "human motion",
    "motion capture",
    "openpose",

    # football
    "football",
    "soccer",
    "penalty kick",
    "goalkeeper"
    "goalkeeping",

    # LLM
    "LLM",
    "prompt engineering",
    "prompting",

    # xR
    "mixed reality",
    "MR",
    "virtual reality",
    "VR",
    "augmented reality",
    "AR",

    # Human Augmentation
    "human augmentation",
    "HA",
    "Internet of Ability",
    "IoA",

    # HCI keywords
    "Fitts's law",
    "haptics",
    "HCI",
    "interaction",
    "device",
    "life log",
    "life logging",
    "personal informatics",
    "ubiquitous computing",
    "user interface",
    "UI",
    "wearable computing",
    "wearable device",
    "wearable devices",
    "wearable sensor",
    "wearable sensors",
]
