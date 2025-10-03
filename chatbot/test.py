"""
Complete system test
"""

def test_data_files():
    """Test that all data files exist"""
    import os
    
    required_files = [
        'data/temple_knowledge.json',
        'data/nasa_analysis_results.json',
        'data/processed/sar_displacement.csv',
        'data/processed/temperature_data.csv',
        'data/processed/water_levels.csv'
    ]
    
    print("Testing data files...")
    for file in required_files:
        if os.path.exists(file):
            print(f"  ✅ {file}")
        else:
            print(f"  ❌ {file} - MISSING")

def test_imports():
    """Test that all imports work"""
    print("\nTesting imports...")
    try:
        from src.guardian import AbuSimbelGuardian
        print("  ✅ guardian")
        from src.data_loader import TempleDataLoader
        print("  ✅ data_loader")
        from src.retriever import SmartRetriever
        print("  ✅ retriever")
        import ollama
        print("  ✅ ollama")
    except Exception as e:
        print(f"  ❌ Import error: {e}")

def test_guardian_init():
    """Test guardian initialization"""
    print("\nTesting guardian initialization...")
    try:
        from src.guardian import AbuSimbelGuardian
        guardian = AbuSimbelGuardian(use_retriever=True)
        print("  ✅ Guardian initialized")
        
        # Test chat
        response = guardian.chat("Hello!")
        print(f"  ✅ Chat working: {response[:50]}...")
        
    except Exception as e:
        print(f"  ❌ Guardian error: {e}")

if __name__ == "__main__":
    test_data_files()
    test_imports()
    test_guardian_init()
    print("\n✅ All tests complete!")