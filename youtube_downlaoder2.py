from pytube import YouTube

links = [
'URL: https://www.youtube.com/watch?v=nxPYqsAr38k',
'URL: https://www.youtube.com/watch?v=FZ_edHixNXU',
'URL: https://www.youtube.com/watch?v=cb_lX_TQBtI',
'URL: https://www.youtube.com/watch?v=ciF2lgZc1Pg',
'URL: https://www.youtube.com/watch?v=VpH6OfyYrF0',
'URL: https://www.youtube.com/watch?v=U1Uejy8oBT0',
'URL: https://www.youtube.com/watch?v=LqhaZvQmK1c',
'URL: https://www.youtube.com/watch?v=TPRNYzqWLgU',
'URL: https://www.youtube.com/watch?v=qzkg6vwS8lk',
'URL: https://www.youtube.com/watch?v=8Gg-TdbYnvA',
'URL: https://www.youtube.com/watch?v=J5V8pOrcPyQ',
'URL: https://www.youtube.com/watch?v=fN6RZtgLJXM',
'URL: https://www.youtube.com/watch?v=7wc8NdzVrwg',
'URL: https://www.youtube.com/watch?v=O8Wqz2ff1cY',
'URL: https://www.youtube.com/watch?v=Qr3SbgsQ28M',
'URL: https://www.youtube.com/watch?v=MJ58Gh0Tpsg',
'URL: https://www.youtube.com/watch?v=yKP_LKOGw3w',
'URL: https://www.youtube.com/watch?v=8kOzTdxZbc0',
'URL: https://www.youtube.com/watch?v=d-_WRgQ32EE',
'URL: https://www.youtube.com/watch?v=TxdPiFPH5FY',
'URL: https://www.youtube.com/watch?v=g6f5Jqz53ro',
'URL: https://www.youtube.com/watch?v=vP51y8eae8g',
'URL: https://www.youtube.com/watch?v=PEDq6R2nDrk',
'URL: https://www.youtube.com/watch?v=SJORlbhIrzA',
'URL: https://www.youtube.com/watch?v=KM259sNt5Vc',
'URL: https://www.youtube.com/watch?v=egIQq4vwcHo',
'URL: https://www.youtube.com/watch?v=xH3Q4hsi1HQ',
'URL: https://www.youtube.com/watch?v=yNQjBAqwBu8',
'URL: https://www.youtube.com/watch?v=34D4JTL0Fog',
'URL: https://www.youtube.com/watch?v=lWif19LHflk',
'URL: https://www.youtube.com/watch?v=DCaA1-EcTMk',
'URL: https://www.youtube.com/watch?v=5_gNICaTFq0',
'URL: https://www.youtube.com/watch?v=Hu2so5nX0LY',
'URL: https://www.youtube.com/watch?v=4gJyqgBIeuI',
'URL: https://www.youtube.com/watch?v=gLmCsU0ezd0',
'URL: https://www.youtube.com/watch?v=3OvEHInvzP0',
'URL: https://www.youtube.com/watch?v=cU3RB20yHk8',
'URL: https://www.youtube.com/watch?v=Lb_fezpUEXc',
'URL: https://www.youtube.com/watch?v=2HbQKUuFDXo',
'URL: https://www.youtube.com/watch?v=8JBMkeB7-EE',
'URL: https://www.youtube.com/watch?v=fxPk_-oNsZg',
'URL: https://www.youtube.com/watch?v=H5p7cQYprzc',
'URL: https://www.youtube.com/watch?v=X7mIhIPjC38',
'URL: https://www.youtube.com/watch?v=qesQEb1d7LY',
'URL: https://www.youtube.com/watch?v=RBZIGovTd98'
]


for i in range(len(links)):
    links[i] = links[i].split(': ')[1]



for link in links :
    yt = YouTube(link)
    yt.streams.filter(resolution='720p').first().download()
