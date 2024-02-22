# main.py
from chatgpt_integration import analyze_traffic
from network_monitoring import capture_network_traffic, preprocess_data

def is_malicious_traffic(text_data):
    # Implement your logic to determine if the network traffic is malicious
    # You can use any method such as pattern matching, machine learning models, or third-party APIs

    # For demonstration purposes, let's assume all traffic is considered malicious
    return True

def main():
    print("Bot is starting to work...")
    print("Capturing network traffic...")
    packets = capture_network_traffic()
    print("Preprocessing captured data...")
    text_data = preprocess_data(packets)
    print("Detecting malicious traffic...")
    if is_malicious_traffic(text_data):
        print("Malicious traffic detected.")
        feedback = analyze_traffic(text_data)
        print("Feedback from ChatGPT:", feedback)
    else:
        print("No malicious traffic detected.")

if __name__ == "__main__":
    main()
