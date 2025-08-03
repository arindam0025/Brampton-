#!/usr/bin/env python3
"""
One-liner installation script for Brampton AI
Users can run this with: python -c "$(curl -s https://raw.githubusercontent.com/arindam0025/Brampton-/main/install_one_liner.py)"
"""

import subprocess
import sys
import os
import tempfile
import urllib.request

def download_and_install():
    """Download and install Brampton AI"""
    print("🤖 Brampton AI - One-Click Installation")
    print("=" * 40)
    
    try:
        # Create temporary directory
        temp_dir = tempfile.mkdtemp()
        os.chdir(temp_dir)
        
        print("📥 Downloading Brampton AI...")
        
        # Download the main script
        script_url = "https://raw.githubusercontent.com/arindam0025/Brampton-/main/start_brampton.py"
        urllib.request.urlretrieve(script_url, "start_brampton.py")
        
        print("📦 Installing required packages...")
        
        # Install required packages
        packages = [
            "flask>=2.3.3",
            "openai>=1.3.0", 
            "anthropic>=0.25.0",
            "python-dotenv>=1.0.0",
            "requests>=2.31.0"
        ]
        
        for package in packages:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        
        print("✅ Installation complete!")
        print("\n🚀 Starting Brampton AI...")
        
        # Run the chatbot
        subprocess.call([sys.executable, "start_brampton.py"])
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n🔧 Try running: python -m pip install --upgrade pip")
        sys.exit(1)

if __name__ == "__main__":
    download_and_install() 