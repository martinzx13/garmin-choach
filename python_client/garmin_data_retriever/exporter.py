"""
Data Exporter

This module provides functionality to export Garmin data in various formats.
"""

import json
from typing import Dict, List, Any
from datetime import datetime


class DataExporter:
    """
    Export Garmin data to various formats.
    """
    
    @staticmethod
    def to_json(data: Any, filepath: str = None) -> str:
        """
        Export data to JSON format.
        
        Args:
            data: Data to export
            filepath: Optional file path to save JSON
            
        Returns:
            JSON string
        """
        json_str = json.dumps(data, indent=2, default=str)
        
        if filepath:
            with open(filepath, 'w') as f:
                f.write(json_str)
        
        return json_str
    
    @staticmethod
    def format_activity_summary(activities: List[Dict[str, Any]]) -> str:
        """
        Format activities into a human-readable summary.
        
        Args:
            activities: List of activity dictionaries
            
        Returns:
            Formatted summary string
        """
        if not activities:
            return "No activities found."
        
        summary = "Activity Summary\n"
        summary += "=" * 50 + "\n\n"
        
        for i, activity in enumerate(activities, 1):
            summary += f"Activity {i}: {activity.get('activityName', 'Unknown')}\n"
            summary += f"  Type: {activity.get('activityType', 'N/A')}\n"
            summary += f"  Date: {activity.get('startTime', 'N/A')}\n"
            summary += f"  Distance: {activity.get('distance', 0) / 1000:.2f} km\n"
            summary += f"  Duration: {activity.get('duration', 0) / 60:.0f} minutes\n"
            summary += f"  Avg HR: {activity.get('averageHR', 'N/A')} bpm\n"
            summary += f"  Calories: {activity.get('calories', 'N/A')} kcal\n"
            summary += "\n"
        
        return summary
    
    @staticmethod
    def format_health_summary(heart_rate: Dict, sleep: Dict, stress: Dict) -> str:
        """
        Format health data into a human-readable summary.
        
        Args:
            heart_rate: Heart rate data dictionary
            sleep: Sleep data dictionary
            stress: Stress data dictionary
            
        Returns:
            Formatted summary string
        """
        summary = "Health Summary\n"
        summary += "=" * 50 + "\n\n"
        
        summary += f"Heart Rate Data ({heart_rate.get('date', 'N/A')})\n"
        summary += f"  Resting HR: {heart_rate.get('restingHeartRate', 'N/A')} bpm\n"
        summary += f"  Average HR: {heart_rate.get('averageHeartRate', 'N/A')} bpm\n"
        summary += f"  Max HR: {heart_rate.get('maxHeartRate', 'N/A')} bpm\n\n"
        
        summary += f"Sleep Data ({sleep.get('date', 'N/A')})\n"
        summary += f"  Total Sleep: {sleep.get('totalSleepTime', 0) / 3600:.1f} hours\n"
        summary += f"  Deep Sleep: {sleep.get('deepSleep', 0) / 3600:.1f} hours\n"
        summary += f"  Light Sleep: {sleep.get('lightSleep', 0) / 3600:.1f} hours\n"
        summary += f"  REM Sleep: {sleep.get('remSleep', 0) / 3600:.1f} hours\n"
        summary += f"  Sleep Score: {sleep.get('sleepScore', 'N/A')}/100\n\n"
        
        summary += f"Stress Data ({stress.get('date', 'N/A')})\n"
        summary += f"  Average Stress: {stress.get('averageStressLevel', 'N/A')}\n"
        summary += f"  Max Stress: {stress.get('maxStressLevel', 'N/A')}\n"
        summary += f"  Rest Time: {stress.get('restTime', 0)} minutes\n"
        
        return summary
