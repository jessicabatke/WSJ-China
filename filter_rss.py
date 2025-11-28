import feedparser
import xml.etree.ElementTree as ET
from datetime import datetime
import requests

# Fetch the original feed
feed_url = "https://feeds.content.dowjones.io/public/rss/RSSWorldNews"
feed = feedparser.parse(feed_url)

# Create new RSS feed
rss = ET.Element('rss', version='2.0')
channel = ET.SubElement(rss, 'channel')
ET.SubElement(channel, 'title').text = 'China News Filter'
ET.SubElement(channel, 'link').text = feed.feed.get('link', '')
ET.SubElement(channel, 'description').text = 'Filtered China-related news'

# Filter and add items
for entry in feed.entries:
    if 'china' in entry.link.lower():
        item = ET.SubElement(channel, 'item')
        ET.SubElement(item, 'title').text = entry.title
        ET.SubElement(item, 'link').text = entry.link
        ET.SubElement(item, 'description').text = entry.get('description', '')
        ET.SubElement(item, 'pubDate').text = entry.get('published', '')

# Write to file
tree = ET.ElementTree(rss)
ET.indent(tree, space='  ')
tree.write('china_feed.xml', encoding='unicode', xml_declaration=True)
```

### 2. Create requirements.txt
```
feedparser
requests
