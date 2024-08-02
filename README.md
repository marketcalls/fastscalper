
# FastScalper

This project provides a FastScalper tool built using Flask for the backend and CustomTkinter for the frontend GUI. It integrates with the OpenAlgo API for placing smart orders.

## Prerequisites

- **Python 3.x**
- **Flask**
- **CustomTkinter**
- **OpenAlgo API**

Ensure that OpenAlgo is configured with supported brokers and running. You also need to get the API key from OpenAlgo and configure the settings to place smart orders.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/marketcalls/fastscalper.git
    cd fastscalper
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure OpenAlgo API:**

    Replace `your_api_key_here` with your actual API key in the `config.ini` file:

    ```ini
    [DEFAULT]
    api_key = your_api_key_here
    exchange = NSE
    product = MIS
    ```

## Running the Application

1. **Start the Flask server:**

    ```bash
    python app.py
    ```

2. **Open your browser and go to:**

    ```
    http://127.0.0.1:5001
    ```

3. **Launch the FastScalper Tool:**

    Click the "Launch Trading Tool" button to start the CustomTkinter-based FastScalper tool.

## Project Structure

- `app.py`: Flask application to serve the web interface and handle the launch of the trading tool.
- `trading.py`: Contains the logic for the CustomTkinter trading application and OpenAlgo integration.
- `templates/index.html`: HTML template for the web interface.
- `config.ini`: Configuration file for storing the OpenAlgo API key and other settings.

## Usage

1. **Launch the FastScalper Tool:**

    From the web interface, click the "Launch Trading Tool" button.

2. **Configure Settings:**

    In the FastScalper GUI, click on "Settings" to configure your OpenAlgo API key, exchange, and product.

3. **Place Orders:**

    Use the provided buttons in the FastScalper GUI to place long entry (LE), long exit (LX), short entry (SE), and short exit (SX) orders.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
