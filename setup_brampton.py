#!/usr/bin/env python3
"""
Brampton Finance AI Setup Script
Automated setup for the complete Brampton chatbot system
"""

import subprocess
import sys
import os
import time
import webbrowser
from pathlib import Path

def run_command(command, cwd=None, shell=True):
    """Run a command and return the result"""
    try:
        result = subprocess.run(command, shell=shell, cwd=cwd, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def check_python():
    """Check if Python is installed"""
    success, stdout, stderr = run_command("python --version")
    if success:
        print(f"✅ Python found: {stdout.strip()}")
        return True
    else:
        print("❌ Python not found. Please install Python 3.8+")
        return False

def check_ollama():
    """Check if Ollama is installed and running"""
    print("🔍 Checking Ollama installation...")
    success, stdout, stderr = run_command("ollama --version")
    if success:
        print(f"✅ Ollama found: {stdout.strip()}")
        
        # Check if Ollama service is running
        success, stdout, stderr = run_command("ollama list")
        if success:
            print("✅ Ollama service is running")
            if "llama3" in stdout:
                print("✅ Llama3 model is available")
            else:
                print("⚠️  Llama3 model not found. Installing...")
                run_command("ollama pull llama3")
        else:
            print("⚠️  Ollama service not running. Starting...")
            run_command("ollama serve", shell=True)
        return True
    else:
        print("❌ Ollama not found. Please install from https://ollama.com/")
        return False

def install_backend_deps():
    """Install backend dependencies"""
    print("📦 Installing backend dependencies...")
    backend_path = Path(__file__).parent / "backend"
    success, stdout, stderr = run_command("pip install -r requirements.txt", cwd=backend_path)
    if success:
        print("✅ Backend dependencies installed")
        return True
    else:
        print(f"❌ Failed to install backend dependencies: {stderr}")
        return False

def start_backend():
    """Start the FastAPI backend server"""
    print("🚀 Starting backend server...")
    backend_path = Path(__file__).parent / "backend"
    
    # Start the server in background
    try:
        process = subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"],
            cwd=backend_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait a moment for server to start
        print("⏳ Waiting for server to start...")
        time.sleep(5)
        
        # Check if server is running using requests
        try:
            import requests
            response = requests.get("http://localhost:8000/", timeout=5)
            if response.status_code == 200 and "Brampton Finance AI Backend is running" in response.text:
                print("✅ Backend server started successfully at http://localhost:8000")
                return True, process
            else:
                print("⚠️  Backend server responded but may not be fully ready")
                return True, process  # Still consider it successful if we get a response
        except requests.exceptions.RequestException:
            # Check if process is still running
            if process.poll() is None:
                print("✅ Backend server process started (unable to verify HTTP response)")
                return True, process
            else:
                stdout, stderr = process.communicate()
                print(f"❌ Backend server failed to start. Error: {stderr.decode()}")
                return False, process
            
    except Exception as e:
        print(f"❌ Failed to start backend server: {e}")
        return False, None

def open_frontend():
    """Open the frontend in the browser"""
    print("🌐 Opening frontend...")
    frontend_path = Path(__file__).parent / "frontend" / "index.html"
    
    if frontend_path.exists():
        file_url = f"file://{frontend_path.absolute()}"
        webbrowser.open(file_url)
        print(f"✅ Frontend opened at: {file_url}")
        return True
    else:
        print("❌ Frontend file not found")
        return False

def main():
    """Main setup function"""
    print("🏦 Brampton Finance AI - Setup Script")
    print("=" * 50)
    
    # Check prerequisites
    if not check_python():
        sys.exit(1)
    
    # Install backend dependencies
    if not install_backend_deps():
        sys.exit(1)
    
    # Check Ollama (optional for OpenRouter mode)
    ollama_available = check_ollama()
    if not ollama_available:
        print("⚠️  Ollama not available. Using OpenRouter API mode.")
    
    # Start backend server
    backend_success, backend_process = start_backend()
    if not backend_success:
        print("❌ Failed to start backend. Please check the logs.")
        sys.exit(1)
    
    # Open frontend
    frontend_success = open_frontend()
    
    print("\n" + "=" * 50)
    print("🎉 Brampton Finance AI Setup Complete!")
    print("\n📋 Summary:")
    print(f"   Backend: {'✅ Running' if backend_success else '❌ Failed'} (http://localhost:8000)")
    print(f"   Frontend: {'✅ Opened' if frontend_success else '❌ Failed'}")
    print(f"   AI Model: {'✅ OpenRouter API' if not ollama_available else '✅ Local Ollama'}")
    
    print("\n🚀 Usage:")
    print("   1. The frontend should open automatically in your browser")
    print("   2. Start chatting with Brampton about finance topics!")
    print("   3. Press Ctrl+C to stop the backend server when done")
    
    if backend_process:
        try:
            print("\n⏳ Backend server is running. Press Ctrl+C to stop...")
            backend_process.wait()
        except KeyboardInterrupt:
            print("\n🛑 Stopping backend server...")
            backend_process.terminate()
            backend_process.wait()
            print("✅ Backend server stopped")

if __name__ == "__main__":
    main()
