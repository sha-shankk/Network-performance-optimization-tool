import random

def generate_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

data = []
for _ in range(100):
    ip_address = generate_ip()
    packets_sent = random.randint(500, 2000)
    packets_received = random.randint(400, packets_sent)
    latency = round(random.uniform(50, 200), 2)
    entry = f"{ip_address} {packets_sent} {packets_received} {latency}"
    print(entry)  # Debug print
    data.append(entry)

try:
    with open("network_data.txt", "w") as file:
        for entry in data:
            file.write(entry + "\n")
    print("100 entries of network data have been written to network_data.txt.")
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")
