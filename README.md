[![PyPI Version](https://img.shields.io/pypi/v/tweety.svg)](https://pypi.org/project/tweety)
[![License](https://img.shields.io/pypi/l/tweety.svg)](https://pypi.python.org/pypi/tweety/)
[![Documentation Status](https://readthedocs.org/projects/pip/badge/?version=latest\&style=flat)](https://santhoshse7en.github.io/tweety_doc)
[![Downloads](https://pepy.tech/badge/tweety/month)](https://pepy.tech/project/tweety)

# 🐦 Tweety

**Tweety** is a Python-based tweet scraper that bypasses Twitter’s API limitations by using **Selenium** to collect tweets directly from the web. No API keys, no rate limits, no restrictions — just fast and flexible scraping.

---

## 🔗 Project Links

| Resource       | URL                                                          |
| -------------- | ------------------------------------------------------------ |
| 🐍 PyPI	       | [tweety on PyPI](https://pypi.org/project/tweety/)           |
| 🛠 Repository  | [GitHub Repo](https://github.com/santhoshse7en/tweety/)      |
| 📚 Documentation| [Documentation](https://santhoshse7en.github.io/tweety_doc/) |

---

## ✨ Features

* 🔍 Scrape tweets by keyword/topic — no login required
* 🚫 No Twitter API needed — no rate limits!
* 🧠 Sentiment analysis using **VADER** and **TextBlob**
* 📊 Structured output using **pandas**

> 🧪 You can scrape \~25 pages (\~1200 tweets) reliably in one run.

---

## 📦 Dependencies

* `beautifulsoup4`
* `selenium`
* `chromedriver-binary`
* `vaderSentiment`
* `textblob`
* `pandas`

---

## 📥 Installation

Install the dependencies with `pip`:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Usage

```python
from twitter.tweety import tweets

# Scrape tweets related to "Super Deluxe"
tweety = tweets("Super Deluxe")

# Print sentiment analysis results
print("Polarity Scores : " + str(tweety.final_sentiment_scores))
```

### 📂 Tweety Directory Structure

![Directory Structure](https://user-images.githubusercontent.com/47944792/58116804-d3727b80-7c1a-11e9-9e2e-a675d98b8682.PNG)

### 📊 Output Example

```python
Polarity Scores : {'positive': 0.55, 'neutral': 0.35, 'negative': 0.10}
```

![Output Screenshot](https://user-images.githubusercontent.com/47944792/53886316-c3002b00-4045-11e9-8a56-10ef06275951.PNG)

---

## 🤝 Contributing

Contributions are welcome!
For major changes, please open an issue first to discuss what you'd like to improve.
Don't forget to update or add tests as needed.

---

## 📜 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
