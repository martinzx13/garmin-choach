#!/usr/bin/env python3
"""
AI Coaching Example

This script demonstrates how to use the AI Coach to analyze Garmin data
and provide personalized recommendations.
"""

import sys
import os
from datetime import datetime, timedelta

# Add the parent directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from garmin_data_retriever.client import GarminConnectClient
from garmin_data_retriever.ai_coach import AICoach


def main():
    """Main function to demonstrate AI coaching."""
    
    print("=" * 60)
    print("Garmin Coach - AI Coaching Example")
    print("=" * 60)
    print()
    
    # Initialize clients
    print("Initializing Garmin Connect Client...")
    garmin_client = GarminConnectClient()
    garmin_client.authenticate()
    print("✓ Connected to Garmin")
    print()
    
    print("Initializing AI Coach...")
    # Try Ollama first, will fall back to mock responses if not available
    ai_coach = AICoach(api_type="ollama", api_url="http://localhost:11434")
    print("✓ AI Coach ready")
    print("  (Note: Using Ollama if available, otherwise mock responses)")
    print()
    
    # Get recent activity
    print("Step 1: Analyzing Recent Activity")
    print("-" * 60)
    activities = garmin_client.get_activities(limit=1)
    if activities:
        activity = activities[0]
        print(f"Activity: {activity['activityName']}")
        print(f"Type: {activity['activityType']}")
        print(f"Distance: {activity['distance'] / 1000:.2f} km")
        print(f"Duration: {activity['duration'] / 60:.0f} minutes")
        print()
        
        print("AI Coach Feedback:")
        feedback = ai_coach.analyze_activity(activity)
        print(feedback)
        print()
    
    # Analyze health metrics
    print("Step 2: Analyzing Health Metrics")
    print("-" * 60)
    health_data = {
        "heart_rate": garmin_client.get_heart_rate_data(),
        "sleep": garmin_client.get_sleep_data(),
        "stress": garmin_client.get_stress_data()
    }
    
    print("AI Coach Health Recommendations:")
    health_recommendations = ai_coach.analyze_health_metrics(health_data)
    print(health_recommendations)
    print()
    
    # Create training plan
    print("Step 3: Creating Personalized Training Plan")
    print("-" * 60)
    user_stats = garmin_client.get_user_stats()
    goal = "Improve 5K running time and build endurance"
    
    print(f"Goal: {goal}")
    print()
    print("AI Coach Training Plan:")
    training_plan = ai_coach.create_training_plan(user_stats, goal)
    print(training_plan)
    print()
    
    print("=" * 60)
    print("AI Coaching Example Completed!")
    print("=" * 60)
    print()
    print("Next Steps:")
    print("1. Install Ollama locally for real AI responses:")
    print("   https://ollama.ai")
    print("2. Set up actual Garmin Connect credentials")
    print("3. Customize the AI prompts for your specific needs")
    print()


if __name__ == "__main__":
    main()
