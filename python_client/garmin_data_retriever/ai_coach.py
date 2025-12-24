"""
AI Coach Module

This module provides AI-powered coaching functionality using a free AI API.
It analyzes Garmin data and provides personalized coaching recommendations.
"""

import json
import requests
from typing import Dict, List, Any, Optional


class AICoach:
    """
    AI-powered coach that analyzes Garmin data and provides recommendations.
    
    This implementation uses Ollama (local free AI) or can be configured
    to use other free AI APIs like:
    - Ollama (local)
    - HuggingFace Inference API (free tier)
    - Together AI (free tier)
    """
    
    def __init__(self, api_type: str = "ollama", api_url: str = "http://localhost:11434"):
        """
        Initialize the AI Coach.
        
        Args:
            api_type: Type of AI API to use ("ollama", "huggingface", "together")
            api_url: URL of the AI API endpoint
        """
        self.api_type = api_type
        self.api_url = api_url
    
    def analyze_activity(self, activity_data: Dict[str, Any]) -> str:
        """
        Analyze an activity and provide coaching feedback.
        
        Args:
            activity_data: Dictionary containing activity information
            
        Returns:
            Coaching feedback as a string
        """
        prompt = self._create_activity_prompt(activity_data)
        return self._get_ai_response(prompt)
    
    def analyze_health_metrics(self, health_data: Dict[str, Any]) -> str:
        """
        Analyze health metrics and provide recommendations.
        
        Args:
            health_data: Dictionary containing health metrics
            
        Returns:
            Health recommendations as a string
        """
        prompt = self._create_health_prompt(health_data)
        return self._get_ai_response(prompt)
    
    def create_training_plan(self, user_stats: Dict[str, Any], goal: str) -> str:
        """
        Create a personalized training plan based on user stats and goals.
        
        Args:
            user_stats: Dictionary containing user statistics
            goal: Training goal description
            
        Returns:
            Training plan as a string
        """
        prompt = self._create_training_plan_prompt(user_stats, goal)
        return self._get_ai_response(prompt)
    
    def _create_activity_prompt(self, activity_data: Dict[str, Any]) -> str:
        """Create a prompt for activity analysis."""
        return f"""As a personal fitness coach, analyze this workout activity and provide brief feedback:

Activity: {activity_data.get('activityName')}
Type: {activity_data.get('activityType')}
Distance: {activity_data.get('distance', 0) / 1000:.2f} km
Duration: {activity_data.get('duration', 0) / 60:.0f} minutes
Average Heart Rate: {activity_data.get('averageHR', 'N/A')} bpm
Max Heart Rate: {activity_data.get('maxHR', 'N/A')} bpm
Calories: {activity_data.get('calories', 'N/A')} kcal

Provide concise coaching feedback in 2-3 sentences focusing on:
1. Performance assessment
2. One specific recommendation for improvement
"""
    
    def _create_health_prompt(self, health_data: Dict[str, Any]) -> str:
        """Create a prompt for health metrics analysis."""
        hr_data = health_data.get('heart_rate', {})
        sleep_data = health_data.get('sleep', {})
        stress_data = health_data.get('stress', {})
        
        return f"""As a health coach, analyze these daily health metrics and provide brief recommendations:

Heart Rate:
- Resting: {hr_data.get('restingHeartRate', 'N/A')} bpm
- Average: {hr_data.get('averageHeartRate', 'N/A')} bpm

Sleep:
- Total: {sleep_data.get('totalSleepTime', 0) / 3600:.1f} hours
- Sleep Score: {sleep_data.get('sleepScore', 'N/A')}/100

Stress:
- Average Level: {stress_data.get('averageStressLevel', 'N/A')}
- Rest Time: {stress_data.get('restTime', 0)} minutes

Provide 2-3 actionable health recommendations based on this data.
"""
    
    def _create_training_plan_prompt(self, user_stats: Dict[str, Any], goal: str) -> str:
        """Create a prompt for training plan generation."""
        return f"""Create a brief weekly training plan for this athlete:

User Profile:
- Age: {user_stats.get('userAge')} years
- Fitness Age: {user_stats.get('fitnessAge')} years
- VO2 Max: {user_stats.get('vo2Max')}
- Total Activities: {user_stats.get('totalActivities')}

Goal: {goal}

Provide a concise 7-day training plan with daily recommendations.
"""
    
    def _get_ai_response(self, prompt: str) -> str:
        """
        Get response from AI API.
        
        Args:
            prompt: The prompt to send to the AI
            
        Returns:
            AI response as a string
        """
        if self.api_type == "ollama":
            return self._get_ollama_response(prompt)
        else:
            # Placeholder for other AI APIs
            return self._get_mock_response(prompt)
    
    def _get_ollama_response(self, prompt: str) -> str:
        """Get response from Ollama API."""
        try:
            response = requests.post(
                f"{self.api_url}/api/generate",
                json={
                    "model": "llama2",  # or "mistral", "codellama", etc.
                    "prompt": prompt,
                    "stream": False
                },
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json().get("response", "No response from AI")
            else:
                return self._get_mock_response(prompt)
        except Exception as e:
            print(f"Note: Ollama not available ({e}). Using mock response.")
            return self._get_mock_response(prompt)
    
    def _get_mock_response(self, prompt: str) -> str:
        """Generate a mock response when AI is not available."""
        if "activity" in prompt.lower() or "workout" in prompt.lower():
            return """Great workout! Your heart rate data suggests you maintained a good intensity level. 
For improvement, consider adding interval training to boost your cardiovascular fitness. 
Keep monitoring your recovery between sessions."""
        
        elif "health" in prompt.lower() or "sleep" in prompt.lower():
            return """Your health metrics look good overall. Consider these recommendations:
1. Aim for 7-9 hours of quality sleep to optimize recovery
2. Practice stress management techniques like meditation or deep breathing
3. Monitor your resting heart rate trends as an indicator of overall fitness"""
        
        elif "training plan" in prompt.lower():
            return """7-Day Training Plan:
Day 1: Easy run/walk 30 min (recovery pace)
Day 2: Strength training (upper body focus)
Day 3: Interval training 40 min
Day 4: Rest or light yoga
Day 5: Tempo run 45 min
Day 6: Strength training (lower body focus)
Day 7: Long slow distance 60 min

Remember to listen to your body and adjust intensity as needed."""
        
        else:
            return "Keep up the good work with your training! Stay consistent and focus on gradual improvement."
