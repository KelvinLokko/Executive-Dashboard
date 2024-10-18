# Kedebah API Integration

This project is a Flask-based API that integrates with the Kedebah API and a Ticketing Tool API to provide various project and system metrics.

## Features

- Total Active Projects (cashflow and non-cashflow)
- Targets vs. Actual
- Timelines vs. Slippages
- Activity Output against Service Experience
- System Availability Score
- Data Warehouse Availability
- Server Response Score
- Network Latency

## Prerequisites

- Python 3.7+
- PostgreSQL database

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/kedebah-api-integration.git
   cd kedebah-api-integration
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your configuration:
   ```
   KEDEBAH_API_URL=https://kedebah.com/api
   TICKETING_TOOL_API_URL=https://ticketing-tool.com/api
   API_KEY=your_api_key_here
   DB_USERNAME=your_db_username
   DB_PASSWORD=your_db_password
   DB_HOST=your_db_host
   DB_PORT=your_db_port
   DB_NAME=your_db_name
   ```

## Usage

To run the application:

```
python app.py
```

The API will be available at `http://localhost:5000`.

## API Endpoints

- `/projects/active`: Get total active projects
- `/projects/targets-vs-actual`: Get targets vs. actual metrics
- `/projects/timelines-vs-slippages`: Get timelines vs. slippages metrics
- `/activity/output-vs-experience`: Get activity output vs. service experience metrics
- `/system/availability`: Get system availability score
- `/data-warehouse/availability`: Get data warehouse availability
- `/server/response-score`: Get server response score
- `/network/latency`: Get network latency metrics

## Configuration

The application uses a `config.py` file to manage configuration. This file loads environment variables from the `.env` file.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Your Name - kelvinlokko17@gmail.com
