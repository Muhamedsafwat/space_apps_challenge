#!/usr/bin/env python3
"""
Abu Simbel Guardian - Interactive Chatbot
Run this to chat with the temple!
"""

import sys
import os
from src.guardian import AbuSimbelGuardian

def print_header():
    """Print welcome header"""
    print("\n" + "="*70)
    print("🏺 ABU SIMBEL DIGITAL GUARDIAN 🏺")
    print("="*70)
    print("\nWelcome! I am Abu Simbel, speaking to you across 3,300 years.")
    print("I am monitored by NASA satellites and can share my story with you.\n")
    print("Commands:")
    print("  'quit' or 'exit' - End conversation")
    print("  'status' - Show my current health status")
    print("  'reset' - Clear conversation history")
    print("  'save' - Save conversation to file")
    print("="*70 + "\n")

def test_questions_demo(guardian):
    """Run through demo questions"""
    demo_questions = [
        "How are you feeling today?",
        "What's your biggest threat right now?",
        "Tell me about your relocation in 1968",
        "What do NASA's satellites show about your movement?",
        "Should I visit you this week?"
    ]
    
    print("\n🎬 DEMO MODE - Running sample questions...\n")
    
    for i, question in enumerate(demo_questions, 1):
        print(f"\n{'='*70}")
        print(f"Q{i}: {question}")
        print('='*70)
        
        response = guardian.chat(question)
        print(f"\n🏺 Abu Simbel:\n{response}\n")
        
        input("Press Enter for next question...")
    
    print("\n✅ Demo complete! Now you can ask your own questions.\n")

def interactive_mode(guardian):
    """Run interactive chat session"""
    print_header()
    
    # Show quick menu
    print("\n📚 SPECIAL COMMANDS:")
    print("  'history' - Show 3,300-year timeline")
    print("  'nisar' - Learn about NISAR satellite")
    print("  'status' - Current health report")
    print("  'demo' - Run sample questions")
    print("  'save' - Save conversation")
    print("  'reset' - Clear history")
    print("  'quit' - Exit\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Commands
            if user_input.lower() in ['quit', 'exit']:
                print("\n👋 May you stand for another 3,300 years!")
                break
            
            if user_input.lower() == 'history':
                print(guardian.get_historical_timeline())
                continue
            
            if user_input.lower() == 'nisar':
                print(guardian.get_nisar_info())
                continue
            
            if user_input.lower() == 'status':
                print(guardian.get_status_summary())
                continue
            
            if user_input.lower() == 'demo':
                run_demo(guardian)
                continue
            
            if user_input.lower() == 'reset':
                guardian.reset_conversation()
                continue
            
            if user_input.lower() == 'save':
                guardian.export_conversation()
                continue
            
            # Regular chat
            print("\n🏺 Abu Simbel: ", end="")
            response = guardian.chat(user_input)
            print(f"{response}\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Farewell!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


def run_demo(guardian):
    """Run demo questions"""
    demo_questions = [
        "Tell me about when you were moved in 1968",
        "What challenges have you faced over 3,300 years?",
        "How is NASA helping monitor you?",
        "Explain how NISAR will save you",
        "Can NISAR help protect other Egyptian monuments?"
    ]
    
    print("\n🎬 RUNNING DEMO QUESTIONS...\n")
    
    for i, question in enumerate(demo_questions, 1):
        print(f"\n{'='*70}")
        print(f"Q{i}: {question}")
        print('='*70)
        
        response = guardian.chat(question)
        print(f"\n🏺 {response}\n")
        
        input("Press Enter for next question...")

def main():
    """Main entry point"""
    try:
        print("\n🔧 Initializing Guardian...")
        guardian = AbuSimbelGuardian(use_retriever=True)
        
        interactive_mode(guardian)
        
    except FileNotFoundError as e:
        print(f"\n❌ Missing data files: {e}")
        print("\nPlease run the data preparation scripts first:")
        print("  1. python scripts/download_nasa_data.py")
        print("  2. python scripts/integrate_data.py\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()