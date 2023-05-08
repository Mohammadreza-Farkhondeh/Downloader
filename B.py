# Import Libraries
from bs4 import BeautifulSoup
import requests

# Input for URL
url = input('URL:')
# Get page and make soup
r = requests.get(url)
soup =  BeautifulSoup(r.content, 'html.parser')
# Input for file type
type = input('TYPE: .')


# Find all a tag in soup
links = soup.find_all('a')

# Get all file links in a tag's href list that they have .{type} in the end
target_type_links = [link['href'] for link in links if link['href'].endswith('%s' % type) ]

# Print the list of files to be downloaded
for link in target_type_links:
    print(int(target_type_links.index(link))+1, link)
    
# Get all links in target_type_links
for link in target_type_links:
    # Try for Download the i if url is full path
    try:
        # Get the file and name
        file_name = link.split('/')[-1]
        r = requests.get(link, stream = True)
        print('downloading file: %s' %file_name)
        # Download File chunk by chunk
        with open(file_name, 'wb') as f:
            # for chunk in r.iter_content(chunk_size = 1024 * 1024 * 10): # Set chunk size 10 MB
                # if chunk: 
                    # f.write(chunk)
            f.write(r.content)
        print( "%s downloaded!\n"%file_name )
        
    except: # If urls wasnt full path
        # Get the file and name
        file_name = link.split('/')[-1]
        link = url + link # add the main page url to beggining of link
        r = requests.get(link, stream = True)
        print('downloading file: %s' %file_name)
        # Download File chunk by chunk
        with open(file_name, 'wb') as f:
            # for chunk in r.iter_content(chunk_size = 1024 * 1024 * 10): # Set chunk size 10 MB
                # if chunk: 
                    # f.write(chunk)
            f.write(r.content)
        print( "%s downloaded!\n"%file_name )



print ("All files downloaded!")
