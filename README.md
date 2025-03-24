# 📌 URL Shortener API

## A Friendly Guide to Our URL Shortening Service

Welcome to our FastAPI-based URL Shortener! This tool transforms those unwieldy, lengthy web addresses into neat, concise links that are perfect for sharing across platforms. Whether you're trying to share links in character-limited spaces like tweets, looking to track click-through rates, or simply wanting cleaner-looking URLs, our shortener has you covered.

## 🚀 What You Can Do With Our Service

Our URL shortener comes packed with features designed to make your life easier:

* **Transform Long URLs**: Convert lengthy web addresses into compact, shareable links that don't break in emails or messages
* **Access Original Links**: Easily retrieve the original destination behind any shortened link
* **Seamless Redirection**: When someone clicks your shortened URL, they'll be automatically redirected to the intended destination
* **Developer-Friendly API**: Built with FastAPI, our service offers comprehensive documentation and lightning-fast performance

## 🌟 Why Use Our URL Shortener?

* **Aesthetics**: Replace lengthy URLs with clean, professional-looking links
* **Tracking Capabilities**: Monitor how many people click on your links
* **Cross-Platform Sharing**: Perfect for social media, messaging apps, and anywhere with character limits
* **Easy Memory**: Share links that people can actually remember and type

## 🛠️ Getting Started

### Setting Up Your Environment

First, let's grab the code and set up your working environment:

```sh
# Clone the repository to your local machine
git clone https://github.com/your-username/url-shortener.git

# Navigate into the project directory
cd url-shortener
```

### Installing Dependencies

Our service requires a few packages to run properly. We've made this easy:

```sh
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install all required packages
pip install -r requirements.txt
```

### Configuration

Before running the service, you may want to configure a few settings to match your environment:

```sh
# Copy the example configuration
cp .env.example .env

# Edit the .env file with your preferred settings
# You can change the database connection, base URL, etc.
```

### Starting the Server

Once everything is set up, you can launch the URL shortener service:

```sh
# Start the FastAPI server
uvicorn app.main:app --reload

# You should see output indicating the server is running
# Typically at http://127.0.0.1:8000
```

## 🔍 Using the API

After starting the server, you can access the interactive API documentation at `http://127.0.0.1:8000/docs`, which provides a user-friendly interface to test all available endpoints.

### Creating a Short URL

To shorten a URL, send a POST request to the `/shorten` endpoint:

```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/shorten",
    json={"url": "https://example.com/very/long/url/that/needs/shortening"}
)

# The response will contain your new short URL
print(response.json())
```

### Retrieving the Original URL

When you need to find the original destination of a shortened URL:

```python
import requests

response = requests.get(
    "http://127.0.0.1:8000/info/abcd123"  # Replace with your short code
)

# The response will contain details about the original URL
print(response.json())
```

### Redirecting to the Original URL

The main functionality - when someone clicks on your shortened URL:

```
GET /{short_code}
```

When accessed in a browser, this endpoint automatically redirects to the original URL.

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/shorten` | POST | Create a short URL from a long one |
| `/info/{short_code}` | GET | Get information about a shortened URL |
| `/{short_code}` | GET | Redirect to the original URL |

## 📦 Project Structure

```
url-shortener/
├── app/
│   ├── __init__.py
│   ├── main.py         # Main FastAPI application
│   ├── models.py       # Database models
│   ├── schemas.py      # Pydantic schemas for validation
│   └── utils.py        # Utility functions
├── tests/              # Test directory
├── .env.example        # Example environment variables
├── requirements.txt    # Project dependencies
└── README.md           # This documentation
```

## 💻 Technical Details

### Technology Stack

- **FastAPI**: High-performance web framework
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation and settings management
- **Uvicorn**: ASGI server for running the application

### Database Models

Our service uses a simple but effective data model for storing URLs:

```python
class URL(Base):
    __tablename__ = "urls"
    
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, index=True)
    short_code = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    clicks = Column(Integer, default=0)
```

## 🤝 Contributing

We welcome contributions from the community! If you'd like to improve our URL shortener:

1. Fork the repository
2. Create a feature branch (`git checkout -b amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin amazing-feature`)
6. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Write tests for new features
- Keep documentation updated

## 🔒 Security Considerations

- The service checks for malicious URLs
- Rate limiting is implemented to prevent abuse
- Regular security audits are performed

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Need Help?

If you encounter any issues or have questions about using our URL shortener:

* Check the [FAQ section](#) in our documentation
* Open an issue on GitHub
* Contact our support team at support@urlshortener.example.com

## 🔮 Future Plans

We're constantly improving our URL shortener! Here are some features on our roadmap:

- Custom short codes
- Advanced analytics dashboard
- API key authentication
- Bulk URL shortening

---

Happy URL shortening!
