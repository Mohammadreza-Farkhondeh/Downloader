# Import Libraries
from bs4 import BeautifulSoup
import requests
import os
import shutil
import opener

# Input for URL
url = input('URL: ')
# Get page and make soup
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
# Input for file type
file_type = input('TYPE: .')

# Find all a tag in soup
links = soup.find_all('a')

# Get all file links in a tag's href list that they have .{file_type} in the end
target_type_links = [link['href'] for link in links if link['href'].endswith('.%s' % file_type)]

# Print the list of files to be downloaded
for link in target_type_links:
    print(int(target_type_links.index(link))+1, link)

# Get all links in target_type_links
for link in target_type_links:
    # Get the file name
    file_name = link.split('/')[-1]
    # Check if the link is a full path or a relative path
    if link.startswith('http'):
        # The link is a full path
        file_url = link
    else:
        # The link is a relative path
        file_url = os.path.join(url, link)
    # Try to download the file from the url
    try:
        # Get the file content as a stream
        file_content = requests.get(file_url, stream=True, timeout=10)
        print('Downloading file: %s' % file_name)
        # Create a temporary file to store the content
        with open(file_name + '.tmp', 'wb') as temp_file:
            # Copy the content from the stream to the temporary file
            shutil.copyfileobj(file_content.raw, temp_file)
        # Rename the temporary file to the original file name
        os.rename(file_name + '.tmp', file_name)
        print('%s downloaded!\n' % file_name)
    except requests.exceptions.RequestException as e:
        # An error occurred while requesting the file
        print('An error occurred while downloading %s: %s' % (file_name, e))
    except OSError as e:
        # An error occurred while creating or renaming the file
        print('An error occurred while saving %s: %s' % (file_name, e))
    else:
        # The download was successful
        print('%s downloaded successfully!\n' % file_name)
    finally:
        # Close the stream if it is still open
        if file_content:
            file_content.close()

print('All files downloaded!')
