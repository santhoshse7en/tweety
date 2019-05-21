"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/santhoshse7en/tweety
"""
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

# Always prefer setuptools over distutils
import setuptools

keywords = ['twitter', "tweets", "without-api", "twitter_scraper", 'selenium', 'vaderSentiment',
'bs4', 'textblob', 'twitter_sentiment', "sentiment_analysis", 'twitter_analysis']

setuptools.setup(
    name="tweety",
    version="0.0.2",
    author="M Santhosh Kumar",
    author_email="santhoshse7en@gmail.com",
    description="Python package which to access the Twitter database without API",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/santhoshse7en/tweety",
    keywords = keywords,
    install_requires=['beautifulsoup4', 'pandas', 'selenium', 'vaderSentiment', 'textblob'],
    packages=setuptools.find_packages(),
    classifiers=['Development Status :: 4 - Beta',
              'Intended Audience :: End Users/Desktop',
              'Intended Audience :: Developers',
              'Intended Audience :: System Administrators',
              'License :: OSI Approved :: MIT License',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Topic :: Communications :: Email',
              'Topic :: Office/Business',
              'Topic :: Software Development :: Bug Tracking',
              ],
)
