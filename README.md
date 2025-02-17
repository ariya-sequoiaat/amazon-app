Amazon Product Scraper
An automated tool for searching and analyzing products on Amazon India using Selenium WebDriver.


Features

Automated product search on Amazon.in
Sorting products by customer reviews
Filtering out sponsored products
Automated add-to-cart functionality
Comprehensive test suite using pytest
Dockerized environment for consistent testing

Prerequisites

Python 3.11 or higher
Docker (for containerized usage)
Make (for using Makefile commands)
Chrome/Chromium browser
ChromeDriver matching your Chrome version

Installation
Local Setup

Clone the repository:

git clone <repository-url>
cd amazon-scraper

Set up the environment using Make:

make setup
This will:

Update pip
Install required Python packages

Docker Setup
Build the Docker image:
make build
Usage
Running the Scraper

Local execution:

python main.py

When prompted, enter the product you want to search for.

Running Tests

Local test execution:

make test

Docker test execution:

make run
Project Structure
amazon-scraper/
│
├── main.py                 # Main scraper script
├── test_amazon_scraper.py  # Test suite
├── Dockerfile             # Docker configuration
├── Makefile              # Make commands
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
Available Make Commands

make setup: Set up local development environment
make test: Run tests locally
make clean: Clean up cache and temporary files
make build: Build Docker image
make run: Run tests in Docker container

Docker Commands
Direct Docker commands if you prefer not using Make:
# Build image
docker build -t amazon-scraper .

# Run container
docker run amazon-scraper
Testing
The test suite includes:

Homepage loading verification
Search functionality testing
Sort functionality testing
Non-sponsored product detection
Add to cart button verification
Error handling tests

To run specific tests:
pytest test_amazon_scraper.py -k "test_name" -v
Troubleshooting
Common Issues

Chrome/ChromeDriver version mismatch:

Ensure your ChromeDriver version matches your Chrome browser version
Update both Chrome and ChromeDriver if necessary


Docker permission issues:

Run Docker commands with sudo if needed
Add your user to the docker group:
sudo usermod -aG docker $USER



Selenium timing issues:

Increase wait times in the test configuration
Check network connectivity
Verify element selectors



Solutions

If tests fail in Docker:
# Check Docker logs
docker logs $(docker ps -q --filter ancestor=amazon-scraper)

If elements aren't found:

Check if selectors have changed
Increase wait times
Verify page loading completely



Future Improvements

Add support for multiple browsers
Implement proxy rotation
Add support for different Amazon domains
Implement data export functionality
Add detailed logging
Add configuration file support