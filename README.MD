# AWS Working Fetcher

This project is a Python application that retrieves information about EC2 instances from AWS using the `boto3` library. It securely manages AWS credentials using environment variables and the `python-dotenv` library.

## Features

- Uses `boto3` for AWS SDK integration.
- Securely loads AWS credentials from a `.env` file.
- Supports configurable AWS regions.

## Prerequisites

- Python 3.7 or higher
- AWS account with access to EC2, S3 and IAM services
- AWS credentials (Access Key ID and Secret Access Key)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install --upgrade pip
   ```

3. Create a `.env` file in the project root and add your AWS credentials:
   ```
   AWS_ACCESS_KEY_ID=your-access-key-id
   AWS_SECRET_ACCESS_KEY=your-secret-access-key
   AWS_REGION=your-region
   ```

4. Ensure the `.env` file is listed in `.gitignore` to prevent accidental exposure of credentials.

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. The application will fetch and display details of your EC2 instances.

## File Structure

- `app.py`: Main application file.
- `requirements.txt`: Lists the Python dependencies.
- `.env`: Stores AWS credentials (not included in the repository).
- `.gitignore`: Ensures sensitive files like `.env` are ignored by Git.

## Dependencies

- `boto3==1.38.27`
- `python-dotenv>=0.19.2`

## Security Notes

- Do not hardcode AWS credentials in the code.
- Ensure the `.env` file is not shared or committed to version control.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.