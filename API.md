# API Documentation

## Python Client API

### GarminConnectClient

The main client for interacting with Garmin Connect.

#### Initialization

```python
from garmin_data_retriever.client import GarminConnectClient

client = GarminConnectClient(
    email="your-email@example.com",
    password="your-password"
)
```

#### Methods

##### authenticate()

Authenticate with Garmin Connect.

```python
success = client.authenticate()
```

**Returns:** `bool` - True if authentication successful

---

##### get_activities(start_date=None, end_date=None, limit=10)

Retrieve activities from Garmin Connect.

```python
activities = client.get_activities(limit=5)
```

**Parameters:**
- `start_date` (datetime, optional): Start date for activity retrieval
- `end_date` (datetime, optional): End date for activity retrieval
- `limit` (int): Maximum number of activities to retrieve (default: 10)

**Returns:** `List[Dict]` - List of activity dictionaries

**Activity Structure:**
```python
{
    "activityId": 1,
    "activityName": "Morning Run",
    "activityType": "running",
    "startTime": "2024-01-01T07:00:00",
    "distance": 5000,      # meters
    "duration": 1800,      # seconds
    "averageHR": 145,      # bpm
    "maxHR": 165,          # bpm
    "calories": 350        # kcal
}
```

---

##### get_heart_rate_data(date=None)

Retrieve heart rate data for a specific date.

```python
hr_data = client.get_heart_rate_data()
```

**Parameters:**
- `date` (datetime, optional): Date to retrieve data for (defaults to today)

**Returns:** `Dict` - Heart rate data

**Structure:**
```python
{
    "date": "2024-01-01",
    "restingHeartRate": 55,
    "maxHeartRate": 165,
    "averageHeartRate": 70,
    "heartRateZones": {
        "zone1": 120,  # minutes
        "zone2": 45,
        "zone3": 15,
        "zone4": 5,
        "zone5": 1
    }
}
```

---

##### get_sleep_data(date=None)

Retrieve sleep data for a specific date.

```python
sleep_data = client.get_sleep_data()
```

**Parameters:**
- `date` (datetime, optional): Date to retrieve data for (defaults to yesterday)

**Returns:** `Dict` - Sleep data

---

##### get_stress_data(date=None)

Retrieve stress level data for a specific date.

```python
stress_data = client.get_stress_data()
```

**Parameters:**
- `date` (datetime, optional): Date to retrieve data for (defaults to today)

**Returns:** `Dict` - Stress data

---

##### get_user_stats()

Retrieve user statistics and profile information.

```python
user_stats = client.get_user_stats()
```

**Returns:** `Dict` - User statistics

---

### DataExporter

Export Garmin data to various formats.

#### Static Methods

##### to_json(data, filepath=None)

Export data to JSON format.

```python
from garmin_data_retriever.exporter import DataExporter

json_str = DataExporter.to_json(activities, "activities.json")
```

**Parameters:**
- `data` (Any): Data to export
- `filepath` (str, optional): File path to save JSON

**Returns:** `str` - JSON string

---

##### format_activity_summary(activities)

Format activities into a human-readable summary.

```python
summary = DataExporter.format_activity_summary(activities)
print(summary)
```

**Parameters:**
- `activities` (List[Dict]): List of activity dictionaries

**Returns:** `str` - Formatted summary

---

##### format_health_summary(heart_rate, sleep, stress)

Format health data into a human-readable summary.

```python
summary = DataExporter.format_health_summary(hr_data, sleep_data, stress_data)
print(summary)
```

**Parameters:**
- `heart_rate` (Dict): Heart rate data
- `sleep` (Dict): Sleep data
- `stress` (Dict): Stress data

**Returns:** `str` - Formatted summary

---

### AICoach

AI-powered coaching functionality.

#### Initialization

```python
from garmin_data_retriever.ai_coach import AICoach

# Using Ollama (default)
coach = AICoach(api_type="ollama", api_url="http://localhost:11434")

# Using mock responses
coach = AICoach(api_type="mock")
```

**Parameters:**
- `api_type` (str): Type of AI API ("ollama", "huggingface", "together", "mock")
- `api_url` (str): URL of the AI API endpoint

#### Methods

##### analyze_activity(activity_data)

Analyze an activity and provide coaching feedback.

```python
activity = client.get_activities(limit=1)[0]
feedback = coach.analyze_activity(activity)
print(feedback)
```

**Parameters:**
- `activity_data` (Dict): Activity dictionary

**Returns:** `str` - Coaching feedback

---

##### analyze_health_metrics(health_data)

Analyze health metrics and provide recommendations.

```python
health_data = {
    "heart_rate": client.get_heart_rate_data(),
    "sleep": client.get_sleep_data(),
    "stress": client.get_stress_data()
}
recommendations = coach.analyze_health_metrics(health_data)
print(recommendations)
```

**Parameters:**
- `health_data` (Dict): Dictionary with "heart_rate", "sleep", and "stress" keys

**Returns:** `str` - Health recommendations

---

##### create_training_plan(user_stats, goal)

Create a personalized training plan.

```python
user_stats = client.get_user_stats()
plan = coach.create_training_plan(user_stats, "Improve 5K time")
print(plan)
```

**Parameters:**
- `user_stats` (Dict): User statistics dictionary
- `goal` (str): Training goal description

**Returns:** `str` - Training plan

---

## Rust CLI API

### Commands

#### example

Run example scripts.

```bash
garmin_coach example --example-type <TYPE>
```

**Options:**
- `--example-type, -e`: Type of example to run
  - `data`: Data retrieval example
  - `ai`: AI coaching example

**Examples:**
```bash
cargo run -- example --example-type data
cargo run -- example --example-type ai
```

---

#### fetch-data

Retrieve data from Garmin Connect.

```bash
garmin_coach fetch-data --data-type <TYPE>
```

**Options:**
- `--data-type, -d`: Type of data to fetch
  - `activities`: Activity data
  - `health`: Health metrics
  - `stats`: User statistics

**Examples:**
```bash
cargo run -- fetch-data --data-type activities
```

---

#### coaching

Get AI coaching feedback.

```bash
garmin_coach coaching --coaching-type <TYPE>
```

**Options:**
- `--coaching-type, -c`: Type of coaching
  - `activity`: Activity analysis
  - `health`: Health recommendations
  - `plan`: Training plan

**Examples:**
```bash
cargo run -- coaching --coaching-type activity
```

---

## Example Usage

### Complete Workflow

```python
#!/usr/bin/env python3
from garmin_data_retriever.client import GarminConnectClient
from garmin_data_retriever.exporter import DataExporter
from garmin_data_retriever.ai_coach import AICoach

# Initialize
client = GarminConnectClient()
client.authenticate()
coach = AICoach()

# Get data
activities = client.get_activities(limit=1)
health_data = {
    "heart_rate": client.get_heart_rate_data(),
    "sleep": client.get_sleep_data(),
    "stress": client.get_stress_data()
}

# Get AI feedback
if activities:
    activity_feedback = coach.analyze_activity(activities[0])
    print(activity_feedback)

health_feedback = coach.analyze_health_metrics(health_data)
print(health_feedback)

# Export data
DataExporter.to_json(activities, "my_activities.json")
```

### Using with Rust

```bash
# Quick start
cargo run -- example --example-type data

# Get coaching
cargo run -- example --example-type ai

# Help
cargo run -- --help
```
