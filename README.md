# EDP-LECTURE-EXAM

# Event-Driven Programming (EDP) System

## What is EDP?

Event-Driven Programming (EDP) is a way to make programs react to events like user actions or data changes. It's often used in apps that need to be flexible and responsive.

## About This Project

This project is a simple Python example of EDP. It has four parts:

1. **Sensor**: Detects something and sends an event.
2. **Processor**: Takes the Sensor's data and processes it.
3. **Logger**: Saves the processed data.
4. **UI**: Shows the final result.

## How It Works

- The Sensor detects something (like "Temperature: 25°C") and sends a `data_detected` event.
- The Processor listens for that event, processes the data, and sends a `data_processed` event.
- The Logger listens for processed data and logs it.
- The UI listens for logged data and shows it to the user.

### Example Code

```python
sensor.on("data_detected", processor.process)
processor.on("data_processed", logger.log)
sensor.detect("Temperature: 25°C")
```

## How to Run

1. Clone the project:
   ```bash
   git clone https://github.com/0808doga/EDP-LECTURE-EXAM.git
   ```
2. Go to the folder:
   ```bash
   cd EDP-System
   ```
3. Run it:
   ```bash
   python src/main.py
   ```

## Why Use EDP?

This project shows how EDP makes programs modular, flexible, and easy to extend. Feel free to explore and build on it!
