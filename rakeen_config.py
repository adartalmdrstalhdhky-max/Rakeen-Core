# Rakeen Global Configuration Bridge
PROJECT_NAME = "Rakeen Education"
CORE_VERSION = "1.0.0"
ORIGIN = "Yemen"
TARGET_EXPANSION = "Global"

# ربط المحركات المضافة
COMPONENTS = {
    "AI_TEACHER": "rakeen_data/ai_engine/teacher_protocol.txt",
    "YEMEN_CURRICULUM": "rakeen_data/yemen_curriculum/manifest.json",
    "PARENT_TRACKER": "rakeen_data/student_tracker.json"
}

def load_rakeen_mode():
    print("Rakeen Mode Activated: Offline-First AI Teacher Ready.")
  
