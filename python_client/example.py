#!/usr/bin/env python3
"""
Example script for using the Garmin Data Retriever.

This script demonstrates how to:
1. Authenticate with Garmin Connect
2. Retrieve activity data
3. Retrieve health metrics (heart rate, sleep, stress)
4. Export data to various formats
"""

import sys
import os
from datetime import datetime, timedelta

# Add the parent directory to the path so we can import our module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from garmin_data_retriever.client import GarminConnectClient
from garmin_data_retriever.exporter import DataExporter


def main():
    """Main function to demonstrate Garmin data retrieval."""
    
    print("=" * 60)
    print("Garmin Coach - Data Retrieval Example")
    print("=" * 60)
    print()
    
    # Initialize the client
    # In a real scenario, you would use actual credentials or environment variables
    print("Step 1: Initializing Garmin Connect Client...")
    client = GarminConnectClient(
        email=os.getenv("GARMIN_EMAIL"),
        password=os.getenv("GARMIN_PASSWORD")
    )
    print("✓ Client initialized")
    print()
    
    # Authenticate
    print("Step 2: Authenticating with Garmin Connect...")
    client.authenticate()
    print("✓ Authentication successful")
    print()
    
    # Retrieve activities
    print("Step 3: Retrieving recent activities...")
    activities = client.get_activities(limit=5)
    print(f"✓ Retrieved {len(activities)} activities")
    print()
    
    # Display activity summary
    activity_summary = DataExporter.format_activity_summary(activities)
    print(activity_summary)
    
    # Retrieve health metrics
    print("Step 4: Retrieving health metrics...")
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    
    heart_rate = client.get_heart_rate_data(today)
    sleep_data = client.get_sleep_data(yesterday)
    stress_data = client.get_stress_data(today)
    
    print("✓ Health metrics retrieved")
    print()
    
    # Display health summary
    health_summary = DataExporter.format_health_summary(
        heart_rate, sleep_data, stress_data
    )
    print(health_summary)
    
    # Retrieve user stats
    print("Step 5: Retrieving user statistics...")
    user_stats = client.get_user_stats()
    print("✓ User statistics retrieved")
    print()
    
    print("User Profile:")
    print(f"  Name: {user_stats.get('userName')}")
    print(f"  Age: {user_stats.get('userAge')} years")
    print(f"  Weight: {user_stats.get('userWeight')} kg")
    print(f"  Height: {user_stats.get('userHeight')} cm")
    print(f"  VO2 Max: {user_stats.get('vo2Max')}")
    print(f"  Fitness Age: {user_stats.get('fitnessAge')} years")
    print(f"  Total Activities: {user_stats.get('totalActivities')}")
    print()
    
    # Export data to JSON
    print("Step 6: Exporting data to JSON...")
    all_data = {
        "activities": activities,
        "health": {
            "heart_rate": heart_rate,
            "sleep": sleep_data,
            "stress": stress_data
        },
        "user_stats": user_stats,
        "export_timestamp": datetime.now().isoformat()
    }
    
    json_output = DataExporter.to_json(all_data, "garmin_data_export.json")
    print("✓ Data exported to garmin_data_export.json")
    print()
    
    print("=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
