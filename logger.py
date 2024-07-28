import os
from datetime import datetime

# HTML file setup
html_file = 'drowsiness_log.html'
if not os.path.exists(html_file):
    with open(html_file, mode='w') as file:
        file.write('<html><head><title>Drowsiness Log</title></head><body style="font-family: Arial, sans-serif; background-color: black; color: white;">')
        file.write('<h1 style="text-align: center; color: white;">Drowsiness Detection Log</h1>')
        file.write('<table border="1" cellspacing="0" cellpadding="8" style="width: 80%; margin: auto; border-collapse: collapse;">')
        file.write('<tr><th style="background-color: #333; color: white;">Timestamp</th><th style="background-color: #333; color: white;">Image</th><th style="background-color: #333; color: white;">Location</th><th style="background-color: #333; color: white;">Name</th><th style="background-color: #333; color: white;">Car Number</th></tr>')

def log_drowsiness(image_path, location, name, car_number):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(html_file, mode='a') as file:
        file.write(f'<tr>')
        file.write(f'<td style="text-align: center;">{timestamp}</td>')
        file.write(f'<td style="text-align: center;"><img src="{image_path}" width="200"></td>')
        file.write(f'<td style="text-align: center;">{location}</td>')
        file.write(f'<td style="text-align: center;">{name}</td>')
        file.write(f'<td style="text-align: center;">{car_number}</td>')
        file.write('</tr>')
