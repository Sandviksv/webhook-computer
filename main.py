import psutil,time, requests
import GPUtil
url = input('WebhookUrl >')
while True:
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load*100}%"
    x = psutil.cpu_percent()
    svmem = psutil.virtual_memory()
    def get_size(bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor
    json = {
    "embeds": [
        {
        "description": f"CPU {x}%\nRAM {get_size(svmem.used)} GB\n GPU NAME\n{gpu.name}\nLoad%\n{gpu_load}",
        "color": 36007,
        "author": {
            "name": "CPU & RAM CHECK & GPU"
        }
        }
    ],
    "avatar_url": "https://scontent.fbkk29-1.fna.fbcdn.net/v/t39.30808-6/327658970_990618138567512_6512244974626364113_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeEDE55yQoWvdEvmo4uCEzqu8GsCEGp0ThHwawIQanROEdz8n-dLn-z_U5sqyk1Vv8_-O9TzF2v9hnEHU80AgvUN&_nc_ohc=dHgZkW6jJ8wAX-SV-4j&_nc_ht=scontent.fbkk29-1.fna&oh=00_AfC9Q70XHzEpzFH879zyfkwntleOJTzwY23jVwx6Jl5txA&oe=63EF0BB1",
    "attachments": []
    
    }
    respon = requests.post(url, json=json)
    print(respon)
    time.sleep(10)

