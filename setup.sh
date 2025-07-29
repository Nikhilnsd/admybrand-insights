#!/bin/bash

# ADmyBRAND Insights Setup Script
echo "🚀 Setting up ADmyBRAND Insights Dashboard..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18+ from https://nodejs.org"
    exit 1
fi

# Check Node.js version
NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
    echo "❌ Node.js version 18+ required. Current version: $(node -v)"
    exit 1
fi

echo "✅ Node.js $(node -v) detected"

# Install dependencies
echo "📦 Installing dependencies..."
npm install

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Create .env.local if it doesn't exist
if [ ! -f .env.local ]; then
    echo "🔧 Creating environment file..."
    cat > .env.local << EOL
# ADmyBRAND Insights Environment Variables
NEXT_PUBLIC_APP_NAME="ADmyBRAND Insights"
NEXT_PUBLIC_APP_VERSION="1.0.0"
EOL
    echo "✅ Environment file created"
fi

echo ""
echo "🎉 Setup complete! Run the following commands to start:"
echo ""
echo "   npm run dev     # Start development server"
echo "   npm run build   # Build for production"
echo "   npm run start   # Start production server"
echo ""
echo "🌐 Development server will be available at: http://localhost:3000"
echo ""
