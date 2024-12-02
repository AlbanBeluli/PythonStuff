import subprocess

def base64_encode(text):
    # Ensure text is bytes
    if isinstance(text, str):
        text = text.encode()
    process = subprocess.run(["openssl", "enc", "-base64", "-A"], input=text, capture_output=True, text=False)
    # -A flag removes the line feed character from the end of the output
    return process.stdout.decode().strip()

def base64_decode(base64_str):
    process = subprocess.run(["openssl", "enc", "-base64", "-A", "-d"], input=base64_str.encode(), capture_output=True, text=False)
    # -A flag removes the line feed character from the end of the output
    return process.stdout.decode()

# Main execution
if __name__ == "__main__":
    action = input("Do you want to 'encode' or 'decode'? ").strip().lower()
    
    if action == 'encode':
        text = input("Enter the text to encode: ").strip()
        result = base64_encode(text)
        print(f"Encoded: {result}")
    elif action == 'decode':
        base64_str = input("Enter the Base64 string to decode: ").strip()
        result = base64_decode(base64_str)
        if result:
            print(f"Decoded: {result}")
        else:
            print("Decoding failed.")
    else:
        print("Invalid action. Please use 'encode' or 'decode'.")
