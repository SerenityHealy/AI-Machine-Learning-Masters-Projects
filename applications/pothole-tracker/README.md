# Pothole Tracking and Repair System

A use-case demonstration system for municipal pothole reporting, tracking, and repair management.

## Overview

This application demonstrates a pothole management system with three actor types (Citizen, System, Repair Crew) and their respective use cases. It serves as an educational tool for understanding system design and use-case modeling.

## Features

- **Multi-Actor System**: Citizens, System, and Repair Crew
- **Use Case Documentation**: Detailed descriptions for each actor
- **Interactive Menu**: Browse use cases by actor
- **System Diagram Description**: Overview of actor interactions
- **Educational Focus**: Demonstrates requirements gathering and system design

## Actors and Use Cases

### Citizen
1. **Report Pothole**: Submit reports based on location and severity
2. **View Repair Status**: Check status of previously reported potholes

### System
1. **Log Pothole Data**: Assign ID, store address, size (1-10 scale), priority, location, district
2. **Generate Work Orders**: Create orders with location, crew ID, equipment, status, cost, hours
3. **Track Repairs**: Maintain damage files with citizen info and damage costs

### Repair Crew
1. **Log Repairs**: Update system with progress and completion status
2. **Report Additional Work**: Flag additional work needed, apply temporary fixes, reschedule

## Usage

```bash
python pothole_tracker.py
```

### Menu Options

```
Welcome to the Pothole Tracking and Repair System!
1. View use cases for Citizen
2. View use cases for System
3. View use cases for Repair Crew
4. View a brief description of the diagram
5. Exit
```

## Example Output

```
Select an option (1-5): 1

Use Cases for Citizen:
  - Use Case: Report Pothole
    Description: Citizens can report potholes based on location and severity.

  - Use Case: View Repair Status
    Description: Citizens can check the status of potholes that have been reported previously.
```

## System Workflow

```
Citizen Reports Pothole
    ↓
System Logs Data (ID, address, size, priority, location, district)
    ↓
System Generates Work Order (crew ID, equipment, cost, hours)
    ↓
Repair Crew Executes Repair
    ↓
Crew Logs Progress/Completion
    ↓
System Updates Status
    ↓
Citizen Views Repair Status
```

## Data Structure

### Pothole Data
- **ID Number**: Unique identifier
- **Address**: Location
- **Size**: Scale of 1-10
- **Priority**: Repair urgency
- **Location**: Curb position
- **District**: Municipal district

### Work Order
- **Location & Size**: Pothole details
- **Repair Crew ID**: Assigned crew
- **Crew Size**: Number of workers
- **Equipment**: Required tools
- **Status**: Current repair status
- **Cost**: Estimated repair cost
- **Hours**: Estimated time

### Damage File
- **Citizen Information**: Reporter details
- **Damage Cost**: Incurred damages

## Technical Details

**Language**: Python 3
**Design Pattern**: Menu-driven with data dictionaries
**Concepts**:
- Use case modeling
- Actor-based system design
- Data structure organization
- Menu navigation
- Requirements documentation

## Code Structure

### Data Structure
```python
actors_and_use_cases = {
    "Citizen": [use_cases...],
    "System": [use_cases...],
    "Repair Crew": [use_cases...]
}
```

### Functions
- `display_main_menu()`: Main navigation loop
- `display_actor_use_cases(actor)`: Show use cases for specific actor
- `display_diagram_description()`: System overview

## Learning Outcomes

- **Requirements Engineering**: Gathering and documenting requirements
- **Use Case Analysis**: Identifying actors and their interactions
- **System Design**: Modeling multi-actor systems
- **Data Modeling**: Structuring related data
- **Process Flow**: Understanding workflows
- **Stakeholder Analysis**: Identifying system users

## Application Domains

This type of system is used in:
- **Municipal Services**: City infrastructure management
- **Public Works**: Maintenance tracking
- **Citizen Engagement**: Public reporting systems
- **Resource Allocation**: Crew and equipment scheduling
- **Budget Management**: Cost tracking and estimation

## Possible Enhancements

1. **Database Integration**: Store potholes and work orders
2. **Real-Time Tracking**: GPS-based location
3. **Photo Upload**: Allow citizens to attach images
4. **Priority Algorithm**: Auto-prioritize based on size/location
5. **Crew Scheduling**: Optimize crew assignments
6. **Cost Estimation**: Calculate repair costs automatically
7. **Notification System**: Alert citizens of status changes
8. **Analytics Dashboard**: Visualize repair statistics
9. **Mobile App**: Citizen reporting via smartphone
10. **GIS Integration**: Map-based visualization
