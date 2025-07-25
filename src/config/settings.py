"""
Centralized configuration settings for the HTS Classification System.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Main configuration class containing all system settings."""
    
    # Base paths
    BASE_DIR = Path(__file__).parent.parent.parent
    DATA_DIR = BASE_DIR / "Data"
    LOGS_DIR = BASE_DIR / "logs"
    CACHE_DIR = BASE_DIR / "cache"

    
    # Azure OpenAI Configuration
    AZURE_OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY')
    AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')
    AZURE_OPENAI_EMBEDDING_MODEL = "text-embedding-3-small"
    AZURE_OPENAI_CHAT_MODEL = "gpt-4"
    AZURE_OPENAI_API_VERSION = "2024-12-01-preview"
    AZURE_FEEDBACK_BLOB_KEY = "feedback-data-canada.csv"
    AZURE_STORAGE_ACCOUNT_NAME="abscustoms"
    AZURE_CONTAINER_NAME="feedback-customs-canada"
    AZURE_STORAGE_CONNECTION_STRING = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    
    # Pinecone Configuration
    PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
    PINECONE_INDEX_NAME = "hts-codes"
    PINECONE_FEEDBACK_INDEX_NAME = "hts-feedback"  # New feedback index
    PINECONE_CLOUD = "aws"
    PINECONE_REGION = "us-east-1"
    
    # Classification Settings
    SEMANTIC_THRESHOLD = 0.50
    HIGH_CONFIDENCE_THRESHOLD = 0.70
    VERY_HIGH_CONFIDENCE_THRESHOLD = 0.80
    BASE_CONFIDENCE_THRESHOLD = 20
    CATEGORY_42_THRESHOLD = 10
    APPAREL_THRESHOLD = 15
    ALUMINUM_THRESHOLD = 15
    
    # Feedback Settings
    FEEDBACK_CACHE_DURATION = 5  # minutes
    DEFAULT_FEEDBACK_DAYS = 30
    
    # Pinecone Feedback Configuration
    PINECONE_FEEDBACK_SIMILARITY_THRESHOLD = 0.5
    PINECONE_FEEDBACK_TOP_K_DEFAULT = 5
    
    # System Settings
    BATCH_SIZE = 100
    MAX_RETRIES = 3
    BASE_DELAY = 1  # seconds
    LOG_ROTATION = "500 MB"

    # Log file names - centralized configuration
    MAIN_LOG_FILE = "HTS_Classifier.log"
    TEST_LOG_FILE = "test_classifier.log"
    STREAMLIT_LOG_FILE = "HTS_Classifier.log"
    
    # Log retention settings
    LOG_RETENTION_DAYS = "30 days"
    LOG_COMPRESSION = "zip"
    
    # Dashboard Settings
    DASHBOARD_RECENT_ENTRIES_COUNT = 10
    DASHBOARD_TOP_CORRECTIONS_COUNT = 5
    PERFORMANCE_CACHE_DURATION = 300  # 5 minutes in seconds

class HTSMappings:
    """HTS-specific mappings and constants."""
    
    # Material replacements for text preprocessing
    MATERIAL_REPLACEMENTS = {
        r'stainless\s+steel': 'ss',
        r'carbon\s+steel': 'cs',
        r'aluminum': 'al',
        r'aluminium': 'al',
        r'polyethylene': 'pe',
        r'polypropylene': 'pp',
        r'polyvinyl\s+chloride': 'pvc',
        r'poly\s*vinyl\s*chloride': 'pvc'
    }

    # Material Group chapter mappings
    MATERIAL_GROUP_CHAPTERS = {
    }

    # Product category mappings
    PRODUCT_MAPPINGS = {
        # Resale Products
        ('reactor', None): ['8504.50.80.00'],
        ('coil inductor', None): ['8504.50.80.00'],
        ('transformer', None): ['8504.21.00'],
        ('bushings', None): ['8535.90.80'],
        
        # Aluminum building components (Chapter 76)
        ('window', 'aluminum'): ['7610.10'],  # Windows and frames
        ('door', 'aluminum'): ['7610.10'],    # Doors and frames
        ('frame', 'aluminum'): ['7610.10'],   # Frames

        # =================== FOR TESTING =========================
        # Leather goods (Chapter 42)
        ('wallet', 'leather'): ['4202.31', '4202.32'],  # Wallets and similar items
        ('handbag', 'leather'): ['4202.21', '4202.22'],  # Handbags
        ('briefcase', 'leather'): ['4202.11', '4202.12'],  # Briefcases
        ('suitcase', 'leather'): ['4202.11', '4202.12'],  # Suitcases
        
        # Apparel (Chapter 61)
        ('t-shirt', 'cotton'): ['6109.10'],   # Cotton t-shirts
        ('t-shirt', 'knit'): ['6109.90'],     # Other t-shirts
        ('sweater', 'cotton'): ['6110.20'],   # Cotton sweaters
        ('sweater', 'wool'): ['6110.11'],     # Wool sweaters
        
        # Electronics (Chapter 85)
        ('solar panel', ''): ['8541.43'],     # Solar panels
        ('coffee maker', ''): ['8516.71'],    # Coffee makers
        ('robot', 'industrial'): ['8428.70']  # Industrial robots
        # ==========================================================
        }
    # Chapter contexts for classification
    CHAPTER_CONTEXTS = {
        "01": "Live animals",
        "02": "Meat and edible meat offal",
        "03": "Fish and crustaceans",
        "04": "Dairy, eggs, honey, and other edible animal products",
        "41": "Raw hides, skins and leather",
        "42": "Articles of leather; handbags, wallets, cases, similar containers",
        "43": "Furskins and artificial fur",
        "61": "Articles of apparel and clothing accessories, knitted or crocheted",
        "62": "Articles of apparel and clothing accessories, not knitted or crocheted",
        "63": "Other made up textile articles",
        "71": "Natural or cultured pearls, precious stones, precious metals",
        "72": "Iron and steel",
        "73": "Articles of iron or steel",
        "74": "Copper and articles thereof",
        "76": "Aluminum and articles thereof",
        "84": "Machinery and mechanical appliances",
        "85": "Electrical machinery and equipment"
    }
    
    # Subchapter contexts
    SUBCHAPTER_CONTEXTS = {
        "4202": "Trunks, suitcases, handbags, wallets, similar containers",
        "4203": "Articles of apparel and accessories of leather",
        "4205": "Other articles of leather or composition leather",
        "6109": "T-shirts, singlets, tank tops, knitted or crocheted",
        "6110": "Sweaters, pullovers, sweatshirts, knitted or crocheted",
        "6205": "Men's or boys' shirts, not knitted or crocheted",
        "7318": "Screws, bolts, nuts, washers of iron or steel",
        "7324": "Sanitary ware and parts of iron or steel",
        "7610": "Aluminum structures and parts (doors, windows, frames)",
        "8516": "Electric heating equipment and appliances",
        "8541": "Semiconductor devices, LEDs, solar cells",
        "8428": "Lifting, handling, loading machinery; industrial robots"
    }


# Remove these commented sections (lines 216-258):

# # Add electrical equipment contexts
#     ELECTRICAL_EQUIPMENT_CONTEXTS = {
#         "transformer": "Electrical power equipment for voltage conversion",
#         "bushing": "Electrical insulating component for high voltage equipment",
#         "insulator": "Electrical insulation component preventing current flow",
#         "core": "Magnetic core for electrical transformers",
#         "winding": "Electrical coil assembly for transformers",
#         "ct": "Current transformer for electrical measurement",
#         "terminal": "Electrical connection component",
#     }
    
#     MATERIAL_CONTEXTS = {
#         "porcelain": "Ceramic material for electrical insulation",
#         "aluminum": "Lightweight metal for electrical housings",
#         "kraft paper": "Insulating paper for electrical equipment",
#         "crepe paper": "Flexible insulating material",
#         "rubber": "Sealing and insulating material",
#     }


# Before Mappings:
# Input: "al ct bushing"
# AI sees: "al ct bushing" (confusing abbreviations)

# After Mappings:
# Input: "al ct bushing" 
# → Material replacement: "aluminum current transformer electrical bushing"
# AI sees: Clear, descriptive terms that match HTS vocabulary

# Mapping flow
# Input: "cem porc 123kV insulator" -> Frontend
# ↓
# Material Replacement: "camantic porcelain 123kV insulator" -> Backend
# ↓
# Product Mapping: ('insulator', 'porcelain') → ['8546.20'] -> Backend
# ↓
# RAG Search(classification flow): Within Chapter 8546.20.XX.XX subset to find complete 10-digit code -> Backend
# ↓
# Final Result: 8546.20.00.40 (complete 10-digit HTS code) -> Frontend